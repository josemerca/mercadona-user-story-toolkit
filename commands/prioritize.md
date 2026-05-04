---
name: prioritize
description: "Priorizar stories validadas y generar batches de entrega iterativos"
---

> **Paso 0 (obligatorio): Cargar ground-rules.** Antes de proceder, lee `shared-config.md` y aplica:
> - **§Filosofía del Plugin** — modo copiloto, NO inventar, preguntar antes de generar
> - **§Estilo de Escritura** — frases ≤30 palabras, sin adjetivos sin datos, NUNCA inventar métricas
> - **§Antipatrones Compartidos** — los 7 antipatrones a detectar
>
> Si no puedes leer el fichero, detén la ejecución y reporta el problema.

Ejecuta `/story-prioritization` para priorizar stories validadas y generar batches de entrega iterativos.

**Input necesario:** Stories validadas con scoring 6 dimensiones (del paso anterior del pipeline o pegadas).

**Proceso:**
1. Leer el SKILL.md de `skills/story-prioritization/`
2. Cargar stories validadas
3. Evaluar cada story con 5 lentes (Value 30%, Learning 25%, Dependencies 20%, Risk of Delay 15%, Inv. Complexity 10%) usando `scripts/score_priority.py`
4. Construir grafo de dependencias → Checkpoint con usuario
5. **Generar 2 ordenamientos alternativos** (cast-wide):
   - **Plan Value-first:** prioriza Priority Score puro
   - **Plan Learning-first:** adelanta stories con Learning≥4 aunque su Priority Score sea menor — útil si hay incertidumbre técnica o de mercado
   - Presentar ambos con trade-offs (qué se entrega antes vs. qué se aprende antes)
   - Checkpoint con el usuario para elegir antes de generar batches finales
6. Generar batches iterativos del plan elegido (2-4 stories por batch)
7. Validar reglas anti-waterfall (AW-1 a AW-5)
8. Generar reporte de priorización

**Siguiente paso:** Llevar Batch 1 a tu issue tracker como Sprint/Iteración (o pasarlo a Superpowers para implementación con `/superpowers:writing-plans`).
