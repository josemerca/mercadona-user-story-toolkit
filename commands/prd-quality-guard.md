---
name: prd-quality-guard
description: "Evaluar calidad de un PRD como quality gate"
---

Ejecuta `/prd-quality-guard` para evaluar la calidad de un PRD antes de pasar a research.

**Input necesario:** Ruta de fichero, URL del documento, o contenido pegado del PRD.

**Proceso:**
1. Cargar PRD desde la fuente que indique el usuario (fichero local, URL pública, o contenido pegado)
2. Leer el SKILL.md de `skills/prd-quality-guard/`
3. Ejecutar análisis completo: Inventario → D1 (EAC), D2 (EFC+Métricas), D3 (Discovery+Scope) → Gate Decision
4. Detectar antipatrones PRD-específicos (AP-PRD-1 a AP-PRD-5)
5. Score ≥7 → PASS (proceder a research) | 5-6 → CONDICIONAL | <5 → FAIL

**Siguiente paso:** Si PASS → ejecutar `/research` con source_type=PRD
