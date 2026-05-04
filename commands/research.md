---
name: research
description: "Diseñar entrevistas de usuario a partir de un PRD (Mom Test)"
---

> **Paso 0 (obligatorio): Cargar ground-rules.** Antes de proceder, lee `shared-config.md` y aplica:
> - **§Filosofía del Plugin** — modo copiloto, NO inventar, preguntar antes de generar
> - **§Estilo de Escritura** — frases ≤30 palabras, sin adjetivos sin datos, NUNCA inventar métricas
> - **§Antipatrones Compartidos** — los 7 antipatrones a detectar
>
> Si no puedes leer el fichero, detén la ejecución y reporta el problema.

Ejecuta `/research-from-prd` completo: Gap Detection → Diseño de entrevistas.

**Input necesario:** Ruta de fichero, URL del documento, o contenido pegado del PRD.

**Proceso:**
1. Cargar PRD
2. Leer el SKILL.md de `skills/research-from-prd/`
3. Ejecutar Paso 0: Gap Detection (si no se ha ejecutado antes)
4. Determinar modo:
   - **Descubrir**: Entrevistas exploratorias (problema poco explorado)
   - **Validar**: Entrevistas de validación (hipótesis ya formuladas)
5. Leer references:
   - `prd-to-interview-mapping.md` para mapeo PRD → preguntas
   - `mom-test-principles.md` para reglas de entrevista
6. Generar guión completo de entrevista con 5 fases

**Output:** Guión de entrevista + briefing interno + notas para moderador.

**Siguiente paso:** Realizar entrevistas → `/analyze-research` con las notas.

**Nota:** Si vienes de `/from-gsd` y tienes `phases/N/RESEARCH.md` con evidencia previa, indícalo al comando con `--evidence-from=.planning/phases/N/RESEARCH.md` para no duplicar trabajo.
