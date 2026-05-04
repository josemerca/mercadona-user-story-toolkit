---
name: prd-quality-guard
description: |
  Evalúa la calidad de un PRD como quality gate antes de pasar a research.
  Analiza 3 dimensiones: D1 Completitud EAC (Estado Actual Conocido),
  D2 Claridad EFC + Métricas (Estado Futuro Conocido), D3 Rigor Discovery + Scope.
  Score ≥7 = PASS.

  TRIGGERS: analizar calidad PRD, revisar PRD, evaluar PRD, quality gate PRD,
  "¿está listo el PRD?", "evalúa este PRD", "PRD quality check",
  "calidad del PRD de..."

  INTEGRACIÓN: Se ejecuta ANTES de /research (research-from-prd).
  Score ≥7 = listo para research.
version: 1.0.0
---

# PRD Quality Guard v1.0 — Quality Gate para PRDs

Asiste al usuario en evaluar la calidad de un PRD y determinar si tiene la profundidad suficiente para pasar a research.

> **Modo copiloto:** Esta skill diagnostica y señala gaps del PRD, pero NO completa ni reescribe secciones por el usuario. Propone preguntas para completar lo que falta. Ver shared-config.md §Filosofía del Plugin.

> "Un buen PRD define con precisión el problema (EAC) y la dirección (EFC).
> El research valida si lo que creemos saber es cierto."

## Principio Fundamental

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                   │
│   EAC (Estado Actual Conocido)       EFC (Estado Futuro Conocido)│
│   ────────────────────────           ────────────────────────────│
│                                                                   │
│   ✅ Problema con evidencia          ✅ Hipótesis de solución     │
│   ✅ Farolas (datos cuantitativos)   ✅ Métricas medibles        │
│   ✅ Penumbras (observaciones)       ✅ Impacto dimensionado     │
│   ✅ Discovery realizado             ✅ Funcionalidades claras   │
│   ✅ FAQs / Exclusiones              ✅ Flujos de usuario        │
│                                                                   │
│   ❌ NO vagas ("necesitamos          ❌ NO métricas sin          │
│       mejorar...")                        baseline/target          │
│   ❌ NO soluciones en el problema    ❌ NO features sin usuario   │
│   ❌ NO adjetivos sin datos          ❌ NO scope sin exclusiones  │
│                                                                   │
└──────────────────────────────────────────────────────────────────┘
```

---

> Ver SKILL-reference.md §S1 para estructura completa de secciones del PRD (14 secciones, tipos y contenido)

---

## Flujo de Evaluación

```
PRD (fichero, URL o contenido pegado)
    │
    ▼
┌──────────────────────────────────────┐
│  1. CARGAR PRD                        │
│     - Leer fichero local (Read tool)  │
│     - Fetch URL pública (WebFetch)    │
│     - O contenido pegado por usuario  │
└──────────────────────────────────────┘
    │
    ▼
┌──────────────────────────────────────┐
│  2. INVENTARIO DE SECCIONES           │
│     - Escanear todas las secciones    │
│     - Marcar estado por sección       │
│     - Detectar secciones faltantes    │
└──────────────────────────────────────┘
    │
    ▼
┌──────────────────────────────────────┐
│  🗣️ CHECKPOINT 1: POST-INVENTARIO    │
│     Comunicar estado al usuario       │
│     Ofrecer opciones de continuación  │
└──────────────────────────────────────┘
    │
    ▼
┌──────────────────────────────────────┐
│  3. SCORING 3 DIMENSIONES             │
│     D1: Completitud EAC (0-10)        │
│     D2: Claridad EFC + Métricas       │
│     D3: Rigor Discovery + Scope       │
│     Global = Promedio(D1, D2, D3)     │
└──────────────────────────────────────┘
    │
    ▼
┌──────────────────────────────────────┐
│  4. DETECCIÓN ANTIPATRONES            │
│     AP-PRD-1 a AP-PRD-5              │
└──────────────────────────────────────┘
    │
    ▼
┌──────────────────────────────────────┐
│  5. GATE DECISION                     │
│     ≥7 → PASS (proceder a research)  │
│     5-6 → CONDICIONAL                │
│     <5 → FAIL                         │
│     D3 < 5 → FAIL automático         │
└──────────────────────────────────────┘
    │
    ▼
┌──────────────────────────────────────┐
│  6. REPORTE DE CALIDAD                │
│     Leer report-template-prd.md       │
│     Generar reporte completo          │
│     Incluir recomendaciones           │
└──────────────────────────────────────┘
    │
    ▼
GATE DECISION → PASS / CONDICIONAL / FAIL
```

---

## Sistema de Scoring (3 Dimensiones)

**Rúbrica detallada:** `references/scoring-guide-prd.md`

> Ver SKILL-reference.md §S2 para rúbrica completa D1 (checklist, pesos, score rápido)

> Ver SKILL-reference.md §S3 para rúbrica completa D2 (checklist, pesos, score rápido)

> Ver SKILL-reference.md §S4 para rúbrica completa D3 (checklist, pesos, score rápido, regla D3<5)

**Resumen de dimensiones:**

| Dim | Nombre | Secciones PRD clave | Regla especial |
|-----|--------|---------------------|----------------|
| D1 | Completitud EAC | Problema, Farolas, Penumbras, Próximos pasos | — |
| D2 | Claridad EFC + Métricas | Hipótesis, Financiero, Métricas, Dimensionamiento | — |
| D3 | Rigor Discovery + Scope | Discovery, Explore, Funcionalidades, Flujos, FAQs, Exclusiones | D3 < 5 = FAIL automático |

---

## Gate Decision

### Umbrales

| Score Global | Gate | Acción |
|-------------|------|--------|
| 0-4 | **FAIL** | PRD requiere reescritura significativa |
| 5-6 | **CONDICIONAL** | Iterar secciones débiles antes de research |
| 7-8 | **PASS** | Proceder a research |
| 9-10 | **PASS** | Referencia para otros PRDs |

> Ver SKILL-reference.md §S5 para matriz de decisión combinada (D1xD2xD3) y prioridad de mejora

---

## Antipatrones PRD-Específicos (5)

> Ver SKILL-reference.md §S6 para detalle completo de antipatrones (señales, ejemplos, impacto, corrección)

| ID | Nombre | Impacto |
|----|--------|---------|
| AP-PRD-1 | EAC Vago | D1 <=4 |
| AP-PRD-2 | EFC Sin Métricas Medibles | D2 <=4 |
| AP-PRD-3 | Solución en Sección de Problema | D1 penalizado, D3 sesgado |
| AP-PRD-4 | Sin FAQs o Exclusiones Explícitas | D3 <=6 |
| AP-PRD-5 | Violación Reglas Escritura del PRD | -1pt por cada 3 violaciones (máx -3 en D1) |

---

## Paso a Paso Detallado

### Paso 1: Cargar PRD

1. **Fichero local:** Leer la ruta indicada por el usuario con `Read`
2. **URL pública:** Si el documento está accesible vía web, usar `WebFetch`
3. **Contenido pegado:** Aceptar el texto del usuario directamente
4. **MCP de tu herramienta de docs:** Si el usuario tiene un MCP configurado (Notion, Confluence, etc.), invocarlo con la URL/ID que proporcione
5. Verificar que el contenido tiene estructura reconocible de PRD

### Paso 2: Inventario de Secciones

Escanear el PRD y clasificar cada sección (completo / parcial / vacío).

> Ver SKILL-reference.md §S7 para template de inventario de secciones

### Paso 3: Checkpoint Post-Inventario

Comunicar al usuario el estado del inventario y ofrecer opciones:
- Si >=70% completo -> continuar con scoring
- Si 50-70% -> advertir de secciones faltantes, preguntar si continuar
- Si <50% -> recomendar completar PRD antes de evaluar

### Paso 4: Scoring 3 Dimensiones

Evaluar D1, D2, D3 siguiendo las rúbricas de `references/scoring-guide-prd.md`.

### Paso 5: Detección de Antipatrones

Escanear el PRD buscando los 5 antipatrones (AP-PRD-1 a AP-PRD-5).
Documentar cada instancia encontrada con texto literal.

### Paso 6: Gate Decision

Calcular Score Global = Promedio(D1, D2, D3).
Aplicar regla especial: D3 < 5 -> FAIL automático.

**Cálculo determinista (offload-deterministic):** ejecutar el script en lugar de hacer la aritmética en el LLM.

```bash
python3 scripts/score_prd.py --d1=<D1> --d2=<D2> --d3=<D3>
```

El script devuelve `Score Global`, `Gate`, `Decisión` y `Razón`. Aplica ya la regla `D3<5 → FAIL`. Citar su output literal en el reporte.

### Paso 7: Reporte de Calidad

Generar reporte siguiendo `references/report-template-prd.md`.

---

## Referencias

- **Estructura del PRD:** `references/prd-structure.md`
- **Rúbrica de scoring:** `references/scoring-guide-prd.md`
- **Template de reporte:** `references/report-template-prd.md`
- **Material de referencia:** `SKILL-reference.md`

---

## Reglas Estrictas

1. **SIEMPRE** incluir evidencia literal del PRD (quotes)
2. **SIEMPRE** dar recomendaciones accionables (no genéricas)
3. **SIEMPRE** incluir inventario de secciones como primera sección del reporte
4. **NUNCA** asumir que una sección vacía está "implícita en otra"
5. **SIEMPRE** generar el reporte como markdown (no como documento ofimático)
6. **SIEMPRE** indicar el antipatrón específico cuando lo detecte
7. Si Score es CONDICIONAL, listar las 3 acciones más importantes para subir a PASS
8. Si Score es FAIL, indicar claramente qué secciones bloquean y con quién resolverlas
