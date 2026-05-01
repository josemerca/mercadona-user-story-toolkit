# Template del PRD sintético generado por `/from-gsd`

Este es el formato exacto del fichero `prd-from-gsd.md` que el comando produce.

---

## Cabecera de metadatos

```markdown
# PRD sintético — [Project Name]

**Generado por:** `/from-gsd` (Mercadona User Story Toolkit)
**Origen:** `.planning/` ([ruta absoluta])
**Fecha de generación:** [YYYY-MM-DD HH:MM]
**Última fase ejecutada (de STATE.md):** [phase number / "no STATE.md"]
**Estado:** Borrador sintético — completar GAPs antes de `/prd-quality-guard`

---
```

---

## Bloque 1: EAC (Estado Actual Conocido)

### 1.1 Problema

[Contenido fusionado de PROJECT.md §What This Is + §Core Value + §Context]

> Origen: PROJECT.md §What This Is + §Context

### 1.2 Farolas (Evidencia Cuantitativa)

> ⚠️ **GAP — sección no cubierta por GSD**
> 
> GSD no captura métricas con baseline + fuente + temporalidad.
> Esta sección debe completarla el PM tras `/research` con:
> - ≥3 métricas cuantitativas
> - Cada una con: nombre, valor actual, fuente del dato, fecha de medición
> 
> Formato esperado:
> 
> | Farola | Valor | Fuente | Fecha |
> |--------|-------|--------|-------|
> | [...]  | [...] | [...]  | [...] |

### 1.3 Penumbras (Evidencia Cualitativa)

[Si phases/N/RESEARCH.md tiene citas extraíbles, se ponen aquí. Si no:]

> ⚠️ **GAP — sección parcialmente cubierta**
> 
> GSD no estructura citas de usuarios. Si tienes `RESEARCH.md` con observaciones,
> el comando intenta extraer literales. Si no, completar tras `/research` con
> ≥3 observaciones cualitativas reales (citas, contexto, fuente).

### 1.4 Próximos Pasos

[Lista de fases pendientes de ROADMAP.md, con dependencias]

> Origen: ROADMAP.md §Phases (status: Not started / In progress)

---

## Bloque 2: EFC (Estado Futuro Conocido)

### 2.1 Hipótesis de Solución

[Construida a partir de phases/01/SPEC.md §Goal + §Background + PROJECT.md §Core Value]

**Hipótesis principal:**
> Creemos que [acción] para [usuario] resultará en [outcome].

**Justificación:**
[Background de SPEC.md §Background]

**Alternativas consideradas:**
[Si PROJECT.md §Key Decisions tiene filas → tabla; si no → ⚠️ GAP]

> Origen: phases/01/SPEC.md §Goal + PROJECT.md §Key Decisions

### 2.2 Aspectos Financieros

> ⚠️ **GAP — sección no cubierta por GSD**
> 
> GSD se centra en ejecución, no captura ROI ni payback.
> El PM debe estimar:
> - Coste de la solución (horas dev × rate, infra, tooling)
> - Ahorro estimado (cálculo basado en farolas de §1.2)
> - Payback period

### 2.3 Métricas

**Comportamientos observables (de ROADMAP.md):**

[Lista de Success Criteria de cada fase, agrupados por fase]

> Origen: ROADMAP.md §Phase Details (Success Criteria)

**Métricas medibles con baseline → target:**

> ⚠️ **GAP** — GSD captura criterios observables pero no KPIs medibles.
> El PM debe definir ≥2 métricas con: nombre, baseline actual, target, plazo, método.

### 2.4 Dimensionamiento

**Fases de rollout (de ROADMAP.md):**

| Fase | Goal | Plans | Depends on |
|------|------|-------|------------|
| 1    | [...] | [N]  | Nothing    |
| 2    | [...] | [N]  | Phase 1    |
[etc.]

**Usuarios afectados:** [extraído de PROJECT.md §Context si lo menciona, si no ⚠️ GAP parcial]

> Origen: ROADMAP.md §Phases + PROJECT.md §Context

---

## Bloque 3: Discovery + Scope

### 3.1 Discovery

[Caso A: hay phases/N/RESEARCH.md]

**Discovery previo disponible en GSD:**
- Metodología: [extraído del header de RESEARCH.md]
- Hallazgos principales:
  - [Bullet 1]
  - [Bullet 2]
  - [Bullet 3]
- Fichero completo: `.planning/phases/N/RESEARCH.md`

> El comando `/research source_type=PRD` puede reutilizar esta evidencia con `--evidence-from=.planning/phases/N/RESEARCH.md`.

[Caso B: no hay RESEARCH.md]

> ⚠️ **GAP — no hay research previo en GSD**
> 
> Ejecutar `/research source_type=PRD` para diseñar entrevistas y completar esta sección.

### 3.2 Explore (Alternativas)

**Alternativas consideradas (de PROJECT.md §Key Decisions):**

| Alternativa | Rationale | Outcome |
|-------------|-----------|---------|
| [...]       | [...]     | [...]   |

[Si Key Decisions vacío:]

> ⚠️ **GAP** — `PROJECT.md §Key Decisions` vacío. PM debe documentar ≥2 alternativas exploradas con criterios.

### 3.3 Funcionalidades Principales

**Features must-have (Phase 1-2):**

[Generado fusionando REQUIREMENTS.md §v1 + phases/01/SPEC.md §Requirements + Acceptance Criteria]

- **[REQ-ID]**: [descripción]
  - Acceptance: [de SPEC.md §Acceptance]
  - Origen: REQUIREMENTS.md §v1 / phases/01/SPEC.md
- **[REQ-ID]**: [descripción]
  - Acceptance: [...]

**Features nice-to-have (Phase 3+):**

[Mismo formato, fases posteriores]

**Features deferred (REQUIREMENTS v2):**

[Lista de v2, sin acceptance — solo descripción]

> Origen: REQUIREMENTS.md §v1/v2 + phases/N/SPEC.md §Requirements §Acceptance

### 3.4 Flujos de Usuario

[Si phases/N/SPEC.md describe flujos → extraer]
[Si no:]

> ⚠️ **GAP parcial — flujos de usuario**
> 
> GSD no estructura flujos formalmente. Si los necesitas para implementación,
> diagramarlos manualmente o extraerlos de la documentación de research.

### 3.5 FAQs

> ⚠️ **GAP — sección no cubierta por GSD**
> 
> GSD no anticipa FAQs. El PM debe añadir ≥5 preguntas tras `/research`.
> Categorías recomendadas:
> - Preguntas técnicas del equipo de ingeniería
> - Preguntas de stakeholders de negocio
> - Preguntas de usuarios finales

### 3.6 Exclusiones

**Exclusiones explícitas:**

| Exclusión | Razón | Origen |
|-----------|-------|--------|
| [Feature] | [Why] | REQUIREMENTS.md §Out of Scope |
| [Feature] | [Why] | phases/N/SPEC.md §Boundaries |

> Origen: REQUIREMENTS.md §Out of Scope + phases/*/SPEC.md §Boundaries §Out of scope

---

## Footer (resumen)

```markdown
---

## Resumen de generación

| Bloque | Secciones rellenas | GAPs |
|--------|---------------------|------|
| 1. EAC | [N] | [M] |
| 2. EFC | [N] | [M] |
| 3. Discovery + Scope | [N] | [M] |
| **Total** | **[N]** | **[M]** |

**GAPs típicos a completar tras /research:**
- 1.2 Farolas (cuantitativo) — siempre GAP
- 1.3 Penumbras (cualitativo) — GAP si no hay RESEARCH.md
- 2.2 Aspectos Financieros — siempre GAP
- 2.3 Métricas baseline→target — GAP cuantitativo
- 3.5 FAQs — siempre GAP

**Siguiente paso:**
1. Revisar `prd-from-gsd.md`
2. Completar GAPs (especialmente 1.2 Farolas y 2.3 Métricas si tienes datos)
3. Ejecutar `/prd-quality-guard prd-from-gsd.md`
4. Si PASS → `/research source_type=PRD`

---

*PRD generado el [date] por `/from-gsd` v0.1.0 (Mercadona User Story Toolkit)*
*Fichero fuente: `.planning/` ([path])*
```
