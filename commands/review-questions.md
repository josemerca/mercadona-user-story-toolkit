---
name: review-questions
description: "Revisar preguntas de entrevista contra Mom Test"
---

> **Paso 0 (obligatorio): Cargar ground-rules.** Antes de proceder, lee `shared-config.md` y aplica:
> - **§Filosofía del Plugin** — modo copiloto, NO inventar, preguntar antes de generar
> - **§Estilo de Escritura** — frases ≤30 palabras, sin adjetivos sin datos, NUNCA inventar métricas
> - **§Antipatrones Compartidos** — los 7 antipatrones a detectar
>
> Si no puedes leer el fichero, detén la ejecución y reporta el problema.

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
