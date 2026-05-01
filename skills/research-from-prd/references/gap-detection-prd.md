# Detección de Gaps en PRDs

Sistema para identificar lagunas en un PRD que impiden diseñar research efectivo
y generar JTBDs de máxima calidad.

> Adaptado a la estructura EAC/EFC/Discovery del PRD.

---

## Filosofía

> "Un research solo puede ser tan bueno como la comprensión del problema que lo origina"

### Objetivo
Detectar gaps **ANTES** de diseñar research para:
1. Identificar qué información falta en el PRD
2. Generar preguntas para el PM o stakeholders
3. Distinguir qué gaps resolver con stakeholders vs con research
4. Determinar el modo de research: Descubrir vs Validar

---

## Taxonomía de Gaps

### 🔴 Gaps Críticos (Bloqueantes)
Impiden diseñar research válido. Requieren respuesta obligatoria del PM.

### 🟠 Gaps Mayores (Alta Prioridad)
Permiten diseñar research pero con menor foco. Afectan múltiples dimensiones.

### 🟡 Gaps Menores (Media Prioridad)
Research diseñable con buen foco. Afectan una dimensión específica.

### ⚪ Gaps de Refinamiento (Baja Prioridad)
Research diseñable con excelente foco. Mejoran calidad de stories de 8 a 9-10.

---

## Gaps de EAC (Estado Actual Conocido)

### GAP-PRD-01: Problema Indefinido o Vago
| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🔴 Crítico |
| **Indicador** | Sección "Problema" vacía, genérica o con frases tipo AP-PRD-1 |
| **Síntomas** | "Necesitamos mejorar...", "El proceso no es eficiente", sin datos concretos |
| **Impacto** | Dim 1 (JTBD) ≤3, no hay contexto para diseñar research |
| **Dimensiones afectadas** | 1, 4, 5 |
| **Resolver con** | PM (BLOQUEA research) |

**Preguntas para PM:**
1. ¿Cuál es el problema específico? ¿Para quién?
2. ¿Cuál es el impacto actual (cuantificado)?
3. ¿Desde cuándo existe este problema?
4. ¿Cómo se detectó? ¿Qué datos lo respaldan?

---

### GAP-PRD-02: Farolas Insuficientes
| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🟠 Mayor |
| **Indicador** | <3 Farolas o Farolas sin baseline |
| **Síntomas** | "Los tiempos son altos" sin número, métricas sin fuente |
| **Impacto** | Dim 1-2 (JTBD, Contexto) máx 5-6 |
| **Dimensiones afectadas** | 1, 2 |
| **Resolver con** | PM + datos existentes |

**Preguntas para PM:**
1. ¿Qué datos cuantitativos tenemos sobre este problema?
2. ¿De qué fuente vienen los datos? ¿Son recientes?
3. ¿Cuál es el baseline actual de las métricas principales?
4. ¿Hay tendencia (mejorando/empeorando)?

---

### GAP-PRD-03: Penumbras Ausentes o Genéricas
> Penumbras = evidencia cualitativa recogida (quotes, observaciones de campo, testimonios). NO son dudas ni incertidumbres.

| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🟠 Mayor |
| **Indicador** | <3 Penumbras o Penumbras sin fuente/cita directa |
| **Síntomas** | "Los usuarios se quejan" sin identificar quién, cuándo, dónde |
| **Impacto** | Dim 2-3 (Contexto, Actors) máx 5-6, research sin punto de partida cualitativo |
| **Dimensiones afectadas** | 2, 3 |
| **Resolver con** | PM + observaciones de campo |

**Preguntas para PM:**
1. ¿Has observado el problema de primera mano? ¿Dónde?
2. ¿Qué dicen los usuarios afectados? (citas directas)
3. ¿Hay feedback en canales de soporte/Slack/incidencias?
4. ¿Quién puede darnos acceso para observar el problema?

---

### GAP-PRD-04: Sin Contexto Temporal
| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🟡 Menor |
| **Indicador** | No explica por qué resolver esto AHORA |
| **Síntomas** | "Necesitamos esto" sin urgencia real justificada |
| **Impacto** | Dim 5 (Time Constraints) máx 6-7 |
| **Dimensiones afectadas** | 5 |
| **Resolver con** | PM |

**Preguntas para PM:**
1. ¿Por qué es importante ahora vs. Q3?
2. ¿Qué ha cambiado recientemente?
3. ¿Hay deadline externo o ventana de oportunidad?
4. ¿Cuál es el coste de esperar?

---

## Gaps de EFC (Estado Futuro Conocido)

### GAP-PRD-05: Métricas Sin Baseline→Target
| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🟠 Mayor |
| **Indicador** | Métricas sin formato baseline→target→plazo |
| **Síntomas** | "Mejorar tiempos", "Reducir errores" sin números concretos |
| **Impacto** | Dim 3 (Behavior Change) y Dim 6 (Survivable) máx 5-6 |
| **Dimensiones afectadas** | 3, 6 |
| **Resolver con** | PM (definir targets) |

**Preguntas para PM:**
1. ¿Cuál es el valor actual de cada métrica?
2. ¿Cuál es el target realista?
3. ¿En qué plazo esperamos alcanzarlo?
4. ¿Cómo mediremos el progreso?

---

### GAP-PRD-06: Hipótesis de Solución No Basada en EAC
| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🟡 Menor |
| **Indicador** | La solución propuesta no conecta con la evidencia del EAC |
| **Síntomas** | Solución que parece "idea del PM" sin justificación en datos |
| **Impacto** | Dim 4 (Zone of Control) máx 6-7, riesgo de solución incorrecta |
| **Dimensiones afectadas** | 4 |
| **Resolver con** | Research (validar si la solución ataca el problema real) |

**Preguntas para Research:**
1. ¿Los usuarios confirman el problema que la solución intenta resolver?
2. ¿Hay workarounds que contradicen la dirección propuesta?
3. ¿El struggle real coincide con la hipótesis del PRD?

---

## Gaps de Discovery + Scope

### GAP-PRD-07: Discovery Insuficiente o Ausente
| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🔴 Crítico |
| **Indicador** | Sección Discovery vacía o sin metodología documentada |
| **Síntomas** | "Hicimos research" sin detallar qué, con quién, qué hallaron |
| **Impacto** | D3 ≤4, FAIL automático en quality gate |
| **Dimensiones afectadas** | 1, 2, 3 |
| **Resolver con** | PM (documentar Discovery existente o realizar nuevo) |

**Preguntas para PM:**
1. ¿Qué investigación se realizó para validar el problema?
2. ¿Con cuántas personas se habló/observó?
3. ¿Cuáles fueron los hallazgos principales?
4. ¿Cómo informaron la solución propuesta?

---

### GAP-PRD-08: Scope Sin Exclusiones
| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🟡 Menor |
| **Indicador** | No hay sección de exclusiones o FAQs |
| **Síntomas** | Scope que solo dice qué incluye sin decir qué no |
| **Impacto** | D3 máx 6, riesgo de scope creep |
| **Dimensiones afectadas** | 4, 5 |
| **Resolver con** | PM |

**Preguntas para PM:**
1. ¿Qué NO está en scope? ¿Por qué?
2. ¿Hay funcionalidades que se posponen a una fase futura?
3. ¿Qué preguntas frecuentes anticipas del equipo?

---

## Matriz de Severidad y Dimensiones

```
GAP          Severidad  Dim1  Dim2  Dim3  Dim4  Dim5  Dim6  Resolver con
PRD-01       🔴        |||   -     -     |||   |||   -     PM (BLOQUEA)
PRD-02       🟠        |||   |||   -     -     -     -     PM + datos
PRD-03       🟠        -     |||   |||   -     -     -     PM + observación
PRD-04       🟡        -     -     -     -     |||   -     PM
PRD-05       🟠        -     -     |||   -     -     |||   PM (definir targets)
PRD-06       🟡        -     -     -     |||   -     -     Research (validar)
PRD-07       🔴        |||   |||   |||   -     -     -     PM (BLOQUEA si D3<5)
PRD-08       🟡        -     -     -     |||   |||   -     PM
```

---

## Gap Score

### Fórmula
```
Gap Score = (Críticos × 10) + (Mayores × 5) + (Menores × 2) + (Refinamiento × 1)
```

### Umbrales

| Gap Score | Nivel | Acción |
|---|---|---|
| ≤5 | Bajo | Diseñar research directamente |
| 6-15 | Medio | Resolver gaps críticos con PM antes de research |
| 16-30 | Alto | Sesión con PM + stakeholders obligatoria |
| >30 | Crítico | PRD no apto. Requiere completar Discovery |

---

## Regla de Enrutamiento: Gaps → PM vs Research

### Resolver con PM (ANTES del research)
- GAP-PRD-01 (Problema indefinido) → **BLOQUEA** todo
- GAP-PRD-02 (Farolas insuficientes) → Necesario para diseñar research
- GAP-PRD-03 (Penumbras ausentes) → Necesario para saber dónde observar
- GAP-PRD-05 (Métricas sin target) → Necesario para medir éxito
- GAP-PRD-07 (Discovery ausente) → BLOQUEA si D3 < 5
- GAP-PRD-08 (Sin exclusiones) → Nice-to-have pre-research

### Resolver con Research
- GAP-PRD-06 (Solución no basada en EAC) → Validar con usuarios reales
- GAP-PRD-04 (Sin contexto temporal) → Explorar urgencia en entrevistas

---

## Determinación del Modo de Research

### Modo Descubrir
Se activa cuando:
- GAP-PRD-01 presente (problema vago)
- GAP-PRD-07 presente (Discovery insuficiente)
- PRD no tiene JTBDs implícitos en la sección de funcionalidades
- Las Penumbras (feedback cualitativo recogido) aún no se han validado con usuarios finales

### Modo Validar
Se activa cuando:
- EAC completo con Farolas y Penumbras
- Discovery documentado con hallazgos
- Funcionalidades vinculadas a problemas
- Gaps son de profundidad, no de existencia

### Señales para cada modo

| Señal | Modo |
|---|---|
| EAC vago, sin Farolas | Descubrir |
| Discovery ausente | Descubrir |
| EAC completo + Discovery documentado | Validar |
| Funcionalidades sin vincular a problemas | Descubrir |
| Funcionalidades con justificación en Discovery | Validar |
| Penumbras sin validar por usuarios | Validar |
