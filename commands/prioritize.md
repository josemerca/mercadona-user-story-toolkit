---
name: prioritize
description: "Priorizar stories validadas y generar batches de entrega iterativos"
---

Ejecuta `/story-prioritization` para priorizar stories validadas y generar batches de entrega iterativos.

**Input necesario:** Stories validadas con scoring 6 dimensiones (del paso anterior del pipeline o pegadas).

**Proceso:**
1. Leer el SKILL.md de `skills/story-prioritization/`
2. Cargar stories validadas
3. Evaluar cada story con 5 lentes (Value 30%, Learning 25%, Dependencies 20%, Risk of Delay 15%, Inv. Complexity 10%)
4. Construir grafo de dependencias → Checkpoint con usuario
5. Generar batches iterativos (2-4 stories por batch)
6. Validar reglas anti-waterfall (AW-1 a AW-5)
7. Generar reporte de priorización

**Siguiente paso:** Llevar Batch 1 a tu issue tracker como Sprint/Iteración (o pasarlo a Superpowers para implementación con `/superpowers:writing-plans`).
