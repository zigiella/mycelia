---
descripcion: "Propuesta a Relay: el issue debe declarar qué parte de la tarea ya está cubierta y por qué commit; hallazgo del piloto T3-004"
capa: metodo
tipo: propuesta
estado: adoptada
adoptada_en: Mycelia Relay 0.2
autor: Xenia
fuente: propio
creado: 2026-07-29
---

# Propuesta · el issue declara la cobertura previa

**Problema que ataca.** Relay define el ciclo `ready → working → review → done` asumiendo que la tarea empieza en cero. En la práctica, cuando se adopta Relay sobre un **proyecto en marcha**, muchas tareas ya están hechas en parte. En el piloto T3-004 (primera tarea real bajo Relay), al escribir los criterios de aceptación se descubrió que **4 de 7 ya estaban cubiertos** por trabajo anterior. Si el issue no lo hubiera declarado, la agente entrante habría rehecho trabajo existente o, peor, lo habría sustituido por una versión distinta creyendo que partía de cero.

Esto no es un caso raro: es **el caso normal al instalar Relay**, y el propio Mycelia contempla sumarse a proyectos en marcha ("basta anclar el presente").

**Cambio concreto.** En `.github/ISSUE_TEMPLATE/agent-task.yml`, añadir un campo (opcional pero explícito) **"Estado de partida"**: qué criterios están ya cubiertos, por qué ruta y **por qué commit**. Y en `AGENTS.relay.md`, sección "Antes de trabajar", un punto: *comprueba el estado de partida declarado y verifícalo contra el repositorio antes de escribir; si difiere, corrige el issue antes de trabajar, no después*.

Forma sugerida en la práctica: criterios de aceptación como lista de casillas, con las ya cubiertas marcadas y una línea de "estado de partida" que enlace el commit. Coste de escritura: un minuto. Ahorro: una tarea rehecha.

**Qué empeora si se adopta (coste).** Un campo más en la plantilla, que en proyectos nuevos estará casi siempre vacío (ruido para el caso limpio). Y un riesgo real: un "estado de partida" **desactualizado o falso** es peor que ninguno, porque la agente entrante confía en él. Por eso el cambio en `AGENTS.relay.md` incluye la obligación de **verificarlo contra el repo**, no de creérselo: la declaración orienta, el commit manda.

**Adoptada** en Mycelia Relay 0.2 (2026-07-30). Nació de fricción real del piloto T3-004.
