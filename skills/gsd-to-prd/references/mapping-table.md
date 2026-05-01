# Mapeo determinístico GSD → PRD

Tabla canónica que el comando `/from-gsd` aplica para transformar artefactos GSD en un PRD sintético.

## Convenciones

- **Origen primario**: fichero y sección de `.planning/` que rellena la sección PRD
- **Fallback**: si el primario no existe, qué usar
- **GAP**: si ninguno existe, marcar como gap y explicar al PM qué falta
- **Reglas de extracción**: cómo procesar el contenido GSD para ajustarlo al formato PRD

---

## Bloque 1: EAC (Estado Actual Conocido)

### 1.1 Problema

| Campo | Origen GSD | Reglas |
|-------|------------|--------|
| Definición del problema | `PROJECT.md` §What This Is | Tomar tal cual, ajustar a 2-3 frases |
| Quién sufre | `PROJECT.md` §Context (extraer roles mencionados) | Si no hay roles → ⚠️ GAP parcial |
| Desde cuándo | `PROJECT.md` §Context (buscar fechas) | Si no hay → omitir, no ⚠️ GAP |
| Impacto | `PROJECT.md` §Core Value (inverso del valor = impacto del problema) | — |
| Por qué AHORA | `PROJECT.md` §Constraints (timeline) o `ROADMAP.md` (priorización) | — |

**Regla de fusión:** combinar §What This Is + §Core Value en un párrafo introductorio, luego §Context para detallar.

### 1.2 Farolas (Cuantitativo)

**Origen GSD:** ⚠️ NINGUNO  
**Acción:** Marcar como GAP con instrucción explícita.

```markdown
> ⚠️ **GAP — sección no cubierta por GSD**
> 
> GSD no captura métricas con baseline + fuente + temporalidad.
> Esta sección debe completarla el PM tras `/research` con:
> - ≥3 métricas cuantitativas
> - Baseline actual + fuente del dato + fecha de medición
> 
> Formato esperado:
> | Farola | Valor | Fuente | Fecha |
> |--------|-------|--------|-------|
> | [...]  | [...] | [...]  | [...] |
```

### 1.3 Penumbras (Cualitativo)

**Origen GSD:** ⚠️ NINGUNO (a menos que `phases/N/RESEARCH.md` contenga citas explícitas)  
**Acción:** Si hay RESEARCH.md → extraer citas literales (`"...."`). Si no → GAP.

```markdown
> ⚠️ **GAP — sección parcialmente cubierta**
> 
> GSD captura research como notas pero no estructura citas.
> Si tienes RESEARCH.md con observaciones, copia las citas literales aquí.
> Si no, completa tras `/research` con ≥3 observaciones cualitativas reales.
```

### 1.4 Próximos Pasos

| Origen | Reglas |
|--------|--------|
| `ROADMAP.md` fases con status `Not started` o `In progress` | Listar primeras 3-5 fases pendientes |
| `STATE.md` (si existe) `## Current Focus` | Tomar como contexto adicional |

---

## Bloque 2: EFC (Estado Futuro Conocido)

### 2.1 Hipótesis de Solución

| Campo | Origen GSD | Reglas |
|-------|------------|--------|
| Hipótesis principal | `phases/01/SPEC.md` §Goal + §Background | Si no hay phase 1 SPEC → usar `PROJECT.md` §Core Value |
| Justificación | `phases/01/SPEC.md` §Background | Conectar con problema (1.1) |
| Alternativas | `PROJECT.md` §Key Decisions (filas con "Choice" descartadas) | Si no hay → ⚠️ GAP |
| Riesgos | `phases/01/SPEC.md` §Constraints | — |

**Formato:** "Creemos que [acción derivada de SPEC.Goal] para [usuario de PROJECT.Context] resultará en [outcome derivado de Core Value]"

### 2.2 Aspectos Financieros

**Origen GSD:** ⚠️ NINGUNO  
**Acción:** GAP completo.

```markdown
> ⚠️ **GAP — sección no cubierta por GSD**
> 
> GSD se centra en ejecución, no captura ROI ni payback.
> El PM debe estimar:
> - Coste de la solución (horas dev × rate, infra, tooling)
> - Ahorro estimado (cálculo basado en farolas de §1.2)
> - Payback period
```

### 2.3 Métricas

| Campo | Origen GSD | Reglas |
|-------|------------|--------|
| Métricas cualitativas | `ROADMAP.md` Success Criteria por fase | Tomar como "comportamientos observables" |
| Métricas con baseline→target | ⚠️ GAP | — |

**Formato:**

```markdown
**Comportamientos observables (de ROADMAP.md):**
- [Lista de Success Criteria de cada fase]

**Métricas medibles:**
> ⚠️ **GAP** — GSD captura criterios observables pero no métricas con baseline.
> El PM debe definir ≥2 métricas con: nombre, baseline actual, target, plazo, método.
```

### 2.4 Dimensionamiento

| Campo | Origen GSD | Reglas |
|-------|------------|--------|
| Usuarios afectados | `PROJECT.md` §Context (extraer si menciona escala) | Si no → ⚠️ GAP parcial |
| Volumen | ⚠️ GAP típicamente | — |
| Fases de rollout | `ROADMAP.md` fases | Listar todas con dependencias |

---

## Bloque 3: Discovery + Scope

### 3.1 Discovery

| Origen | Reglas |
|--------|--------|
| `phases/N/RESEARCH.md` (si existe) | Resumir metodología + hallazgos principales. Citar como evidencia previa para `/research`. |
| Sin RESEARCH.md | ⚠️ GAP — discovery debe hacerse |

```markdown
**Si hay RESEARCH.md:**

> Discovery previo disponible en GSD:
> - Metodología: [extraída del header de RESEARCH.md]
> - Hallazgos principales: [primeros 3-5 bullet points]
> - Fichero completo: `.planning/phases/N/RESEARCH.md`
> 
> El comando `/research` puede reutilizar esta evidencia con `--evidence-from=.planning/phases/N/RESEARCH.md`

**Si NO hay RESEARCH.md:**

> ⚠️ **GAP** — No hay research previo en GSD.
> Ejecutar `/research source_type=PRD` para diseñar entrevistas.
```

### 3.2 Explore (Alternativas)

| Origen | Reglas |
|--------|--------|
| `PROJECT.md` §Key Decisions | Si tiene filas con rationale → mapear como alternativas exploradas |
| Sin Key Decisions | ⚠️ GAP |

**Formato:**

```markdown
**Alternativas consideradas (de PROJECT.md §Key Decisions):**

| Alternativa | Por qué se descartó / eligió |
|-------------|------------------------------|
| [Decision] | [Rationale] |

[Si no hay Key Decisions:]
> ⚠️ **GAP** — GSD §Key Decisions vacío. PM debe documentar ≥2 alternativas exploradas.
```

### 3.3 Funcionalidades Principales

**Combinación de fuentes** (esta es la sección más rica):

| Campo | Origen | Reglas |
|-------|--------|--------|
| Lista de features | `REQUIREMENTS.md` §v1 active | Cada `- [ ] **REQ-ID**: descripción` → 1 feature |
| Priorización (must vs nice) | `ROADMAP.md` (Phase 1 = must, fases tardías = nice) | — |
| Vinculación a problema/JTBD | `REQUIREMENTS.md` Traceability | Si no hay → omitir vinculación, no ⚠️ GAP |
| Criterios de aceptación | `phases/N/SPEC.md` §Acceptance Criteria por fase | Cada checkbox → criterio |

**Formato esperado (estructurado):**

```markdown
**Features must-have (Phase 1-2):**

- **[REQ-ID]**: [descripción]
  - Origen: REQUIREMENTS.md §v1 + phases/01/SPEC.md
  - Acceptance: [criterios de SPEC.md]

[continuar para cada feature]

**Features nice-to-have (Phase 3+):**

[mismo formato]

**Roadmap (de ROADMAP.md):**

| Fase | Goal | Plans |
|------|------|-------|
| 1 | [...] | [count] |
| 2 | [...] | [count] |
```

### 3.4 Flujos de Usuario

| Origen | Reglas |
|--------|--------|
| `phases/N/SPEC.md` §Background o §Boundaries (si describe flujos) | Extraer y formatear |
| `PROJECT.md` §Context (si menciona interacciones) | Fallback débil |
| Ninguno | ⚠️ GAP parcial |

```markdown
> ⚠️ **GAP — frecuentemente parcial**
> 
> GSD no estructura flujos de usuario formalmente. Si phases/N/SPEC.md
> los menciona, se extraen aquí. Si no, el PM debe diagramar.
```

### 3.5 FAQs

**Origen GSD:** ⚠️ NINGUNO  
**Acción:** GAP completo.

```markdown
> ⚠️ **GAP — sección no cubierta por GSD**
> 
> GSD no anticipa FAQs. El PM debe añadir ≥5 preguntas tras `/research`.
> Categorías recomendadas:
> - Preguntas técnicas del equipo de ingeniería
> - Preguntas de stakeholders de negocio
> - Preguntas de usuarios finales
```

### 3.6 Exclusiones

| Origen | Reglas |
|--------|--------|
| `REQUIREMENTS.md` §Out of Scope | Tabla `Feature \| Reason` → trasladar tal cual |
| `phases/N/SPEC.md` §Boundaries §Out of scope | Combinar con anteriores |

```markdown
**Exclusiones explícitas (de REQUIREMENTS.md + SPEC.md):**

| Exclusión | Razón | Origen |
|-----------|-------|--------|
| [Feature] | [Why] | REQUIREMENTS.md / phases/N/SPEC.md |
```

---

## Casos especiales

### Proyecto GSD sin fases ejecutadas

Si solo hay `PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md` (sin `phases/N/SPEC.md`) → el PRD generado tendrá más GAPs (especialmente 2.1 Hipótesis y 3.3 Acceptance criteria). El comando lo reporta:

```
✓ PRD sintético generado (modo light, no hay phase specs aún)
  Secciones rellenas: 6
  GAPs: 8
  
Recomendación: ejecuta /gsd-spec-phase 1 antes de /from-gsd para enriquecer el PRD.
```

### Proyecto GSD con múltiples milestones

Si `ROADMAP.md` tiene múltiples milestones (v1.0 SHIPPED, v1.1 in progress) → el PRD se centra en el milestone activo (`In Progress` o el siguiente `Planned`). Los milestones shipped se mencionan como contexto.

### Proyecto GSD con `--prd <file>` ya usado

Si `phases/N/PLAN.md` referencia un PRD externo (flag `--prd`), el comando lo detecta y warningea:

```
⚠️ Detectado PRD externo en phases/01/PLAN.md (--prd usado).
   El PRD generado por /from-gsd puede solapar con el original.
   Considera: ¿quieres mergear ambos o usar el original directamente?
```

### Proyecto sin GSD (solo SP)

Si no existe `.planning/` → el comando aborta con mensaje:

```
✗ No se encontró .planning/ en la ruta indicada.
  Si tu proyecto no usa GSD, considera:
  - /build-story (ruta C: sin documento)
  - Crear manualmente un PRD y usar /prd-quality-guard
```
