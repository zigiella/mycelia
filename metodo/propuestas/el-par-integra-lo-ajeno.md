---
descripcion: "Propuesta: el par integra el trabajo ajeno rutinario tras verificarlo, nunca el suyo; resuelve el choque entre la preferencia de la dirección y las reglas de roles/el-par selladas en v0.2"
capa: metodo
tipo: propuesta
estado: vigente
autor: NEOCAM
fuente: propio
creado: 2026-07-30
---

# Propuesta · el par integra lo ajeno, nunca lo suyo

**Problema que ataca.** La dirección expresó (2026-07-30) que prefiere que su par se encargue de los merges en vez de hacerlos ella. Eso choca de frente con dos frases de `metodo-v0.2`: el verificador «no asigna, **no integra**, no manda» ([[../nucleo/roles]]) y el par «no es una puerta ni una autoridad única de merge que serializa a un equipo plano» ([[../nucleo/el-par]]).

El choque es real y merece resolverse por escrito, no por costumbre: una práctica que contradice el método sellado y nadie nombra es la vía por la que la doctrina se erosiona en silencio.

**Lo que la regla vieja protegía.** No era «no toques el botón»: era **no seas juez y parte**, y **no crees una cola que serialice el trabajo de un equipo plano**. Ambas razones siguen siendo buenas. Lo que la formulación de v0.2 no vio es que la alternativa por defecto también las viola: si cada agente integra su propio trabajo, hay juez y parte en cada proyecto. Un par que integra trabajo **ajeno** tiene más independencia que el autor integrándose a sí mismo.

**Cambio concreto.** En [[../nucleo/roles]] y [[../nucleo/el-par]], sustituir «no integra» por la regla que preserva su razón:

> El par puede integrar el trabajo **que no ha escrito**, después de verificarlo. **Lo que el par escribe lo integra la dirección**, o pasa antes por un adversario de otra tecnología. Integrar no lo convierte en coordinadora de proceso: las agentes no esperan al par para trabajar, solo para integrar, y el trabajo se sigue coordinando por el entorno.

El suelo no se toca: lo irreversible hacia fuera (publicar, desplegar, enviar, gastar, cambiar reglas duras) lo cruza la dirección siempre ([[../nucleo/membrana-no-muralla]]).

**Qué empeora si se adopta (coste).** Dos riesgos, ambos con síntoma observable:

- **Serialización.** El par se vuelve cola si N proyectos canalizan sus PRs por él. Síntoma: PRs esperando. Mitigación declarada: devolver el merge rutinario a la agente del proyecto por clases de bajo riesgo (partición), no ampliar la cola.
- **Confianza excesiva en un solo par de ojos.** Si el par verifica y además integra, su error no lo caza nadie aguas abajo. Mitigación: el adversario de otra tecnología sigue siendo obligatorio para propuestas de método y para lo caro, y la dirección conserva el suelo.

**Estado.** Mientras no se selle, la dirección delegó explícitamente los merges (2026-07-30) y esa delegación manda por ser suya; lo que esta propuesta busca es que la norma escrita diga lo que la práctica hace. Si al leerla la dirección prefiere la formulación de v0.2, se rechaza y los merges vuelven a ella: la propuesta pierde, la doctrina gana.
