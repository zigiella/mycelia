---
descripcion: "Propuesta: convención de linaje por cifra (valor + entorno + snapshot) para hechos derivados de datos, traída del marco anfitrión univot3"
capa: metodo
tipo: propuesta
estado: vigente
autor: Xenia
fuente: propio
creado: 2026-07-26
---

# Propuesta · linaje por cifra para hechos derivados de datos

**Problema que ataca.** El frontmatter da procedencia **por nota** (`fuente` + `fecha_acceso`), suficiente para papers y herramientas. Pero una nota de mundo derivada de un almacén de datos suele contener **varias cifras del mismo origen con distinto entorno y momento**, y ahí la procedencia por nota no basta. Cicatriz real de univot3: la misma fuente reportó **100.004** reseñas (imagen local/BQ del 21-07) y **1.846.525** (sync BQ del 22-07); sin etiquetar entorno y snapshot por cifra, un agente posterior toma la vieja como actual y construye encima. El fallo no es de veracidad, es de **linaje**: las dos cifras son ciertas en su momento.

**Cambio concreto.** Recomendar en [[../nucleo/grafo-con-procedencia]] que toda cifra dinámica embebida en una nota lleve, junto al número, su **entorno** (local / warehouse / producción / definición / imagen) y su **snapshot** (`AAAA-MM-DD`). No es un campo nuevo de frontmatter obligatorio: es una convención de redacción para cifras (p. ej. `1.846.525 reseñas [BigQuery, snapshot 2026-07-22]`). Complementa `invalidar-no-borrar`: cuando llega una cifra nueva, la vieja no se borra, se fecha.

**Qué empeora si se adopta (coste).** Fricción de escritura: cada número pide dos etiquetas más, y en notas con muchas cifras se vuelve verboso. Riesgo de teatro de procedencia (etiquetar por ritual sin que aporte). Mitigación: aplicarlo solo a **cifras dinámicas** (las que cambian con el tiempo o el entorno), no a constantes ni a cifras de un paper ya fechado por la nota.
