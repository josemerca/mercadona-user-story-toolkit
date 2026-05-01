# Detección de Gaps en Research

Sistema para evaluar si la evidencia de research es SUFICIENTE para producir
JTBDs de alta confianza antes de entregarlos a jtbd-to-stories.

---

## Filosofía

> "No entregues JTBDs con huecos. Es mejor decir 'nos falta esto' que inventar evidencia."

### Objetivo
Detectar gaps en la evidencia de research **DESPUÉS** de analizar observaciones y
entrevistas y **ANTES** de entregar JTBDs, para:
1. Evaluar si los criterios de éxito del Bloque 3 se cubrieron
2. Evaluar si cada JTBD tiene evidencia suficiente en las 3 dimensiones
3. Decidir si entregar o hacer más sesiones
4. Documentar limitaciones de los hallazgos

---

## Métrica Primaria: Cobertura de Criterios de Éxito

Los criterios de éxito definidos en el Bloque 3 son el METRO principal para evaluar
si el research fue suficiente. Son preguntas verificables con umbral de evidencia claro.

### Evaluación por criterio

Para cada criterio del Bloque 3:

| Aspecto | Evaluar |
|---------|---------|
| **¿Cubierto?** | ¿Tenemos evidencia que responde la pregunta del criterio? |
| **¿Alcanza el umbral?** | ¿La evidencia cumple el mínimo definido (N participantes, N workarounds, etc.)? |
| **¿De qué fuente?** | ¿Observación, entrevista, o ambos? (triangulación es más fuerte) |
| **¿Con qué calidad?** | ¿Quotes literales + comportamiento observado, o solo inferencias? |

### Umbrales de cobertura

| Cobertura de criterios | Nivel | Acción |
|------------------------|-------|--------|
| 100% cubiertos (todos ✅) | 🟢 Verde | Entregar JTBDs a jtbd-to-stories |
| 75%+ cubiertos (≥3 de 4 ✅) | 🟡 Amarillo | Entregar con advertencias de gaps |
| 50-74% cubiertos | 🟠 Naranja | Recomendar 2-3 sesiones adicionales focalizadas |
| <50% cubiertos | 🔴 Rojo | Bloquear entrega. Research insuficiente |

### Template de evaluación de criterios

```markdown
### Evaluación de Criterios de Éxito

| # | Criterio | Estado | Evidencia | Fuente | Umbral alcanzado |
|---|----------|--------|-----------|--------|------------------|
| 1 | [Pregunta] | ✅/🟡/❌ | [Resumen] | Obs+Ent / Solo Ent / Solo Obs | Sí / Parcial / No |
| 2 | [Pregunta] | ✅/🟡/❌ | [Resumen] | [Fuente] | Sí / Parcial / No |
| 3 | [Pregunta] | ✅/🟡/❌ | [Resumen] | [Fuente] | Sí / Parcial / No |

**Cobertura total:** [N]/[N] criterios cubiertos → [🟢/🟡/🟠/🔴]
```

---

## Métrica Secundaria: Research Gap Score por JTBD

Se mantiene como validación complementaria de cada JTBD individual.

### Taxonomía de Gaps de Research

#### 🔴 Gaps Críticos de Evidencia
Impiden entregar un JTBD válido. Requieren más sesiones obligatorias.

#### 🟠 Gaps Mayores de Evidencia
JTBD entregable pero con advertencia clara. Afectan confianza.

#### 🟡 Gaps Menores de Evidencia
JTBD entregable con nota. Un matiz que mejoraría la calidad.

#### ⚪ Gaps de Refinamiento
JTBD entregable tal cual. Mejoraría con evidencia adicional.

---

## Gaps de Cobertura de Componentes JTBD

### GAP-RES-01: Sin Job Performer Real
| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🔴 Crítico |
| **Indicador** | No se observó/entrevistó al usuario que realmente ejecuta el proceso |
| **Síntomas** | Se entrevistó a stakeholders/jefes en lugar de operadores; no hubo observación de campo |
| **Impacto** | JTBD basado en perspectiva indirecta, no en experiencia real |
| **Acción** | Observar y entrevistar al perfil correcto |

**Preguntas de diagnóstico:**
- ¿Quién de los participantes HACE el proceso vs quién lo SUPERVISA?
- ¿Los quotes son de experiencia directa o de observación de terceros?
- ¿Se observó al performer real en su entorno de trabajo?

---

### GAP-RES-02: Sin Trigger Concreto
| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🟠 Mayor |
| **Indicador** | No se descubrió QUÉ dispara el job |
| **Síntomas** | El JTBD dice "Cuando necesito..." pero sin situación concreta observada/narrada |
| **Impacto** | Stories sin contexto de cuándo/por qué surge la necesidad |
| **Acción** | Observar el momento de inicio + preguntar en próximas sesiones |

---

### GAP-RES-03: Sin Struggle con Evidencia de Comportamiento
| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🔴 Crítico |
| **Indicador** | El struggle es una inferencia, no un comportamiento observado o narrado |
| **Síntomas** | "Los usuarios se frustran con..." sin workarounds observados ni quotes |
| **Impacto** | No hay evidencia de que el problema sea real |
| **Acción** | Observar workarounds en campo + reentrevistar con preguntas de comportamiento pasado |

**Criterio de validación — el struggle es REAL si:**
- ≥2 participantes lo muestran/describen espontáneamente
- Workarounds activos observados (están invirtiendo esfuerzo)
- Ejemplos narrados con fechas y detalles
- Emoción visible al describirlo o realizarlo

---

### GAP-RES-04: Sin Desired Outcome Explícito
| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🟠 Mayor |
| **Indicador** | Sabemos el struggle pero no qué quieren lograr |
| **Síntomas** | "Les molesta X" pero sin "lo que quieren es Y" |
| **Impacto** | Stories sin "para poder" claro |
| **Acción** | Preguntar outcomes en próximas entrevistas; observar qué verifican al terminar |

---

### GAP-RES-05: Motivación Funcional sin Evidencia
| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🟡 Menor |
| **Indicador** | La motivación funcional es obvia pero no tiene quote ni observación |
| **Síntomas** | "Quiere completar el proceso rápido" — inferido, no dicho ni visto |
| **Impacto** | JTBD con motivación funcional débil |
| **Acción** | Buscar quotes de comportamiento o secuencias observadas que confirmen |

---

### GAP-RES-06: Motivación Emocional Ausente
| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🟠 Mayor |
| **Indicador** | No hay datos sobre cómo se SIENTE el usuario |
| **Síntomas** | JTBD puramente funcional, sin dimensión emocional |
| **Impacto** | Stories frías, sin empatía |
| **Acción** | Observar expresiones/reacciones emocionales + preguntar en próximas entrevistas |

---

### GAP-RES-07: Motivación Social Ausente
| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🟠 Mayor |
| **Indicador** | No hay datos sobre percepción social/profesional |
| **Síntomas** | No sabemos quién observa, juzga o depende del resultado |
| **Impacto** | Stories sin contexto de equipo/organización |
| **Acción** | Observar interacciones con otros + preguntar quién depende/observa |

---

### GAP-RES-08: Wendel Checklist Incompleto
| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🟡 Menor |
| **Indicador** | Faltan 1+ elementos del Wendel Checklist |
| **Elementos** | 1. Experiencia previa, 2. Relación con producto, 3. Motivación situacional, 4. Impedimento actual |
| **Impacto** | JTBD sin contexto completo para jtbd-to-stories |
| **Acción** | Completar en próximas sesiones o inferir con advertencia |

---

## Gaps de Calidad de Evidencia

### GAP-RES-09: Muestra Insuficiente
| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🟠 Mayor |
| **Indicador** | Menos de 3 sesiones para un JTBD |
| **Síntomas** | Solo 1-2 participantes muestran/mencionan el struggle |
| **Impacto** | Confianza baja — puede ser caso aislado |
| **Acción** | Más sesiones con perfil similar |

**Umbrales de confianza:**
| N participantes | Confianza |
|---|---|
| 1 de N | 🔴 Baja — posible caso aislado |
| 2 de N | 🟡 Media — podría ser patrón |
| 3+ de N | 🟢 Alta — patrón confirmado |

---

### GAP-RES-10: Sin Quotes Literales
| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🟡 Menor |
| **Indicador** | Los hallazgos son paráfrasis, no palabras exactas |
| **Síntomas** | "Los usuarios dicen que es complicado" sin quote textual |
| **Impacto** | Evidencia más débil, pierde matiz emocional |
| **Acción** | Revisar notas o grabar próximas sesiones |

---

### GAP-RES-11: Sesgo de Confirmación
| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🔴 Crítico |
| **Indicador** | Los hallazgos coinciden EXACTAMENTE con las hipótesis del PRD |
| **Síntomas** | Todas las Penumbras "confirmadas", todos los struggles "validados", 0 hallazgos nuevos |
| **Impacto** | Posible leading en preguntas o sesgo en observación — datos no fiables |
| **Acción** | Revisar guión de entrevistas + protocolo de observación + considerar re-sesiones |

**Señales de alerta:**
- 100% de coincidencia PRD ↔ Research → Sospechoso
- Solo se "confirman" hipótesis, no se descubre nada nuevo → Sospechoso
- No hay quotes de desacuerdo ni comportamientos inesperados → Sospechoso
- Lo observado y lo dicho coincide al 100% → Revisar si la observación fue realmente "silenciosa"

---

### GAP-RES-12: Sin Hallazgos Nuevos
| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🟡 Menor |
| **Indicador** | No se descubrió NADA que no estuviera ya en el PRD |
| **Síntomas** | Research solo confirma, no amplía |
| **Impacto** | Puede indicar leading, scope cerrado, o sesgo de observación |
| **Acción** | Revisar si el guión y el protocolo de observación eran suficientemente abiertos |

---

### GAP-RES-13: Farolas No Evaluadas
| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🟡 Menor |
| **Indicador** | Hay Farolas del PF sin contraste ni en observación ni en entrevista |
| **Impacto** | No sabemos si las métricas del PF son correctas |
| **Acción** | Incluir área en próximas sesiones |

---

### GAP-RES-14: Penumbras No Validadas
> Penumbras = feedback cualitativo recogido en campo (quotes, observaciones). Este gap indica que ese feedback aún no se ha contrastado con usuarios finales.

| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🟡 Menor |
| **Indicador** | Hay Penumbras (feedback cualitativo) sin confirmar ni desmentir con usuarios |
| **Impacto** | Se pasa a stories con evidencia cualitativa no contrastada |
| **Acción** | Incluir área en próximas sesiones |

---

### GAP-RES-15: Sin Triangulación Observación-Entrevista
| Aspecto | Detalle |
|---------|---------|
| **Severidad** | 🟡 Menor |
| **Indicador** | Solo hay datos de un método (solo observación O solo entrevista) |
| **Síntomas** | No hay contraste entre lo que dicen y lo que hacen |
| **Impacto** | Evidencia unidimensional — puede haber discrepancias no detectadas |
| **Acción** | Completar con el método faltante si es posible |

---

## Matriz de Severidad

```
GAP         Severidad  Componente/Calidad        Acción
RES-01      🔴        Job Performer              Observar + entrevistar perfil correcto
RES-02      🟠        Trigger                    Observar inicio + preguntas de trigger
RES-03      🔴        Struggle                   Observar workarounds + buscar comportamientos reales
RES-04      🟠        Desired Outcome            Observar verificación final + preguntas de outcome
RES-05      🟡        Motivación Funcional       Buscar quotes/comportamientos confirmatorios
RES-06      🟠        Motivación Emocional       Observar reacciones + preguntas emocionales
RES-07      🟠        Motivación Social          Observar interacciones + preguntas sociales
RES-08      🟡        Wendel Checklist           Completar datos
RES-09      🟠        Muestra                    Más sesiones
RES-10      🟡        Quotes                     Revisar notas / grabar
RES-11      🔴        Calidad datos              Revisar protocolo + re-sesiones
RES-12      🟡        Cobertura                  Revisar apertura del protocolo
RES-13      🟡        Validación Farolas         Incluir en próximas sesiones
RES-14      🟡        Validación Penumbras       Incluir en próximas sesiones
RES-15      🟡        Triangulación              Completar con método faltante
```

---

## Research Gap Score

### Fórmula
```
Research Gap Score = (Críticos × 10) + (Mayores × 5) + (Menores × 2) + (Refinamiento × 1)
```

Se calcula POR JTBD y TOTAL.

### Umbrales de decisión

| Score | Nivel | Acción |
|---|---|---|
| ≤3 | 🟢 Verde | Entregar JTBDs |
| 4-8 | 🟡 Amarillo | Entregar con advertencias |
| 9-15 | 🟠 Naranja | Recomendar 2-3 sesiones adicionales |
| >15 | 🔴 Rojo | Bloquear entrega |

---

## Proceso Completo de Evaluación

### Paso 1: Evaluar criterios de éxito (métrica primaria)

Para cada criterio del Bloque 3:
- ¿Cubierto? (✅/🟡/❌)
- ¿Umbral alcanzado?
- ¿Con qué fuente? (triangulación es más fuerte)

### Paso 2: Evaluar cada JTBD candidato (métrica secundaria)

Para cada JTBD descubierto o validado:

| Componente | ¿Presente? | ¿Con evidencia? | ¿Observación + Entrevista? | ¿Cuántos? | Gap |
|---|---|---|---|---|---|
| Job Performer | Sí/No | Quote / Observado / Inferido | Obs / Ent / Ambos | N/M | RES-01? |
| Trigger | Sí/No | Ejemplo / Observado / Genérico | Obs / Ent / Ambos | N/M | RES-02? |
| Struggle | Sí/No | Workaround / Comportamiento / Opinión | Obs / Ent / Ambos | N/M | RES-03? |
| Desired Outcome | Sí/No | En sus palabras / Observado / Inferido | Obs / Ent / Ambos | N/M | RES-04? |
| Mot. Funcional | Sí/No | Quote / Comportamiento / Inferido | Obs / Ent / Ambos | N/M | RES-05? |
| Mot. Emocional | Sí/No | Quote / Expresión / Ausente | Obs / Ent / Ambos | N/M | RES-06? |
| Mot. Social | Sí/No | Interacción / Quote / Ausente | Obs / Ent / Ambos | N/M | RES-07? |

### Paso 3: Evaluar las 3 dimensiones motivacionales

Cada JTBD debe tener las 3 dimensiones con evidencia:

| Dimensión | Tiene evidencia | Tipo de evidencia | Fuente |
|-----------|-----------------|-------------------|--------|
| Funcional | ✅/❌ | [Comportamiento / Quote / Inferido] | [Obs / Ent / Ambos] |
| Emocional | ✅/❌ | [Expresión / Quote / Inferido] | [Obs / Ent / Ambos] |
| Social | ✅/❌ | [Interacción / Quote / Inferido] | [Obs / Ent / Ambos] |

Si alguna dimensión está "Inferida" en todos los JTBDs → research adicional focalizado.

### Paso 4: Evaluar calidad transversal

| Criterio | Estado | Gap |
|---|---|---|
| Wendel Checklist (4 elementos) | Completo / Parcial / Vacío | RES-08? |
| Muestra (≥3 participantes) | Sí / No | RES-09? |
| Quotes literales | Sí / Solo paráfrasis | RES-10? |
| Sesgo de confirmación | No detectado / Sospechoso | RES-11? |
| Hallazgos nuevos (no en PRD) | Sí / No | RES-12? |
| Farolas del PF evaluadas | Todas / Parcial / Ninguna | RES-13? |
| Penumbras del PF validadas | Todas / Parcial / Ninguna | RES-14? |
| Triangulación obs-entrevista | Sí / Parcial / No | RES-15? |

### Paso 5: Decisión combinada

```
┌─────────────────────────────────────────────────────┐
│ DECISIÓN FINAL = Criterios (primario) + Score (sec.) │
├─────────────────────────────────────────────────────┤
│                                                       │
│  Criterios ✅ + Score 🟢 → Entregar JTBDs             │
│  Criterios ✅ + Score 🟡 → Entregar con advertencias  │
│  Criterios 🟡 + Score 🟡 → Entregar con advertencias  │
│  Criterios 🟡 + Score 🟠 → Recomendar más sesiones    │
│  Criterios ❌ + cualquier → Bloquear hasta cubrir      │
│                                                       │
└─────────────────────────────────────────────────────┘
```

---

## Template: Research Quality Report

```markdown
## Research Quality Report: PRD [Nombre]

### Evaluación Primaria: Criterios de Éxito
| # | Criterio | Estado | Evidencia | Fuente | Umbral |
|---|----------|--------|-----------|--------|--------|
| 1 | [Pregunta] | ✅/🟡/❌ | [Resumen] | [Obs/Ent/Ambos] | [Sí/No] |
| 2 | ... | ... | ... | ... | ... |

**Cobertura:** [N]/[N] → [🟢/🟡/🟠/🔴]

### Evaluación Secundaria: Research Gap Score
- **Score Total:** [N] ([🟢/🟡/🟠/🔴])
- **JTBDs con evidencia completa:** [N]
- **JTBDs con gaps:** [N]

### Detalle por JTBD

#### JTBD 1: [Título]
| Componente | Estado | Evidencia | Fuente | Participantes | Gap |
|---|---|---|---|---|---|
| Job Performer | ✅ | Observado + Quote | Ambos | 5/8 | — |
| Trigger | ✅ | Ejemplo específico | Ent | 4/8 | — |
| Struggle | ✅ | Workaround observado + quote | Ambos | 6/8 | — |
| Desired Outcome | ✅ | En sus palabras | Ent | 3/8 | — |
| Mot. Funcional | ✅ | Comportamiento | Obs | 5/8 | — |
| Mot. Emocional | ✅ | Quote con emoción | Ent | 3/8 | — |
| Mot. Social | 🟡 | Inferido | — | 1/8 | RES-07 |
**Score JTBD 1:** 5 (🟡 — motivación social débil)

### Validación cruzada PRD
| Elemento | Estado | Evidencia |
|---|---|---|
| Farola: "[métrica]" | ✅/❌/🟡 | "[dato real]" |
| Penumbra: "[quote]" | ✅/❌/🟡 | "[quote real]" |

### Gaps pendientes
| Gap | JTBD | Severidad | Acción |
|---|---|---|---|
| [GAP-RES-XX] | JTBD [N] | [emoji] | [Acción concreta] |

### Decisión final
**Criterios:** [N]/[N] cubiertos → [nivel]
**Score:** [N] → [nivel]
**Decisión:** [Entregar / Entregar con advertencias / Más sesiones / Bloquear]
[Justificación]
```

---

## Señales de Buen Research vs Mal Research

### Research de Alta Calidad
- Todos los criterios de éxito cubiertos (✅)
- Todos los JTBDs con Research Gap Score ≤3
- Hay triangulación observación-entrevista
- Hay hallazgos nuevos no presentes en el PRD
- Hay alguna Penumbra no confirmada (indica observación/preguntas abiertas)
- Los quotes capturan emoción real
- Los struggles tienen workarounds observados
- ≥3 participantes por JTBD principal
- Observaciones y aprendizajes claramente separados

### Research de Baja Calidad
- Criterios de éxito parcialmente cubiertos
- JTBDs con score >8
- Sin observación de campo (solo entrevistas)
- Todo coincide exactamente con el PRD (sesgo)
- Solo paráfrasis, no quotes literales
- Motivaciones emocionales y sociales ausentes
- Menos de 3 sesiones totales
- No hay hallazgos nuevos
- Observaciones y aprendizajes mezclados
