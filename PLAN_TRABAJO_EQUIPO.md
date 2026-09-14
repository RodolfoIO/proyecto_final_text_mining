# Plan de trabajo - Proyecto final de Text Mining

## 1. Objetivo del proyecto

Tomar la narración de un partido de fútbol, convertirla en texto y aplicar técnicas de minería de texto para estimar las estadísticas principales del encuentro.

El resultado final debe incluir:

- Metodología y estrategia utilizadas.
- Script o transcripción de la narración.
- Nube de palabras de la narración.
- Estadísticas aproximadas del partido, incluyendo como mínimo goles, tiros de esquina y saques de banda.
- Video grupal de máximo 12 minutos que muestre la implementación y sus resultados.
- Entrega de la presentación en el GES el domingo 27 de septiembre, según las instrucciones del proyecto.

## 2. Acuerdos que deben tomar los tres antes de comenzar

Durante la primera reunión, el equipo debe:

1. Elegir un partido cuya narración completa esté disponible y sea clara.
2. Guardar el enlace y los datos del partido: equipos, fecha, competición y resultado real.
3. Definir un solo formato para la transcripción, preferiblemente una línea por intervención o evento.
4. Acordar las estadísticas que se intentarán detectar. Como mínimo:
   - Goles.
   - Tiros de esquina.
   - Saques de banda.
   - Tiros o remates.
   - Faltas.
   - Tarjetas amarillas y rojas.
   - Fuera de juego, si la narración permite identificarlo.
5. Crear una tabla de referencia con las estadísticas oficiales del partido para medir qué tan cercana es la estimación.
6. Definir los nombres de los integrantes en lugar de "Integrante 1", "Integrante 2" e "Integrante 3" en este documento.

## 3. Distribución equitativa de responsabilidades

Cada integrante es responsable de un componente principal, participa en la integración y explica su parte en el video. Ninguna parte se considera terminada hasta que haya sido revisada por otro integrante.

### Integrante 1 - Obtención, transcripción y preparación de los datos

**Responsabilidad principal:** producir una narración completa, ordenada y lista para ser analizada.

Tareas:

1. Localizar y descargar o registrar la fuente de la narración elegida por el grupo.
2. Extraer o elaborar la transcripción completa del partido.
3. Conservar dos versiones:
   - `narracion_original.txt`: texto sin modificaciones importantes.
   - `narracion_limpia.txt`: texto corregido y organizado para el análisis.
4. Eliminar elementos que no pertenecen al partido, como anuncios, pausas comerciales o introducciones extensas.
5. Mantener las expresiones futbolísticas relevantes; por ejemplo, "tiro de esquina", "córner", "gol", "saque de banda" y "tarjeta amarilla".
6. Separar la narración por líneas y conservar marcas de tiempo cuando estén disponibles.
7. Documentar la procedencia del audio, video o texto y explicar cómo se obtuvo la transcripción.
8. Entregar al Integrante 2 una muestra inicial y después la versión completa.
9. Entregar al Integrante 3 fragmentos representativos de cada tipo de evento para construir y probar las reglas de conteo.
10. Revisar el código de preprocesamiento del Integrante 2 y comprobar que no elimine términos futbolísticos importantes.

Entregables propios:

- Fuente y ficha del partido.
- Transcripción original.
- Transcripción limpia.
- Explicación breve del proceso de obtención y limpieza.
- Lista de problemas encontrados en la narración y cómo se resolvieron.

### Integrante 2 - Preprocesamiento lingüístico y nube de palabras

**Responsabilidad principal:** transformar la narración en texto procesable y generar el análisis visual de palabras.

Tareas:

1. Crear el módulo de preprocesamiento de texto.
2. Normalizar mayúsculas, minúsculas, signos, espacios y variantes ortográficas sin perder información útil.
3. Tokenizar el texto y retirar palabras vacías del español.
4. Crear una lista adicional de palabras frecuentes de la narración que no aporten al análisis, como muletillas del comentarista.
5. Proteger términos compuestos y relevantes, por ejemplo "tiro de esquina", "saque de banda", "tarjeta amarilla" y "fuera de juego".
6. Calcular y presentar las palabras o expresiones más frecuentes.
7. Generar la nube de palabras con título, colores legibles y resolución adecuada para el video.
8. Dejar el preprocesamiento en funciones reutilizables para que el Integrante 3 utilice exactamente el mismo texto normalizado.
9. Comparar los resultados obtenidos con la transcripción original para detectar pérdidas o alteraciones importantes.
10. Revisar una muestra de los eventos detectados por el Integrante 3 y señalar falsos positivos o eventos omitidos.

Entregables propios:

- Código de limpieza, normalización y tokenización.
- Lista documentada de palabras vacías y expresiones protegidas.
- Tabla de frecuencias.
- Imagen final de la nube de palabras.
- Explicación de las decisiones de preprocesamiento.

### Integrante 3 - Extracción de eventos, estadísticas y evaluación

**Responsabilidad principal:** identificar eventos futbolísticos en el texto, estimar las estadísticas y medir la calidad de los resultados.

Tareas:

1. Diseñar un diccionario de palabras, sinónimos y patrones para cada evento. Ejemplos:
   - Gol: "gol", "anota", "marca".
   - Tiro de esquina: "córner", "tiro de esquina".
   - Saque de banda: "lateral", "saque de banda".
   - Tarjeta: "amonestado", "amarilla", "expulsado", "roja".
2. Implementar el conteo de eventos usando el texto preprocesado del Integrante 2.
3. Añadir reglas de contexto para evitar conteos incorrectos. Por ejemplo, "casi gol", "gol anulado" o la repetición de una jugada no deben contarse automáticamente como goles válidos.
4. Intentar separar los eventos por equipo cuando la narración contenga información suficiente.
5. Generar una tabla final con:
   - Estadística.
   - Estimación obtenida.
   - Valor oficial.
   - Diferencia absoluta.
   - Porcentaje de acierto, cuando sea aplicable.
6. Seleccionar ejemplos de aciertos, falsos positivos y eventos no detectados.
7. Crear un resumen de resultados y de las limitaciones del método.
8. Preparar la salida final para que pueda ejecutarse de principio a fin y producir las estadísticas de forma reproducible.
9. Entregar al Integrante 1 los casos dudosos para verificarlos contra la narración original.
10. Revisar la metodología escrita por el equipo y comprobar que coincida con lo que realmente hace el programa.

Entregables propios:

- Diccionario o catálogo de eventos y sinónimos.
- Código para detectar y contar eventos.
- Tabla de estadísticas estimadas y oficiales.
- Evaluación de errores y limitaciones.
- Resumen final de hallazgos.

## 4. Flujo continuo de trabajo

El equipo debe trabajar mediante entregas pequeñas. No es necesario esperar a tener toda la transcripción para empezar el análisis.

### Fase 1 - Preparación conjunta

- Los tres seleccionan el partido y acuerdan las estadísticas objetivo.
- El Integrante 1 entrega una muestra de entre 5 y 10 minutos de narración.
- El Integrante 2 prueba la limpieza y la tokenización con esa muestra.
- El Integrante 3 diseña el primer diccionario de eventos y lo prueba con la misma muestra.

**Resultado de la fase:** una prueba pequeña que recorre todo el proceso desde la narración hasta las estadísticas.

### Fase 2 - Desarrollo en paralelo

- El Integrante 1 completa y depura la transcripción.
- El Integrante 2 termina el preprocesamiento, las frecuencias y una primera nube de palabras.
- El Integrante 3 amplía las reglas de extracción y prepara la tabla de evaluación.
- Cada integrante registra sus decisiones, dificultades y resultados mientras trabaja; estas notas servirán para explicar la metodología en el video.

**Resultado de la fase:** los tres componentes principales funcionan por separado con la narración completa.

### Fase 3 - Integración y revisión cruzada

- El Integrante 1 verifica manualmente una muestra de los eventos extraídos.
- El Integrante 2 confirma que el texto procesado conserva las expresiones necesarias para el conteo.
- El Integrante 3 ejecuta el flujo completo y compara los resultados con las estadísticas oficiales.
- Los tres corrigen los errores detectados y acuerdan qué limitaciones deben declararse.

**Resultado de la fase:** una ejecución reproducible que genera la nube de palabras y la tabla final de estadísticas.

### Fase 4 - Presentación y entrega

- Los tres preparan un guion único y realizan al menos un ensayo cronometrado.
- Cada integrante presenta su componente y muestra evidencia de su funcionamiento.
- Se graba el video, se comprueba el audio, la imagen y la duración, y luego se sube al GES.

**Resultado de la fase:** video final de máximo 12 minutos y todos los archivos organizados para la entrega.

## 5. Revisión cruzada obligatoria

| Trabajo producido | Responsable | Revisor principal |
|---|---|---|
| Transcripción y limpieza manual | Integrante 1 | Integrante 2 |
| Preprocesamiento y nube de palabras | Integrante 2 | Integrante 3 |
| Extracción y evaluación de estadísticas | Integrante 3 | Integrante 1 |
| Integración completa | Los tres | Los tres |
| Guion y video | Los tres | Los tres |

El revisor debe ejecutar o leer el entregable, dejar observaciones concretas y confirmar que las correcciones fueron atendidas.

## 6. Estructura sugerida de archivos

```text
proyecto_final_text_mining/
├── README.md
├── Proyecto.pdf
├── datos/
│   ├── narracion_original.txt
│   ├── narracion_limpia.txt
│   └── estadisticas_oficiales.csv
├── src/
│   ├── preprocesamiento.py
│   ├── extraccion_eventos.py
│   └── ejecutar_proyecto.py
├── resultados/
│   ├── frecuencia_palabras.csv
│   ├── nube_palabras.png
│   └── estadisticas_estimadas.csv
├── documentacion/
│   ├── metodologia.md
│   ├── evaluacion.md
│   └── guion_video.md
└── requirements.txt
```

La estructura puede adaptarse a las herramientas que use el grupo, pero todos deben trabajar sobre los mismos archivos de entrada y conservar los resultados finales.

## 7. Distribución sugerida del video

Para no exceder los 12 minutos, se recomienda una duración total de entre 10:30 y 11:30 minutos.

| Sección | Responsable | Tiempo aproximado |
|---|---|---:|
| Presentación del problema, partido y objetivo | Integrante 1 | 1:00 |
| Obtención y preparación de la narración | Integrante 1 | 2:15 |
| Preprocesamiento, frecuencias y nube de palabras | Integrante 2 | 3:15 |
| Extracción, estadísticas y comparación oficial | Integrante 3 | 3:15 |
| Demostración del flujo completo | Los tres | 1:00 |
| Limitaciones, conclusiones y cierre | Los tres | 0:45 |
| **Total estimado** |  | **11:30** |

Cada integrante debe hablar aproximadamente el mismo tiempo y mostrar su contribución en funcionamiento.

## 8. Lista de comprobación para la entrega

- [ ] El partido y la fuente están identificados.
- [ ] La narración original está completa.
- [ ] La narración limpia conserva los términos futbolísticos relevantes.
- [ ] El código puede ejecutarse desde el inicio hasta producir los resultados.
- [ ] La nube de palabras es legible y representa la narración procesada.
- [ ] Se estiman al menos goles, tiros de esquina y saques de banda.
- [ ] Las estadísticas estimadas se comparan con datos oficiales.
- [ ] Se documentan la metodología, las reglas, los errores y las limitaciones.
- [ ] Cada componente fue revisado por otro integrante.
- [ ] El video muestra la implementación y los resultados.
- [ ] Los tres integrantes participan de forma equilibrada en el video.
- [ ] El video dura menos de 12 minutos.
- [ ] Los archivos finales tienen nombres claros y están organizados.
- [ ] La presentación fue subida correctamente al GES.

## 9. Criterio para considerar terminado el proyecto

El proyecto está terminado cuando una persona puede tomar la narración seleccionada, ejecutar el proceso documentado y obtener la nube de palabras y la tabla de estadísticas sin realizar pasos ocultos. Además, el equipo debe poder explicar por qué se eligieron las reglas usadas, qué tan cerca quedaron las estimaciones de los valores oficiales y cuáles son las principales limitaciones del enfoque.
