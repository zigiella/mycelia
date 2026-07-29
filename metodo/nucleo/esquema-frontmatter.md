---
descripcion: "El esquema de metadatos que toda nota del grafo debe llevar; validado por scripts/validate_graph.py en CI"
capa: metodo
tipo: guia
estado: vigente
autor: NEOCAM
creado: 2026-07-25
---

# Esquema de frontmatter

Toda nota del grafo abre con este frontmatter YAML. Campos obligatorios:

```yaml
---
descripcion: una línea que dice de qué va la nota (es lo que se lee en la visita sin abrirla)
capa: mundo | equipo | proyecto | direccion | metodo
tipo: hecho | hipotesis | pregunta | especulacion | decision | herramienta | cicatriz | propuesta | guia | ficha
estado: vigente | superado
autor: nombre del agente o persona
creado: AAAA-MM-DD
---
```

Condicionales:

```yaml
fuente: URL visitada (obligatorio si tipo: hecho con origen externo; "propio" si nace dentro)
fecha_acceso: AAAA-MM-DD (obligatorio si fuente es URL; las fuentes mueren, la fecha queda)
cuarentena: true (obligatorio si la nota deriva de contenido externo y aún no fue revisada)
supersedido_por: "[[nota-que-la-supera]]" (obligatorio si estado: superado)
consolida: ["[[fuente-1]]", "[[fuente-2]]"] (obligatorio en consolidaciones: procedencia transitiva)
---
```

Reglas: fechas siempre AAAA-MM-DD; los valores de `estado` y `tipo` son los de esta lista, sin sinónimos (`status`, `vigente: true` y variantes se rechazan); una nota, una idea (aviso a partir de ~100 líneas); el nombre de fichero es un slug único y estable (renombrar exige migrar los enlaces; mejor no renombrar). Para hechos derivados de datos, la convención de linaje por cifra (valor + entorno + snapshot junto a la cifra) está propuesta en `metodo/propuestas/` y se ratifica en el sello v0.2.

Nota de linaje: `pregunta` entró como etiqueta epistémica de primera clase a propuesta del equipo de univot3 (un hueco explícito que aún no es hipótesis); se ratifica con el sello v0.2.
