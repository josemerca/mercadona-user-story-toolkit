---
name: split-stories
description: "Detectar stories demasiado grandes y proponer splits incrementales"
skill: story-splitting
---

> **Paso 0 (obligatorio): Cargar ground-rules.** Antes de proceder, lee `shared-config.md` y aplica:
> - **§Filosofía del Plugin** — modo copiloto, NO inventar, preguntar antes de generar
> - **§Estilo de Escritura** — frases ≤30 palabras, sin adjetivos sin datos, NUNCA inventar métricas
> - **§Antipatrones Compartidos** — los 7 antipatrones a detectar
>
> Si no puedes leer el fichero, detén la ejecución y reporta el problema.

Analiza stories para detectar red flags lingüísticos y propone splits incrementales.

**Input necesario:** User stories a analizar (de `/stories`, `/validate-stories` o de tu issue tracker).

**Proceso:**
1. Leer el SKILL.md de `skills/story-splitting/`
2. Para cada story:
   - Escanear las 6 categorías de red flags lingüísticos
   - Consultar tabla de decisión para seleccionar técnica
   - Aplicar heurísticas de splitting (9 técnicas disponibles)
   - Proponer 3-5 splits concretos con orden de entrega
3. Generar reporte con:
   - Diagnóstico de red flags
   - Splits propuestos (en formato User Story)
   - Orden de entrega recomendado
   - Impacto esperado en Dim 6 (Survivable Experiment)

**Output:** Stories divididas en incrementos pequeños, seguros y valiosos, listas para tu issue tracker.

**Nota:** Si las stories ya tienen Score Dim 6 ≥8, el splitting es opcional. Se recomienda ejecutar siempre después de `/validate-stories` para asegurar granularidad óptima.
