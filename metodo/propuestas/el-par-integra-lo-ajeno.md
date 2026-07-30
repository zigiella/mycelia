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

## Auditoría adversaria (2026-07-30): SIN VALE

Un adversario sin contexto la atacó tal como exige [[../nucleo/metodo-sellado]], advertido del conflicto de interés (la escribe quien recibe la autoridad). Veredicto: **sin vale**, con cuatro objeciones ALTA que el autor concede enteras:

- **A-01 · El test de autoría mide el diff, no la decisión.** El par escribe el issue, otra agente lo implementa, el par verifica *contra su propio issue* e integra. Formalmente «no lo escribió»; sustantivamente nadie ajeno miró la decisión.
- **A-02 · La cláusula «o» anula la salvaguarda.** «Lo integra la dirección **o** pasa por un adversario»: quien elige la vía, invoca al adversario y lee su veredicto es el par. Bucle cerrado operado por el auditado.
- **A-03 · La salvaguarda es inverificable, y el método ya lo sabía.** Con una sola cuenta humana, quién integró no deja rastro distinguible ([[../nucleo/identidad-y-nombres]] ya lo declara). El propio PR de esta propuesta figura mergeado por la cuenta de la dirección.
- **A-04 · Viola la regla que pretende enmendar.** [[../nucleo/metodo-sellado]]: «los procesos que proponen método argumentan desde evidencia y cicatrices, **no desde las preferencias de la dirección**». El problema declarado aquí es literalmente una preferencia, sin cicatriz, sin coste medido, y la delegación en que se apoya no está escrita en `direccion/`.

Y una omisión de fondo (**F-01**): la propuesta compara con un contrincante de paja. v0.2 **nunca dice que el autor integre lo suyo**; dice quién no integra y calla quién sí. La alternativa real observada siempre fue «integra la dirección».

**Alternativas que no consideré y que probablemente ganan:** separar *aprobar* de *pulsar el botón* (el par verifica y aprueba, el anfitrión integra solo con checks verdes: resuelve el problema real sin mover un milímetro de autoridad), e integración cruzada entre proyectos (que además escala con N en vez de embudar en 1, y es más fiel a [[../nucleo/el-entorno-coordina]] que esta propuesta).

**Estado:** a decisión de la dirección. El autor recomienda **rechazarla** en favor de las alternativas de arriba. Lo único que merece sobrevivir de ella es el hueco que sí destapó: **v0.2 dice quién no integra y nunca dice quién sí**, y eso hay que cerrarlo en cualquier caso.
