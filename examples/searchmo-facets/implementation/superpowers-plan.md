# Superpowers Plan — Batch 1: Backend Faceted Search

**Generado por:** `/superpowers:writing-plans`
**Input:** `stories/stories-validated.md` (stories 1 + 2 = Batch 1) + `.planning/phases/01-faceted-search/SPEC.md` para criterios técnicos
**Stories cubiertas:** DETECT-01, DETECT-02, DETECT-03, FACET-01, FACET-02, FACET-03, FACET-04
**Phase GSD:** 01-faceted-search
**Estimated tokens:** 180k-280k (subagent-driven)

---

## Plan Overview

Implementación TDD del backend de Faceted Search. La estrategia es **vertical slicing**: para cada REQ-ID, escribir test rojo → implementación mínima → test verde → refactor. Subagent-driven para paralelizar partes independientes (ej: clasificador y generador pueden trabajar en paralelo una vez definido el contrato).

```
Step 1: Setup contracts (data structures + types)
   └─ shared between detect + generate
Step 2: Detect ambiguity (DETECT-01, DETECT-02, DETECT-03)
   └─ subagent: SearchClassifier
Step 3: Generate facets (FACET-01, FACET-02)
   └─ subagent: FacetGenerator
Step 4: Order facets + values (FACET-03, FACET-04)
   └─ depends on Step 3
Step 5: Integration (extend /search endpoint response)
   └─ wires up Steps 2+3+4
Step 6: Performance + regression tests
```

---

## Step 1: Setup contracts

**Goal:** Definir los tipos que comparten clasificador, generador y endpoint.

**Tests to write (red):**
- Test que valida la estructura del schema de respuesta (tipo `SearchResponse` con campo opcional `facets`)
- Test de schema validation contra payload sintético

**Implementation:**
- Tipos `QueryClassification = "ambiguous" | "specific"`
- Tipo `Facet = { name: string, values: FacetValue[] }`
- Tipo `FacetValue = { value: string, count: number }`
- Extensión del tipo `SearchResponse` con `query_classification` y `facets?`

**Acceptance:** Test verde, sin lógica todavía.

---

## Step 2: Clasificador de ambigüedad (DETECT-01, 02, 03)

**Goal:** Implementar `SearchClassifier.classify(topKResults): QueryClassification`.

**Tests to write (red):**
- 25 queries específicas → todas devuelven `"specific"`
- 25 queries ambiguas → todas devuelven `"ambiguous"` (acceptance ≥90%)
- Cambio de feature flag en runtime cambia el threshold sin reiniciar
- Latencia <10ms p99 en 1000 ejecuciones (microbenchmark)

**Implementation:**
- Función `categorize(topKResults, k=20): Map<categoryId, weight>`
- Función `isAmbiguous(weights, threshold): boolean` — true si ≥`threshold.minCategories` con peso ≥`threshold.minWeight`
- Lectura del feature flag al inicio de cada request (no en boot — debe ser runtime)
- Cache de threshold de 30s para evitar overhead de lookup en cada query

**Refactor signals:**
- Si la función `categorize` >30 líneas → extraer helper para weight calculation
- Si el cache de threshold tiene race condition → usar lock granular o atomic ref

**Acceptance:** 6/6 tests verdes, incluyendo benchmark de latencia.

---

## Step 3: Generador de facetas (FACET-01, FACET-02)

**Goal:** Implementar `FacetGenerator.generate(topKResults, productAttributes): Facet[]` que devuelve 3-5 facetas con mayor entropía discriminatoria.

**Tests to write (red):**
- 25 queries ambiguas de prueba → cada una devuelve 3-5 facetas válidas
- Cada faceta devuelve 2-10 valores
- Test de cobertura: ≥80% de facetas devueltas existen en ≥70% de productos del top-K (no facetas "huérfanas")

**Implementation:**
- Calcular `discriminativePower(attribute, results): number` = entropía normalizada de los valores del atributo en los resultados
- Filtrar atributos con `discriminativePower < 0.4` (no aportan separación)
- Seleccionar top 5 por discriminativePower
- Si <3 atributos pasan el filtro → devolver array vacío (no merece la pena facetar)

**Subagent dispatch:** este step puede correr en paralelo con Step 2 una vez Step 1 está hecho.

**Acceptance:** 3/3 tests verdes.

---

## Step 4: Ordenación (FACET-03, FACET-04)

**Goal:** Ordenar facetas por uso histórico y valores por frecuencia local.

**Tests to write (red):**
- Test con dump sintético de `facet_usage_stats` → orden de facetas matchea el ranking esperado
- Test de orden de valores: descendente por `count` en los resultados de la query

**Implementation:**
- Extender `FacetGenerator` con consulta a `facet_usage_stats` (cacheada en memoria, refresh cada hora)
- Re-ordenar el array de facetas por `usage_count` descendente antes de devolver
- Para cada faceta, ordenar `values` por `count` descendente

**Acceptance:** 2/2 tests verdes.

---

## Step 5: Integración con endpoint `/search`

**Goal:** El endpoint `/search` invoca el clasificador y el generador, y serializa la respuesta extendida.

**Tests to write (red):**
- Test E2E: query ambigua devuelve respuesta con `query_classification: "ambiguous"` y `facets` con 3-5 entradas
- Test E2E: query específica devuelve `query_classification: "specific"` y `facets` ausente o vacío
- Test E2E con flag desactivado: respuesta idéntica a la actual (test de regresión)

**Implementation:**
- En el handler de `/search`, tras construir top-K results:
  1. Si feature flag `search.facets.enabled = true` → invocar clasificador
  2. Si `query_classification = "ambiguous"` → invocar generador
  3. Serializar respuesta extendida
- Si flag desactivado → respuesta sin extensión, idéntica al baseline

**Acceptance:** 3/3 tests verdes.

---

## Step 6: Performance + regression

**Goal:** Validar que el feature no degrada SLA y que el flag desactivado es indistinguible del baseline.

**Tests to write (red):**
- Test de carga: 1000 queries (mix de específicas y ambiguas) — p99 latencia ≤195ms con flag activo
- Test de carga baseline: 1000 queries con flag desactivado — p99 latencia ≤145ms (no degradación)
- Test de diff de respuesta con flag desactivado vs baseline pre-feature → 0 diferencias

**Implementation:**
- Añadir test de carga en suite existente (no es código de producción nuevo)
- Si p99 >195ms → optimizar (probable: cache adicional o parallel calls a product service)

**Acceptance:** 3/3 tests verdes.

---

## Hand-off a Phase 2 + 3

Tras completar Batch 1:
- Endpoint `/search` listo con facetas (validable vía curl/Postman)
- Documentación del schema actualizada
- Feature flag al 0% (deshabilitado en prod hasta que UI esté lista)
- Bridge GSD↔SP detectará los REQ-IDs en commits y actualizará `STATE.md`, `01-01-PLAN.md`, y `ROADMAP.md` automáticamente

Phase 2 (UI) arranca con un nuevo plan de Superpowers; el contrato del endpoint ya está fijo.
