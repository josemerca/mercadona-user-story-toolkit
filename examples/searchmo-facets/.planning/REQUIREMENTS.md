# Requirements: SearchMO Faceted Search

**Defined:** 2026-04-28
**Core Value:** Reducir fricción en búsquedas ambiguas mediante facetas inline auto-generadas

## v1 Requirements

Requirements for initial release.

### Detección de ambigüedad

- [ ] **DETECT-01**: El sistema clasifica una query como ambigua/específica usando dispersión de categorías en top-K resultados (default K=20)
- [ ] **DETECT-02**: El threshold de ambigüedad es configurable vía feature flag (default: ≥3 categorías con peso ≥10% en top-20)
- [ ] **DETECT-03**: La clasificación se calcula en <10ms p99 (no impacta latencia del search response)

### Generación de facetas

- [ ] **FACET-01**: Para una query ambigua, el sistema selecciona 3-5 facetas con mayor poder discriminatorio
- [ ] **FACET-02**: El poder discriminatorio se calcula como entropía normalizada de los valores de la faceta en los resultados ambiguos
- [ ] **FACET-03**: Las facetas se ordenan por uso histórico de la faceta (no por entropía); las más usadas primero
- [ ] **FACET-04**: Los valores de cada faceta se ordenan por frecuencia de aparición en los resultados de la query (más comunes primero)

### UI de facetas

- [ ] **UI-01**: Las facetas se renderizan como chips horizontales debajo del search bar y encima de los resultados
- [ ] **UI-02**: Los chips son scrollables horizontalmente si no caben (sin ocultar resultados)
- [ ] **UI-03**: Tap en un chip aplica la faceta y refresca los resultados sin recargar la página
- [ ] **UI-04**: Faceta aplicada se renderiza con estado "active" y un botón ✕ para quitarla
- [ ] **UI-05**: La transición visual al aplicar/quitar faceta es <300ms

### Telemetría

- [ ] **TELEM-01**: Cada chip mostrado dispara evento `facet_shown` con `{query, facet_name, position}`
- [ ] **TELEM-02**: Cada chip aplicado dispara evento `facet_applied` con `{query, facet_name, value, position, time_to_apply_ms}`
- [ ] **TELEM-03**: Cada chip ignorado al cambiar de query dispara evento `facet_dismissed` con `{query, facet_name}`
- [ ] **TELEM-04**: Eventos se envían al pipeline de analytics estándar de la app

## v2 Requirements

Deferred to future release.

### Multi-faceta

- **MULTI-01**: Aplicar ≥2 facetas a la vez (combinación)
- **MULTI-02**: UI de "facetas activas" cuando hay ≥2 aplicadas
- **MULTI-03**: Lógica de qué facetas seguir mostrando cuando ya hay alguna aplicada

### Personalización

- **PERS-01**: Ranking de facetas personalizado por historial del cliente
- **PERS-02**: Facetas frecuentes del cliente en posiciones 1-2

## Out of Scope

| Feature | Reason |
|---------|--------|
| Facetas en queries no ambiguas | Añade ruido visual sin valor diferencial; degrada UX |
| Facetas curated manualmente | No escalable con el catálogo; opuesto a la decisión arquitectural |
| Facetas en búsqueda por voz | Depende del roadmap de voz, fuera de este Q |
| Sidebar de facetas (estilo desktop ecommerce) | Consume viewport en mobile-first; chips son la decisión validada con design |
| Predicción de faceta sin que el usuario tape | Asume intención; mejor enseñar opciones y dejar que decida |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| DETECT-01 | Phase 1 | Pending |
| DETECT-02 | Phase 1 | Pending |
| DETECT-03 | Phase 1 | Pending |
| FACET-01 | Phase 1 | Pending |
| FACET-02 | Phase 1 | Pending |
| FACET-03 | Phase 1 | Pending |
| FACET-04 | Phase 1 | Pending |
| UI-01 | Phase 2 | Pending |
| UI-02 | Phase 2 | Pending |
| UI-03 | Phase 2 | Pending |
| UI-04 | Phase 2 | Pending |
| UI-05 | Phase 2 | Pending |
| TELEM-01 | Phase 3 | Pending |
| TELEM-02 | Phase 3 | Pending |
| TELEM-03 | Phase 3 | Pending |
| TELEM-04 | Phase 3 | Pending |

**Coverage:**
- v1 requirements: 16 total
- Mapped to phases: 16
- Unmapped: 0 ✓

---

*Requirements defined: 2026-04-28*
*Last updated: 2026-04-28 after kickoff*
