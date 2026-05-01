# Template de User Story JTBD (formato compacto)

> Cada dato aparece UNA vez. Frases cortas. Datos > adjetivos. Ver shared-config.md §Estilo de Escritura.

---

## User Story

**Cuando** [situación que dispara necesidad],
**quiero** [capacidad/resultado — NO solución],
**para** [beneficio medible].

**Usuario:** [Quién: rol, experiencia, frecuencia uso, relación con producto. Qué le impide conseguirlo hoy. 2-3 frases máx.]
**Motivación:** F: [tarea práctica]. E: [cómo quiere sentirse]. S: [cómo quiere ser percibido]. _(omitir E/S si no genuinas)_
**Ansiedad:** [Si aplica — preocupaciones del cambio]

---

## Evidencia

- **Cuanti:** [dato1]. [dato2]. Fuente: [sistema].
- **Cuali:** "[quote real]". [observación]. Fuente: [entrevista/research].

---

## Comportamiento

| AHORA | NUEVO |
|-------|-------|
| [qué hace hoy] | START: [qué empezará] |
| | STOP: [qué dejará] |
| | DIFFERENT: [qué cambiará] |

---

## Métricas (ÚNICO lugar para KPIs + analytics)

> SOLO métricas explícitas del usuario/fuente. NUNCA inventar valores.

| Nivel | KPI | Valor |
|-------|-----|-------|
| Mínimo | [métrica explícita o ⚠️ Pendiente] | [valor explícito o —] |
| Target | [métrica explícita o ⚠️ Pendiente] | [valor explícito o —] |
| Over | [métrica explícita o ⚠️ Pendiente] | [valor explícito o —] |

💡 **Recomendación:** [si no hay métricas, sugerir qué medir y con quién definirlo]

**Analytics:** [evento] con props [prop1, prop2]. Guardrail: [métrica ≥ valor].
**Go-to-market:** [Plan de activación: feature flag, comunicación, coordinación. 1-2 frases.]

---

## Criterios de Aceptación

Given [precondición]
When [acción]
Then [resultado]

Given [caso edge]
When [situación]
Then [resultado]

---

## Scoring (6D)

| Dim | Score | Justificación (5-10 palabras) |
|-----|-------|-------------------------------|
| 1. JTBD | X/10 | [breve] |
| 2. User | X/10 | [breve] |
| 3. Behavior | X/10 | [breve] |
| 4. Control | X/10 | [breve] |
| 5. Time | X/10 | [breve] |
| 6. Experiment | X/10 | [breve] |

**Global: X.X/10**
