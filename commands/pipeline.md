---
name: pipeline
description: "Ejecutar pipeline completo: PRD/GSD → Research → Stories → Validación → Splitting → Priorización"
---

> **Paso 0 (obligatorio): Cargar ground-rules.** Antes de proceder, lee `shared-config.md` y aplica:
> - **§Filosofía del Plugin** — modo copiloto, NO inventar, preguntar antes de generar
> - **§Estilo de Escritura** — frases ≤30 palabras, sin adjetivos sin datos, NUNCA inventar métricas
> - **§Antipatrones Compartidos** — los 7 antipatrones a detectar
>
> Si no puedes leer el fichero, detén la ejecución y reporta el problema.

# Pipeline orquestado por sub-agentes

Este comando funciona como **orquestador**. No carga las SKILLs en su propio contexto: delega cada paso pesado a un sub-agente fresco vía la herramienta `Agent` (Task). El orquestador conserva sólo la ruta elegida, los artefactos intermedios y los CHECKPOINTs con el usuario.

**Por qué:** un solo modelo cargando 8 SKILLs + PRD + entrevistas + JTBDs + stories + scoring entra en `distracted-agent` (Lada Kesseler). El dispatch a sub-agente acota cada paso a su SKILL y devuelve sólo el artefacto, no el chain-of-thought.

---

## Selección de ruta (orquestador, no se delega)

Preguntar al PM:

> ¿Qué tipo de documento tienes como punto de partida?
> 1. **PRD** — Documento con problema, solución, métricas, scope
> 2. **GSD** — Proyecto con `.planning/` de Get Shit Done
> 3. **Sin documento** — Empezar desde cero con guía conversacional

| Ruta | Secuencia |
|---|---|
| **A: PRD** | `prd-quality-guard → research → [entrevistas] → analyze-research → stories → validate-stories → split-stories → prioritize` |
| **B: GSD** | `from-gsd → [completar GAPs] → prd-quality-guard → research → [entrevistas] → analyze-research → stories → validate-stories → split-stories → prioritize` |
| **C: Sin doc** | `build-story → validate-stories → split-stories → prioritize` |

---

## Cómo dispatchar un paso (contrato)

Para cada paso del pipeline, usa la herramienta `Agent` con:

- **subagent_type:** `general-purpose`
- **description:** nombre corto del paso (ej. `"PRD quality gate"`)
- **prompt:** bloque autocontenido con:
  1. Qué `SKILL.md` cargar (ruta absoluta dentro del plugin)
  2. Input concreto (fichero, contenido pegado, JTBDs serializados, etc.)
  3. Output esperado (artefacto puntual, sin razonamiento intermedio)
  4. Recordatorio del modo copiloto y prohibición de inventar

**Reglas del orquestador:**

1. **NUNCA** cargar más de un `SKILL.md` en el orquestador. Las SKILLs se cargan dentro del sub-agente.
2. **SIEMPRE** pasar al sub-agente sólo los inputs que necesita — no historial.
3. **ENTRE pasos**, mostrar al usuario el artefacto y obtener confirmación antes de seguir.
4. **PARA `validate-stories`**, dispatcho **OBLIGATORIO** a sub-agente fresco. Es feedback-flip: el revisor no debe haber visto cómo se generó la story.
5. **ANTE FAIL** en quality gate o research, detener pipeline y reportar.
6. **ENTRE `research` y `analyze-research`**, hay pausa natural (entrevistas reales). Comunicar al usuario y NO continuar hasta que aporte notas.

---

## Catálogo de pasos dispatcheables

| # | Paso | Skill cargada por sub-agente | Input | Output |
|---|---|---|---|---|
| A0 | from-gsd | `skills/gsd-to-prd/SKILL.md` | Ruta a `.planning/` | `prd-from-gsd.md` con GAPs marcados |
| 1 | prd-quality-gate | `skills/prd-quality-guard/SKILL.md` | PRD (fichero/URL/paste) | Gate decision + score 3D + 3 recomendaciones |
| 2 | research-design | `skills/research-from-prd/SKILL.md` | PRD | Guión de entrevistas + briefing moderador |
| 3 | analyze-research | `skills/research-from-prd/SKILL.md` | Notas de entrevistas + PRD | JTBDs con evidencia + Research Gap Score |
| 4 | stories | `skills/jtbd-to-stories/SKILL.md` | JTBDs + PRD opcional | User stories con scoring 6D |
| 5 | validate-stories | `skills/user-story-quality-coach/SKILL.md` | Stories del paso 4 | Reporte calidad + antipatrones |
| 6 | split-stories | `skills/story-splitting/SKILL.md` | Stories validadas | Splits incrementales (3-5 por story) |
| 7 | prioritize | `skills/story-prioritization/SKILL.md` | Stories validadas/divididas | Batches iterativos anti-waterfall |
| C1 | build-story | `skills/user-story-builder/SKILL.md` | Idea / requisito | Story completa JTBD + scoring |

---

## Plantilla de prompt para sub-agente

Adapta este patrón al paso concreto (sustituir `{...}`):

```
Carga la skill {ruta-absoluta-a-SKILL.md} y aplícala con el siguiente input:

INPUT:
{contenido del PRD / JTBDs / stories / notas, según paso}

CONTEXTO:
- Modo copiloto (shared-config.md §Filosofía): NO inventar métricas, NO completar
  secciones por el usuario, marcar gaps como ⚠️ Pendiente.
- Estilo: frases ≤30 palabras, sin adjetivos sin datos.
- Si la SKILL define CHECKPOINTs interactivos, en lugar de preguntar al usuario,
  documenta las preguntas que harías y devuélvelas en el output como "Preguntas
  pendientes para el orquestador".

PARA CÁLCULOS NUMÉRICOS: usa los scripts deterministas en `scripts/` (ver
`scripts/README.md`). NO calcules medias, scores ni regex en tu razonamiento.

OUTPUT ESPERADO:
{artefacto concreto del paso — formato exacto}

NO devuelvas tu chain-of-thought ni resumen de cómo razonaste. Sólo el artefacto.
```

---

## Ejecución por ruta

### Ruta A — PRD

Por cada paso de la secuencia, el orquestador hace:

1. **Pre-checkpoint con el usuario** — confirmar input y mostrar qué va a delegar.
2. **Dispatch al sub-agente** — invocar `Agent` con la plantilla anterior.
3. **Mostrar artefacto al usuario** — sin reformular, presentar lo que devolvió el sub-agente.
4. **Post-checkpoint** — confirmar antes de avanzar al siguiente paso (o aplicar reglas FAIL/PASS).

Pasos:

1. **prd-quality-gate** — Si FAIL → detener. Si CONDICIONAL → mostrar gaps al PM y preguntar si itera o continúa. Si PASS → siguiente.
2. **research-design** — Devolver guión al usuario y declarar **PAUSA**: "realiza las entrevistas y vuelve con las notas".
3. **analyze-research** *(reanudar tras la pausa)* — Input: notas + PRD. Si Research Gap Score sigue en bloqueante → recomendar más entrevistas.
4. **stories** — Input: JTBDs validados.
5. **validate-stories** — **Sub-agente fresco obligatorio** (feedback-flip). El sub-agente no recibe el contexto del paso 4, sólo las stories serializadas.
6. **split-stories** — Saltar si Score Dim 6 ≥ 8 en todas las stories.
7. **prioritize** — Devolver batches al usuario.

### Ruta B — GSD

0. **from-gsd** — Sub-agente genera `prd-from-gsd.md`. Mostrar al usuario qué secciones quedaron como GAP y pedir que las complete antes de continuar.
1-7. Igual que Ruta A, partiendo del PRD generado.

### Ruta C — Sin documento

1. **build-story** — Conversación guiada con el usuario. Este paso **no** se delega (es 100% interactivo). El orquestador carga directamente `skills/user-story-builder/SKILL.md`.
2. **validate-stories** — Sub-agente fresco (feedback-flip).
3. **split-stories** — Sub-agente.
4. **prioritize** — Sub-agente.

---

## Por qué `validate-stories` va siempre a sub-agente fresco

`feedback-flip` (Lada Kesseler) requiere que el evaluador no haya producido lo que evalúa. Si el orquestador (o el mismo sub-agente que generó las stories) las valida, su contexto está sesgado: ya "sabe" cómo se llegó a cada decisión y tenderá a justificarla en lugar de cuestionarla. El dispatch fresco corta ese sesgo.

---

## Output final

Stories validadas, correctamente dimensionadas y **priorizadas en batches iterativos** listas para tu issue tracker o para pasar a tu ejecutor (Superpowers, Cursor agents, equipo).

**Bridge a ejecución (opcional):** Si usas GSD para planning + Superpowers para implementación, instala `bridge/gsd-bridge.py` para mantener `STATE.md` / `ROADMAP.md` / `PLAN.md` sincronizados con los commits. Ver `bridge/README.md`.

---

## Modo legacy (un solo agente)

Si por alguna razón el dispatch a sub-agentes no está disponible en tu setup, puedes ejecutar cada SKILL secuencialmente en una misma sesión llamando a su comando individual (`/prd-quality-guard`, `/research`, etc.). Pierdes el aislamiento de contexto y el feedback-flip — usa esto sólo como fallback.
