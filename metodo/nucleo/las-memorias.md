---
descripcion: "El mapa de la memoria de Mycelia: la corta (working, en el contexto) y las largas (mundo, equipo, proyecto, dirección, método), cada una con su casa, su regla de compartición y quién lee/escribe"
capa: metodo
tipo: guia
estado: vigente
autor: NEOCAM
creado: 2026-07-25
---

# Las memorias

Mycelia no tiene "una" memoria: tiene una corta y varias largas, y **es el método el que le dice a cada agente cómo manejar cada una** (encargo de la dirección, 2026-07-25: el método configura al agente, no al revés).

## Memoria corta (working)

El contexto de la sesión. Efímera, vive en la ventana del agente, no en el grafo. La gobierna [[la-visita]]: trae lo mínimo, no acumules, y al salir consolida a la larga el poso que valga. La corta que no se deja escrita se pierde, y está bien: no todo merece pasar a larga. Esta distinción es la que hace ligero el arnés: casi todo el trabajo ocurre en corta.

## Memorias largas (en la instancia, con procedencia)

Cada una con su casa y su regla ([[grafo-con-procedencia]]):

- **mundo/** (pool) — hechos del mundo, compartidos por todos los proyectos de la instancia. Lectura libre; escritura mediada + cuarentena para lo externo.
- **equipos/<nombre>/** — fichas de agente (identidad + tecnología + qué sabe hacer) y convenciones que sobreviven a una tarea. El estado operativo (tareas, claims, handoffs) NO vive aquí: vive en el tracker del repositorio anfitrión de cada proyecto ([[el-entorno-coordina]]).
- **proyectos/<nombre>/** — qué construimos: decisiones con su porqué, estado duradero, riesgos, punteros al repo anfitrión.
- **direccion/** — cómo trabaja la dirección ([[la-capa-personal]]): la leen todos, se escribe con su ratificación.
- **metodo/** (en el repo público del método) — cómo trabajamos: núcleo sellado por tag ([[metodo-sellado]]) + propuestas abiertas.

Un agente, al [[arranque|arrancar]], aprende de dónde leer cada capa y qué puede escribir en cada una. Nombres tomados de la taxonomía estándar: la corta es *working*; mundo/equipo/proyecto/dirección son *semántica* por ámbitos; la bitácora de un proyecto es *episódica*; las guías y skills son *procedimental*.
