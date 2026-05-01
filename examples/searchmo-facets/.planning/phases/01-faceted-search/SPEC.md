# Phase 1: Faceted Search Backend — Specification

**Created:** 2026-04-29
**Ambiguity score:** 0.14 (gate: ≤ 0.20)
**Requirements:** 7 locked

## Goal

El endpoint `/search` extiende su respuesta con un campo `facets` que, para queries ambiguas, contiene 3-5 facetas relevantes con sus valores ordenados por relevancia. Para queries específicas, el campo está vacío. La latencia p99 del endpoint se mantiene ≤200ms.

## Background

SearchMO opera hoy en producción con búsqueda exacta + tolerancia a typos (Phase 1 del roadmap del buscador, ya desplegado). Los logs de search service muestran:

- ~12% de queries son ambiguas (top-20 results con ≥3 categorías de peso ≥10%)
- Las queries ambiguas tienen 1.8x más "search abandons" (cliente sale del buscador sin tap en resultado)
- El catálogo tiene atributos estructurados por producto (categoría, marca, formato, tipo, intensidad, etc.) — disponibles via product service

El backend de search ya tiene acceso a estos atributos cuando construye los resultados. La fase 1 añade la lógica de detección de ambigüedad y generación de facetas sobre la respuesta existente.

## Requirements

1. **Detección de ambigüedad**: El servicio clasifica cada query como `ambiguous` o `specific`.
   - Current: No existe esta clasificación; todas las queries reciben los mismos resultados sin metadata adicional.
   - Target: Cada respuesta de search incluye `query_classification: "ambiguous" | "specific"` en metadata.
   - Acceptance: Test con 50 queries de prueba (25 ambiguas, 25 específicas) — el clasificador acierta ≥90%.

2. **Threshold configurable**: El umbral de ambigüedad se ajusta vía feature flag sin redeploy.
   - Current: N/A.
   - Target: Feature flag `search.facets.ambiguity_threshold` (default: 3 categorías, 10% peso) controla el comportamiento.
   - Acceptance: Cambiar el flag en runtime modifica la clasificación sin reiniciar el servicio.

3. **Generación de facetas**: Para queries `ambiguous`, el servicio selecciona 3-5 facetas relevantes.
   - Current: N/A.
   - Target: Respuesta incluye array `facets: [{name, values: [{value, count}]}]` con 3-5 entradas.
   - Acceptance: Para cada query de prueba ambigua, el array tiene 3-5 facetas; cada faceta tiene 2-10 valores.

4. **Ordenación de facetas por uso histórico**: Las facetas se ordenan por frecuencia histórica de aplicación (no por entropía).
   - Current: N/A.
   - Target: Cuando hay >5 facetas candidatas, las 5 elegidas son las que más se han aplicado históricamente.
   - Acceptance: Tabla `facet_usage_stats` consultada por el servicio; test verifica el orden con datos sintéticos.

5. **Ordenación de valores por frecuencia local**: Los valores de cada faceta se ordenan por aparición en los resultados de la query actual.
   - Current: N/A.
   - Target: `facets[i].values` está ordenado descendente por `count` (frecuencia en los resultados de la query).
   - Acceptance: Test con respuesta sintética verifica el orden.

6. **Latencia**: La extensión de la respuesta no degrada la latencia p99 más de 50ms.
   - Current: p99 = 145ms (con buffer respecto al SLA de 200ms).
   - Target: p99 ≤195ms con facetas habilitadas.
   - Acceptance: Test de carga con 1000 queries — comparar p99 antes/después de habilitar facetas.

7. **Compatibilidad**: Las respuestas existentes (sin facetas) siguen funcionando si el flag está deshabilitado.
   - Current: N/A.
   - Target: Si flag `search.facets.enabled = false`, el endpoint responde idéntico al pre-feature.
   - Acceptance: Test de regresión completo del endpoint con flag desactivado — 0 cambios respecto a baseline.

## Boundaries

**In scope:**
- Lógica de clasificación de ambigüedad (en search service)
- Lógica de selección de facetas + ordenación de valores
- Extensión del schema de respuesta del endpoint `/search`
- Tabla `facet_usage_stats` (lectura inicial; la actualización viene en Phase 3 con telemetría)
- Feature flag de control

**Out of scope:**
- UI de facetas (Phase 2)
- Eventos de telemetría (Phase 3)
- Persistencia de facetas aplicadas en sesión del cliente
- Multi-faceta combinada (v2)

## Constraints

- Performance: latencia p99 ≤200ms (SLA del search service, no negociable)
- Compatibilidad: flag desactivado debe ser indistinguible del estado actual
- Tech stack: consistente con search service existente (sin nuevas dependencias mayores)

## Acceptance Criteria

- [ ] Test unitario del clasificador con 50 queries — ≥90% de aciertos
- [ ] Test de generación de facetas con 25 queries ambiguas — todas devuelven 3-5 facetas válidas
- [ ] Test de feature flag — cambio en runtime sin redeploy
- [ ] Test de latencia — p99 ≤195ms con flag activo, ≤145ms con flag inactivo
- [ ] Test de regresión del endpoint con flag desactivado — diff vs baseline = 0
- [ ] Documentación del schema actualizada
