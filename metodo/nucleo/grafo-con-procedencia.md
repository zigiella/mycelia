---
descripcion: "La memoria es el sistema nervioso, par del repo de código: markdown+git, procedencia en escritura, invalidar sin borrar, cuarentena para lo externo, rollback nombrado"
capa: metodo
tipo: guia
estado: vigente
autor: NEOCAM
creado: 2026-07-25
---

# El grafo con procedencia

La memoria compartida es el órgano principal del arnés, par del repo de código, nunca "bandeja subordinada". Sustrato: markdown plano + git (la convergencia del campo 2025-2026: da procedencia, escritura auditada, sync multi-equipo, rollback y borrado, gratis). Índices derivados (vector, grafo, MAPA) siempre regenerables, jamás fuente de verdad, jamás editados a mano.

Reglas de escritura, ancladas en el enforcement del repo (no en la buena voluntad; la disciplina es tan fuerte como el equipo más débil que escriba):

- **Procedencia en tiempo de escritura**: frontmatter conforme a [[esquema-frontmatter]] + commit con identidad. La procedencia de confianza es quién autenticó el push (llave por equipo); la identidad inline es metadato.
- **Invalidar, no borrar**: `estado: superado` + `supersedido_por`, el texto se queda. Y su gemela: antes de usar una nota, filtrar por `estado`.
- **Cuarentena para lo externo**: el envenenamiento por contenido externo es práctico (>95% de éxito solo con queries); lo derivado de fuera entra con `cuarentena: true` y lo promueve el bibliotecario evaluando también si contiene instrucciones, no solo si es cierto.
- **Consolidar es exclusivo del bibliotecario**, con `consolida:` (procedencia transitiva, para poder rastrear y limpiar un envenenamiento propagado).
- **Rollback como operación nombrada**: revertir el commit del hecho envenenado + pase del bibliotecario sobre lo que bebió de él.
- **Linaje por cifra.** Una nota puede traer varias cifras del mismo origen con distinto entorno y momento, y ahí la procedencia por nota no basta. Toda **cifra dinámica** (la que cambia con el tiempo o el entorno) lleva junto al número su entorno y su snapshot: `1.846.525 reseñas [BigQuery, snapshot 2026-07-22]`. No aplica a constantes ni a cifras de un paper que la nota ya fecha. Nace de una cicatriz real: dos cifras verdaderas del mismo origen (100.004 y 1.846.525) con un día de diferencia, y sin etiquetar, la vieja se toma por actual y se construye encima. Complementa invalidar-no-borrar: cuando llega una cifra nueva, la vieja se fecha, no se borra.
- Escribir poco y con criterio es una defensa: memoria conservadora > memoria agresiva.
