# Estructura del PRD — Template Completo

## Qué es este PRD

Un Product Requirements Document estructurado en tres bloques: EAC (Estado Actual Conocido),
EFC (Estado Futuro Conocido) y Discovery/Scope. Diseñado para hacer falsable la definición
de producto: cada sección produce contenido testeable, no narrativa.

---

## Estructura Completa

### Bloque 1: EAC (Estado Actual Conocido)

#### 1.1 Problema

**Propósito:** Definir con precisión QUÉ problema existe, para QUIÉN y con qué impacto.

**Checklist:**
- [ ] Definición en 2-3 frases concretas
- [ ] Quién sufre el problema (rol específico, no "usuario")
- [ ] Desde cuándo existe
- [ ] Qué impacto tiene (cuantificado si posible)
- [ ] Por qué es importante resolverlo AHORA

**Ejemplo bueno:**
> Los pickers del almacén central de Valencia tardan una media de 45 minutos por pedido urgente
> (vs 30 min objetivo), con un 8% de tasa de error en selección de producto. Esto genera
> +15% de horas extra y un NPS de -12 puntos en pedidos urgentes. El problema se ha agravado
> desde la apertura del turno de tarde en octubre 2025.

**Ejemplo malo:**
> Necesitamos mejorar el proceso de picking para ser más eficientes.

---

#### 1.2 Farolas (Evidencia Cuantitativa)

**Propósito:** Datos concretos que iluminan el problema.

**Checklist:**
- [ ] ≥3 métricas cuantitativas
- [ ] Cada métrica tiene baseline actual
- [ ] Fuente de los datos identificada
- [ ] Temporalidad de los datos (cuándo se midieron)
- [ ] Tendencia si aplica (mejorando/empeorando)

**Formato recomendado:**
```
| Farola | Valor | Fuente | Fecha |
|--------|-------|--------|-------|
| Tiempo medio picking urgente | 45 min (obj: 30 min) | Dashboard OPS | Ene 2026 |
| Tasa error selección producto | 8% | Jira incidencias | Q4 2025 |
| Horas extra semanales | +15% vs presupuesto | SAP HR | Dic 2025 |
```

---

#### 1.3 Penumbras (Evidencia Cualitativa — quotes, observaciones de campo, testimonios)

**Propósito:** Feedback cualitativo real recogido de personas que viven el problema. NO son dudas ni áreas sin explorar.

**Checklist:**
- [ ] ≥3 observaciones cualitativas reales
- [ ] Procedencia identificada (quién lo dijo/observó)
- [ ] Contexto de la observación (dónde, cuándo)
- [ ] Citas directas cuando sea posible

**Formato recomendado:**
```
| Penumbra | Fuente | Contexto |
|----------|--------|----------|
| "Cuando llega un pico, me siento apagando fuegos" | Picker senior, Valencia | Observación turno tarde, 15-Ene |
| "Consulto 3 pantallas distintas para saber qué hacer" | Coordinador, Madrid | Entrevista 1on1, 20-Ene |
```

---

#### 1.4 Próximos Pasos

**Propósito:** Qué se necesita hacer para avanzar en la comprensión del problema.

**Checklist:**
- [ ] Acciones concretas con responsable
- [ ] Plazo estimado
- [ ] Dependencias identificadas

---

### Bloque 2: EFC (Estado Futuro Conocido)

#### 2.1 Hipótesis de Solución

**Propósito:** La propuesta de solución con justificación basada en el EAC.

**Checklist:**
- [ ] Hipótesis formulada como: "Creemos que [acción] para [usuario] resultará en [outcome]"
- [ ] Justificación basada en datos del EAC
- [ ] Alternativas consideradas y por qué se descartaron
- [ ] Riesgos identificados

**Ejemplo bueno:**
> Creemos que una vista consolidada de pedidos con priorización automática para los pickers
> resultará en una reducción del 30% en el tiempo de picking urgente, porque las Farolas
> muestran que el 60% del tiempo extra se dedica a decidir qué pedido hacer primero.

**Ejemplo malo:**
> Vamos a hacer un dashboard nuevo que mejore la experiencia.

---

#### 2.2 Aspectos Financieros

**Propósito:** Impacto económico cuantificado.

**Checklist:**
- [ ] Coste estimado de la solución
- [ ] Ahorro estimado (con cálculo)
- [ ] ROI o payback period
- [ ] Impacto en métricas de negocio

---

#### 2.3 Métricas

**Propósito:** KPIs medibles con baseline y target.

**Checklist:**
- [ ] ≥2 métricas primarias
- [ ] Cada métrica tiene: nombre, baseline, target, plazo
- [ ] Método de medición definido
- [ ] Frecuencia de medición

**Formato recomendado:**
```
| Métrica | Baseline | Target | Plazo | Cómo medir |
|---------|----------|--------|-------|-------------|
| Tiempo picking urgente | 45 min | 30 min | Q2 2026 | Dashboard OPS |
| Tasa error selección | 8% | 3% | Q2 2026 | Jira incidencias |
```

---

#### 2.4 Dimensionamiento

**Propósito:** Escala y alcance de la solución.

**Checklist:**
- [ ] Usuarios afectados (número)
- [ ] Volumen de operaciones
- [ ] Centros/ubicaciones impactadas
- [ ] Fases de rollout si aplica

---

### Bloque 3: Discovery + Scope

#### 3.1 Discovery

**Propósito:** Investigación realizada para validar el problema y la solución.

**Checklist:**
- [ ] Metodología usada (entrevistas, observación, análisis datos...)
- [ ] Número de participantes/fuentes
- [ ] Hallazgos principales (≥3)
- [ ] Cómo los hallazgos informan la solución

---

#### 3.2 Explore

**Propósito:** Alternativas exploradas antes de decidir la solución.

**Checklist:**
- [ ] ≥2 alternativas consideradas
- [ ] Criterios de evaluación
- [ ] Razón de descarte de cada alternativa
- [ ] Por qué la opción elegida es la mejor

---

#### 3.3 Funcionalidades Principales

**Propósito:** Features incluidas, priorizadas.

**Checklist:**
- [ ] Lista clara de funcionalidades
- [ ] Priorización (must-have vs nice-to-have)
- [ ] Cada feature vinculada a un problema/JTBD
- [ ] Criterios de aceptación alto nivel

---

#### 3.4 Flujos de Usuario

**Propósito:** Cómo el usuario interactúa con la solución.

**Checklist:**
- [ ] Al menos 1 flujo principal documentado
- [ ] Puntos de entrada y salida claros
- [ ] Actores identificados
- [ ] Caminos alternativos/error

---

#### 3.5 FAQs

**Propósito:** Preguntas frecuentes que anticipa el equipo.

**Checklist:**
- [ ] ≥5 preguntas con respuesta
- [ ] Incluye preguntas de equipo técnico
- [ ] Incluye preguntas de stakeholders negocio

---

#### 3.6 Exclusiones

**Propósito:** Qué NO está en scope.

**Checklist:**
- [ ] ≥3 exclusiones explícitas
- [ ] Cada exclusión justificada
- [ ] Referencia a fase futura si aplica

---

## Reglas de Escritura del PRD

| # | Regla | Detalle |
|---|-------|---------|
| 1 | Frases ≤30 palabras | Frases largas pierden foco |
| 2 | Sin adjetivos sin datos | "Muy lento" → "45 min vs 30 min objetivo" |
| 3 | Bullet points ≤3 niveles | Anidación excesiva = estructura confusa |
| 4 | Cada sección con encabezado | Navegación clara del documento |
| 5 | Datos con fuente | "45 min (analytics dashboard, Ene 2026)" |
| 6 | Citas textuales entrecomilladas | Diferenciar observación de interpretación |
| 7 | Métricas con formato baseline→target | "De 45 min a 30 min" |
