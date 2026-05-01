# Story Prioritization — Reference

Material de referencia para la skill `story-prioritization`. El flujo principal esta en `SKILL.md`.

---

## S1 Principio Fundamental (Diagrama Comparativo)

```
+-----------------------------------------------------------------+
|                                                                   |
|   WATERFALL DISFRAZADO              ENTREGA ITERATIVA REAL       |
|   --------------------              ----------------------       |
|                                                                   |
|   Batch 1: "Infraestructura"        Batch 1: Story valor + base  |
|   Batch 2: "Backend"                Batch 2: Story valor + learn  |
|   Batch 3: "Frontend"               Batch 3: Story valor + risk   |
|   Batch 4: "Valor usuario"          Batch 4: Story valor + deuda  |
|                                                                   |
|   X Valor al final                  OK Valor en CADA batch        |
|   X Feedback tardio                 OK Feedback temprano          |
|   X Riesgo acumulado                OK Riesgo distribuido         |
|                                                                   |
+-----------------------------------------------------------------+
```

---

## S2 Rubrica: Lente 1 — Value (Peso: 30%)

**Pregunta:** Cuanto impacto genera esta story para el negocio y el usuario?

| Score | Criterio | Senales |
|-------|----------|---------|
| **5** | Impacto critico en metrica de negocio + usuario directo | Story resuelve el struggle principal del JTBD. KPI primario del PRD. |
| **4** | Impacto alto en negocio o usuario | Story resuelve un struggle secundario. Mejora KPI significativamente. |
| **3** | Impacto moderado | Story aporta valor incremental. Mejora experiencia sin cambiar KPI core. |
| **2** | Impacto bajo o indirecto | Story aporta valor tecnico que eventualmente beneficia al usuario. |
| **1** | Sin impacto directo en usuario | Story puramente tecnica sin valor usuario demostrable. |

**Fuentes de evidencia:**
- Scoring Dim 1 (JTBD & Problem Context) de la story
- Farolas/Penumbras del EAC del PRD
- Desired Outcomes del JTBD

---

## S3 Rubrica: Lente 2 — Learning (Peso: 25%)

**Pregunta:** Cuanta incertidumbre reduce esta story?

| Score | Criterio | Senales |
|-------|----------|---------|
| **5** | Reduce incertidumbre critica del producto/negocio | Story es un spike o MVP que valida hipotesis central. Sin ella, todo lo demas es apuesta. |
| **4** | Reduce incertidumbre alta | Story valida un JTBD con baja confianza de evidencia. |
| **3** | Reduce incertidumbre moderada | Story prueba una solucion tecnica no probada. |
| **2** | Reduce incertidumbre baja | Story implementa algo conocido con variacion menor. |
| **1** | No reduce incertidumbre | Story implementa patron conocido y probado. |

**Regla anti-waterfall:** Stories con Learning 5 van PRIMERO, no despues de "fundaciones".

**Fuentes de evidencia:**
- Scoring Dim 6 (Survivable Experiment) de la story
- Gaps de research no resueltos
- Hipotesis no validadas del PRD

---

## S4 Rubrica: Lente 3 — Dependencies (Peso: 20%)

**Pregunta:** Cuantas stories desbloquea esta story?

| Score | Criterio | Senales |
|-------|----------|---------|
| **5** | Desbloquea >=4 stories | Pieza central del grafo. Sin ella, nada avanza. |
| **4** | Desbloquea 2-3 stories | Pieza importante del grafo. Varias stories esperan. |
| **3** | Desbloquea 1 story | Dependencia directa con otra story. |
| **2** | No desbloquea pero tiene dependencia | Depende de otra story pero no bloquea a nadie. |
| **1** | Sin dependencias | Completamente independiente (puede ir en cualquier batch). |

**Regla anti-waterfall:** Solo considerar dependencias tecnicas GENUINAS.
- Dep. genuina: "La story B necesita el endpoint que crea la story A"
- Dep. falsa: "Primero necesitamos la base de datos completa" (waterfall disfrazado)

---

## S5 Rubrica: Lente 4 — Risk of Delay (Peso: 15%)

**Pregunta:** Cual es el coste de NO hacer esta story pronto?

| Score | Criterio | Senales |
|-------|----------|---------|
| **5** | Coste critico de retraso | Deadline externo real (regulacion, compromiso). Cada dia sin ella = perdida medible. |
| **4** | Coste alto de retraso | Bloquea a otro equipo. Oportunidad de mercado con ventana limitada. |
| **3** | Coste moderado de retraso | Ineficiencia acumulada pero tolerable a corto plazo. |
| **2** | Coste bajo de retraso | Puede esperar sin impacto significativo. |
| **1** | Sin coste de retraso | Mejora nice-to-have sin urgencia. |

**Regla anti-waterfall:** Solo deadlines REALES. "Es urgente porque lo digo yo" no puntua 5.

---

## S6 Rubrica: Lente 5 — Inverse Complexity (Peso: 10%)

**Pregunta:** Que tan simple es implementar esta story?

| Score | Criterio | Senales |
|-------|----------|---------|
| **5** | Muy simple (1-2 dias) | Cambio acotado, patron conocido, bajo riesgo tecnico. |
| **4** | Simple (2-3 dias) | Requiere algo de trabajo pero es predecible. |
| **3** | Moderada (3-5 dias) | Requiere diseno, algunos unknowns tecnicos. |
| **2** | Compleja (5-8 dias) | Multiples componentes, integracion, riesgo tecnico. |
| **1** | Muy compleja (>8 dias) | Requiere investigacion, multiples equipos, alto riesgo. |

**Regla anti-waterfall:** Story compleja + incierta = SPIKE primero (time-boxed <=3 dias).

---

## S7 Interpretacion del Priority Score

```
Priority Score = (Value x 0.30) + (Learning x 0.25) + (Dependencies x 0.20)
               + (Risk of Delay x 0.15) + (Inv. Complexity x 0.10)

Rango: 1.00 -- 5.00
```

| Priority Score | Nivel | Batch sugerido |
|----------------|-------|----------------|
| 4.0 -- 5.0 | Muy Alta | Batch 1 (entregar primero) |
| 3.0 -- 3.9 | Alta | Batch 2 |
| 2.0 -- 2.9 | Media | Batch 3-4 |
| 1.0 -- 1.9 | Baja | Batch final o backlog |

---

## S8 Deteccion de Patrones Waterfall

### Pattern 1: "Infraestructura Primero"

**Senal:** Batch 1 tiene solo stories con Value <=2 y Inv. Complexity <=2.
**Diagnostico:** Se esta priorizando la base tecnica antes del valor.
**Correccion:** Mover al menos 1 story con Value >=4 al Batch 1 y co-ubicar la infra.

### Pattern 2: "Capas Tecnicas"

**Senal:** Batches organizados por capa (backend -> frontend -> integracion).
**Diagnostico:** Se esta cortando horizontalmente en vez de verticalmente.
**Correccion:** Reorganizar cada batch como slice vertical (de UI a BD).

### Pattern 3: "Valor al Final"

**Senal:** Stories con Value 5 estan en Batch 3+.
**Diagnostico:** Lo mas importante se entrega al final.
**Correccion:** Subir stories de Value 5 a Batch 1, incluso si requiere simplificar scope.

### Pattern 4: "Spike Infinito"

**Senal:** Story de Learning 5 sin time-box ni criterio de decision.
**Diagnostico:** Investigacion sin limite = paralisis.
**Correccion:** Time-box a <=3 dias con pregunta binaria de decision clara.

### Pattern 5: "Dependencias Circulares"

**Senal:** A depende de B, B depende de A.
**Diagnostico:** Falsa dependencia o scope mal cortado.
**Correccion:** Revisar si la dependencia es genuina o si se puede romper con un stub/mock.

---

## S9 Reglas Anti-Waterfall (Tabla Completa)

| # | Regla | Verificacion | Si viola |
|---|-------|-------------|----------|
| AW-1 | Cada batch DEBE tener >=1 story con Value >=3 | Revisar Value scores por batch | Flag + reordenar |
| AW-2 | Stories con Learning 5 van en Batch 1-2 | Verificar posicion de learning stories | Mover antes |
| AW-3 | Spikes time-boxed <=3 dias con criterio de decision | Verificar que spike tiene timebox | Anadir timebox |
| AW-4 | Infraestructura necesita story usuario que justifique | Verificar que infra tiene story asociada | Flag + justificar |
| AW-5 | Spikes co-ubicados con las stories que informan | Spike en mismo batch que story dependiente | Co-ubicar |

---

## S10 Grafo de Dependencias — Formato y Reglas

### Formato de Visualizacion

```
STORY-A (PS: 4.2) --blocks--> STORY-C (PS: 3.5)
                               |
STORY-B (PS: 3.8) ------------+
                               |
                               v
                    STORY-D (PS: 3.1)

[INDEPENDIENTES]
STORY-E (PS: 2.8)
STORY-F (PS: 2.3)
```

### Reglas del Grafo

1. **Dependencias genuinas** = la story B necesita un artefacto tecnico que produce la story A
2. **Falsas dependencias** = "primero hay que hacer la base" (waterfall disfrazado)
3. **Test de la dependencia:** "Puede B entregar valor parcial sin que A este completa?" Si si -> no es dependencia real
4. **Dependencias circulares** = smell de scope mal cortado -> revisar splitting

---

## S11 Template de Scoring por Story

```markdown
### Story: [Titulo]
| Lente | Score | Peso | Ponderado | Justificacion |
|-------|-------|------|-----------|---------------|
| Value | X/5 | 30% | X.XX | [Razon con evidencia] |
| Learning | X/5 | 25% | X.XX | [Razon con evidencia] |
| Dependencies | X/5 | 20% | X.XX | [Razon con evidencia] |
| Risk of Delay | X/5 | 15% | X.XX | [Razon con evidencia] |
| Inv. Complexity | X/5 | 10% | X.XX | [Razon con evidencia] |
| **Priority Score** | | | **X.XX** | |
```

---

## S12 Template de Reporte de Priorizacion

```markdown
# Priorizacion de Stories: [Nombre PRD]

**Fuente:** [PRD nombre]
**Stories evaluadas:** [N]
**Batches propuestos:** [N]
**Fecha:** [YYYY-MM-DD]

---

## Ranking General

| # | Story | PS | V | L | D | R | C | Batch |
|---|-------|----|---|---|---|---|---|-------|
| 1 | [Titulo] | X.XX | X | X | X | X | X | 1 |
| ... |

---

## Grafo de Dependencias

[Visualizacion]

---

## Batches de Entrega

### Batch 1: [Nombre descriptivo]
**Valor entregado:** [Que puede hacer el usuario tras este batch]
**Stories:**
- Story X (PS: X.XX) -- [1 linea de justificacion]
- Story Y (PS: X.XX) -- [1 linea de justificacion]

**Duracion estimada:** [N dias]
**Desbloquea:** [Que habilita para Batch 2]

### Batch 2: [Nombre descriptivo]
[Mismo formato]

---

## Alertas Anti-Waterfall

[Si hay violaciones detectadas]

| Regla | Violacion | Correccion aplicada |
|-------|-----------|---------------------|
| AW-X | [Descripcion] | [Que se cambio] |

---

## Siguiente Paso

Llevar Batch 1 a Jira como Sprint 1.
```
