---
name: stories
description: "Generar user stories desde JTBDs con evidencia"
---

Ejecuta `/jtbd-to-stories` para convertir JTBDs validados en user stories.

**Input necesario:** JTBDs con evidencia (output de `/analyze-research`) + PRD original (opcional, para contexto adicional).

**Proceso:**
1. Leer el SKILL.md de `skills/jtbd-to-stories/`
2. Para cada JTBD:
   - Paso 1: Obtener input (JTBDs + PRD)
   - Paso 2: Mapear JTBD → Story (formato JTBD Reforzado)
   - Paso 3: Extraer 3 Motivaciones (F+E+S)
   - Paso 4: Aplicar Wendel Checklist (4/4)
   - Paso 5: Definir Behavior Change (AHORA→NUEVO)
   - Paso 6: Calcular Scoring (6 dimensiones)
3. Generar stories con template completo

**Output:** User stories con scoring 6 dimensiones.

**Siguiente paso:** `/validate-stories` para validación final.
