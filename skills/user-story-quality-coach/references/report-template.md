# Template de Reporte

## Estructura del reporte

```markdown
# Análisis Calidad User Stories - {Equipo} {Sprint/Backlog}
**Fecha:** YYYY-MM-DD
**Equipo:** {Nombre equipo}
**Proyecto Jira:** {KEY}
**Stories analizadas:** N

---

## 📊 RESUMEN EJECUTIVO

### Score Global: X.X/10 [🔴/🟡/🟢/⭐]

| Categoría | Stories | % |
|-----------|---------|---|
| 🔴 Deficientes (0-4) | X | Y% |
| 🟡 Necesita Mejora (5-6) | X | Y% |
| 🟢 Aceptables (7-8) | X | Y% |
| ⭐ Excelentes (9-10) | X | Y% |

### Scores por Dimensión

| Dimensión | Score | Estado |
|-----------|-------|--------|
| 1. JTBD & Problem Context | X.X/10 | 🔴/🟡/🟢 |
| 2. User Specificity | X.X/10 | 🔴/🟡/🟢 |
| 3. Behavior Change | X.X/10 | 🔴/🟡/🟢 |
| 4. Zone of Control | X.X/10 | 🔴/🟡/🟢 |
| 5. Time Constraints | X.X/10 | 🔴/🟡/🟢 |
| 6. Survivable Experiment | X.X/10 | 🔴/🟡/🟢 |

### Antipatrones Detectados

| Antipatrón | Ocurrencias | % Stories |
|------------|-------------|-----------|
| "As a user..." | X | Y% |
| No Behavior Change | X | Y% |
| Fake Story | X | Y% |
| Solution as Need | X | Y% |
| Deliverable Outside Control | X | Y% |
| Everything is Urgent | X | Y% |
| Division by Technical Layers | X | Y% |

---

## 🏆 TOP 3 MEJORES STORIES

### 1. {STORY-KEY}: {Título}
**Score: X.X/10**

| Dimensión | Score | Comentario |
|-----------|-------|------------|
| ... | ... | ... |

**Por qué destaca:**
- [Qué la hace ejemplar]

---

## 🚨 TOP 3 REQUIEREN ATENCIÓN

### 1. {STORY-KEY}: {Título}
**Score: X.X/10**

| Dimensión | Score | Problema |
|-----------|-------|----------|
| ... | ... | ... |

**Antipatrones:** [Lista]

**Versión mejorada (JTBD):**
```
Cuando [situación específica],
quiero [capacidad/outcome],
para [beneficio medible].

Evidencia cuantitativa:
- [Dato 1]
- [Dato 2]

Evidencia cualitativa:
- "[Quote usuario]"

Comportamiento esperado:
- START: [qué empezarán]
- STOP: [qué dejarán]
- DIFFERENT: [qué cambiarán] [X% mejora]

Rango: Min X% / Target Y% / Over Z%
```

---

## 📋 ANÁLISIS DETALLADO POR STORY

### {STORY-KEY}: {Título}

**Score Global: X.X/10** [🔴/🟡/🟢/⭐]

| Dimensión | Score | Justificación |
|-----------|-------|---------------|
| 1. JTBD & Problem Context | X/10 | [Breve justificación] |
| 2. User Specificity | X/10 | [Breve justificación] |
| 3. Behavior Change | X/10 | [Breve justificación] |
| 4. Zone of Control | X/10 | [Breve justificación] |
| 5. Time Constraints | X/10 | [Breve justificación] |
| 6. Survivable Experiment | X/10 | [Breve justificación] |

**Antipatrones detectados:** [Lista o "Ninguno"]

**Completitud operativa:**
| Sección | Estado |
|---------|--------|
| Diseño (Protos/Pantallas) | ✅/⚠️/❌/➖ [detalle] |
| Traducciones | ✅/⚠️/❌/➖ [detalle] |
| Métricas/Analytics | ✅/⚠️/❌/➖ [detalle] |
| Go-to-market | ✅/⚠️/❌/➖ [detalle] |

**Recomendación:** [Acción específica]

---

## 🎯 RECOMENDACIONES PRIORITARIAS

### 🚨 Críticas (Hacer HOY)
1. [Acción específica con story afectada]
2. [Acción específica]

### 🟡 Importantes (Esta semana)
1. [Acción específica]
2. [Acción específica]

### ⚪ Mejora Continua (Este mes)
1. [Acción específica]
2. [Acción específica]

---

## ✅ DEFINITION OF READY ACTUALIZADA

Basada en los hallazgos, una story está Ready cuando:

- [ ] Usuario específico identificado (responde ≥3/4 preguntas Wendel)
- [ ] Problema documentado con evidencia (cuanti O cuali mínimo)
- [ ] Behavior change definido (START/STOP/DIFFERENT)
- [ ] Métrica de éxito cuantificada con rango min/target
- [ ] Dependencias identificadas y en control del equipo
- [ ] Tamaño ≤2 sprints (experimento supervivable)
- [ ] Sin antipatrones críticos (Fake Story, As a user)
- [ ] Diseño: Protos/pantallas Figma linkados por plataforma (si tiene UI)
- [ ] Traducciones: Definidas o marcadas N/A (si tiene textos visibles)
- [ ] Métricas: Eventos + propiedades + medición de éxito definidos
- [ ] Go-to-market: Plan de activación claro

---

## 🎬 PRÓXIMOS PASOS

| Acción | Responsable | Fecha |
|--------|-------------|-------|
| [Acción 1] | [Quién] | [Cuándo] |
| [Acción 2] | [Quién] | [Cuándo] |
```

## Template para Story Individual Reescrita (JTBD)

> Usar formato compacto de shared-config.md §Template JTBD Unificado. NO repetir métricas.

```markdown
**Cuando** [situación],
**quiero** [capacidad/resultado],
**para** [beneficio medible].

**Usuario:** [Rol, experiencia, impedimento actual. 2-3 frases.]
**Evidencia:** Cuanti: [dato]. Cuali: "[quote]".
**Comportamiento:** AHORA: [actual]. START: [nuevo]. STOP: [dejar]. DIFFERENT: [cambiar].
**Métricas:** Min: [valor explícito o ⚠️ Pendiente]. Target: [ídem]. Over: [ídem]. _(NUNCA inventar valores)_

```
