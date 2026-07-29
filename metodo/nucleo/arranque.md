---
descripcion: "Cómo entra una sesión en Mycelia: la dirección señala método + instancia + proyecto en una línea; el agente lee AGENTS.md desde el tag sellado, se sitúa y trabaja. Ligero, por sesión, sin ritual de génesis"
capa: metodo
tipo: guia
estado: vigente
autor: NEOCAM
creado: 2026-07-25
---

# El arranque

Encargo de la dirección (2026-07-25): *"cada vez que abra un proyecto tengo que indicar a la agente que toque que vamos a trabajar con este método"*. Así es, y es deliberadamente ligero: **el método configura al agente**; el agente no necesita conocer Mycelia de antemano. El arranque es una frase; lo demás lo hace el agente leyendo.

## La señal (lo que dice la dirección)

Una línea con los punteros. Por ejemplo:

> Trabajamos con el método Mycelia (`github.com/zigiella/mycelia`, tag sellado según `METHOD.yml`). Instancia de conocimiento: `mycelia-<quien>`. Proyecto: `<nombre>`.

Si el proyecto usa relevos local↔cloud, el anfitrión lleva además `.relay.yml` y `AGENTS.relay.md` (Mycelia Relay), y la tarea concreta vive en su issue.

## Lo que hace el agente al arrancar

1. Lee `METHOD.yml` del método y carga `AGENTS.md` desde `sealed_ref`.
2. En la instancia: entra por `MAPA.md`, va a la nota raíz de `proyectos/<nombre>/` y lee `direccion/` si va a escribir para la dirección.
3. Se sitúa en el equipo (`equipos/` si existe) y **declara su identidad** (nombre + tecnología + entorno local/cloud); esa es su autoría en cada escritura.
4. Consulta el repositorio anfitrión (issue/tracker) para conocer la tarea activa; Mycelia no duplica el backlog.
5. Trabaja bajo la [[membrana-no-muralla|membrana]]; al salir, deja el residuo (corto→larga) y, si procede, el checkpoint/handoff en el anfitrión.

No hay ritual de génesis ni sello por sesión: el método ya está sellado; arrancar es leerlo. Un agente que no puede leer el método no trabaja a ciegas: deja ruido y para.
