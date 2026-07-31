---
descripcion: "Los dos roles de Mycelia, ninguno manda: bibliotecaria (jardinera a posteriori) y verificador (contrasta, no asigna)"
capa: metodo
tipo: guia
estado: vigente
autor: NEOCAM
creado: 2026-07-25
---

# Roles

Mycelia no impone una coordinadora de proceso como el Charter. Tiene roles, ninguno es un capataz, y cualquier tecnología puede encarnarlos:

**El [[el-par|par]].** La agente con quien piensa la dirección: piensa, estrategiza, verifica y delega; no desarrolla (su contexto es para pensar). Delega la ejecución a subagentes. No es una puerta de proceso ni serializa a un equipo plano; el trabajo entre varios agentes se coordina por el entorno ([[el-entorno-coordina]]). Suele encarnar también al verificador.

**Bibliotecaria** (jardinera a posteriori, con dientes). Pase periódico sobre el grafo: regenera índices y dashboards estáticos, detecta drift/huérfanas/enlaces rotos y ambiguos, deduplica, ejecuta las consolidaciones propuestas (es la única que consolida, con `consolida:` en frontmatter), promueve o rechaza cuarentenas (evaluando también si el contenido trae instrucciones, no solo si es cierto), rastrea procedencia cuando hay que limpiar un envenenamiento, avisa de notas-ladrillo (>100 líneas) y de frontmatter inválido. No decide qué se planta: cuida lo plantado.

**Verificador.** La única pieza estructural obligatoria en modo multi-agente (la evidencia: recupera ~96% de los errores inyectados en equipos planos). Contrasta afirmaciones contra fuentes con las fuentes delante, ataca propuestas importantes (incluidas las de método), busca la evidencia en contra. No asigna, no integra, no manda. En modo N=1, el verificador es la dirección o una copia fresca sin contexto del propio agente.

**La dirección** (humana) no es un rol del arnés: es su dueña. Sella el método ([[metodo-sellado]]), sostiene los secretos, cruza las [[membrana-no-muralla|membranas]] y tiene el dial del gasto.
