# Guía para el manejo de datos en Text Mining con RAG

Este documento describe cómo preparar, fragmentar, vectorizar y consultar información textual mediante una arquitectura **RAG** (*Retrieval-Augmented Generation*). El propósito es convertir documentos sin estructurar en una fuente de conocimiento que un modelo de lenguaje pueda consultar de manera rápida, precisa y verificable.

> **Importante:** RAG no es un modelo por sí mismo. Es una arquitectura que combina un sistema de recuperación de información con un modelo generativo.

## Contenido

1. [Flujo general](#flujo-general)
2. [Ingesta y normalización](#1-ingesta-y-normalización)
3. [Fragmentación o *chunking*](#2-fragmentación-o-chunking)
4. [Selección de la estrategia de fragmentación](#3-selección-de-la-estrategia-de-fragmentación)
5. [Generación de *embeddings*](#4-generación-de-embeddings)
6. [Almacenamiento en una base de datos vectorial](#5-almacenamiento-en-una-base-de-datos-vectorial)
7. [Consulta y recuperación](#6-consulta-y-recuperación)
8. [Parámetros de control](#7-parámetros-de-control)
9. [Buenas prácticas y validación](#8-buenas-prácticas-y-validación)
10. [Conclusiones](#9-conclusiones)

## Flujo general

El proceso se divide en dos fases independientes:

- **Indexación:** se prepara el corpus y se almacena una representación vectorial de cada fragmento. Se ejecuta inicialmente y cada vez que cambian los documentos.
- **Consulta:** se procesa cada pregunta, se recuperan los fragmentos más relevantes y se entregan como contexto al modelo generativo.

```mermaid
flowchart LR
    A[Fuentes de información] --> B[Ingesta y normalización]
    B --> C[Fragmentación]
    C --> D[Generación de embeddings]
    D --> E[(Base de datos vectorial)]
    Q[Pregunta del usuario] --> F[Embedding de la pregunta]
    F --> E
    E --> G[Fragmentos relevantes]
    G --> H[Modelo generativo]
    H --> I[Respuesta con fuentes]
```

## 1. Ingesta y normalización

La primera etapa consiste en recolectar y limpiar la información que formará el corpus.

### Fuentes admitidas

- Documentos PDF.
- Páginas web.
- Tickets de soporte.
- Manuales y documentación técnica.
- Transcripciones y entrevistas.
- Bases de datos.

### Procedimiento

1. Extraer el contenido como texto plano.
2. Eliminar elementos que no aporten información, como encabezados y pies de página repetidos, menús u otros componentes de navegación.
3. Evaluar cuidadosamente tablas e imágenes antes de descartarlas. Si contienen información importante, convertirlas a una representación textual útil.
4. Normalizar caracteres especiales, espacios duplicados y saltos de línea innecesarios.
5. Conservar la estructura lógica del documento siempre que sea posible: títulos, secciones, cláusulas, preguntas y respuestas.
6. Asociar metadatos a cada documento, como mínimo:
   - fuente o archivo de origen;
   - título;
   - página o sección;
   - fecha;
   - autor;
   - categoría, área o versión, si aplica.

Los metadatos permiten filtrar la búsqueda y citar el origen de una respuesta. Por ello, deben mantenerse vinculados al texto durante todo el proceso.

## 2. Fragmentación o *chunking*

Los documentos normalizados se dividen en fragmentos pequeños llamados *chunks*. Esta división es necesaria porque el contexto de un modelo de lenguaje es limitado y la búsqueda suele ser más precisa cuando opera sobre unidades breves y específicas.

Como punto de partida general se recomienda:

- **Tamaño:** entre 300 y 800 *tokens* por fragmento.
- **Solapamiento (*overlap*):** entre 10 % y 20 %.

El solapamiento conserva el contexto alrededor de los cortes y evita que una definición o idea quede dividida entre dos fragmentos. Estos valores no son reglas absolutas: deben ajustarse al tipo de documento y validarse con consultas reales.

## 3. Selección de la estrategia de fragmentación

### Estrategias disponibles

#### Tamaño fijo

Divide el texto cada cierta cantidad de *tokens* o caracteres y normalmente aplica solapamiento. Es una estrategia sencilla y rápida, pero ignora la estructura y el significado del contenido.

#### Fragmentación recursiva

Intenta dividir primero por párrafos; si un fragmento todavía es demasiado grande, continúa por oraciones y después por palabras. Respeta mejor la estructura natural del texto mediante separadores jerárquicos.

#### Fragmentación por estructura

Utiliza unidades lógicas del documento, como títulos, secciones, encabezados Markdown, filas de una tabla, cláusulas, artículos, funciones o clases. Cada fragmento representa una unidad coherente.

#### Fragmentación semántica

Calcula *embeddings* de oraciones contiguas y crea un corte cuando disminuye su similitud, lo que suele indicar un cambio de tema.

### Estrategia recomendada según el documento

| Tipo de documento | Estrategia | Tamaño sugerido |
|---|---|---:|
| FAQ o preguntas frecuentes | Una pregunta y su respuesta por fragmento | 100–300 *tokens* |
| Manual o documentación técnica | Por estructura: títulos y secciones | 500–800 *tokens* |
| Contratos y normativas | Por cláusula o artículo | 300–600 *tokens* |
| Transcripciones y entrevistas | Semántica o ventanas de oraciones | 300–500 *tokens* |
| Código fuente | Por función o clase | Bloque lógico completo |

## 4. Generación de *embeddings*

Un modelo de *embeddings* transforma cada fragmento en un vector numérico que representa su significado. A diferencia de técnicas como TF-IDF, que se apoyan principalmente en la presencia de palabras, los *embeddings* capturan relaciones semánticas: dos textos de significado similar pueden quedar cerca en el espacio vectorial aunque no compartan las mismas palabras.

Para esta etapa se debe:

1. Seleccionar un modelo que comprenda el idioma y el dominio del corpus. Para documentos en español, comprobar que sea multilingüe o que tenga un buen desempeño en español.
2. Generar un vector para cada fragmento.
3. Conservar la relación entre el vector, el texto original y sus metadatos.
4. Registrar el nombre y la versión del modelo utilizado.

El modelo de *embeddings* es distinto del modelo generativo. Sin embargo, debe utilizarse **el mismo modelo y la misma versión** para vectorizar tanto los documentos como las preguntas; de lo contrario, los vectores no serán comparables.

## 5. Almacenamiento en una base de datos vectorial

La base de datos vectorial almacena e indexa los fragmentos para realizar búsquedas rápidas por similitud. Cada registro debería contener una estructura equivalente a la siguiente:

```json
{
  "id": "man-042-c7",
  "vector": [0.021, -0.44, 0.13],
  "texto": "La garantía cubre...",
  "metadatos": {
    "fuente": "Manual_v3.pdf",
    "pagina": 42,
    "version": 3
  }
}
```

Comparar una consulta uno a uno contra millones de vectores no es escalable. Por ello se utilizan índices de búsqueda aproximada de vecinos más cercanos, como **ANN** o **HNSW**, que intercambian una pequeña cantidad de exactitud por una mejora considerable de velocidad.

Los metadatos también permiten restringir la búsqueda. Por ejemplo: recuperar únicamente documentos del área legal publicados en 2025.

## 6. Consulta y recuperación

En cada solicitud se ejecuta el siguiente flujo:

1. Recibir y, si es necesario, normalizar la pregunta del usuario.
2. Generar su *embedding* con el mismo modelo usado durante la indexación.
3. Aplicar los filtros de metadatos correspondientes.
4. Buscar los fragmentos más similares en la base vectorial.
5. Seleccionar una cantidad limitada de resultados relevantes.
6. Entregar al modelo generativo la pregunta, los fragmentos recuperados y sus fuentes.
7. Generar una respuesta basada únicamente en la evidencia recuperada e incluir las referencias de origen.

Si el corpus no contiene información suficiente, el sistema debe indicarlo explícitamente en lugar de inventar una respuesta.

## 7. Parámetros de control

### Tamaño del fragmento

- Un fragmento demasiado grande incorpora ruido y puede diluir la idea principal.
- Un fragmento demasiado pequeño puede perder el contexto necesario para interpretar la información.

### Solapamiento

Un valor inicial de 10 % a 20 % ayuda a conservar ideas que atraviesan el límite entre dos fragmentos. Un solapamiento excesivo genera duplicados, aumenta el almacenamiento y puede devolver contenido redundante.

### Cantidad de fragmentos recuperados

- Recuperar muy pocos puede dejar fuera información necesaria.
- Recuperar demasiados puede distraer al modelo, aumentar el costo y reducir la precisión de la respuesta.

### Modelo de *embeddings*

Debe entender el idioma, el vocabulario y el dominio de los documentos. Cualquier cambio de modelo o versión exige volver a generar los vectores del corpus.

## 8. Buenas prácticas y validación

Antes de utilizar el sistema, verificar que:

- [ ] El texto fue extraído sin perder información relevante.
- [ ] Se eliminaron elementos repetidos o sin valor semántico.
- [ ] Las tablas e imágenes importantes fueron convertidas a texto o tratadas por un proceso específico.
- [ ] Cada fragmento conserva sus metadatos y puede rastrearse hasta la fuente.
- [ ] Los cortes respetan unidades lógicas del documento.
- [ ] El tamaño y el solapamiento fueron evaluados con preguntas representativas.
- [ ] El mismo modelo de *embeddings* se usa en indexación y consulta.
- [ ] Los filtros de metadatos devuelven únicamente documentos válidos.
- [ ] Las respuestas incluyen la fuente o referencia utilizada.
- [ ] El sistema declara que no tiene información cuando el corpus no contiene la respuesta.

La evaluación debe centrarse primero en la recuperación. Si los fragmentos correctos no llegan al modelo generativo, modificar el *prompt* no resolverá el problema. Conviene crear un conjunto de preguntas de prueba con sus fuentes esperadas y medir si los resultados relevantes aparecen entre los primeros fragmentos recuperados.

## 9. Conclusiones

- RAG combina recuperación de información y generación de lenguaje; no constituye un modelo independiente.
- La indexación se ejecuta al preparar o actualizar el corpus, mientras que la consulta se realiza para cada solicitud.
- La calidad del sistema depende principalmente de la limpieza del corpus, la estrategia de fragmentación, los metadatos, el modelo de *embeddings* y la recuperación.
- El modelo de *embeddings* debe ser idéntico en la indexación y la consulta.
- Una respuesta confiable debe estar respaldada por el corpus y reconocer explícitamente cuando no existe información suficiente.

## Material de referencia

El contenido de esta guía fue elaborado a partir de las imágenes disponibles en [`imagenes_informacion/`](./imagenes_informacion/).
