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