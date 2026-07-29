---
descripcion: "Los agentes no responden de memoria: buscan fuera, citan con fecha y verifican con herramientas; etiqueta epistémica siempre"
capa: metodo
tipo: guia
estado: vigente
autor: NEOCAM
creado: 2026-07-25
---

# Evidencia antes que memoria paramétrica

Para HECHOS: no se inventan jamás; se buscan fuera, se citan y se verifican. Para HIPÓTESIS: se inventan todas las que hagan falta, etiquetadas, y se llevan al experimento más barato que pueda matarlas. La etiqueta epistémica (`hecho` / `hipotesis` / `especulacion` en frontmatter) es obligatoria; confundir los tres estados produce basura convincente.

El gate es arquitectónico, no exhortativo (pedir "busca antes" en un prompt no es un gate):

- Regla de una línea + herramientas de búsqueda siempre disponibles.
- En trabajo serio, separación dura investigar→crear: la etapa de creación recibe las referencias recogidas, no memoria del modelo.
- Cita = enlace vivo + relevante + **respalda el hecho** (las dos primeras capas sin la tercera son teatro). Verificar visitando la fuente, nunca de memoria. Toda cita con `fecha_acceso`; claims importantes, dos fuentes.
- Paso opcional de búsqueda de contradicción antes de fijar decisiones importantes.
- Presupuesto escalonado: consulta simple = 1 agente y pocas llamadas; más búsqueda sin síntesis EMPEORA la precisión. La métrica es citas efectivas, no fuentes tocadas.
