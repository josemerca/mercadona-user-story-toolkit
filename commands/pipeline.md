---
name: pipeline
description: "Ejecutar pipeline completo: PRD/GSD → Research → Stories → Validación → Splitting → Priorización"
---

Ejecuta el pipeline completo del toolkit de user stories.

**Paso 0: ¿De dónde partes?**

Preguntar al PM:

> ¿Qué tipo de documento tienes como punto de partida?
> 1. **PRD** — Documento con problema, solución, métricas, scope
> 2. **GSD** — Proyecto con `.planning/` de Get Shit Done
> 3. **Sin documento** — Empezar desde cero con guía conversacional

---

**Ruta A: PRD**
```
/prd-quality-guard → /research (source_type=PRD) → [entrevistas] → /analyze-research → /stories → /validate-stories → /split-stories → /prioritize
```

**Ruta B: GSD**
```
/from-gsd → [completar GAPs] → /prd-quality-guard → /research (source_type=PRD, reutiliza .planning/phases/N/RESEARCH.md si existe) → [entrevistas] → /analyze-research → /stories → /validate-stories → /split-stories → /prioritize
```

**Ruta C: Sin documento**
```
/build-story → /validate-stories → /split-stories → /prioritize
```

---

**Proceso paso a paso:**

### Ruta A: PRD

1. **PRD Quality Gate** (`/prd-quality-guard`)
   - Evaluar calidad del PRD (problema, solución, métricas, discovery, scope)
   - Si FAIL → detener y dar feedback
   - Si PASS → continuar

2. **Research Design** (`/research`)
   - Diseñar guión de entrevistas (Mom Test)
   - Adaptar según gaps detectados
   - **PAUSA:** El usuario debe realizar las entrevistas

3. **Analysis** (`/analyze-research`)
   - Analizar notas de entrevistas
   - Evaluar calidad de evidencia (Research Gap Detection)
   - Generar JTBDs con evidencia real

4. **Story Generation** (`/stories`)
   - Convertir JTBDs en stories
   - Aplicar scoring 6 dimensiones

5. **Validation** (`/validate-stories`)
   - Validar stories contra antipatrones
   - Generar reporte de calidad

6. **Story Splitting** (`/split-stories`)
   - Escanear stories validadas buscando red flags lingüísticos
   - Aplicar heurísticas de splitting (9 técnicas)
   - **Opcional si** Score Dim 6 ≥8 en todas las stories

7. **Priorización** (`/prioritize`)
   - Evaluar stories con 5 lentes (Value, Learning, Dependencies, Risk of Delay, Inv. Complexity)
   - Construir grafo de dependencias
   - Generar batches iterativos anti-waterfall

### Ruta B: GSD

1. **GSD → PRD synthesis** (`/from-gsd`)
   - Lee `.planning/PROJECT.md` + `REQUIREMENTS.md` + `ROADMAP.md` + `phases/N/SPEC.md|RESEARCH.md`
   - Genera `prd-from-gsd.md` con secciones rellenas o marcadas como GAP
   - GAPs típicos: Farolas (cuantitativo), Penumbras (cualitativo), aspectos financieros, métricas baseline→target, FAQs

2. **Completar GAPs** (PM trabajo manual)
   - Especialmente Farolas y Métricas si hay datos disponibles

3-9. **Mismos pasos que Ruta A** (desde `/prd-quality-guard prd-from-gsd.md`)
   - Si `phases/N/RESEARCH.md` existe → `/research` lo reutiliza con `--evidence-from`

### Ruta C: Sin documento

1. **Story Builder** (`/build-story`)
   - Guía conversacional para crear stories desde cero
   - Output: stories con JTBD

2-4. **Validation → Splitting → Priorización** (mismos pasos que Ruta A, steps 5-7)

---

**Output:** Stories validadas, correctamente dimensionadas, y **priorizadas en batches iterativos** listas para tu issue tracker o para pasar a tu ejecutor (Superpowers, Cursor agents, equipo, etc.).

**Nota:** El pipeline tiene una pausa natural entre `/research` y `/analyze-research` (tiempo para realizar las entrevistas). Cada comando puede ejecutarse individualmente.

**Bridge a ejecución (opcional):** Si usas GSD para planning + Superpowers para implementación, instala el `bridge/gsd-bridge.py` para mantener `STATE.md`/`ROADMAP.md`/`PLAN.md` sincronizados con los commits. Ver `bridge/README.md`.
