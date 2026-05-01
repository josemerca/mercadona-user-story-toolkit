# PRD Quality Guard — Reference

Material de referencia para el skill `prd-quality-guard`. El procedimiento core esta en `SKILL.md`.

---

## S1 Estructura del PRD

El PRD sigue la estructura definida en `references/prd-structure.md`.

**Secciones principales:**

| Seccion | Tipo | Que contiene |
|---------|------|--------------|
| Problema | EAC | Definicion del problema con contexto |
| Farolas | EAC | Evidencia cuantitativa |
| Penumbras | EAC | Evidencia cualitativa |
| Proximos pasos | EAC | Que se necesita para avanzar |
| Hipotesis Solucion | EFC | Propuesta de solucion con justificacion |
| Aspectos financieros | EFC | Impacto economico y ROI |
| Metricas | EFC | KPIs medibles con baseline y target |
| Dimensionamiento | EFC | Alcance y escala |
| Discovery | Discovery | Investigacion realizada |
| Explore | Discovery | Alternativas exploradas |
| Funcionalidades principales | Scope | Features incluidas |
| Flujos de usuario | Scope | User flows |
| FAQs | Scope | Preguntas frecuentes y respuestas |
| Exclusiones | Scope | Que NO esta en scope |

---

## S2 Rubrica D1: Completitud EAC (0-10)

Evalua si el Estado Actual Conocido esta definido con suficiente profundidad y evidencia.

**Secciones PRD implicadas:** Problema, Farolas, Penumbras, Proximos pasos

**Checklist de evaluacion:**

| # | Criterio | Peso | Presente | Score parcial |
|---|----------|------|----------|---------------|
| 1 | Problema definido en 2-3 frases concretas (no vagas) | Alto | _ | 0-2 |
| 2 | Farolas: >=3 datos cuantitativos con baseline | Alto | _ | 0-2 |
| 3 | Penumbras: >=3 observaciones cualitativas reales | Alto | _ | 0-2 |
| 4 | Contexto temporal: por que ahora? | Medio | _ | 0-2 |
| 5 | Impacto cuantificado (usuarios, EUR, operaciones) | Medio | _ | 0-1 |
| 6 | Proximos pasos claros y accionables | Bajo | _ | 0-1 |

**Score rapido:**
- 0-4: Problema vago, sin datos, sin observaciones
- 5-6: Problema definido pero sin Farolas/Penumbras suficientes
- 7-8: Problema claro + >=3 Farolas + >=3 Penumbras + contexto
- 9-10: Todo anterior + impacto cuantificado en EUR + triangulacion de fuentes

---

## S3 Rubrica D2: Claridad EFC + Metricas (0-10)

Evalua si el Estado Futuro Conocido es especifico, medible y con impacto dimensionado.

**Secciones PRD implicadas:** Hipotesis Solucion, Aspectos financieros, Metricas, Dimensionamiento

**Checklist de evaluacion:**

| # | Criterio | Peso | Presente | Score parcial |
|---|----------|------|----------|---------------|
| 1 | Hipotesis de solucion especifica (no generica) | Alto | _ | 0-2 |
| 2 | Metricas con baseline -> target | Alto | _ | 0-2 |
| 3 | Aspectos financieros con numeros concretos | Alto | _ | 0-2 |
| 4 | Dimensionamiento realista | Medio | _ | 0-2 |
| 5 | Criterios de exito medibles | Medio | _ | 0-1 |
| 6 | Impacto en >=2 dimensiones (usuario, negocio, ops) | Bajo | _ | 0-1 |

**Score rapido:**
- 0-4: Sin metricas, solucion vaga, sin impacto financiero
- 5-6: Metricas genericas, solucion descrita pero no especifica
- 7-8: Metricas con baseline->target + solucion especifica + financiero
- 9-10: Todo anterior + multi-dimensional + criterios de exito claros

---

## S4 Rubrica D3: Rigor Discovery + Scope (0-10)

Evalua si el Discovery fue riguroso y el scope esta bien definido (incluidas y excluidas).

**Secciones PRD implicadas:** Discovery, Explore, Funcionalidades principales, Flujos usuario, FAQs, Exclusiones

**Checklist de evaluacion:**

| # | Criterio | Peso | Presente | Score parcial |
|---|----------|------|----------|---------------|
| 1 | Discovery documentado con metodologia | Alto | _ | 0-2 |
| 2 | Explore con >=2 alternativas consideradas | Alto | _ | 0-2 |
| 3 | Funcionalidades claramente priorizadas | Alto | _ | 0-2 |
| 4 | Flujos de usuario documentados | Medio | _ | 0-2 |
| 5 | Exclusiones explicitas | Medio | _ | 0-1 |
| 6 | FAQs que anticipan preguntas del equipo | Bajo | _ | 0-1 |

**Score rapido:**
- 0-4: Sin Discovery, sin Explore, scope vago
- 5-6: Discovery basico, pocas alternativas, scope parcial
- 7-8: Discovery riguroso + >=2 alternativas + scope con exclusiones
- 9-10: Todo anterior + flujos detallados + FAQs anticipatorias

**Regla especial:** Si D3 < 5 -> FAIL automatico (Discovery insuficiente = alto riesgo)

---

## S5 Gate Decision — Matriz y Prioridad

### Matriz de Decision

| D1 | D2 | D3 | Global | Gate | Accion |
|----|----|----|--------|------|--------|
| >=7 | >=7 | >=7 | >=7 | PASS | Proceder a research |
| >=7 | >=7 | 5-6 | ~6.5 | CONDICIONAL | Mejorar Discovery/Scope |
| >=7 | 5-6 | >=7 | ~6.5 | CONDICIONAL | Mejorar metricas EFC |
| 5-6 | >=7 | >=7 | ~6.5 | CONDICIONAL | Mejorar EAC |
| >=7 | >=7 | <5 | -- | FAIL | D3 < 5 = FAIL automatico |
| <5 | <5 | any | <5 | FAIL | Reescritura significativa |

### Prioridad de mejora (si CONDICIONAL)

1. **D3 primero** — Mejorar Discovery/Scope (fundamento del research)
2. **D1 segundo** — Mejorar EAC (problema bien definido)
3. **D2 tercero** — Mejorar EFC (se beneficia de D1+D3 mejorados)

---

## S6 Antipatrones PRD-Especificos (5)

### AP-PRD-1: EAC Vago

**Senal:** Seccion Problema con frases genericas sin datos.
**Ejemplos:**
- "Necesitamos mejorar la experiencia del usuario"
- "El proceso actual no es eficiente"
- "Hay margen de mejora en..."

**Impacto:** D1 <=4
**Correccion:** Definir el problema con datos concretos: quien, que, cuanto, desde cuando.

---

### AP-PRD-2: EFC Sin Metricas Medibles

**Senal:** Hipotesis de solucion sin baseline->target.
**Ejemplos:**
- "Mejorar significativamente los tiempos"
- "Aumentar la satisfaccion del usuario"
- "Reducir costes operativos"

**Impacto:** D2 <=4
**Correccion:** Cada metrica debe tener: nombre, baseline actual, target, plazo.

---

### AP-PRD-3: Solucion en Seccion de Problema

**Senal:** La seccion EAC/Problema ya describe COMO resolver, no solo QUE pasa.
**Ejemplos:**
- "El problema es que no tenemos un dashboard de..."
- "Necesitamos implementar un sistema que..."
- "La solucion pasa por automatizar..."

**Impacto:** D1 penalizado, D3 sesgado
**Correccion:** Separar claramente el problema (EAC) de la solucion propuesta (EFC).

---

### AP-PRD-4: Sin FAQs o Exclusiones Explicitas

**Senal:** No hay seccion de exclusiones ni FAQs.
**Ejemplos:**
- Scope que solo dice "incluye" sin decir "excluye"
- Sin FAQs que anticipen preguntas del equipo
- Scope ambiguo en los bordes

**Impacto:** D3 <=6
**Correccion:** Anadir al menos 3 exclusiones explicitas y 5 FAQs.

---

### AP-PRD-5: Violacion Reglas de Escritura el PRD

**Senal:** Texto que no cumple reglas de escritura del formato el PRD.
**Criterios:**
- Frases >30 palabras
- Adjetivos sin datos que los respalden ("muy", "bastante", "significativo")
- Bullet points con >3 niveles de anidacion
- Secciones sin encabezado claro

**Impacto:** -1 punto por cada 3 violaciones detectadas (max -3 puntos en D1)
**Correccion:** Reescribir siguiendo reglas de escritura el PRD.

---

## S7 Template Inventario de Secciones

```markdown
## Inventario de Secciones PRD

### EAC (Estado Actual Conocido)
| Seccion | Estado | Observacion |
|---------|--------|-------------|
| Problema | ok/parcial/vacio | {Detalle} |
| Farolas | ok/parcial/vacio | {Detalle} |
| Penumbras | ok/parcial/vacio | {Detalle} |
| Proximos pasos | ok/parcial/vacio | {Detalle} |

### EFC (Estado Futuro Conocido)
| Seccion | Estado | Observacion |
|---------|--------|-------------|
| Hipotesis Solucion | ok/parcial/vacio | {Detalle} |
| Aspectos financieros | ok/parcial/vacio | {Detalle} |
| Metricas | ok/parcial/vacio | {Detalle} |
| Dimensionamiento | ok/parcial/vacio | {Detalle} |

### Discovery + Scope
| Seccion | Estado | Observacion |
|---------|--------|-------------|
| Discovery | ok/parcial/vacio | {Detalle} |
| Explore | ok/parcial/vacio | {Detalle} |
| Funcionalidades | ok/parcial/vacio | {Detalle} |
| Flujos usuario | ok/parcial/vacio | {Detalle} |
| Exclusiones | ok/parcial/vacio | {Detalle} |
| FAQs | ok/parcial/vacio | {Detalle} |

**Resumen:** {N}/14 secciones completas ({%})
```
