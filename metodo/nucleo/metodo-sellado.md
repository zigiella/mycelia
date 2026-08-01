---
descripcion: "El auto-modelo con núcleo sellado: los agentes cargan el método desde el último tag aprobado por la dirección (METHOD.yml → sealed_ref), proponen en propuestas/, y solo la dirección promueve a norma"
capa: metodo
tipo: guia
estado: vigente
autor: NEOCAM
creado: 2026-07-25
---

# El método sellado

Mycelia se conoce a sí misma: este repositorio ES el método (principios como notas enlazables, propuestas, cicatrices, métricas) y cualquier agente puede proponer mejoras sobre él plantando en `metodo/propuestas/` ([[ocio-genera]] aplicado al método mismo).

Pero quien escribe el método programa a todos los agentes de todas las sesiones futuras: `metodo/nucleo/` es el peor objetivo de envenenamiento del sistema. El peaje mínimo que protege sin matar la auto-mejora:

- Los agentes cargan el método desde el **tag declarado en `METHOD.yml → sealed_ref`**, nunca desde `main`.
- Los agentes escriben solo en `metodo/propuestas/`; el núcleo no se toca.
- Promover propuesta a norma = editar núcleo + declarar el sello + tag: **solo la dirección**.
- **El tag sellado se declara a sí mismo.** El commit que se va a etiquetar ya lleva `sealed_ref: <ese mismo tag>`; después se etiqueta ese commit, y por último `main` queda apuntando al tag nuevo. Así, quien aterriza en un tag lee que ese tag es el sello y para, y quien aterriza en `main` salta una vez y para. Cualquier otro orden hace que cada tag apunte al anterior y que seguir la regla camine hacia atrás hasta `null`: es exactamente el fallo que tuvieron `metodo-v0.2` y `metodo-v0.2.1`, encontrado por una agente que siguió el arranque a la letra (Clara, mp1-escritores, 2026-07-31).
- Toda propuesta al núcleo pasa un [[roles|verificador]] de otro modelo/equipo, un resumen del cambio en lenguaje llano para la dirección, y enfriamiento.
- Los procesos que proponen o revisan método argumentan desde evidencia y cicatrices, no desde las preferencias de la dirección.
- La cuarentena no se lava en dos saltos: una propuesta que cite una nota derivada de contenido externo hereda su origen (procedencia transitiva).

Linaje: `metodo-v0.1` se selló el 2026-07-26 en la instancia original (método y conocimiento aún juntos). Desde la separación de planos, los sellos viven en este repositorio público; el primero será `metodo-v0.2`, tras piloto real y revisión adversaria.
