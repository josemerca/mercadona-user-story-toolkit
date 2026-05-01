# Generación de User Stories desde PRD v1.3

**Compatible con:**
- `/user-story-quality-coach` - Scoring 6 dimensiones (0-10)
- `/user-story-builder` - Template JTBD Reforzado + 3 motivaciones

**Nuevo en v1.3:** Gap Detection integrado

---

## Template de Reporte de Gaps (Ejecutar Primero)

```markdown
# 🔍 ANÁLISIS DE GAPS - [NOMBRE PRD]

## Resumen Ejecutivo

| Tipo | Cantidad | Ejemplos |
|------|----------|----------|
| 🔴 Críticos | X | [Códigos] |
| 🟠 Mayores | X | [Códigos] |
| 🟡 Menores | X | [Códigos] |
| ⚪ Refinamiento | X | [Códigos] |

**Gap Score Total:** X/100
**Estado:** [Emoji] [Descripción]
**Recomendación:** [Acción sugerida]

---

## Gaps Detectados

### 🔴 Gaps Críticos (Bloqueantes)

#### [GAP-XX-YY] [Nombre del Gap]
- **Campo afectado:** [Sección del PRD]
- **Contenido actual:** "[Lo que dice o 'VACÍO']"
- **Problema:** [Por qué es un gap]
- **Dimensiones afectadas:** [1,2,3...]
- **Impacto en score:** Máximo alcanzable = X/10

---

### 🟠 Gaps Mayores

[Mismo formato]

---

### 🟡 Gaps Menores

[Mismo formato]

---

## 📋 Preguntas para Stakeholders

### Para Process Owner (PF)

| # | Gap | Pregunta |
|---|-----|----------|
| 1 | GAP-PF-XX | [Pregunta específica] |
| 2 | GAP-PF-XX | [Pregunta específica] |

### Para Product Manager (PM)

| # | Gap | Pregunta |
|---|-----|----------|
| 1 | GAP-PI-XX | [Pregunta específica] |
| 2 | GAP-PI-XX | [Pregunta específica] |

### Para Data/Analytics

| # | Gap | Pregunta |
|---|-----|----------|
| 1 | GAP-XX-XX | [Pregunta específica] |

### Para Product Designer

| # | Gap | Pregunta |
|---|-----|----------|
| 1 | GAP-XX-XX | [Pregunta específica] |

### Para Tech Lead

| # | Gap | Pregunta |
|---|-----|----------|
| 1 | GAP-XX-XX | [Pregunta específica] |

### Para Alineamiento (PF + PI juntos)

| # | Gap | Pregunta |
|---|-----|----------|
| 1 | GAP-AL-XX | [Pregunta específica] |

---

## 📊 Impacto en Scoring Esperado

Si NO se resuelven los gaps, el score máximo alcanzable será:

| Dimensión | Score Máx | Gap Limitante | Impacto |
|-----------|-----------|---------------|---------|
| 1. JTBD & Problem Context | X/10 | GAP-XX-YY | [Descripción] |
| 2. User Specificity | X/10 | GAP-XX-YY | [Descripción] |
| 3. Behavior Change | X/10 | GAP-XX-YY | [Descripción] |
| 4. Zone of Control | X/10 | GAP-XX-YY | [Descripción] |
| 5. Time Constraints | X/10 | GAP-XX-YY | [Descripción] |
| 6. Survivable Experiment | X/10 | GAP-XX-YY | [Descripción] |

**Score Global Máximo Alcanzable:** X/10 [Emoji]

---

## ✅ Checklist de Completitud PRD

### Fase 1 - Procesos (PF)
- [ ] Problema de Procesos definido específicamente
- [ ] Contexto organizacional documentado
- [ ] Líneas Rojas identificadas
- [ ] Farolas con datos cuantitativos
- [ ] Penumbras con evidencia cualitativa

### Fase 1 - Producto (PI)
- [ ] Job Performer específico (no genérico)
- [ ] Contexto Situacional con trigger claro
- [ ] Motivación es un JOB (no solución)
- [ ] Criterio de Éxito medible
- [ ] Limitaciones actuales documentadas
- [ ] Jobs Emocionales (dimensión E+S)

### Fase 2 - Priorización
- [ ] Hipótesis de Solución con comportamiento NUEVO
- [ ] KPIs con rangos min-target-over
- [ ] Alcance del Q justificado
- [ ] Riesgo/Impacto analizado

### Alineamiento PF-PI
- [ ] Problemas PF y PI conectados
- [ ] Matriz de alineamiento completada

---

## 🚦 Próximos Pasos

| Prioridad | Acción | Responsable | Deadline |
|-----------|--------|-------------|----------|
| 1 | [Acción para gap crítico] | [Rol] | [Fecha] |
| 2 | [Acción para gap mayor] | [Rol] | [Fecha] |
| 3 | Re-ejecutar análisis | Claude | [Tras respuestas] |
```

---

## Template Completo de User Story (Post-Gap Detection)

> **REGLA ANTI-VERBOSIDAD:** Seguir estrictamente shared-config.md §Estilo de Escritura. Cada dato aparece UNA vez. Frases cortas. Datos > adjetivos. Métricas solo en §Métricas.

```markdown
## [VERTICAL]-[NUM] - [Título en infinitivo]

> **Gaps:** [GAP-XX-YY → Dim X, GAP-XX-YY → Dim Y] | Score limitado a X/10 sin resolver

---

### User Story

**Cuando** [situación que dispara necesidad],
**quiero** [capacidad/resultado — NO solución],
**para** [beneficio medible].

**Usuario:** [Quién: rol, experiencia, frecuencia uso, relación con producto. Qué le impide conseguirlo hoy. 2-3 frases máx.]
**Motivación:** F: [tarea]. E: [sentimiento]. S: [percepción]. _(omitir E/S si no genuinas)_
**Ansiedad:** [Si aplica]

---

### Evidencia

- **Cuanti:** [dato1]. [dato2]. Fuente: [sistema]. ⚠️ GAP-PF-03 si vacío
- **Cuali:** "[quote]". [observación]. Fuente: [entrevista]. ⚠️ GAP-PF-04 si vacío

---

### Comportamiento

| AHORA | NUEVO |
|-------|-------|
| [qué hace hoy] | START: [qué empezará] |
| | STOP: [qué dejará] |
| | DIFFERENT: [qué cambiará] |

---

### Métricas

> SOLO métricas del PRD/PRD. Si no hay métricas en la fuente, usar placeholder ⚠️ y recomendar.

| Nivel | KPI | Valor |
|-------|-----|-------|
| Mínimo | [métrica explícita o ⚠️ Pendiente] | [valor explícito o —] |
| Target | [métrica explícita o ⚠️ Pendiente] | [valor explícito o —] |
| Over | [métrica explícita o ⚠️ Pendiente] | [valor explícito o —] |

💡 **Recomendación:** [si no hay métricas, sugerir qué medir y con quién definirlo]

**Analytics:** [evento] con props [prop1, prop2]. Medición éxito: [criterio].

---

### Criterios de Aceptación

Given [precondición]
When [acción]
Then [resultado]

Given [caso edge]
When [situación]
Then [resultado]

---

### Scoring (6D)

| Dim | Score | Justificación (5-10 palabras) | Gap |
|-----|-------|-------------------------------|-----|
| 1. JTBD | X/10 | [breve] | [GAP o ✅] |
| 2. User | X/10 | [breve] | [GAP o ✅] |
| 3. Behavior | X/10 | [breve] | [GAP o ✅] |
| 4. Control | X/10 | [breve] | [GAP o ✅] |
| 5. Time | X/10 | [breve] | [GAP o ✅] |
| 6. Experiment | X/10 | [breve] | [GAP o ✅] |

**Global: X.X/10** | Potencial sin gaps: X.X/10

---

### Gaps pendientes (si hay)

| Gap | Pregunta clave | Quién |
|-----|----------------|-------|
| GAP-XX-YY | [pregunta] | [rol] |

**Bloquea desarrollo:** [Sí/No — solo si gaps 🔴]
```

---

## Mapeo Detallado PRD → Template

### Campos de Fase 1 (Problema de Producto)

| Campo PRD | Sección Template | Gap si falta |
|------------|-----------------|--------------|
| Job Performer | User Story "Como" + Wendel | GAP-PI-01 |
| Contexto Situacional | User Story "Cuando" + Trigger | GAP-PI-02 |
| Motivación | User Story "quiero" + Job Principal | GAP-PI-03 |
| Criterio de Éxito | User Story "para" + Desired Outcome | GAP-PI-04 |
| Limitaciones actuales | Struggle + AHORA + Ansiedades | GAP-PI-05 |
| Jobs Emocionales | Motivación Emocional + Social | GAP-PI-06 |
| Penumbras | Evidencia Cualitativa | GAP-PF-04 |
| Farolas | Evidencia Cuantitativa | GAP-PF-03 |

### Campos de Fase 2 (Priorización)

| Campo PRD | Sección Template | Gap si falta |
|------------|-----------------|--------------|
| Hipótesis de Solución | NUEVO (START) | GAP-F2-01 |
| KPIs Esperados | Rangos min-target-over | GAP-F2-02 |
| Alcance del Q | Dim 5: Time Constraints | GAP-F2-03 |
| Boceto de Solución | Criterios de Aceptación | - |
| Riesgo/Impacto | Experimento + Dim 6 | GAP-F2-04 |

---

## Scoring Detallado (0-10) con Impacto de Gaps

### Dim 1: JTBD & Problem Context

| Score | Criterio | Gaps que limitan |
|-------|----------|------------------|
| 9-10 | Job Story perfecto + Penumbras (feedback cualitativo) Y Farolas (datos cuantitativos) | Ninguno |
| 7-8 | Job Story correcto + solo Penumbras O Farolas | GAP-PF-03 o GAP-PF-04 |
| 5-6 | Problema mencionado, evidencia débil | GAP-PF-03 + GAP-PF-04 |
| 0-4 | Sin contexto de problema | GAP-PF-01 |

### Dim 2: User Specificity

| Score | Criterio | Gaps que limitan |
|-------|----------|------------------|
| 9-10 | Job Performer específico + 4/4 Wendel | Ninguno |
| 7-8 | 3/4 Wendel, segmento claro | GAP-PI-02 |
| 5-6 | Usuario parcialmente definido | GAP-PI-01 parcial |
| 0-4 | Job Performer genérico o vacío | GAP-PI-01 |

### Dim 3: Behavior Change

| Score | Criterio | Gaps que limitan |
|-------|----------|------------------|
| 9-10 | AHORA→NUEVO claro + START/STOP/DIFFERENT + rangos | Ninguno |
| 7-8 | Cambio definido, falta algún rango | GAP-F2-02 parcial |
| 5-6 | Cambio mencionado sin cuantificar | GAP-F2-02 |
| 0-4 | Sin KPIs en Fase 2 del PRD | GAP-F2-01 + GAP-F2-02 |

### Dim 4: Zone of Control

| Score | Criterio | Gaps que limitan |
|-------|----------|------------------|
| 9-10 | Hipótesis 100% en control del equipo | Ninguno |
| 7-8 | Dependencias menores identificadas | GAP-PF-02 parcial |
| 5-6 | Dependencia externa significativa | GAP-PF-02 |
| 0-4 | Bloqueadores críticos en PRD | GAP-AL-01 |

### Dim 5: Time Constraints

| Score | Criterio | Gaps que limitan |
|-------|----------|------------------|
| 9-10 | Alcance Q con consecuencia real | Ninguno |
| 7-8 | Deadline justificado por negocio | GAP-F2-03 parcial |
| 5-6 | "Para este Q" sin justificación | GAP-F2-03 |
| 0-4 | Urgencia artificial o sin deadline | GAP-PF-01 |

### Dim 6: Survivable Experiment

| Score | Criterio | Gaps que limitan |
|-------|----------|------------------|
| 9-10 | ≤2 sprints + Riesgo documentado + rollback | Ninguno |
| 7-8 | Esfuerzo moderado, mitigación clara | GAP-F2-04 parcial |
| 5-6 | Sin plan de rollback | GAP-F2-04 |
| 0-4 | Alto riesgo sin mitigación | GAP-F2-04 + GAP-PF-02 |

---

## Antipatrones y Gaps Relacionados

| Si el PRD tiene... | Gap Detectado | El template tendrá... | Acción |
|---------------------|---------------|----------------------|--------|
| Job Performer vacío | GAP-PI-01 🔴 | Usuario genérico | Bloquear, preguntar |
| Sin Jobs Emocionales | GAP-PI-06 🟡 | Solo motivación F | Inferir o preguntar |
| Sin Farolas | GAP-PF-03 🟠 | Score Dim1 ≤7 | Preguntar Analytics |
| Sin KPIs Esperados | GAP-F2-02 🟠 | Score Dim3 ≤5 | Preguntar PF |
| Fase 1 = solución | GAP-PI-03 🔴 | Fake Story | Bloquear, reformular |
| Sin Líneas Rojas | GAP-PF-02 🟠 | Dim4, Dim6 limitadas | Preguntar PF |

---

## Checklist de Validación

Antes de entregar la story, verificar:

| Criterio | Fuente PRD | Gap si falla | ✓ |
|----------|-------------|--------------|---|
| Job Principal claro (no solución) | Motivación | GAP-PI-03 | ☐ |
| 3 motivaciones (F+E+S) | Motivación + Jobs Emocionales | GAP-PI-06 | ☐ |
| Wendel 4/4 respondido | Múltiples campos | GAP-PI-01, PI-02 | ☐ |
| AHORA → NUEVO definido | Limitaciones + Hipótesis | GAP-F2-01 | ☐ |
| Rangos min-target-over | KPIs Esperados | GAP-F2-02 | ☐ |
| Penumbras Y Farolas | Fase 1 | GAP-PF-03, PF-04 | ☐ |
| Score ≥7 en 6 dimensiones | Análisis | Varios | ☐ |

**Si hay gaps críticos (🔴), NO proceder con desarrollo.**
**Si hay gaps mayores (🟠), documentar y priorizar resolución.**
**Si hay gaps menores (🟡), generar con advertencia.**
