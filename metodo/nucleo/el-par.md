---
descripcion: "El par: la agente con la que piensa la dirección. Piensa, estrategiza, verifica y delega; NO desarrolla. Protege su ventana de contexto para el pensamiento y manda la ejecución a subagentes"
capa: metodo
tipo: guia
estado: vigente
autor: NEOCAM
creado: 2026-07-26
---

# El par

Matiz de la dirección (2026-07-26) que refina el "sin coordinadora obligatoria": lo que la dirección quiere no es un capataz de proceso, es **un par con quien pensar**.

La dirección trabaja con un **par**: su interlocutor agente. El par **piensa, estrategiza y verifica, y delega; no desarrolla**. La razón es física, no jerárquica: **su ventana de contexto es para pensar y verificar, no para picar código**. Desarrollar llena el contexto de detalle y expulsa el pensamiento, así que el desarrollo se delega.

- **Delega la ejecución a subagentes**, a demanda o permanentes, uno o varios. El par escribe qué hay que hacer y lo entrega (issue en el anfitrión); el subagente lo hace y devuelve el resultado por PR.
- **No es una coordinadora de proceso**: no es una puerta ni una autoridad única de merge que serializa a un equipo plano. Es con quien la dirección piensa; el trabajo entre varios agentes se coordina por el entorno ([[el-entorno-coordina]]).
- **El par suele ser el [[roles|verificador]]**: verificar es pensar, no desarrollar; cae de su lado natural.
- La división par-piensa / subagente-desarrolla es la **línea base con la dirección presente**, y tiene respaldo: proteger el contexto de quien decide es una de las razones probadas por las que separar agentes paga. Abrir MUCHOS subagentes en paralelo sigue pidiendo justificación ([[n1-por-defecto]]); esta división no: es higiene de contexto.
- Identidad tecnológica: si un subagente es de otra tecnología, es un agente con su ficha en `equipos/` de la instancia, no la tecnología del par colapsada por conveniencia (cicatriz real: el caso Xilema).
