---
name: gsd-to-prd
description: |
  Transforma los artefactos de un proyecto GSD (Get Shit Done) en un PRD sintético
  compatible con /prd-quality-guard. Lee .planning/PROJECT.md, REQUIREMENTS.md,
  ROADMAP.md y phases/N/SPEC.md|RESEARCH.md, y produce un fichero prd-from-gsd.md
  con las secciones del PRD rellenas o marcadas como GAP cuando GSD no captura
  ese tipo de información.

  TRIGGERS: "from-gsd", "convertir GSD a PRD", "/from-gsd", "GSD → PRD",
  "leer .planning/", "generar PRD desde GSD"

  INTEGRACIÓN: Punto de entrada del pipeline cuando el origen es GSD.
  Equivale a la "Ruta B" del pipeline (junto a PRD y sin documento).
  Su output entra a /prd-quality-guard.
version: 1.0.0
---

# GSD → PRD — Mapeo de artefactos

Asiste al usuario en transformar los artefactos generados por GSD en un PRD sintético, marcando explícitamente los gaps que GSD no cubre.

> **Filosofía:** El PRD generado es **fiel pero incompleto**. GSD captura contexto, scope y fases con criterios de aceptación, pero NO captura métricas con baseline, citas cualitativas, o ROI. Esos gaps se marcan para que el PM los complete tras `/research`.

## Principio Fundamental

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                  │
│   GSD captura                       GSD NO captura              │
│   ────────────                      ─────────────                │
│                                                                  │
│   ✅ Contexto del producto          ❌ Métricas con baseline     │
│   ✅ Requirements v1/v2             ❌ Citas de usuarios         │
│   ✅ Out of scope                   ❌ ROI / aspectos financ.    │
│   ✅ Fases con success criteria     ❌ FAQs anticipadas          │
│   ✅ Specs por fase                 ❌ Penumbras (cualitativo)   │
│   ✅ Research previo (si lo hay)    ❌ Farolas (cuantitativo)    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

GSD opera con **principios falsables y testeables**. el PRD opera con **evidencia cualitativa y cuantitativa**. El bridge respeta ambos: rellena lo que se puede mapear, marca lo que falta.

---

## Flujo de Generación

```
.planning/ (GSD)
    │
    ▼
┌──────────────────────────────────────┐
│  1. VALIDAR ARTEFACTOS                │
│     - PROJECT.md (REQ)                │
│     - REQUIREMENTS.md (REQ)           │
│     - ROADMAP.md (REQ)                │
│     - phases/N/SPEC.md (OPT)          │
│     - phases/N/RESEARCH.md (OPT)      │
└──────────────────────────────────────┘
    │
    ▼
┌──────────────────────────────────────┐
│  2. APLICAR MATRIZ DE MAPEO           │
│     Ver references/mapping-table.md   │
└──────────────────────────────────────┘
    │
    ▼
┌──────────────────────────────────────┐
│  3. RELLENAR SECCIONES MAPEABLES      │
│     - 1.1 Problema (de PROJECT)       │
│     - 1.4 Próximos pasos (de ROADMAP) │
│     - 2.1 Hipótesis (de SPEC.Goal)    │
│     - 2.4 Dimensionamiento (ROADMAP)  │
│     - 3.1 Discovery (RESEARCH si hay) │
│     - 3.2 Explore (Key Decisions)     │
│     - 3.3 Funcionalidades (REQ + SPEC)│
│     - 3.4 Flujos (de SPEC si los hay) │
│     - 3.6 Exclusiones (REQ Out-Scope) │
└──────────────────────────────────────┘
    │
    ▼
┌──────────────────────────────────────┐
│  4. MARCAR GAPS EXPLÍCITOS            │
│     - 1.2 Farolas → ⚠️ GAP            │
│     - 1.3 Penumbras → ⚠️ GAP          │
│     - 2.2 Aspectos financieros → ⚠️   │
│     - 2.3 Métricas baseline→target ⚠️│
│     - 3.5 FAQs → ⚠️ GAP               │
└──────────────────────────────────────┘
    │
    ▼
┌──────────────────────────────────────┐
│  5. GENERAR prd-from-gsd.md           │
│     - Header con metadata origen      │
│     - 14 secciones (rellenas+gaps)    │
│     - Footer con resumen+next steps   │
└──────────────────────────────────────┘
    │
    ▼
PRD sintético listo para /prd-quality-guard
```

---

## Proceso paso a paso

### Paso 1: Localizar y validar artefactos

```bash
# Default: .planning/ en el directorio actual
PLANNING_DIR="${1:-./.planning/}"

# Requeridos
test -f "$PLANNING_DIR/PROJECT.md" || exit "PROJECT.md no encontrado"
test -f "$PLANNING_DIR/REQUIREMENTS.md" || exit "REQUIREMENTS.md no encontrado"
test -f "$PLANNING_DIR/ROADMAP.md" || exit "ROADMAP.md no encontrado"

# Opcionales (enriquecen el PRD pero no son obligatorios)
ls "$PLANNING_DIR/phases/"*/SPEC.md 2>/dev/null
ls "$PLANNING_DIR/phases/"*/RESEARCH.md 2>/dev/null
test -f "$PLANNING_DIR/STATE.md"  # solo informativo
```

Si falta un requerido → mensaje claro al usuario y stop.

### Paso 2: Leer y parsear

Leer los ficheros completos. Para cada uno extraer las secciones canónicas:

**PROJECT.md** → secciones: `## What This Is`, `## Core Value`, `## Context`, `## Constraints`, `## Key Decisions`
**REQUIREMENTS.md** → `## v1 Requirements`, `## v2 Requirements`, `## Out of Scope`, `## Traceability`
**ROADMAP.md** → `## Phases`, `### Phase N` (Goal, Success Criteria, Plans)
**phases/N/SPEC.md** → `## Goal`, `## Background`, `## Requirements`, `## Boundaries`, `## Acceptance Criteria`
**phases/N/RESEARCH.md** → contenido completo (referencia, no se duplica)

### Paso 3: Aplicar matriz de mapeo

Ver `references/mapping-table.md` para la tabla deterministica completa. Resumen:

| Sección PRD | Origen GSD primario | Fallback |
|-------------|---------------------|----------|
| 1.1 Problema | PROJECT.md "What This Is" + "Context" | — |
| 1.2 Farolas | ⚠️ GAP | (PM tras /research) |
| 1.3 Penumbras | ⚠️ GAP | (PM tras /research) |
| 1.4 Próximos pasos | ROADMAP fases pendientes | PROJECT.md "Active" |
| 2.1 Hipótesis | phases/1/SPEC.md "Goal" + "Background" | PROJECT.md "Core Value" |
| 2.2 Aspectos Financieros | ⚠️ GAP | (PM debe estimar) |
| 2.3 Métricas | ROADMAP "Success Criteria" (cualitativo) + ⚠️ GAP cuantitativo | — |
| 2.4 Dimensionamiento | ROADMAP fases + Plans count | — |
| 3.1 Discovery | phases/N/RESEARCH.md (si existe) | ⚠️ GAP si no hay |
| 3.2 Explore | PROJECT.md "Key Decisions" | ⚠️ GAP si vacío |
| 3.3 Funcionalidades | REQUIREMENTS v1 + phases/N/SPEC.Requirements | — |
| 3.4 Flujos de Usuario | phases/N/SPEC.md (si describe flujos) | ⚠️ GAP |
| 3.5 FAQs | ⚠️ GAP | (PM debe añadir) |
| 3.6 Exclusiones | REQUIREMENTS "Out of Scope" + SPEC "Out of scope" | — |

### Paso 4: Generar el PRD

Usar la plantilla de `references/prd-synthetic-template.md`. Para cada sección:
- **Si hay origen GSD** → rellenar con contenido del fichero, citando origen al final de la sección (`> Origen: PROJECT.md §What This Is`)
- **Si es GAP** → poner el bloque `⚠️ GAP` con instrucciones claras de qué falta y cómo completarlo

### Paso 5: Reportar al usuario

Formato compact:

```
✓ PRD sintético generado: prd-from-gsd.md

  Secciones rellenas desde GSD:    [N]
  Secciones marcadas como GAP:     [M]
  
  GAPs típicos a completar tras /research:
  - 1.2 Farolas (cuantitativo)
  - 1.3 Penumbras (cualitativo, citas)
  - 2.2 Aspectos Financieros (ROI)
  - 2.3 Métricas (baseline → target)
  - 3.5 FAQs

Siguiente paso:
  1. Revisar prd-from-gsd.md (en raíz del proyecto)
  2. Ejecutar /prd-quality-guard prd-from-gsd.md
  3. Si PASS → /research source_type=PRD
  
Nota: Los GAPs no impiden el quality gate, pero el score subirá
si los completas antes de research.
```

---

## Reglas Estrictas

1. **Fidelidad:** No inventar datos que no estén en GSD
2. **Trazabilidad:** Cada sección rellena cita su origen GSD (`> Origen: ...`)
3. **Honestidad:** GAPs explícitos, no rellenos vacíos con palabrería
4. **Idempotencia:** Ejecutar el comando dos veces produce el mismo PRD
5. **Read-only sobre GSD:** El comando NO modifica `.planning/`

---

## Limitaciones conocidas

- Si GSD usa templates customizados (no los standard) puede fallar el parser de secciones
- Si las fases de GSD están dispersas (`phases/01-foo/`, `phases/02-bar/`) se procesan en orden numérico
- `STATE.md` se lee pero solo se usa para añadir metadata "última fase ejecutada" al header del PRD
- No traduce: si GSD está en inglés, el PRD sale en inglés (con headings de el PRD igualmente en español)
