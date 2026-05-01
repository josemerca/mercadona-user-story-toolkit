# Priorización de Stories — SearchMO Faceted Search

**Generado por:** `/prioritize`
**Input:** 5 stories validadas (de `stories-validated.md`)
**Stories evaluadas:** 5
**Batches propuestos:** 3
**Fecha:** 2026-04-30

---

## Scoring por 5 Lentes (escala 1-5)

| Story | Value (30%) | Learning (25%) | Dependencies (20%) | Risk of Delay (15%) | Inv. Complexity (10%) | Total |
|-------|-------------|----------------|--------------------|--------------------|-----------------------|-------|
| 1. DETECT-01 | 3 | 4 | 5 | 5 | 5 | **4.05** |
| 2. FACET-01/02 | 4 | 4 | 5 | 5 | 4 | **4.30** |
| 3. FACET-03/04 | 3 | 3 | 4 | 4 | 4 | **3.45** |
| 4. UI-01 a UI-05 | 5 | 5 | 3 | 4 | 3 | **4.20** |
| 5. TELEM-01 a TELEM-04 | 4 | 5 | 3 | 4 | 4 | **4.05** |

## Grafo de dependencias

```
        ┌──────────────────────┐
        │ 1. DETECT-01         │
        │ (clasifica queries)  │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │ 2. FACET-01/02       │
        │ (genera facetas)     │
        └──────────┬───────────┘
                   │
        ┌──────────┴───────────┐
        ▼                      ▼
┌─────────────────┐    ┌──────────────────┐
│ 3. FACET-03/04  │    │ 4. UI-01 a UI-05 │
│ (orden facetas) │    │ (chips render)   │
└────────┬────────┘    └────────┬─────────┘
         │                      │
         └──────────┬───────────┘
                    ▼
         ┌──────────────────────┐
         │ 5. TELEM-01 a TELEM-04│
         │ (eventos analytics)  │
         └──────────────────────┘
```

**Validación de dependencias genuinas:**
- Story 2 → Story 1: ✓ Genuina (sin clasificación, no se sabe cuándo generar facetas)
- Story 3 → Story 2: ✓ Genuina (sin facetas generadas, no hay nada que ordenar)
- Story 4 → Story 2: ✓ Genuina (sin facetas en respuesta, UI no tiene qué pintar)
- Story 5 → Story 4: ✓ Genuina (sin UI con chips, no hay eventos que disparar)

Sin dependencias falsas detectadas.

---

## Batches propuestos (anti-waterfall)

### Batch 1 — Backend mínimo viable end-to-end

**Stories:** 1 (DETECT-01) + 2 (FACET-01/02)
**Valor entregado:** El endpoint `/search` ya devuelve facetas para queries ambiguas. Aunque sin UI, el backend es completo y testeable.
**Razón anti-waterfall:** En lugar de esperar a tener UI para validar el algoritmo, el batch 1 permite probar el algoritmo end-to-end con clientes API/curl. Si la calidad de las facetas generadas es mala, lo descubrimos antes de invertir en UI.
**Estimación:** ~2 semanas (Phase 1 del roadmap)

### Batch 2 — UI funcional con orden básico

**Stories:** 3 (FACET-03/04) + 4 (UI-01 a UI-05)
**Valor entregado:** Cliente real puede aplicar facetas. Feature funcionalmente completo.
**Razón anti-waterfall:** En lugar de pulir el ranking de facetas (Story 3) en aislamiento, lo entregamos junto con la UI para que el ranking se valide con uso real, no con tests sintéticos.
**Estimación:** ~2-3 semanas (Phase 2 del roadmap)

### Batch 3 — Telemetría y validación

**Stories:** 5 (TELEM-01 a TELEM-04)
**Valor entregado:** Capacidad de medir el feature y decidir GA o rollback.
**Razón anti-waterfall:** El feature ya está en producción tras Batch 2 (con feature flag al 10%). Batch 3 cierra el loop de medición. Si las hipótesis no se cumplen, el flag permite rollback inmediato.
**Estimación:** ~1-1.5 semanas (Phase 3 del roadmap)

---

## Reglas anti-waterfall verificadas

- ✅ AW-1 (Cada batch entrega valor usuario): Batch 1 (validación de algoritmo), Batch 2 (UX completo), Batch 3 (medición). Cada uno aporta valor independiente.
- ✅ AW-2 (No infra-first): el batch 1 es backend pero entrega capacidad usable (testeable vía API), no infra puramente preparatoria.
- ✅ AW-3 (No capas técnicas separadas): batch 2 mezcla deliberadamente lógica de ranking + UI para validar juntos.
- ✅ AW-4 (No valor solo al final): batch 1 ya permite validar la hipótesis del algoritmo sin esperar al final.
- ✅ AW-5 (No spike infinito): no hay spikes en este plan; el spike previo (validación técnica) ya se hizo y está en `Key Decisions` del PROJECT.md.

---

## Recomendación final

Empezar con **Batch 1** ya. Mientras Eng trabaja en él:
- Diseño puede preparar mocks finales para Batch 2
- PM puede preparar plan de telemetría para Batch 3
- Data puede dejar listo el dump inicial de `facet_usage_stats`

Esto permite que Batch 2 arranque sin demoras tras Batch 1.
