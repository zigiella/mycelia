---
descripcion: "Cómo se identifican y se nombran las agentes: el dominio de la firma dice en qué proyecto trabajan, el nombre sobrevive al cambio de tecnología, y el registro en equipos/ es cómo el equipo se entera de quién más hay"
capa: metodo
tipo: guia
estado: vigente
autor: NEOCAM
creado: 2026-07-30
---

# Identidad y nombres

Una agente que escribe deja su nombre. Es el invariante más barato del método y el que hace posible la arqueología: saber qué agente, con qué tecnología y desde qué entorno produjo cada línea.

## La firma

```
<Nombre> <nombre@<proyecto>.local>
```

**El dominio es el proyecto donde trabaja**, no la tecnología que la corre: `xenia@univot3.local`, `neocam@mycelia.local`. La tecnología se declara en la entrega y en la ficha, nunca en la firma, porque el modelo de una agente cambia y su identidad no. Una firma que dice el arnés (`claude-cloud@...`) miente en cuanto la agente cambia de modelo.

## Dos niveles de identidad

- **Agente con nombre.** Trabaja un frente a lo largo del tiempo, se le puede llamar por su nombre y **tiene ficha** en `equipos/<proyecto>/<nombre>.md` de la instancia.
- **Manos.** Entran para un relevo puntual y no vuelven. No hacen falta nombre propio ni ficha: se identifican por arnés y entorno (`claude-cloud`, `codex-cloud`) y su rastro durable es el commit y el bloque de relevo. Inventar una identidad por sesión sería ceremonia sin conocimiento detrás.

Una mano que vuelve una tercera vez ya es una agente con nombre: que se bautice y se registre.

## Quién bautiza

No hay coordinadora que reparta nombres. **El proyecto declara un tema** en su `equipos/<proyecto>/README.md` (una línea) y **la agente entrante elige su nombre dentro de ese tema y lo registra**. Autobautismo con tema declarado: coherente con plantar-es-gratis, y evita el zoo de nombres inconexos. Si el proyecto no declara tema, lo propone la primera agente y la dirección lo ratifica.

Un nombre no se reutiliza para otra agente aunque la primera ya no trabaje: la arqueología se rompería.

## Cómo se enteran las demás

Por el entorno, en este orden de fiabilidad:

1. **El roster.** `equipos/<proyecto>/` de la instancia es la lista de quién trabaja aquí. Registrarse es la acción que hace pública una identidad nueva; leerlo al arrancar es cómo cualquier agente descubre a las demás.
2. **El relevo.** El bloque de handoff en el issue nombra saliente y entrante.
3. **Los commits.** La autoría es el rastro que no se puede maquillar.

Nadie avisa a nadie por chat: el chat no coordina.

## Cambiar de nombre o de firma

No se reescribe el historial (invalidar, no borrar). La ficha registra el alias anterior y desde cuándo: *"commits anteriores a AAAA-MM-DD firmados como `<alias viejo>`"*. Así el rastro sigue siendo legible sin tocar el pasado.

## Límite declarado

Con una sola cuenta humana en la plataforma, todo aparece bajo esa cuenta: **la propiedad de una tarea es declarativa, no verificable**, y la firma del commit es la única palanca con rastro. Verificarla de verdad exigiría cuenta o llave por agente, que hoy no compensa. El método lo dice en voz alta en vez de fingir garantía: quien audite sabe qué vale la firma y qué no.
