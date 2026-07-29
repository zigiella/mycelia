---
descripcion: "La capa de dirección (direccion/ en la instancia): cómo trabaja la dirección y cómo le gustan las cosas; la leen todos sus agentes, se escribe solo con su ratificación; lo íntimo no entra al sistema"
capa: metodo
tipo: guia
estado: vigente
autor: NEOCAM
creado: 2026-07-25
---

# La capa de dirección

Lo que el sistema sabe de la dirección es **conocimiento de trabajo**: a qué se dedica, qué le gusta, cómo le gustan las cosas, cómo le gusta que se escriba, en qué proyectos anda, qué le gusta investigar. Vive en `direccion/` dentro de la instancia, y **todos los agentes de la instancia deben leerla** cuando escriban para ella o decidan por ella. No es un silo: es la capa que hace que cada agente nuevo no tenga que redescubrir a su directora.

Reglas:

- **Explícita siempre**: si no está en un fichero legible por la dirección, no existe. Prohibido el perfil inferido opaco (la lección de las memorias implícitas: contaminan y destruyen confianza).
- **Escribir aquí cruza la [[membrana-no-muralla|membrana]]**: es sobre ella, ella ratifica. Su palabra literal se cita, no se reescribe ni se "mejora".
- **Lo íntimo o sensible no entra al sistema, ni aquí ni en ningún sitio** (suelo duro): salud, credenciales, datos de terceros, material bajo NDA, biometría. Esta capa habla de cómo trabaja la dirección, no de quién es por dentro. Si algún día hiciera falta una capa íntima de verdad, se crearía entonces como repo aparte con acceso por necesidad y borrado de una pieza; no se construye la caja fuerte antes que las joyas.
- Preferir punteros a las fuentes de la dirección sobre copias de sus documentos.

Historia de esta nota: en v0.1 esta capa se diseñó como silo en repo aparte, previendo datos sensibles. La dirección aclaró (2026-07-28) que lo que quiere que el sistema aprenda es su forma de trabajar; con esa premisa, el silo era una caja fuerte sin joyas y la capa volvió al grafo. La versión de silo queda documentada aquí como opción futura, no como norma.
