# Guía de Scoring — PRD Quality Guard

## Escala General

| Score | Estado | Gate Decision |
|-------|--------|---------------|
| 🔴 0-4 | Requiere reescritura significativa | **FAIL** — No pasar a research |
| 🟡 5-6 | Necesita refinamiento | **CONDICIONAL** — Iterar secciones débiles |
| 🟢 7-8 | Listo para research | **PASS** — Proceder a research-from-prd |
| ⭐ 9-10 | Modelo a seguir | **PASS** — Referencia para otros PRDs |

**Score Global = Promedio(D1, D2, D3)**
**Regla especial:** Si D3 < 5 → FAIL automático (Discovery insuficiente = alto riesgo)

---

## D1: Completitud EAC (0-10)

Evalúa si el Estado Actual Conocido (problema + evidencia) está definido con profundidad y rigor.

### Rúbrica detallada

| Score | Criterios | Señales |
|-------|-----------|---------|
| **0-2** | Sin definición clara del problema. No hay Farolas ni Penumbras. | "Necesitamos mejorar X" sin contexto. Sin datos cuantitativos ni cualitativos. |
| **3-4** | Problema vagamente enunciado. ≤2 Farolas sin baseline. Penumbras genéricas sin fuente. | "Los tiempos son altos" sin datos. Penumbras tipo "los usuarios se quejan" sin cita. |
| **5-6** | Problema definido pero incompleto. 2-3 Farolas con baseline parcial. Penumbras con observaciones pero sin citas directas. Falta contexto temporal. | Farolas con baseline pero sin target. Penumbras sin identificar fuente. Sin "¿por qué ahora?". |
| **7-8** | Problema bien definido en 2-3 frases. ≥3 Farolas con baseline + fuente. ≥3 Penumbras con observaciones reales y citas. Contexto temporal claro. Impacto cuantificado. | "Tiempo picking: 45min→30min obj (Dashboard OPS, Ene 2026)". Citas directas de usuarios. |
| **9-10** | Todo lo anterior + triangulación de fuentes (datos + observación + entrevistas). Impacto cuantificado en €. Tendencia temporal. Conexión con objetivos estratégicos. | ROI estimado. Benchmarks. Correlación entre métricas. Alineación con OKRs Q. |

### Checklist de evaluación D1

| # | Criterio | Peso | Presente | Score parcial |
|---|----------|------|----------|---------------|
| 1 | Problema definido concretamente (quién, qué, cuánto) | Alto | ☐ | 0-2 |
| 2 | Farolas (≥3 datos cuantitativos con baseline y fuente) | Alto | ☐ | 0-2 |
| 3 | Penumbras (≥3 observaciones reales con procedencia) | Alto | ☐ | 0-2 |
| 4 | Contexto temporal ("¿por qué ahora?") | Medio | ☐ | 0-2 |
| 5 | Impacto cuantificado (usuarios afectados, €, operaciones) | Medio | ☐ | 0-1 |
| 6 | Próximos pasos concretos y accionables | Bajo | ☐ | 0-1 |

### Ejemplos

**Score 3 (Malo):**
> "Hay problemas con el proceso de preparación de pedidos que afectan a la eficiencia."
> - Sin datos, sin citas, sin cuantificación del impacto

**Score 7 (Bueno):**
> "Los pickers del almacén central tardan 45 min/pedido urgente (vs 30 min objetivo),
> con 8% tasa de error. Genera +15% horas extra y NPS -12 en pedidos urgentes (Q4 2025)."
> - Farolas claras con baseline y fuente
> - Impacto cuantificado en múltiples dimensiones
> - Contexto temporal

---

## D2: Claridad EFC + Métricas (0-10)

Evalúa si el Estado Futuro Conocido es específico, medible y con impacto financiero dimensionado.

### Rúbrica detallada

| Score | Criterios | Señales |
|-------|-----------|---------|
| **0-2** | Sin hipótesis de solución. Sin métricas. Sin aspectos financieros. | "Vamos a mejorar" sin especificar qué ni cómo medir. |
| **3-4** | Solución vaga. Métricas genéricas sin baseline→target. Sin financiero. | "Mejorar tiempos" sin números. "Reducir errores" sin target. |
| **5-6** | Solución descrita pero genérica. Métricas con baseline pero sin target. Financiero estimado sin detalle. | "Dashboard de pedidos" sin justificación. Métricas parciales. ROI "estimamos que positivo". |
| **7-8** | Hipótesis formulada correctamente ("creemos que X resultará en Y"). ≥2 métricas con baseline→target→plazo. Financiero con números. Dimensionamiento realista. | Hipótesis basada en EAC. Métricas: "45min→30min en Q2". Coste estimado. ROI calculado. |
| **9-10** | Todo lo anterior + múltiples escenarios (optimista/pesimista). Criterios de éxito con umbral de decisión go/no-go. Payback period. Sensitivity analysis. | Escenarios cuantificados. "Si no mejora >20% en 4 semanas → pivot". |

### Checklist de evaluación D2

| # | Criterio | Peso | Presente | Score parcial |
|---|----------|------|----------|---------------|
| 1 | Hipótesis de solución específica y basada en EAC | Alto | ☐ | 0-2 |
| 2 | Métricas con baseline → target → plazo → método medición | Alto | ☐ | 0-2 |
| 3 | Aspectos financieros con números (coste, ahorro, ROI) | Alto | ☐ | 0-2 |
| 4 | Dimensionamiento realista (usuarios, volumen, fases) | Medio | ☐ | 0-2 |
| 5 | Criterios de éxito medibles (go/no-go threshold) | Medio | ☐ | 0-1 |
| 6 | Impacto multi-dimensional (usuario + negocio + ops) | Bajo | ☐ | 0-1 |

### Ejemplos

**Score 3 (Malo):**
> "Implementaremos una mejora que aumentará la productividad significativamente."
> - Sin hipótesis, sin métricas, sin financiero

**Score 7 (Bueno):**
> "Creemos que una vista consolidada con priorización automática para pickers reducirá
> el tiempo de picking urgente de 45min a 30min (Q2 2026), la tasa de error del 8% al 3%,
> y las horas extra en un 10%. Coste estimado: 120k€. Ahorro anual: 280k€. Payback: 6 meses."
> - Hipótesis basada en EAC
> - Métricas con baseline→target→plazo
> - Financiero con ROI

---

## D3: Rigor Discovery + Scope (0-10)

Evalúa si el Discovery fue riguroso, si se exploraron alternativas, y si el scope está bien delimitado.

### Rúbrica detallada

| Score | Criterios | Señales |
|-------|-----------|---------|
| **0-2** | Sin Discovery documentado. Sin Explore. Scope vago. | "Hicimos research" sin detallar. Sin alternativas. "El scope incluye todo lo necesario". |
| **3-4** | Discovery mencionado pero sin metodología ni hallazgos. Explore con 1 alternativa descartada sin criterios. Scope sin exclusiones. | "Hablamos con usuarios" sin más detalle. 1 alternativa: "lo descartamos". Sin FAQs. |
| **5-6** | Discovery con metodología y hallazgos parciales. Explore con ≥2 alternativas pero criterios vagos. Funcionalidades listadas sin priorizar. Sin exclusiones explícitas o FAQs. | Entrevistas realizadas con hallazgos. Alternativas con "nos pareció mejor". Features sin must/nice-to-have. |
| **7-8** | Discovery riguroso: metodología + ≥3 hallazgos + cómo informan la solución. Explore con ≥2 alternativas + criterios de evaluación. Funcionalidades priorizadas. Flujos documentados. Exclusiones explícitas. FAQs. | Entrevistas + observación. Criterios: coste, tiempo, complejidad. Features con P1/P2. ≥3 exclusiones. ≥5 FAQs. |
| **9-10** | Todo lo anterior + Discovery multi-método (entrevistas + observación + datos). Explore con análisis coste-beneficio por alternativa. Flujos con caminos alternativos/error. FAQs técnicas + negocio. Exclusiones con justificación y roadmap futuro. | Triangulación completa. Tabla comparativa de alternativas. Flujos con excepciones. FAQs anticipatorias. |

### Checklist de evaluación D3

| # | Criterio | Peso | Presente | Score parcial |
|---|----------|------|----------|---------------|
| 1 | Discovery con metodología documentada y ≥3 hallazgos | Alto | ☐ | 0-2 |
| 2 | Explore con ≥2 alternativas y criterios de evaluación | Alto | ☐ | 0-2 |
| 3 | Funcionalidades priorizadas (must/nice-to-have) | Alto | ☐ | 0-2 |
| 4 | Flujos de usuario documentados con actores | Medio | ☐ | 0-2 |
| 5 | Exclusiones explícitas (≥3) con justificación | Medio | ☐ | 0-1 |
| 6 | FAQs (≥5) que anticipan preguntas del equipo | Bajo | ☐ | 0-1 |

### Ejemplos

**Score 3 (Malo):**
> Discovery: "Hablamos con varios usuarios y coinciden en que hay que mejorar."
> Explore: "No hay alternativas viables."
> - Sin metodología, sin hallazgos, sin alternativas reales

**Score 7 (Bueno):**
> Discovery: "Realizamos 5 entrevistas con pickers + 2 sesiones de observación.
> Hallazgos: (1) 60% del tiempo extra es decidir prioridad, (2) pickers usan
> Post-its como workaround, (3) coordinadores duplican info en 3 herramientas."
> Explore: "Evaluamos 3 opciones: (A) Dashboard custom, (B) Integrar en MOT,
> (C) Alertas Slack. Criterios: coste, adopción, mantenimiento. Elegimos B por..."
> - Metodología clara, hallazgos concretos, alternativas con criterios

---

## Antipatrones y Penalizaciones

### Mecanismo de penalización

Los antipatrones se detectan DESPUÉS del scoring base y modifican los scores de dimensión:

| Antipatrón | Penalización | Dimensión afectada |
|------------|-------------|-------------------|
| AP-PRD-1: EAC vago | Limita D1 ≤4 | D1 |
| AP-PRD-2: EFC sin métricas | Limita D2 ≤4 | D2 |
| AP-PRD-3: Solución en Problema | -2 en D1, -1 en D3 | D1, D3 |
| AP-PRD-4: Sin FAQs/exclusiones | Limita D3 ≤6 | D3 |
| AP-PRD-5: Violación escritura | -1 por cada 3 violaciones (máx -3) | D1 |

---

## Combinación de Dimensiones y Decisión de Gate

### Fórmula

```
Score Global = (D1 + D2 + D3) / 3
```

### Reglas especiales

1. **D3 < 5 → FAIL automático** (Discovery insuficiente = alto riesgo para research)
2. **Si algún AP-PRD es CRÍTICO → advertir explícitamente** (incluso si score global ≥7)
3. **Score Global se redondea a 1 decimal** (ej: 6.7)

### Prioridad de mejora (si CONDICIONAL)

1. **D3 primero** — Discovery/Scope es el fundamento del research
2. **D1 segundo** — EAC es la base de toda decisión
3. **D2 tercero** — EFC se beneficia de D1+D3 mejorados
