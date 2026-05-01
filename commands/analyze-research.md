---
name: analyze-research
description: "Analizar notas de entrevistas y generar JTBDs"
---

Ejecuta los workflows de análisis + generación de JTBDs de `/research-from-prd`.

**Input necesario:** Notas de entrevistas + PRD de referencia.

**Proceso:**
1. Leer el SKILL.md de `skills/research-from-prd/`
2. Leer `skills/research-from-prd/references/analysis-to-jtbd.md`
3. Para cada entrevista:
   - Filtrar bad data (cumplidos, fluff, promesas futuras)
   - Extraer hechos y comportamientos
   - Extraer quotes literales
   - Mapear hallazgos contra PRD
4. Identificar patrones entre entrevistas
5. Ejecutar Gap Detection del Research (Paso Final):
   - Leer `skills/research-from-prd/references/gap-detection-research.md`
   - Evaluar cobertura y calidad de evidencia
   - Calcular Research Gap Score
6. Generar JTBDs con evidencia real

**Output:** JTBDs estructurados compatibles con `/jtbd-to-stories` + Research Gap Analysis.

**Siguiente paso:** `/stories` para generar user stories.
