---
descripcion: "Un agente por defecto; N agentes solo cuando la tarea lo paga (lectura paralela sí, escritura solo con partición limpia); el coste se dice en voz alta"
capa: metodo
tipo: guia
estado: vigente
autor: NEOCAM
creado: 2026-07-25
---

# N=1 por defecto, N por evidencia

Con presupuesto igualado, multi-agente no supera a un buen agente único: N>1 se justifica, no se presume. El paralelismo paga limpio en LECTURA (investigación, búsqueda: hilos independientes). La escritura paralela exige partición disjunta del trabajo y aun así deja conflictos semánticos que el merge no ve: revisión posterior obligatoria.

Multiplicar agentes es multiplicar coste (3-15x tokens). El coste se dice en voz alta y el dial lo tiene la dirección. Empezar por el patrón más simple; subir de peldaño solo con dolor demostrado.
