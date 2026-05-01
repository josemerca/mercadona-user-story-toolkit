---
name: review-questions
description: "Revisar preguntas de entrevista contra Mom Test"
---

Ejecuta el workflow de revisión de preguntas de `/research-from-prd`.

**Input necesario:** Preguntas a revisar + contexto del PRD.

**Proceso:**
1. Leer el SKILL.md de `skills/research-from-prd/`
2. Leer `skills/research-from-prd/references/mom-test-principles.md`
3. Evaluar cada pregunta contra Mom Test + contexto del PRD
4. Detectar problemas:
   - Leading (sugiere respuesta)
   - Pide opinión sobre el producto
   - Pregunta sobre el futuro
   - Cerrada (sí/no)
   - Usa lenguaje del PRD
   - Sesgo de confirmación (en modo Validar)
5. Proponer alternativas

**Output:** Tabla con pregunta original → problema → alternativa + cobertura de gaps.
