# PRD — SearchMO Faceted Search (completado)

**Origen:** `prd-from-gsd.md` (generado por `/from-gsd`) + GAPs completados manualmente por el PM tras revisión inicial.
**Fecha:** 2026-04-30
**Estado:** Listo para `/prd-quality-guard`

---

## 1.1 Problema

Extensión del buscador SearchMO para soportar facetas inline: cuando una consulta es ambigua (ej: "café"), la respuesta del buscador incluye filtros sugeridos (tipo, intensidad, formato, etc.) que el cliente puede aplicar con un tap, sin tener que escribir queries más largas o navegar por categorías.

**Quién sufre el problema:** clientes recurrentes de la app, especialmente perfiles que buscan productos por categoría conceptual ("café", "yogur", "pan") en lugar de por marca/formato específico.

**Desde cuándo:** desde el lanzamiento de SearchMO (Q1 2026), aunque el problema existía antes con el buscador anterior — solo no se medía.

**Impacto cuantificado:** ver §1.2 Farolas.

**Por qué AHORA:** el equipo de SearchMO completó Phase 1 (búsqueda exacta + tolerancia a typos) y la fase 2 del roadmap del buscador es exactamente esta mejora.

## 1.2 Farolas (Evidencia Cuantitativa)

| Farola | Valor | Fuente | Fecha |
|--------|-------|--------|-------|
| % queries ambiguas (top-20 con ≥3 categorías ≥10% peso) | 12.3% | Search service logs | Abril 2026 |
| Tasa de search abandon en queries ambiguas | 28% (vs 16% en específicas) | Analytics dashboard | Abril 2026 |
| Tiempo medio entre query y primer resultado clicado (queries ambiguas) | 4.2s (vs 2.1s en específicas) | Search analytics | Abril 2026 |
| % de queries ambiguas seguidas de una segunda query del mismo cliente en <30s | 41% | Search analytics | Abril 2026 |

## 1.3 Penumbras (Evidencia Cualitativa)

| Penumbra | Fuente | Contexto |
|----------|--------|----------|
| "Cuando busco 'café' me sale de todo y no sé cuál pillar" | Cliente recurrente, sesión de discovery | Entrevista 2026-04-22, casa del cliente |
| "Acabo escribiendo 'café Hacendado molido' aunque tarde más, porque sale más limpio" | Cliente recurrente | Observación de campo, 2026-04-22 |
| "Si pudiera filtrar por tipo de café como en otras apps, sería más rápido" | Cliente recurrente | Entrevista 2026-04-23 |
| "Cuando no encuentro lo que quiero rápido, me voy y compro otra cosa" | Cliente recurrente | Entrevista 2026-04-23 |
| "Tengo un truco: pongo la marca primero y luego el producto, así sale más concreto" | Cliente experimentado | Observación de campo, 2026-04-24 — workaround claro |

## 1.4 Próximos Pasos

Según ROADMAP.md, las fases pendientes son:

1. **Phase 1: Faceted Search Backend** — Detección de ambigüedad + generación algorítmica de facetas
2. **Phase 2: Faceted Search UI** — Chips inline en mobile/web con apply/remove
3. **Phase 3: Telemetry & Validation** — Eventos de analytics + dashboard para decidir GA o rollback

Acción inmediata: ejecutar `/prd-quality-guard prd-completed.md` para validar este PRD, luego `/research source_type=PRD` para diseñar entrevistas adicionales (ya hay evidencia inicial en §1.3 Penumbras pero queremos validar JTBDs antes de implementar).

---

## 2.1 Hipótesis de Solución

**Hipótesis principal:**

> Creemos que ofrecer **facetas inline auto-generadas** para queries ambiguas en SearchMO resultará en una **reducción del 30% en search abandons** y un **aumento del 8% en conversión a "añadir al carrito"** para queries ambiguas, porque las farolas muestran que el 28% de queries ambiguas se abandonan (vs 16% en específicas) y los clientes ya hacen workarounds (escribir queries más largas) para evitar el problema.

**Justificación:** ver §1.2 Farolas + §1.3 Penumbras + spike previo del equipo (Abril 2026) que validó la viabilidad técnica de generación algorítmica.

**Alternativas consideradas:** ver §3.2 Explore.

**Riesgos identificados:**

- Que las facetas auto-generadas no sean intuitivas para el cliente (riesgo de UX) — mitigación: research previo + iteración rápida en Phase 2
- Que la latencia de generación impacte el SLA del search (riesgo técnico) — mitigación: SPEC.md fija constraint p99 ≤195ms
- Que el feature canibalice las queries específicas en lugar de mejorar las ambiguas (riesgo de producto) — mitigación: dispositivo de detección de ambigüedad + threshold configurable

## 2.2 Aspectos Financieros

**Coste estimado:**
- Desarrollo: 3 fases × ~2 semanas/fase × 2 ingenieros = 12 semanas-persona ≈ 30k€
- Infra adicional: marginal (lectura adicional de product service, ya cacheada)
- Testing/QA: incluido en las 3 fases

**Ahorro/impacto estimado** (basado en farolas):
- Search abandons reducidos en 30% sobre el 12% de queries ambiguas → ~3.6% del total de queries deja de abandonarse
- Conversión incremental: si el 8% de esos clientes que ya no abandonan acaban añadiendo al carrito → impacto moderado en GMV (orden de magnitud: 0.3-0.5% GMV incremental)
- Payback estimado: 1-2 trimestres si las hipótesis se confirman

**Importante:** estas estimaciones son ilustrativas. El impacto real solo se mide con la telemetría de Phase 3.

## 2.3 Métricas

**Comportamientos observables (de ROADMAP.md):**

*Phase 1 — Backend:* endpoint `/search?q=café` devuelve `facets` con 3-5 entradas; queries específicas no las llevan; threshold configurable; p99 ≤200ms.
*Phase 2 — UI:* chips renderizados en mobile/web; tap aplica faceta sin recargar; transición ≤300ms.
*Phase 3 — Telemetría:* eventos llegan al pipeline; dashboard segmenta `cart_add_rate` por con/sin faceta; alerta si caída >30% día/día.

**Métricas medibles con baseline → target:**

| Métrica | Baseline | Target | Plazo | Cómo medir |
|---------|----------|--------|-------|------------|
| % queries ambiguas con faceta aplicada | N/A (feature nuevo) | ≥25% | 4 semanas tras GA | Evento `facet_applied` / queries con `query_classification=ambiguous` |
| Tasa de search abandon en queries ambiguas | 28% | 20% (-30%) | 8 semanas tras GA | Analytics existente |
| Conversión a "añadir al carrito" en queries ambiguas | 18% | 19.5% (+8%) | 8 semanas tras GA | Analytics existente |
| Latencia p99 del endpoint `/search` | 145ms | ≤195ms | Continuo | APM dashboard |

## 2.4 Dimensionamiento

**Usuarios afectados:** ~12% de queries del buscador → orden de magnitud de cientos de miles de queries/día (depende del volumen total de SearchMO; cifra exacta no revelable).

**Volumen de operaciones:** la generación de facetas se ejecuta solo en queries ambiguas. La carga adicional sobre el search service es marginal (cálculos en memoria sobre los top-K results ya generados).

**Centros/ubicaciones:** N/A (feature de app, ámbito global).

**Fases de rollout (de ROADMAP.md):**

| Fase | Goal | Plans | Depends on |
|------|------|-------|------------|
| 1    | Faceted Search Backend | 1 | Nothing |
| 2    | Faceted Search UI | 1 | Phase 1 |
| 3    | Telemetry & Validation | 1 | Phase 2 |

Tras Phase 3, periodo de monitorización de 4-8 semanas con feature flag al 10% → 50% → 100% según métricas.

---

## 3.1 Discovery

**Discovery realizado:**

- **Metodología:** Entrevistas Mom Test + Field Study (observación silenciosa de uso real de la app)
- **Participantes:** 5 clientes recurrentes (3 mobile, 2 web), abril 2026
- **Hallazgos principales:**
  1. Los clientes recurrentes reconocen el problema de queries ambiguas y ya tienen workarounds (escribir queries más largas, añadir marca al inicio)
  2. La conceptualización de "tipo de producto" es natural: cuando se les pregunta cómo buscarían "café", la mayoría espontáneamente menciona "molido vs grano" como primer eje de diferenciación
  3. La frustración con queries ambiguas es real: 4/5 mencionaron explícitamente "salir y buscar otra cosa" cuando los resultados no son claros
  4. La preferencia por chips inline vs sidebar/menú es clara: 5/5 eligieron la versión chips cuando se les enseñó dos mockups en sesión

**Notas completas:** ver `research/notes-session-1.md`, `research/notes-session-2.md`.

## 3.2 Explore (Alternativas)

| Alternativa | Rationale | Outcome |
|-------------|-----------|---------|
| Curated vs algorítmica | Curated requiere mantenimiento manual; algorítmico escala con el catálogo | ✓ Algorítmica elegida |
| Dispersión de categorías vs entropía pura | Dispersión es más robusta para detectar ambigüedad real | ✓ Dispersión elegida |
| v1 multi-faceta vs v1 faceta única | Aprender de uso simple antes de complejidad combinatoria | ✓ Faceta única en v1 |
| Sidebar vs chips inline | Sidebar consume viewport en mobile-first; chips son progresivos | ✓ Chips inline elegidos |
| Auto-aplicar faceta inferida vs ofrecerla | Auto-aplicar asume intención; ofrecer respeta agency | ✓ Ofrecer elegido |

## 3.3 Funcionalidades Principales

(Sin cambios respecto a `prd-from-gsd.md` — ver allí.)

## 3.4 Flujos de Usuario

**Flujo principal:**

1. Cliente abre la app y va al buscador
2. Cliente escribe una query ambigua (ej: "café") y pulsa buscar
3. Backend clasifica la query como `ambiguous` y genera 3-5 facetas relevantes
4. Frontend recibe los resultados + array de facetas; renderiza:
   - Search bar con la query
   - Chips de faceta debajo del search bar (scrollables horizontalmente si no caben)
   - Listado de resultados debajo de los chips
5. Cliente revisa los chips y, si uno encaja, hace tap
6. Frontend dispara evento `facet_applied`, llama al backend con la faceta aplicada (`/search?q=café&facet=tipo:molido`)
7. Backend devuelve resultados filtrados; el chip aparece en estado "active" con botón ✕
8. Cliente puede:
   - Hacer tap en el ✕ del chip → vuelve a resultados sin faceta
   - Hacer tap en otro chip → cambia la faceta aplicada
   - Hacer tap en un resultado → añade al carrito o ve detalle

**Caminos alternativos:**

- Si la query NO es ambigua: el array de facetas viene vacío; UI no renderiza chips; flujo idéntico al actual
- Si el cliente cambia la query antes de aplicar faceta: dispara `facet_dismissed` (telemetría) y se calcula nuevo set de facetas para la nueva query

## 3.5 FAQs

| Pregunta | Respuesta |
|----------|-----------|
| **¿Las facetas son las mismas para todos los clientes?** | En v1, sí. Personalización por historial está en v2 (PERS-01, PERS-02). |
| **¿Qué pasa si una query es ambigua pero el catálogo no tiene atributos estructurados para diferenciarla?** | El generador devuelve <3 facetas; en ese caso, el frontend no renderiza chips. Caso esperado: muy raro porque casi todo el catálogo tiene atributos. |
| **¿Cómo se actualiza `facet_usage_stats` (tabla de uso histórico)?** | En v1, lectura desde dump pre-calculado actualizado diariamente. En Phase 3, los eventos `facet_applied` alimentan la tabla en near-real-time. |
| **¿Las facetas funcionan con búsqueda por voz?** | No en v1. Out of scope (ver §3.6). |
| **¿Qué pasa si el flag está desactivado?** | El endpoint responde idéntico al pre-feature. Test de regresión lo verifica (acceptance #7 del SPEC.md). |
| **(Eng) ¿Dónde se calcula la entropía discriminatoria?** | En el search service, post-ranker, antes de serializar la respuesta. <10ms p99 según DETECT-03. |
| **(Eng) ¿Cómo se hace el A/B test?** | Feature flag con audiencia gradual: 10% → 50% → 100%, comparando KPIs vs grupo de control. |

## 3.6 Exclusiones

(Sin cambios respecto a `prd-from-gsd.md` — ver allí.)

---

*PRD completado el 2026-04-30 por José Pérez (PM). Listo para `/prd-quality-guard`.*
