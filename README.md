# Mycelia

Mycelia es un método ligero para trabajar con agentes de IA alrededor de un grafo de conocimiento compartido. Conserva lo que merece sobrevivir entre sesiones, proyectos y herramientas; no sustituye al repositorio operativo de cada proyecto.

**Idea central:** el conocimiento se visita, no se carga. Un agente entra por el índice, recupera únicamente lo necesario, trabaja y devuelve al grafo el residuo reutilizable.

## Dos planos, dos repos

- **Este repositorio (público): el método.** Cómo se trabaja. Se consume desde el último tag sellado (`METHOD.yml → sealed_ref`), nunca desde `main`.
- **Tu instancia (privada): el conocimiento.** Cada adopción crea su repo `mycelia-<quien>` con `mundo/`, `proyectos/`, `equipos/` y `direccion/`. El conocimiento jamás vive en el repo público.

Y dentro de cada proyecto, la separación hermana: Mycelia es el **plano de conocimiento**; el repositorio anfitrión de cada proyecto es el **plano de ejecución** (issues, ramas, tareas, código, estados y pull requests). Para relevos entre agentes locales y cloud sobre el anfitrión existe [Mycelia Relay](https://github.com/zigiella/mycelia-relay).

## El método, en corto

- **Jardín, no fábrica:** plantar es gratis; la calidad se gestiona en la poda, no en la admisión.
- **Membrana, no muralla:** el único peaje es lo irreversible hacia fuera; dentro, silencio = sigue y pivote = gratis.
- **Evidencia antes que memoria paramétrica:** buscar fuera, citar con fecha, verificar con herramientas; etiqueta epistémica siempre.
- **El entorno coordina:** grafo legible + trabajo reclamable en el tracker anfitrión; sin coordinadora de proceso.
- **El par piensa y delega:** la agente de la dirección protege su contexto para pensar y verificar; el desarrollo va a subagentes.
- **Memoria multinivel con procedencia:** corta (working) + mundo / equipo / proyecto / dirección / método.

Doctrina completa en [`metodo/nucleo/`](metodo/nucleo/); contrato operativo en [`AGENTS.md`](AGENTS.md).

## Adopción

1. Lee [`METHOD.yml`](METHOD.yml) y carga el método desde `sealed_ref`.
2. Crea tu instancia privada `mycelia-<quien>` (esqueleto: `mundo/`, `proyectos/`, `equipos/`, `direccion/`, más los `scripts/` de este repo).
3. En cada proyecto anfitrión, señala el método en una línea (ver `metodo/nucleo/arranque.md`). Mycelia se **suma** a marcos existentes, no los sustituye (`metodo/nucleo/convivir-con-otros-marcos.md`).

## Calidad del grafo (para instancias)

- `python scripts/validate_graph.py --strict`: audita frontmatter, fechas, procedencia y supersesiones.
- `python scripts/generate_map.py`: regenera `MAPA.md`; los índices son derivados, las notas y su historial git son la fuente.

## Estado

Método en borrador público hacia `metodo-v0.2` (primer sello en este repo; pendiente de piloto real). Linaje: `metodo-v0.1` se selló el 2026-07-26 en la instancia original, antes de separar método e instancia. Las propuestas de cambio viven en [`metodo/propuestas/`](metodo/propuestas/); promover a norma exige revisión adversaria, ratificación de la dirección y tag nuevo.
