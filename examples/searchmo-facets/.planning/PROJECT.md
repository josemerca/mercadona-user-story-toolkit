# SearchMO — Faceted Search

## What This Is

Extensión del buscador de la app de e-commerce SearchMO para soportar **facetas inline**: cuando una consulta es ambigua (ej: "café"), la respuesta del buscador incluye filtros sugeridos (tipo, intensidad, formato, etc.) que el cliente puede aplicar con un tap, sin tener que escribir queries más largas o navegar por categorías.

## Core Value

Reducir la fricción de la búsqueda ambigua para clientes recurrentes, aumentando la conversión a "añadir al carrito" y reduciendo búsquedas abandonadas.

## Requirements

### Validated

(Ninguno aún — esta es la primera iteración del feature.)

### Active

- [ ] Detección de ambigüedad por query (heurísticas + threshold de diversidad de categorías en top-K resultados)
- [ ] Generación de facetas relevantes por query (las 3-5 facetas con mayor poder discriminatorio en los resultados)
- [ ] Render de chips de faceta en el listado de resultados (ordenados por uso histórico)
- [ ] Aplicar/quitar faceta refresca resultados sin recargar página
- [ ] Telemetría: event `facet_shown`, `facet_applied`, `facet_dismissed` con contexto de query

### Out of Scope

- Multi-faceta combinada (aplicar ≥2 facetas a la vez) — diferido a v2 cuando validemos uso de facetas individuales
- Facetas para queries no ambiguas — fuera de scope porque añade ruido visual sin valor
- Facetas en búsqueda por voz — depende de roadmap de voz, fuera de este Q
- Configuración manual de facetas por categoría — el ranking es algoritmico, no curated

## Context

SearchMO es el buscador propio de la app, en producción desde Q1 2026 reemplazando una solución de terceros. Los logs muestran que el ~12% de queries son ambiguas (multiples categorías de producto en los top-10 resultados con dispersión similar). Las queries ambiguas tienen una tasa de "search abandon" un 1.8x superior a las queries específicas.

El equipo del buscador ha completado la fase 1 (búsqueda exacta + tolerancia a typos). Esta es la fase 2 del roadmap del buscador.

## Constraints

- **Performance:** la generación de facetas no puede añadir más de 50ms p99 a la latencia del search response
- **Mobile-first:** la UI debe funcionar bien en pantalla pequeña; las facetas no pueden empujar los resultados fuera del viewport inicial
- **Sin acoplamiento al ranker:** las facetas se calculan post-ranker, no afectan el orden de los resultados base
- **Tech stack:** consistente con resto de SearchMO (search service en backend + componente React en mobile/web)

## Key Decisions

| Decisión | Rationale | Outcome |
|----------|-----------|---------|
| Facetas algorítmicas, no curated | Curated requiere mantenimiento manual; algorítmico escala con el catálogo | ✓ Aprobado por arquitectura |
| Detección de ambigüedad por dispersión de categorías | Más robusto que solo por entropía de top-K results | ✓ Validado en spike previo |
| Sin multi-faceta en v1 | Aprender de uso de faceta individual antes de añadir complejidad combinatoria | ✓ Aprobado por PM |
| Facetas como chips inline, no como sidebar | Sidebar consume viewport en mobile; chips inline son progresivos | ✓ Validado con design |

---

*Last updated: 2026-04-28 after roadmap kickoff*
