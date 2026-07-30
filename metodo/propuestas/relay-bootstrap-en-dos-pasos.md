---
descripcion: "Propuesta a Relay: documentar que labels y plantillas solo surten efecto desde la rama por defecto, y dar un paso de bootstrap; hallazgo del piloto T3-004"
capa: metodo
tipo: propuesta
estado: adoptada
adoptada_en: Mycelia Relay 0.2
autor: Xenia
fuente: propio
creado: 2026-07-29
---

# Propuesta · instalación de Relay en dos pasos

**Problema que ataca.** La instalación que describe el README ("copia estos archivos") tiene un **huevo-y-gallina** que aparece en la primera tarea real:

1. `.github/ISSUE_TEMPLATE/agent-task.yml` **solo surte efecto desde la rama por defecto**. Si la instalación llega por PR (como debe, para que la revise un humano) y el PR exige `human_merge: true`, entonces **el primer issue no puede usar la plantilla que ese PR está introduciendo**. En el piloto hubo que reproducir los campos a mano en el cuerpo del issue.
2. Las **etiquetas de estado no existen**. El README presenta `ready`, `working-local`, `working-cloud`, `paused-local`, `blocked`, `review`, `done` como el modelo de estados, pero nada las crea: hay que darlas de alta a mano antes del primer issue.

Resultado: la primera tarea bajo Relay se ejecuta **sin la mitad del andamiaje** que Relay promete, justo cuando la agente todavía no conoce el protocolo.

**Cambio concreto.** En el README de Relay, sustituir "Instalación en un proyecto" por **dos pasos explícitos**:

- **Paso 1 · Bootstrap (antes o junto al PR):** crear las etiquetas de estado, y advertir de que la plantilla de issue no estará disponible en la UI hasta que el PR se integre en la rama por defecto. Indicar que el primer issue puede crearse reproduciendo los campos de la plantilla en el cuerpo.
- **Paso 2 · Instalación por PR:** los cuatro archivos, con revisión humana.

Opcionalmente, incluir en `mycelia-relay` un script de bootstrap (equivalente a `scripts/validate_config.py`, que sí existe y funciona) que dé de alta las etiquetas de estado con sus colores.

**Qué empeora si se adopta (coste).** El README deja de poder leerse como "copia cuatro ficheros y ya": la instalación pasa a tener dos pasos y parece más pesada de lo que es, lo que puede desanimar la adopción en proyectos pequeños. Un script de bootstrap añade además superficie que mantener (permisos del token, colisión con labels existentes del repo). Mitigación: dejar el paso 1 como **checklist de tres líneas**, y el script como opcional.

**Adoptada** en Mycelia Relay 0.2 (2026-07-30). Nació de fricción real del piloto T3-004.
