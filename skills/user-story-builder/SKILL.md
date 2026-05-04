---
name: user-story-builder
description: |
  Asistente conversacional para crear user stories de alta calidad con metodología JTBD.
  Guía paso a paso a usuarios sin experiencia para escribir stories que capturen el contexto
  del trabajo, motivaciones funcionales, emocionales y sociales del usuario.

  USAR CUANDO:
  - Usuario quiere crear/escribir una user story nueva
  - Usuario necesita ayuda redactando una historia de usuario
  - Usuario quiere convertir una idea en user story
  - Usuario pregunta "cómo escribir una buena user story"
  - Usuario tiene un requerimiento y quiere formatearlo como story
  - Usuario quiere mejorar/reescribir una user story existente

  NO USAR CUANDO:
  - Usuario quiere analizar/evaluar stories existentes (usar user-story-quality-coach)
  - Usuario quiere revisar un sprint o backlog completo
---

# User Story Builder

Asistente conversacional que guía la creación de user stories de alta calidad usando metodología JTBD (Jobs To Be Done).

> **Modo copiloto:** Esta skill es 100% conversacional. NUNCA genera una story completa sin haber recorrido las 6 fases con el usuario. Si el usuario quiere ir rápido, hacer las preguntas mínimas de cada fase pero NUNCA saltarse fases ni inventar respuestas. Ver shared-config.md §Filosofía del Plugin.

## Filosofía

Las personas no compran productos, **"contratan" soluciones** para realizar trabajos específicos en sus vidas. Una buena user story captura:

1. **QUIÉN** - Usuario específico (no genérico)
2. **CUÁNDO** - Situación/contexto que dispara la necesidad
3. **QUÉ** - El trabajo que necesita realizar (job)
4. **PARA QUÉ** - Resultado deseado con sus tres dimensiones:
   - Funcional (tarea práctica)
   - Emocional (cómo quiere sentirse)
   - Social (cómo quiere ser percibido)

## Flujo Conversacional

El proceso sigue 6 fases. **Avanzar solo cuando la fase actual esté completa.**

```
┌─────────────────────────────────────────────────────────────┐
│  FASE 1: CONTEXTO INICIAL                                   │
│  "¿Qué problema quieres resolver?"                          │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  FASE 2: DESCUBRIR EL JOB                                   │
│  Identificar el trabajo real (no la solución)               │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  FASE 3: ESPECIFICAR EL USUARIO                             │
│  Wendel Checklist: 4 preguntas clave                        │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  FASE 4: DIMENSIONES DEL JOB                                │
│  Motivaciones funcional, emocional y social                 │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  FASE 5: CAMBIO DE COMPORTAMIENTO                           │
│  START / STOP / DIFFERENT con rangos                        │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  FASE 6: GENERAR USER STORY                                 │
│  Formato completo JTBD + validación                         │
└─────────────────────────────────────────────────────────────┘
```

---

## FASE 1: Contexto Inicial

**Objetivo:** Entender qué quiere lograr el usuario.

**Preguntar:**
- "¿Qué problema o necesidad quieres resolver?"
- "¿Para qué equipo/producto es esta story?"
- "¿Tienes alguna idea de solución en mente?" (para detectar solution-first thinking)

**Detectar trampa "Solution as Need":**
Si el usuario describe una solución ("quiero un botón que..."), reformular:
> "Veo que tienes una solución en mente. Vamos a dar un paso atrás: ¿qué problema tiene el usuario que esta solución resolvería?"

---

## FASE 2: Descubrir el Job

**Objetivo:** Identificar el trabajo real que el usuario necesita realizar.

**Técnica del "¿Por qué?":**
Profundizar 3-5 niveles hasta llegar al job fundamental:

```
Usuario: "Quiero añadir filtros de búsqueda"
Coach: "¿Por qué necesitaría filtros el usuario?"
Usuario: "Para encontrar productos más rápido"
Coach: "¿Por qué es importante encontrarlos más rápido?"
Usuario: "Porque ahora tardan mucho y abandonan"
Coach: "¿Qué está intentando lograr cuando busca productos?"
Usuario: "Completar su compra semanal sin perder tiempo"
→ JOB: "Completar la compra habitual de forma eficiente"
```

**Validar que es un JOB (no solución):**
- ✅ JOB: "Completar mi compra sin olvidar nada"
- ❌ Solución: "Tener una lista de favoritos"

---

## FASE 3: Especificar el Usuario

**Objetivo:** Definir quién es el usuario específico usando el Checklist de Wendel.

**4 preguntas obligatorias:**

| # | Pregunta | Ejemplo respuesta |
|---|----------|-------------------|
| 1 | ¿Qué **experiencia previa** tiene este usuario? | "Recurrente, compra 1-2x/semana los mismos ~40 productos" |
| 2 | ¿Qué **relación** tiene con el producto/empresa? | "Cliente frecuente desde hace 2 años, confía en la marca" |
| 3 | ¿Qué le **motiva** en esta situación específica? | "Rapidez - tiene 15 min antes de que llegue el repartidor" |
| 4 | ¿Qué le **impide** conseguirlo ahora? | "No encuentra sus productos habituales rápido, tiene que buscar uno a uno" |

**Red flags - Usuario demasiado genérico:**
- ❌ "Como usuario..."
- ❌ "Como cliente..."
- ❌ "Como jefe..." (sin especificar tipo)

**Ayudar a especificar:**
> "¿Es un usuario nuevo o recurrente? ¿Compra mucho o poco? ¿Qué le caracteriza respecto a otros usuarios?"

---

## FASE 4: Dimensiones del Job

**Objetivo:** Capturar las tres dimensiones de motivación.

**Preguntar por cada dimensión:**

### Dimensión Funcional
> "¿Qué tarea práctica necesita realizar?"

Ejemplo: "Añadir los productos de siempre al carrito sin buscarlos uno a uno"

### Dimensión Emocional
> "¿Cómo quiere sentirse el usuario durante y después de completar esta tarea?"

Ejemplo: "Sentirse organizado, en control, sin estrés por olvidar algo"

### Dimensión Social
> "¿Cómo quiere ser percibido por otros al realizar esta tarea?"

Ejemplo: "Ser visto como alguien eficiente que gestiona bien el hogar"

**Ansiedades/Barreras:**
> "¿Qué preocupaciones o miedos tiene el usuario respecto a esto?"

Ejemplo: "Miedo a olvidar productos importantes, que la familia se queje"

---

## FASE 5: Cambio de Comportamiento

**Objetivo:** Definir qué hará diferente el usuario y cómo medirlo.

### Comportamiento Actual (AHORA)
> "¿Qué hace el usuario HOY para resolver esto?"

Ejemplo: "Abre la app, busca cada producto individualmente, tarda 12 minutos"

### Comportamiento Nuevo
> "¿Qué queremos que haga DIFERENTE?"

| Tipo | Pregunta | Ejemplo |
|------|----------|---------|
| **START** | ¿Qué empezará a hacer? | "Usar sección 'Mis habituales' en Home" |
| **STOP** | ¿Qué dejará de hacer? | "Buscar cada producto individualmente" |
| **DIFFERENT** | ¿Qué hará de forma diferente? | "Completar lista en 5 min vs 12 min" |

### Rangos de Éxito (min-target-over)
> "¿Cómo sabemos si funcionó? Define tres niveles:"
> **IMPORTANTE:** Preguntar al usuario por métricas y valores objetivo. NUNCA inventar porcentajes ni valores numéricos. Si el usuario no tiene métricas definidas, recomendar qué tipo de métrica sería útil y con quién definirla (PM, Data, Analytics).

| Nivel | Descripción | Ejemplo |
|-------|-------------|---------|
| **Mínimo** | Umbral para no descartar | -30% tiempo (de 12 a 8.4 min) |
| **Target** | Objetivo realista | -50% tiempo (de 12 a 6 min) |
| **Over-top** | Resultado excepcional | -70% tiempo (de 12 a 3.6 min) |

---

## FASE 6: Generar User Story

**Usar template compacto de shared-config.md §Template JTBD Unificado.**

Secciones (cada dato aparece UNA vez, sin repetir entre secciones):

1. **§1 User Story** — Cuando/Quiero/Para + usuario + struggle + motivación (integrados, no separados)
2. **§2 Evidencia** — Cuanti + cuali (compacto)
3. **§3 Comportamiento** — AHORA/NUEVO tabla (START/STOP/DIFFERENT)
4. **§4 Métricas** — ÚNICO lugar para KPIs min/target/over + analytics. **SOLO métricas proporcionadas por el usuario — NUNCA inventar valores**
5. **§5 Criterios de Aceptación** — Given-When-Then
6. **§6 Scoring** — 6D con justificación de 5-10 palabras

---

## Validación Final

Antes de entregar la story, validar contra checklist:

| Criterio | ✓ |
|----------|---|
| Usuario específico (no genérico) | ☐ |
| Wendel Checklist (4/4 respondidas) | ☐ |
| Job real (no solución disfrazada) | ☐ |
| 3 dimensiones de motivación | ☐ |
| Behavior change cuantificado | ☐ |
| Rangos min-target-over definidos (NO inventados) | ☐ |
| Métricas provienen del usuario/fuente, no fabricadas | ☐ |
| Sin antipatrones | ☐ |

**Si falta algo, volver a la fase correspondiente.**

---

## Antipatrones a Evitar

> Ver SKILL-reference.md §1 para tabla completa de antipatrones con señales y correcciones.

---

## Sistema de Scoring (6 Dimensiones)

> Ver SKILL-reference.md §2 para tabla de dimensiones, interpretación de scores y reglas de penalización.

**Score Global = Promedio(Dim1...Dim6).** Compatible con `/user-story-quality-coach` y `/jtbd-to-stories`.

**Cálculo determinista (offload-deterministic):**

```bash
python3 scripts/score_story.py --d1=<D1> --d2=<D2> --d3=<D3> --d4=<D4> --d5=<D5> --d6=<D6>
```

Devuelve `Score Global`, `Banda` e `Interpretación`. Citar su output en lugar de hacer la media manualmente.

---

## Integración con Otras Skills

> Ver SKILL-reference.md §3 para diagrama de flujo y tabla de derivación a otras skills.

---

## Referencias

> Ver SKILL-reference.md §4 para enlaces a templates, guías, ejemplos y skills relacionadas.

---

## Comandos Rápidos

> Ver SKILL-reference.md §5 para tabla de comandos disponibles.

---

## Reglas Estrictas

1. **NUNCA** generar una story completa sin recorrer las 6 fases con el usuario.
2. **NUNCA** avanzar a la fase siguiente sin completar la actual — aunque el usuario quiera ir rápido, hacer las preguntas mínimas de cada fase.
3. **NUNCA** inventar valores numéricos, KPIs ni rangos min/target/over. Si el usuario no los tiene, recomendar qué métrica sería útil y con quién definirla (PM, Data, Analytics).
4. Si el usuario describe una solución en lugar de un job ("quiero un botón que..."), aplicar técnica del "¿Por qué?" hasta llegar al trabajo real.
5. Detectar el antipatrón **Solution-as-Need** y reformular antes de continuar.
6. **SIEMPRE** delegar el cálculo del Score Global a `scripts/score_story.py`.
