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
estado: vigente | superado | adoptada
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
adoptada_en: donde vive ya la idea (obligatorio si estado: adoptada; p.ej. "Mycelia Relay 0.2")
consolida: ["[[fuente-1]]", "[[fuente-2]]"] (obligatorio en consolidaciones: procedencia transitiva)
temas: [tema-1, tema-2] (recomendado en mundo/: vocabulario corto y compartido que cruza carpetas)
contradice: ["[[nota-que-contradice]]"] (cuando un hecho choca con otro y ninguno gana todavía)
---
```

Sobre los dos últimos, que son la única concesión a la ontología (y se quedan aquí):

- **`temas`** existe porque las carpetas solo dan una faceta y un hecho sirve a varios proyectos. El vocabulario vive en la instancia (`mundo/TEMAS.md`), es corto, y lo amplía la bibliotecaria cuando un tema se repite; no se inventan temas de un solo uso.
- **`contradice`** es la relación tipada que más paga: un choque nombrado se puede resolver, uno silencioso envenena. Contradecir no es superar; mientras no haya resolución, ambas notas siguen vigentes y enlazadas.

Todo lo demás se relaciona con `[[wikilinks]]` sin tipo. Más vocabulario formal sería deuda que nadie valida.

Una propuesta termina de tres formas y las tres se registran: **adoptada** (`estado: adoptada` + `adoptada_en`, para no dejarla abierta fingiendo que sigue en debate), **rechazada** (`estado: superado` con el porqué, porque los rechazos enseñan) o **vigente** mientras se decide.

Reglas: fechas siempre AAAA-MM-DD; los valores de `estado` y `tipo` son los de esta lista, sin sinónimos (`status`, `vigente: true` y variantes se rechazan); una nota, una idea (aviso a partir de ~100 líneas); el nombre de fichero es un slug único y estable (renombrar exige migrar los enlaces; mejor no renombrar). Para hechos derivados de datos, la convención de linaje por cifra vive en `grafo-con-procedencia`.

Nota de linaje: `pregunta` entró como etiqueta epistémica de primera clase a propuesta del equipo de univot3 (un hueco explícito que aún no es hipótesis), ratificada en `metodo-v0.2`.
