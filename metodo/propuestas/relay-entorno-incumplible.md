---
descripcion: "Propuesta a Relay: qué hace una propietaria que no puede cubrir el entorno declarado en el issue (bloquear, reparticionar o degradar); hallazgo del piloto T3-004"
capa: metodo
tipo: propuesta
estado: vigente
autor: Xenia
fuente: propio
creado: 2026-07-29
---

# Propuesta · propietaria que no puede cumplir el entorno declarado

**Problema que ataca.** El issue declara un `Entorno de ejecución` (`local`, `cloud`, `either`, `hybrid`), y Relay tiene reglas para el agente local y para el agente cloud **por separado**. Pero no dice qué debe hacer una agente cuando **no puede cubrir el entorno declarado**.

Caso real del piloto T3-004: el issue declaraba `hybrid` (parte cloud, parte local), y la propietaria solo podía ejecutar el leg **local** — no tenía forma de invocar un arnés cloud. Relay no ofrece regla. Las tres salidas posibles llevan a resultados muy distintos:

- **bloquear** — marcar `blocked` y parar (conservador; deja valor sin entregar);
- **reparticionar** — ejecutar el subconjunto cubrible y dejar handoff del resto (lo que se hizo);
- **degradar** — simular el otro entorno (p. ej. otro agente del mismo arnés haciendo de "cloud").

La tercera es la peligrosa: produce un **veredicto falso**, porque no reproduce ninguna de las condiciones que el entorno declarado pretendía probar (aislamiento, ausencia de contexto compartido, ausencia de acceso a ficheros locales). En el piloto se descartó a propósito, pero por criterio de la agente, **no por protocolo**.

**Cambio concreto.** Añadir a `AGENTS.relay.md` una sección corta, "Entorno incumplible":

> Si la propietaria no puede cubrir el entorno declarado: (1) **no simules** el entorno que te falta — un relevo simulado invalida la evidencia; (2) ejecuta el subconjunto que sí cubres **solo si es separable** sin dejar el trabajo en estado incoherente; (3) deja `HANDOFF` indicando **qué entorno falta y para qué**; (4) si el subconjunto no es separable, marca `blocked` con el motivo. Registrar la incapacidad es parte del resultado, no un fallo que ocultar.

**Qué empeora si se adopta (coste).** Formaliza una salida ("ejecuta lo que puedas") que puede volverse **excusa por defecto**: agentes que reparticionan de forma rutinaria y entregan mitades, dejando el trabajo perpetuamente a medias entre entornos. El punto (2) —solo si es separable sin incoherencia— es el que contiene ese riesgo, y depende del juicio de la agente, que es justo lo que una norma quisiera no depender. Alternativa más dura, descartada por rígida: prohibir reparticionar y obligar siempre a `blocked`.
