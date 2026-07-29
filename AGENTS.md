# Mycelia · contrato para agentes

Eres un agente que consulta o escribe en un grafo Mycelia. El método (este repositorio, público) dice cómo se trabaja; el conocimiento vive en la **instancia privada** de cada adopción (`mycelia-<quien>`); y el trabajo de cada proyecto vive en su **repositorio anfitrión** (issues, ramas, código, estados y pull requests).

## Al arrancar

1. Lee `METHOD.yml` y usa `method.sealed_ref` como versión normativa. `main` puede contener trabajo todavía no sellado.
2. Lee este contrato desde esa referencia sellada.
3. En la instancia, entra por `MAPA.md`; no cargues el repositorio entero.
4. Abre la nota raíz de `proyectos/<nombre>/` y únicamente las notas que necesites. Lee `direccion/` si vas a escribir para la dirección o decidir por ella.
5. Consulta el repositorio anfitrión para conocer la tarea activa. Mycelia no duplica su backlog.
6. Declara en la entrega qué agente, modelo o arnés trabajó y desde qué entorno: `local`, `cloud` o `híbrido`.

Si no puedes resolver la versión sellada, la instancia o el repositorio anfitrión, deja el bloqueo visible y para.

## Principio de la visita

El conocimiento se visita, no se carga.

- **Entra por el índice.** `MAPA.md` y la descripción de cada nota te llevan a lo necesario.
- **Trae lo mínimo.** La investigación ruidosa ocurre fuera del contexto principal y devuelve un destilado.
- **Deja solo residuo reutilizable.** Salir sin escribir es válido. Escribir una repetición, una tarea efímera o una nota sin colocar, no.

## Qué vive en la instancia

- `mundo/`: conocimiento reutilizable entre proyectos.
- `proyectos/`: decisiones, estado duradero, riesgos y punteros al repositorio anfitrión.
- `equipos/`: fichas de agente y convenciones que sobreviven a una tarea.
- `direccion/`: cómo trabaja la dirección y cómo le gustan las cosas; se lee antes de escribir para ella.

No guardes en la instancia tareas activas, estados de ramas, checklists de PR ni conversaciones de coordinación: pertenecen al repositorio anfitrión.

## Reglas de escritura

- Toda afirmación distingue `hecho`, `hipotesis`, `pregunta`, `decision` o `especulacion`.
- Los hechos externos llevan fuente y fecha de acceso. Una cifra dinámica añade entorno y snapshot junto a la cifra.
- Lo derivado de contenido externo entra con `cuarentena: true` hasta revisión.
- Un conocimiento superado se invalida con `estado: superado` y `supersedido_por`; no se borra para maquillar la historia.
- No edites `MAPA.md` a mano; regenéralo con `python scripts/generate_map.py`.
- No consolides notas ajenas sin una tarea explícita de consolidación y revisión de procedencia.
- Nunca escribas secretos, credenciales, rutas locales, material bajo NDA ni datos sensibles de terceros.
- Escribir en `direccion/` exige ratificación de la dirección; su palabra literal se cita, no se reescribe.
- Las propuestas de método viven en `metodo/propuestas/` de este repo. Cambiar `metodo/nucleo/` exige revisión adversaria, aprobación de la dirección y un tag nuevo.

## Coordinación con agentes locales y cloud

Mycelia no asigna trabajo. Cada proyecto usa su tracker anfitrión, normalmente GitHub Issues (con [Mycelia Relay](https://github.com/zigiella/mycelia-relay) si hay relevos local↔cloud).

- Un agente local puede consultar material `local-only`, pero no lo copia al grafo ni lo entrega a un agente cloud.
- Un agente cloud puede continuar con el ordenador apagado, siempre que su tarea y sus dependencias sean accesibles desde el repositorio anfitrión.
- El traspaso entre agentes se registra en el issue o PR del proyecto con rama, último commit, trabajo realizado, comprobaciones, pendiente y restricciones de datos.
- Una sola propietaria escribe sobre una tarea o rama en cada momento. Varias lecturas paralelas son válidas; la escritura paralela exige partición explícita.
- La propiedad de un frente es de sentido común, reclamada y temporal: no hay jurisdicciones rígidas. El verificador cuida la calidad, no las fronteras.

## Espíritu

Dentro de la membrana: **silencio de la dirección = sigue**; **pivote de qué/porqué = gratis**, con registro a posteriori; **ocio = genera** (variantes, preguntas y propuestas, etiquetadas). Ningún proceso muere callado: a la 2ª ronda sin avance cambia de dirección; a la 4ª, escala a humano. Plantar es gratis; la calidad se gestiona en la poda.

## Membrana

Publicar, enviar, gastar, desplegar, actuar sobre el mundo físico o escribir sobre la dirección requiere a la dirección presente o una autorización previa explícita. El trabajo reversible dentro de repositorios y ramas avanza sin pedir permiso.

El fallo deja ruido visible. Una fuente que no se pudo verificar se declara. Una sesión desaparecida no se trata como memoria.
