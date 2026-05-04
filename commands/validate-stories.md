---
name: validate-stories
description: "Validar calidad de user stories (scoring + antipatrones)"
---

> **Paso 0 (obligatorio): Cargar ground-rules.** Antes de proceder, lee `shared-config.md` y aplica:
> - **§Filosofía del Plugin** — modo copiloto, NO inventar, preguntar antes de generar
> - **§Estilo de Escritura** — frases ≤30 palabras, sin adjetivos sin datos, NUNCA inventar métricas
> - **§Antipatrones Compartidos** — los 7 antipatrones a detectar
>
> Si no puedes leer el fichero, detén la ejecución y reporta el problema.

Ejecuta `/user-story-quality-coach` para validar stories generadas.

**Input necesario:** User stories a validar (de `/stories` o de tu issue tracker).

**Proceso:**
1. Leer el SKILL.md de `skills/user-story-quality-coach/`
2. Para cada story:
   - Evaluar scoring 6 dimensiones
   - Detectar antipatrones (7 tipos)
   - Generar reporte individual
3. Si hay múltiples stories (sprint/backlog):
   - Generar reporte de equipo
   - Comparar con histórico
   - Identificar patrones de mejora

**Output:** Reporte de calidad con scoring + antipatrones + recomendaciones.
