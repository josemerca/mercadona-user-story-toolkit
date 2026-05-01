# PRD sintético — SearchMO Faceted Search

**Generado por:** `/from-gsd` (Mercadona User Story Toolkit v0.1)
**Origen:** `examples/searchmo-facets/.planning/`
**Fecha de generación:** 2026-04-29 14:30
**Última fase ejecutada (de STATE.md):** ninguna (proyecto recién inicializado)
**Estado:** Borrador sintético — completar GAPs antes de `/prd-quality-guard`

---

## 1.1 Problema

Extensión del buscador SearchMO para soportar facetas inline: cuando una consulta es ambigua (ej: "café"), la respuesta del buscador incluye filtros sugeridos (tipo, intensidad, formato, etc.) que el cliente puede aplicar con un tap, sin tener que escribir queries más largas o navegar por categorías.

Reducir la fricción de la búsqueda ambigua para clientes recurrentes, aumentando la conversión a "añadir al carrito" y reduciendo búsquedas abandonadas.

SearchMO es el buscador propio de la app, en producción desde Q1 2026 reemplazando una solución de terceros. Los logs muestran que el ~12% de queries son ambiguas (multiples categorías de producto en los top-10 resultados con dispersión similar). Las queries ambiguas tienen una tasa de "search abandon" un 1.8x superior a las queries específicas.

> Origen: PROJECT.md §What This Is + §Core Value + §Context

## 1.2 Farolas (Evidencia Cuantitativa)

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

## 1.3 Penumbras (Evidencia Cualitativa)

> ⚠️ **GAP — sección parcialmente cubierta**
>
> GSD no estructura citas de usuarios. Si tienes `RESEARCH.md` con observaciones, el comando intenta extraer literales. Si no, completar tras `/research` con ≥3 observaciones cualitativas reales (citas, contexto, fuente).

## 1.4 Próximos Pasos

Las fases pendientes según ROADMAP.md son:

1. **Phase 1: Faceted Search Backend** — Detección de ambigüedad + generación algorítmica de facetas
2. **Phase 2: Faceted Search UI** — Chips inline en mobile/web con apply/remove
3. **Phase 3: Telemetry & Validation** — Eventos de analytics + dashboard para decidir GA o rollback

Acción inmediata según STATE.md: ejecutar `/gsd-spec-phase 1` para detallar Phase 1 (ya completado en este ejemplo) → comenzar implementación.

> Origen: ROADMAP.md §Phases (status: Not started) + STATE.md §Current focus

---

## 2.1 Hipótesis de Solución

**Hipótesis principal:**

> Creemos que ofrecer facetas inline auto-generadas para queries ambiguas en SearchMO resultará en una reducción del 30% en search abandons y un aumento del 8% en conversión a "añadir al carrito" para queries ambiguas.

**Justificación:**

SearchMO opera hoy en producción con búsqueda exacta + tolerancia a typos. Los logs muestran que el ~12% de queries son ambiguas (top-20 results con ≥3 categorías de peso ≥10%) y tienen 1.8x más "search abandons" que queries específicas. El catálogo tiene atributos estructurados por producto (categoría, marca, formato, tipo, intensidad) — disponibles en product service. La hipótesis es que ofrecer estos atributos como filtros inline reduce la fricción de desambiguación sin requerir que el cliente escriba queries más largas.

**Alternativas consideradas (de PROJECT.md §Key Decisions):**

| Alternativa | Rationale | Outcome |
|-------------|-----------|---------|
| Facetas algorítmicas, no curated | Curated requiere mantenimiento manual; algorítmico escala con el catálogo | ✓ Aprobado |
| Detección de ambigüedad por dispersión de categorías | Más robusto que solo por entropía de top-K results | ✓ Validado en spike |
| Sin multi-faceta en v1 | Aprender uso de faceta individual antes de complejidad combinatoria | ✓ Aprobado |
| Facetas como chips inline, no como sidebar | Sidebar consume viewport en mobile; chips son progresivos | ✓ Validado con design |

> Origen: phases/01-faceted-search/SPEC.md §Goal + §Background + PROJECT.md §Key Decisions

## 2.2 Aspectos Financieros

> ⚠️ **GAP — sección no cubierta por GSD**
>
> GSD se centra en ejecución, no captura ROI ni payback.
> El PM debe estimar:
> - Coste de la solución (horas dev × rate, infra, tooling)
> - Ahorro estimado (cálculo basado en farolas de §1.2)
> - Payback period

## 2.3 Métricas

**Comportamientos observables (de ROADMAP.md):**

*Phase 1 — Backend:*
- Para una query ambigua de prueba, el endpoint `/search?q=café` devuelve un campo `facets` con 3-5 entradas
- Para una query específica, el campo `facets` está vacío o ausente
- El threshold de ambigüedad se modifica vía feature flag sin redeploy
- La latencia p99 del endpoint sigue ≤200ms con facetas activas

*Phase 2 — UI:*
- En mobile, los chips se renderizan debajo del search bar y son scrollables horizontalmente
- Tap en un chip aplica la faceta sin recargar la página completa
- Faceta aplicada muestra estado "active" con botón ✕ funcional
- Transición visual ≤300ms

*Phase 3 — Telemetría:*
- Los 3 eventos (`facet_shown`, `facet_applied`, `facet_dismissed`) llegan al pipeline de analytics
- Dashboard muestra `facet_apply_rate` y `cart_add_rate` segmentado por con/sin faceta

> Origen: ROADMAP.md §Phase Details (Success Criteria)

**Métricas medibles con baseline → target:**

> ⚠️ **GAP** — GSD captura criterios observables pero no KPIs medibles con baseline.
> El PM debe definir ≥2 métricas con: nombre, baseline actual, target, plazo, método.

## 2.4 Dimensionamiento

**Fases de rollout (de ROADMAP.md):**

| Fase | Goal | Plans | Depends on |
|------|------|-------|------------|
| 1    | Faceted Search Backend | 1 | Nothing |
| 2    | Faceted Search UI | 1 | Phase 1 |
| 3    | Telemetry & Validation | 1 | Phase 2 |

**Usuarios afectados:** clientes recurrentes de la app (segmento que más sufre el problema según contexto del PROJECT.md §Context — el feature impacta el ~12% de queries que son ambiguas).

> Origen: ROADMAP.md §Phases + PROJECT.md §Context

---

## 3.1 Discovery

> ⚠️ **GAP — no hay research previo en GSD**
>
> Ejecutar `/research source_type=PRD` para diseñar entrevistas y completar esta sección.

(Nota: en este proyecto el research se hace tras `/from-gsd`, así que la sección quedará vacía hasta entonces. Una vez completado, se incorporan las observaciones, JTBDs y hallazgos.)

## 3.2 Explore (Alternativas)

**Alternativas consideradas (de PROJECT.md §Key Decisions):**

| Alternativa | Rationale | Outcome |
|-------------|-----------|---------|
| Curated vs algorítmica | Curated requiere mantenimiento manual; algorítmico escala con el catálogo | ✓ Algorítmica elegida |
| Dispersión de categorías vs entropía pura | Dispersión es más robusta para detectar ambigüedad real | ✓ Dispersión elegida |
| v1 multi-faceta vs v1 faceta única | Aprender de uso simple antes de complejidad combinatoria | ✓ Faceta única en v1 |
| Sidebar vs chips inline | Sidebar consume viewport en mobile-first | ✓ Chips inline elegidos |

> Origen: PROJECT.md §Key Decisions

## 3.3 Funcionalidades Principales

**Features must-have (Phase 1-2):**

- **DETECT-01**: Clasificación de queries ambiguas usando dispersión de categorías en top-K
  - Acceptance: Test con 50 queries (25 ambiguas, 25 específicas) — ≥90% aciertos
  - Origen: REQUIREMENTS.md §v1 + phases/01/SPEC.md §Requirements
- **DETECT-02**: Threshold de ambigüedad configurable vía feature flag
  - Acceptance: Cambiar el flag en runtime modifica clasificación sin reiniciar el servicio
- **DETECT-03**: Clasificación en <10ms p99
- **FACET-01**: Selección de 3-5 facetas con mayor poder discriminatorio
  - Acceptance: Para cada query de prueba ambigua, el array tiene 3-5 facetas; cada faceta tiene 2-10 valores
- **FACET-02**: Cálculo de poder discriminatorio (entropía normalizada)
- **FACET-03**: Ordenación de facetas por uso histórico
- **FACET-04**: Ordenación de valores por frecuencia local en resultados
- **UI-01 a UI-05**: Chips horizontales debajo del search bar; scroll horizontal; apply/remove sin recargar
- **TELEM-01 a TELEM-04**: Eventos `facet_shown`, `facet_applied`, `facet_dismissed`

**Features deferred (REQUIREMENTS v2):**

- Multi-faceta combinada (MULTI-01, MULTI-02, MULTI-03)
- Personalización por historial del cliente (PERS-01, PERS-02)

> Origen: REQUIREMENTS.md §v1/v2 + phases/01/SPEC.md §Requirements §Acceptance

## 3.4 Flujos de Usuario

> ⚠️ **GAP parcial — flujos de usuario**
>
> GSD no estructura flujos formalmente. PROJECT.md §Context menciona el flujo a alto nivel ("cliente busca query ambigua → ve chips inline → tap en chip → resultados refrescados"). Si necesitas flujos detallados para implementación, diagramarlos manualmente o extraerlos de la documentación de research/diseño.

## 3.5 FAQs

> ⚠️ **GAP — sección no cubierta por GSD**
>
> GSD no anticipa FAQs. El PM debe añadir ≥5 preguntas tras `/research`.
> Categorías recomendadas:
> - Preguntas técnicas del equipo de ingeniería
> - Preguntas de stakeholders de negocio
> - Preguntas de usuarios finales

## 3.6 Exclusiones

**Exclusiones explícitas (de REQUIREMENTS.md + SPEC.md):**

| Exclusión | Razón | Origen |
|-----------|-------|--------|
| Multi-faceta combinada (≥2 facetas) | Diferida a v2 — aprender uso individual primero | REQUIREMENTS.md §v2 |
| Facetas en queries no ambiguas | Añade ruido visual sin valor diferencial | REQUIREMENTS.md §Out of Scope |
| Facetas curated manualmente | No escalable; opuesto a decisión arquitectural | PROJECT.md §Key Decisions |
| Facetas en búsqueda por voz | Depende del roadmap de voz, fuera de este Q | REQUIREMENTS.md §Out of Scope |
| Sidebar de facetas | Consume viewport en mobile-first | REQUIREMENTS.md §Out of Scope |
| UI de facetas (Phase 2 de este proyecto) | Out of scope para Phase 1 | phases/01-faceted-search/SPEC.md §Boundaries |
| Eventos de telemetría (Phase 3) | Out of scope para Phase 1 | phases/01-faceted-search/SPEC.md §Boundaries |

> Origen: REQUIREMENTS.md §Out of Scope + phases/01-faceted-search/SPEC.md §Boundaries

---

## Resumen de generación

| Bloque | Secciones rellenas | GAPs |
|--------|---------------------|------|
| 1. EAC | 2 (Problema, Próximos pasos) | 2 (Farolas, Penumbras) |
| 2. EFC | 2 (Hipótesis, Dimensionamiento) | 2 (Aspectos Financieros, Métricas baseline→target) |
| 3. Discovery + Scope | 3 (Explore, Funcionalidades, Exclusiones) | 3 (Discovery, Flujos, FAQs) |
| **Total** | **7** | **7** |

**GAPs típicos a completar tras /research:**
- 1.2 Farolas (cuantitativo) — siempre GAP cuando GSD no tiene RESEARCH previo
- 1.3 Penumbras (cualitativo) — GAP porque GSD no tiene RESEARCH previo
- 2.2 Aspectos Financieros — siempre GAP
- 2.3 Métricas baseline→target — GAP cuantitativo
- 3.5 FAQs — siempre GAP
- 3.1 Discovery — GAP porque no hay phases/N/RESEARCH.md
- 3.4 Flujos de Usuario — GAP parcial

**Siguiente paso:**
1. Revisar `prd-from-gsd.md`
2. Completar GAPs (especialmente 1.2 Farolas y 2.3 Métricas si tienes datos)
3. Ejecutar `/prd-quality-guard prd-from-gsd.md`
4. Si PASS → `/research source_type=PRD`

---

*PRD generado el 2026-04-29 por `/from-gsd` v0.1.0 (Mercadona User Story Toolkit)*
*Fichero fuente: `examples/searchmo-facets/.planning/`*
