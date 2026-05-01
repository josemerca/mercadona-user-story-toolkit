# Walkthrough: Búsqueda con Facetas en SearchMO

Ejemplo end-to-end del pipeline **GSD → Mercadona User Story Toolkit → Superpowers** aplicado a una feature realista: añadir facetas inline en el buscador para que un cliente recurrente pueda desambiguar consultas comunes (ej: "café" → molido / grano / soluble / descafeinado).

**Por qué este ejemplo.** Continúa el caso del [artículo del buscador](https://www.gemba.es/p/como-construimos-nuestro-buscador-en-mercadona-tech). Ya tenemos el buscador en producción; ahora añadimos una mejora identificada por el equipo: el ~12% de queries son ambiguas, y la hipótesis es que un filtro de facetas inline reduce la fricción y mejora la conversión a "añadir al carrito".

> Este es un ejemplo **ilustrativo**: los artefactos son realistas pero los datos cuantitativos (farolas, métricas) son sintéticos. El feature concreto sí puede implementarse así.

---

## Flujo end-to-end

```
Fase 1 (PM): GSD                            Fase 2 (PM): MUST                       Fase 3 (Eng): Superpowers
─────────────────────────────              ────────────────────────────             ──────────────────────────
.planning/PROJECT.md           ───→        prd-from-gsd.md                          /superpowers:writing-plans
.planning/REQUIREMENTS.md       /from-gsd  + completar GAPs (Farolas,               + /superpowers:test-driven-development
.planning/ROADMAP.md           ───→        Métricas, FAQs)                           + /superpowers:subagent-driven-development
.planning/phases/01/SPEC.md                       │                                              │
.planning/phases/01/RESEARCH.md                   ▼                                              ▼
                                            /prd-quality-guard                      Tests verdes + commits con REQ-IDs
                                                  │                                              │
                                                  ▼                                              ▼
                                            /research → /analyze-research            gsd-bridge sync
                                                  │                                              │
                                                  ▼                                              ▼
                                            /stories → /validate                     STATE.md, ROADMAP.md, VERIFICATION.md
                                                  │                                  actualizados automáticamente
                                                  ▼
                                            /split-stories → /prioritize
                                                  │
                                                  ▼
                                            Stories priorizadas en batches
```

---

## Estructura del walkthrough

| Carpeta | Contenido | Producido por |
|---------|-----------|---------------|
| `.planning/` | Artefactos de GSD: PROJECT, REQUIREMENTS, ROADMAP, SPEC, PLAN, RESEARCH | PM con `gsd-new-project` + `gsd-spec-phase` |
| `prd-from-gsd.md` | PRD sintético generado a partir de `.planning/` (con GAPs marcados) | `/from-gsd` |
| `prd-completed.md` | PRD con GAPs completados a mano por el PM (Farolas, Métricas, FAQs) | PM (manual) |
| `research/` | Guión de entrevistas (Mom Test) + notas de campo + JTBDs sintetizados | `/research` + entrevistas reales + `/analyze-research` |
| `stories/` | User stories validadas + reporte priorización en batches | `/stories` + `/validate-stories` + `/split-stories` + `/prioritize` |
| `implementation/` | Plan de implementación (Superpowers) + ejemplos de tests TDD | `/superpowers:writing-plans` + `/superpowers:test-driven-development` |
| `bridge-output.md` | Estado final de `STATE.md` + `VERIFICATION.md` tras `gsd-bridge sync` | `gsd-bridge sync` |

---

## Cómo seguir el ejemplo paso a paso

1. **Lee `.planning/PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`** — entiende el contexto del proyecto
2. **Mira `prd-from-gsd.md`** — observa qué secciones rellenó `/from-gsd` y cuáles marcó como GAP
3. **Compara con `prd-completed.md`** — los GAPs (Farolas, Métricas, FAQs) los completó el PM tras research
4. **Lee `research/`** — guión de entrevistas, notas y JTBDs sintetizados
5. **Lee `stories/`** — stories validadas con scoring 6D y batches priorizados
6. **Lee `implementation/`** — plan SP, ejemplos de tests TDD y commits con REQ-IDs
7. **Lee `bridge-output.md`** — qué actualiza el bridge en `.planning/` después de la implementación

---

## Importante

- **Los datos cuantitativos son sintéticos.** Los porcentajes (12% queries ambiguas, etc.) son ilustrativos, no datos reales de SearchMO.
- **El feature es realista.** Las facetas en búsqueda son una funcionalidad estándar de e-commerce; este ejemplo enseña *el flujo*, no inventa una feature inverosímil.
- **No incluye implementación real del feature.** El walkthrough cubre artefactos hasta `/superpowers:writing-plans`. La ejecución TDD (`/superpowers:subagent-driven-development`) se ilustra con ejemplos de tests pero no produce código real.
