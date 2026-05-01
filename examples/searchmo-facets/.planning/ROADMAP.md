# Roadmap: SearchMO Faceted Search

## Overview

3 fases. Phase 1 entrega el backend (detección + generación), Phase 2 la UI funcional, Phase 3 la telemetría completa para evaluar el feature. Cada fase entrega valor observable: Phase 1 demuestra el algoritmo (con dummy UI), Phase 2 ya es usable por clientes (con telemetría mínima), Phase 3 cierra el loop de medición para decidir continuidad.

## Phases

- [ ] **Phase 1: Faceted Search Backend** — Detección de ambigüedad + generación algorítmica de facetas
- [ ] **Phase 2: Faceted Search UI** — Chips inline en mobile/web con apply/remove
- [ ] **Phase 3: Telemetry & Validation** — Eventos de analytics + dashboard para decidir GA o rollback

## Phase Details

### Phase 1: Faceted Search Backend
**Goal**: El servicio de search clasifica queries ambiguas y devuelve 3-5 facetas relevantes con valores ordenados, manteniendo latencia p99 ≤200ms.
**Depends on**: Nothing (extiende search service existente)
**Requirements**: DETECT-01, DETECT-02, DETECT-03, FACET-01, FACET-02, FACET-03, FACET-04
**Success Criteria** (what must be TRUE):
  1. Para una query ambigua de prueba, el endpoint `/search?q=café` devuelve un campo `facets` con 3-5 entradas
  2. Para una query específica de prueba (`q=Café+Molido+Hacendado+250g`), el campo `facets` está vacío o ausente
  3. El threshold de ambigüedad se modifica vía feature flag sin redeploy
  4. La latencia p99 del endpoint sigue ≤200ms con facetas activas
**Plans**: 1 plan

Plans:
- [ ] 01-01: Implementar detección + generación + endpoint extension

### Phase 2: Faceted Search UI
**Goal**: Cliente recurrente ve chips de faceta inline, los aplica con un tap y los resultados se actualizan sin recargar la página.
**Depends on**: Phase 1
**Requirements**: UI-01, UI-02, UI-03, UI-04, UI-05
**Success Criteria** (what must be TRUE):
  1. En mobile, los chips se renderizan debajo del search bar y son scrollables horizontalmente
  2. Tap en un chip aplica la faceta sin recargar la página completa
  3. Faceta aplicada muestra estado "active" con botón ✕ funcional
  4. Transición visual ≤300ms (medido en device de referencia mid-range)
**Plans**: 1 plan

Plans:
- [ ] 02-01: Componente FacetChips + integración con search results page

### Phase 3: Telemetry & Validation
**Goal**: Eventos de analytics permiten medir adopción y conversión de facetas; dashboard reporta `facet_apply_rate` y `cart_add_rate` segmentado por uso de faceta.
**Depends on**: Phase 2
**Requirements**: TELEM-01, TELEM-02, TELEM-03, TELEM-04
**Success Criteria** (what must be TRUE):
  1. Los 3 eventos (`facet_shown`, `facet_applied`, `facet_dismissed`) llegan al pipeline de analytics
  2. El dashboard muestra `facet_apply_rate` y `cart_add_rate` segmentado por con/sin faceta aplicada
  3. Existe alerta si `facet_apply_rate` cae más del 30% día sobre día (señal de regresión)
**Plans**: 1 plan

Plans:
- [ ] 03-01: Eventos + dashboard + alerting

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Faceted Search Backend | 0/1 | Not started | - |
| 2. Faceted Search UI | 0/1 | Not started | - |
| 3. Telemetry & Validation | 0/1 | Not started | - |
