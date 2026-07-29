---
descripcion: "Sin coordinadora de proceso: el trabajo entre agentes lo coordina el entorno legible (grafo + tracker anfitrión con trabajo reclamable); el verificador es la única pieza estructural obligatoria a N agentes"
capa: metodo
tipo: guia
estado: vigente
autor: NEOCAM
creado: 2026-07-25
---

# El entorno coordina

Mycelia no impone una coordinadora de proceso (puerta única, triaje, cola, llave, que serializa a un equipo plano). Lo que coordina **el trabajo entre agentes** es un **entorno compartido persistente y globalmente legible** con **trabajo reclamable**: el conocimiento en el grafo, y las tareas en el tracker del repositorio anfitrión (normalmente GitHub Issues, con Mycelia Relay si hay relevos local↔cloud). La tarea se publica con requisitos, el agente que se reconoce capaz la reclama, y el claim caduca sin progreso (un claim gratis produce sobre-compromiso: lección con 45 años, Contract Net).

Protocolo mínimo a N agentes: orden definido por el tracker, cada agente lee todo lo anterior (grafo + issue + rama), rol autoelegido. La evidencia 2026: este andamiaje mínimo bate al orquestador central y a la anarquía a la vez; el protocolo explica el triple de varianza de calidad que el modelo elegido. El raíl se endurece por-agente si su modelo es flojo (con modelos débiles la relación se invierte).

Esto no choca con [[el-par]]: el par es con quien piensa la dirección y a quien delega, no el capataz del proceso. El par entrega trabajo por el entorno como cualquiera; la coordinación entre manos la hace el entorno, no el par.

Roles sin mando ([[roles]]): el **bibliotecario** (jardinero a posteriori) y el **verificador**, la única pieza estructural obligatoria en modo N (los equipos planos son los mejores con agentes sanos y los peores con uno defectuoso; un inspector dedicado recupera ~96% de los errores). Verificar no es coordinar: contrasta, no asigna.

El chat no coordina (la información falsa se propaga por conformidad social); la memoria compartida no es un lujo del arnés: es el prerrequisito de coordinar sin jefa.
