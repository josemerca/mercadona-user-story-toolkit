---
name: build-story
description: "Crear una user story desde cero (sin documento previo, guía conversacional)"
---

> **Paso 0 (obligatorio): Cargar ground-rules.** Antes de proceder, lee `shared-config.md` y aplica:
> - **§Filosofía del Plugin** — modo copiloto, NO inventar, preguntar antes de generar
> - **§Estilo de Escritura** — frases ≤30 palabras, sin adjetivos sin datos, NUNCA inventar métricas
> - **§Antipatrones Compartidos** — los 7 antipatrones a detectar
>
> Si no puedes leer el fichero, detén la ejecución y reporta el problema.

Ejecuta `/user-story-builder` para crear una story de forma conversacional.

**Input necesario:** Idea, requerimiento o contexto del problema.

**Proceso:**
1. Leer el SKILL.md de `skills/user-story-builder/`
2. Guía en 6 fases:
   - Fase 1: Contexto Inicial (¿qué problema resolver?)
   - Fase 2: Descubrir el Job (¿qué trabajo necesita hacer el usuario?)
   - Fase 3: Especificar Usuario (Wendel Checklist 4/4)
   - Fase 4: 3 Dimensiones de Motivación (F+E+S)
   - Fase 5: Behavior Change (AHORA→NUEVO, START/STOP/DIFFERENT)
   - Fase 6: Generar Story completa con scoring

**Output:** User story completa con template JTBD Reforzado + scoring.

**Siguiente paso:** `/validate-stories` para validación.
