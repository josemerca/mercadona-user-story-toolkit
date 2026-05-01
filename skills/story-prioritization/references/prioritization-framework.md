# Framework de Priorización — Story Prioritization

## Rúbrica Completa por Lente

### Lente 1: Value (30%)

**Principio:** El valor se mide por impacto en el usuario Y en el negocio. Una story que solo beneficia al equipo técnico sin impacto usuario tiene Value bajo.

#### Rúbrica detallada

| Score | Criterio | Señales positivas | Señales negativas |
|-------|----------|-------------------|-------------------|
| **5** | Impacto crítico en métrica de negocio + usuario directo | Resuelve struggle principal del JTBD. Dim 1 ≥8. Farola/EAC con impacto cuantificado. | — |
| **4** | Impacto alto en negocio o usuario | Resuelve struggle secundario. Dim 1 ≥6. Mejora KPI significativamente. | Impacto solo en una dimensión (negocio OR usuario, no ambos). |
| **3** | Impacto moderado | Mejora experiencia usuario incremental. KPI secundario. | Sin conexión directa con struggle del JTBD. |
| **2** | Impacto bajo o indirecto | Habilita mejoras futuras. Deuda técnica que afecta performance usuario. | "El usuario no nota la diferencia ahora pero eventualmente..." |
| **1** | Sin impacto directo en usuario | Refactoring interno. Infraestructura sin story asociada. | "Es necesario para nosotros" (fake story). |

#### Ejemplos

| Story | Value | Razón |
|-------|-------|-------|
| "Cuando el operario empieza turno, ver tareas ordenadas por urgencia" | 5 | Struggle principal: no saber por dónde empezar. KPI: tiempo primera tarea. |
| "Cuando el coordinador detecta cuello de botella, reasignar carga" | 4 | Struggle real pero secundario. No todos los turnos tienen cuellos de botella. |
| "Migrar API de pedidos a v2" | 2 | Habilita mejoras futuras pero el usuario no nota cambio. |
| "Actualizar dependencias de seguridad" | 1 | Necesario pero sin impacto usuario directo. |

---

### Lente 2: Learning (25%)

**Principio:** Stories que reducen incertidumbre temprano ahorran retrabajo. El "aprendizaje" no es opcional — es inversión en tomar mejores decisiones.

#### Rúbrica detallada

| Score | Criterio | Señales positivas | Señales negativas |
|-------|----------|-------------------|-------------------|
| **5** | Reduce incertidumbre crítica | Valida hipótesis central del producto. Sin esta, todo lo demás es apuesta. Dim 6 ≤5. | — |
| **4** | Reduce incertidumbre alta | Valida JTBD con baja evidencia. Prueba integración no probada. | Algo de evidencia existe pero insuficiente. |
| **3** | Reduce incertidumbre moderada | Prueba UX con usuarios reales. Valida performance bajo carga. | Evidencia parcial disponible. |
| **2** | Reduce incertidumbre baja | Implementa variación de algo conocido. | La mayoría del riesgo ya está mitigado. |
| **1** | No reduce incertidumbre | Implementa patrón conocido y probado en este contexto. | Zero unknowns. |

#### Regla de posición

```
Learning 5 → DEBE ir en Batch 1 o 2 (antes de invertir en stories que dependen de este aprendizaje)
Learning 4 → DEBERÍA ir en Batch 1 o 2
Learning 1-3 → Sin restricción de posición
```

#### Spikes (Learning 5 + Inv. Complexity ≤2)

Cuando una story tiene Learning 5 pero Complexity baja, es candidata a **spike**:

| Spike | Criterio |
|-------|----------|
| Time-box | ≤3 días (sin excepción) |
| Pregunta de decisión | Binaria: "¿funciona o no?" / "¿es viable o no?" |
| Output | Decisión + evidencia, NO código production-ready |
| Posición | Co-ubicado en el batch con las stories que informa |

---

### Lente 3: Dependencies (20%)

**Principio:** Stories que desbloquean a otras son más valiosas que stories independientes, pero solo si la dependencia es GENUINA (técnica), no artificial (organizativa/waterfall).

#### Rúbrica detallada

| Score | Criterio | Cómo verificar |
|-------|----------|----------------|
| **5** | Desbloquea ≥4 stories | Nodo central del grafo. Sin ella, el pipeline se para. |
| **4** | Desbloquea 2-3 stories | Nodo importante. Varias stories esperan un artefacto que esta produce. |
| **3** | Desbloquea 1 story | Dependencia directa con otra story específica. |
| **2** | Tiene dependencia pero no desbloquea | Depende de otra story para empezar pero nadie depende de ella. |
| **1** | Sin dependencias | Completamente independiente. Puede ir en cualquier batch. |

#### Test de Dependencia Genuina

Para cada dependencia declarada, aplicar:

```
¿La story B necesita un ARTEFACTO TÉCNICO específico que produce la story A?
├── SÍ → ¿Puede B entregar valor parcial sin A completa?
│        ├── NO → ✅ Dependencia genuina
│        └── SÍ → 🟡 Dependencia parcial (B puede empezar, stub/mock)
└── NO → ❌ Falsa dependencia (waterfall disfrazado)
```

#### Falsas dependencias comunes

| Parece dependencia | Pero NO lo es | Por qué |
|--------------------|---------------|---------|
| "Primero la BD, luego el API" | Se puede usar BD in-memory o mock | La story del API puede entregar valor con datos fake |
| "Primero el diseño, luego el frontend" | Se puede implementar con diseño parcial/básico | El valor está en la funcionalidad, no en el pixel-perfect |
| "Primero la autenticación, luego todo" | Se puede usar auth hardcoded en dev | No todo necesita auth real en fase de validación |

---

### Lente 4: Risk of Delay (15%)

**Principio:** Urgencia real (deadline externo, regulación, ventana de mercado) vs urgencia artificial (presión interna, "es importante").

#### Rúbrica detallada

| Score | Criterio | Evidencia necesaria |
|-------|----------|---------------------|
| **5** | Coste crítico de retraso | Deadline regulatorio. Compromiso contractual. Pérdida medible por día de retraso. |
| **4** | Coste alto | Bloquea a otro equipo con deadline. Ventana de oportunidad limitada. |
| **3** | Coste moderado | Ineficiencia acumulada (cuantificable). Problema empeora gradualmente. |
| **2** | Coste bajo | Puede esperar 1-2 sprints sin consecuencia real. |
| **1** | Sin coste | Nice-to-have. Mejora continua sin presión temporal. |

#### Señales de urgencia artificial (NO puntuar alto)

- "Es urgente porque el stakeholder lo dice" → ¿Hay evidencia de coste de retraso?
- "Lo necesitamos para ayer" → ¿Qué pasa concretamente si tarda 2 semanas más?
- "Es prioridad 1 del Q" → ¿Por qué? ¿Qué objetivo Q1 bloquea?

---

### Lente 5: Inverse Complexity (10%)

**Principio:** A igualdad de valor, lo más simple va primero. Pero complejidad alta + incertidumbre alta = spike, no story completa.

#### Rúbrica detallada

| Score | Complejidad | Días estimados | Señales |
|-------|-------------|----------------|---------|
| **5** | Muy simple | 1-2 | Cambio acotado, patrón conocido, 1 componente. |
| **4** | Simple | 2-3 | Predecible, 1-2 componentes, bajo riesgo. |
| **3** | Moderada | 3-5 | Requiere diseño, 2-3 componentes, algunos unknowns. |
| **2** | Compleja | 5-8 | Múltiples componentes, integración, riesgo técnico medio. |
| **1** | Muy compleja | >8 | Investigación necesaria, múltiples equipos, alto riesgo. |

#### Regla spike

```
Si Inv. Complexity ≤2 AND Learning ≥4:
  → Proponer SPIKE (≤3 días) antes de la story completa
  → Spike va en el batch ANTERIOR a la story
  → Story no se estima hasta que el spike concluya
```

---

## Reglas Anti-Waterfall — Detalle

### AW-1: Cada batch tiene ≥1 story con Value ≥3

**Qué detecta:** Batches de "infraestructura pura" donde el usuario no recibe valor.

**Ejemplo de violación:**
```
Batch 1: "Configurar CI/CD" (V:1) + "Setup BD" (V:1) + "Crear esqueleto API" (V:2)
```

**Corrección:**
```
Batch 1: "Picker ve pedidos urgentes" (V:5) + "Setup BD" (V:1, co-ubicado como infra necesaria)
```

---

### AW-2: Stories con Learning 5 van en Batch 1-2

**Qué detecta:** Postergar la validación de hipótesis críticas.

**Ejemplo de violación:**
```
Batch 1: Stories con Learning 1-2 (todo conocido)
Batch 3: "Validar si el picker usa la vista consolidada" (L:5)
```

**Corrección:**
```
Batch 1: "Spike: ¿el picker usa vista consolidada?" (L:5, timebox 2 días)
         + "Picker ve pedidos urgentes" (V:5)
```

---

### AW-3: Spikes time-boxed ≤3 días con criterio de decisión

**Qué detecta:** "Investigación" sin límite que se convierte en parálisis.

**Formato spike correcto:**
```markdown
### Spike: [Pregunta]
**Time-box:** [1-3] días
**Criterio de decisión:** [Pregunta binaria: sí/no, viable/no viable]
**Si sí:** [Qué story habilita]
**Si no:** [Qué alternativa o pivot]
```

---

### AW-4: Infraestructura necesita story usuario que justifique

**Qué detecta:** Infra "por si acaso" sin story usuario asociada.

**Test:** ¿Puedo nombrar la story de usuario que necesita esta infra?
- Sí → Infra justificada. Co-ubicar en el mismo batch.
- No → Flag. ¿Realmente la necesitamos ahora?

---

### AW-5: Spikes co-ubicados con las stories que informan

**Qué detecta:** Spikes en un batch y sus stories dependientes en otro.

**Corrección:** Spike y story deben estar en el mismo batch o en batches consecutivos (spike en N, story en N o N+1).

---

## Comparativa con WSJF

| Aspecto | WSJF (SAFe) | Nuestro Framework |
|---------|-------------|-------------------|
| Lentes | CoD (User Value + Time Criticality + Risk Reduction) / Job Size | 5 lentes con pesos explícitos |
| Anti-waterfall | No incluido | 5 reglas obligatorias |
| Dependencies | No incluido | Grafo explícito + test de dependencia genuina |
| Learning | Parcial (Risk Reduction/OE) | Lente dedicada con reglas de posición |
| Output | Número (ratio) | Batches iterativos con justificación |

**Por qué no usamos WSJF puro:**
1. WSJF no tiene reglas anti-waterfall (puede resultar en "infra primero")
2. WSJF no modela dependencias entre stories
3. WSJF no distingue learning de value (ambos en CoD)
4. Los equipos tienden a agrupar por capa técnica ("infra primero") sin proponérselo — necesitamos reglas explícitas que lo impidan

---

## Template del Reporte

```markdown
# Priorización de Stories: [Nombre PRD]

**Fuente:** [PRD nombre]
**Equipo:** [Nombre del equipo]
**Stories evaluadas:** [N]
**Batches propuestos:** [N]
**Fecha:** [YYYY-MM-DD]

---

## Ranking General

| # | Story | PS | Value | Learn | Deps | Risk | Cmplx | Batch |
|---|-------|----|-------|-------|------|------|-------|-------|
| 1 | [Título corto] | X.XX | X | X | X | X | X | 1 |
| 2 | [Título corto] | X.XX | X | X | X | X | X | 1 |
| ... | | | | | | | | |

---

## Grafo de Dependencias

{Visualización del grafo}

**Dependencias genuinas:** [N]
**Falsas dependencias descartadas:** [N] {si hay, listar}

---

## Batches de Entrega

### Batch 1: [Nombre descriptivo — qué valor entrega]
**Valor para el usuario:** [Qué puede hacer el usuario tras este batch]
**Duración estimada:** [N días-equipo]

| Story | PS | Rol en el batch |
|-------|----|-----------------|
| [Título] | X.XX | [Valor principal / Learning / Desbloqueador / Infra asociada] |
| [Título] | X.XX | [Rol] |

**Desbloquea para Batch 2:** [Qué habilita]

---

### Batch 2: [Nombre descriptivo]
{Mismo formato}

---

## Validación Anti-Waterfall

| Regla | Estado | Detalle |
|-------|--------|---------|
| AW-1: ≥1 story Value ≥3 por batch | ✅/❌ | [Detalle] |
| AW-2: Learning 5 en Batch 1-2 | ✅/❌/N/A | [Detalle] |
| AW-3: Spikes time-boxed ≤3d | ✅/❌/N/A | [Detalle] |
| AW-4: Infra con story asociada | ✅/❌/N/A | [Detalle] |
| AW-5: Spikes co-ubicados | ✅/❌/N/A | [Detalle] |

{Si hay violaciones:}
### Correcciones Aplicadas
| Violación | Antes | Después | Razón |
|-----------|-------|---------|-------|
| [AW-X] | [Estado original] | [Estado corregido] | [Justificación] |

---

## Siguiente Paso

→ Llevar Batch 1 a Jira como Sprint/Iteración
→ Revisar priorización al completar cada batch (adaptar según aprendizajes)
```

---

## Reglas de Generación

1. **SIEMPRE** justificar cada score por lente con evidencia concreta
2. **SIEMPRE** aplicar las 5 reglas anti-waterfall antes de presentar el reporte
3. **SIEMPRE** incluir checkpoint de dependencias con el usuario
4. **NUNCA** presentar batches sin validación anti-waterfall
5. **NUNCA** puntuar Risk of Delay 5 sin evidencia de deadline externo real
6. **SIEMPRE** proponer spike cuando Learning ≥4 y Complexity ≤2
7. **SIEMPRE** generar como markdown/Notion — NUNCA Word/Excel
