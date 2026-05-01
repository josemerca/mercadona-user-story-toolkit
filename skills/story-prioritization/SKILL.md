---
name: story-prioritization
description: |
  Prioriza user stories validadas usando 5 lentes ponderadas (Value, Learning,
  Dependencies, Risk of Delay, Inverse Complexity) y genera batches iterativos
  de entrega. Incluye deteccion de patrones waterfall y reglas anti-waterfall
  que garantizan que cada batch entrega valor usuario.

  TRIGGERS: priorizar stories, ordenar backlog, batches de entrega,
  "en que orden entregamos?", "priorizar backlog", prioritize stories,
  "organizar stories por prioridad", "proponer orden de entrega"

  INTEGRACION: Se ejecuta DESPUES de /split-stories (o /validate-stories).
  Input: stories validadas con scoring 6 dimensiones.
  Output: backlog priorizado en batches iterativos con justificacion.
version: 1.0.0
---

# Story Prioritization v1.0 — Batches Iterativos Anti-Waterfall

Ultimo paso del pipeline. Asiste al usuario en definir un orden de entrega iterativo que maximiza valor y aprendizaje, evitando patrones waterfall.

> **Modo copiloto:** Los scores y batches son PROPUESTAS basadas en la información disponible. El usuario valida y ajusta. Si hay incertidumbre sobre el valor o complejidad de una story, PREGUNTAR en vez de asignar un score arbitrario. Ver shared-config.md §Filosofía del Plugin.

> "El orden de entrega importa tanto como la calidad de las stories.
> Entregar infraestructura sin valor usuario es waterfall disfrazado de agile."

> Ver SKILL-reference.md S1 para diagrama comparativo waterfall vs iterativo.

---

## Posicion en el Pipeline

```
quality-guard|prd-quality-guard -> research -> stories -> validate -> split -> PRIORITIZE
                                                                              ^
                                                                          ESTA SKILL
```

**Input:** Stories validadas (con scoring 6 dimensiones) desde `/split-stories` o `/validate-stories`
**Output:** Backlog priorizado en batches iterativos con justificacion por story

---

## Flujo de Priorizacion

```
STORIES VALIDADAS (input)
    |
    v
+--------------------------------------+
|  1. CARGAR STORIES                    |
|     - Desde paso anterior del pipeline|
|     - O stories pegadas por usuario   |
|     - Verificar que tienen scoring    |
+--------------------------------------+
    |
    v
+--------------------------------------+
|  2. SCORING 5 LENTES                  |
|     Por cada story:                   |
|     - Value (30%)                     |
|     - Learning (25%)                  |
|     - Dependencies (20%)             |
|     - Risk of Delay (15%)            |
|     - Inverse Complexity (10%)       |
|     Priority Score = sum(lente*peso)  |
+--------------------------------------+
    |
    v
+--------------------------------------+
|  3. GRAFO DE DEPENDENCIAS             |
|     - Identificar dependencias        |
|       tecnicas genuinas entre stories |
|     - Detectar falsas dependencias    |
|       ("necesitamos infra primero")   |
|     - Visualizar grafo               |
+--------------------------------------+
    |
    v
+--------------------------------------+
|  CHECKPOINT: DEPENDENCIAS             |
|     Validar con usuario:             |
|     - Dependencias correctas?        |
|     - Alguna falsa dependencia?      |
|     - Falta alguna dependencia?      |
+--------------------------------------+
    |
    v
+--------------------------------------+
|  4. GENERACION DE BATCHES             |
|     - Agrupar stories por Priority    |
|       Score respetando dependencias   |
|     - 2-4 stories por batch           |
|     - Validar anti-waterfall          |
|     - Generar justificacion           |
+--------------------------------------+
    |
    v
+--------------------------------------+
|  5. VALIDACION ANTI-WATERFALL         |
|     - Cada batch tiene >=1 story      |
|       con valor usuario directo       |
|     - Spikes time-boxed (<=3 dias)   |
|     - Infra justificada con story     |
|     - Detectar patrones waterfall     |
+--------------------------------------+
    |
    v
+--------------------------------------+
|  6. REPORTE DE PRIORIZACION           |
|     - Ranking con justificacion       |
|     - Batches con entrega de valor    |
|     - Alertas waterfall (si hay)      |
|     - Visualizacion del orden         |
+--------------------------------------+
    |
    v
BACKLOG PRIORIZADO
```

---

## Las 5 Lentes de Priorizacion

Cada story se evalua con 5 lentes ponderadas. La formula:

```
Priority Score = (Value x 0.30) + (Learning x 0.25) + (Dependencies x 0.20)
               + (Risk of Delay x 0.15) + (Inv. Complexity x 0.10)
```

| Lente | Peso | Pregunta clave |
|-------|------|----------------|
| Value | 30% | Cuanto impacto genera para negocio y usuario? |
| Learning | 25% | Cuanta incertidumbre reduce? |
| Dependencies | 20% | Cuantas stories desbloquea? |
| Risk of Delay | 15% | Cual es el coste de NO hacerla pronto? |
| Inv. Complexity | 10% | Que tan simple es implementarla? |

> Ver SKILL-reference.md S2-S6 para rubricas detalladas (tablas de scoring 1-5 por lente).

> Ver SKILL-reference.md S7 para tabla de interpretacion del Priority Score.

---

## Paso a Paso

### Paso 1: Cargar Stories

1. Recibir stories del paso anterior del pipeline (o pegadas por el usuario)
2. Si las stories vienen de Jira: OBLIGATORIO leer TODOS los campos (description + custom fields). Ver shared-config.md §Lectura de Stories desde Jira
3. Verificar que cada story tiene:
   - Titulo / descripcion (formato Cuando-Quiero-Para)
   - Scoring 6 dimensiones
   - JTBD asociado
4. Si faltan stories o scoring -> pedir al usuario que complete

### Paso 2: Scoring 5 Lentes

Para cada story, evaluar las 5 lentes usando las rubricas de referencia.

> Ver SKILL-reference.md S2-S6 para rubricas completas por lente.

> Ver SKILL-reference.md S11 para template de scoring por story.

### CHECKPOINT: Validar Scoring con usuario

Presentar tabla de scores propuestos:

> Estos son los scores que propongo para cada lente. ¿Estás de acuerdo?
> [tabla story × 5 lentes con justificación breve]
>
> Si algún score no te convence, dime cuál y por qué.

**Esperar confirmación antes de continuar con dependencias y batches.**

### Paso 3: Grafo de Dependencias

1. Identificar dependencias tecnicas genuinas entre stories
2. Aplicar test de la dependencia para cada una
3. Descartar falsas dependencias
4. Visualizar grafo

> Ver SKILL-reference.md S10 para formato de visualizacion y reglas del grafo.

### Paso 4: Checkpoint — Dependencias

**Comunicar al usuario:**

> He identificado las siguientes dependencias entre stories:
> [Grafo]
>
> Son correctas? Hay alguna que sobre o falte?

Esperar confirmacion antes de generar batches.

### Paso 5: Generacion de Batches

1. Ordenar stories por Priority Score (descendente)
2. Respetar dependencias del grafo (bloqueantes van antes)
3. Agrupar en batches de 2-4 stories
4. Para cada batch, definir:
   - Stories incluidas con Priority Score
   - Valor que entrega el batch al usuario
   - Duracion estimada (suma de Inv. Complexity)
   - Que desbloquea para el siguiente batch

### Paso 6: Validacion Anti-Waterfall

Aplicar las 5 reglas AW-1 a AW-5. Para cada violacion:
1. Identificar la regla violada
2. Explicar por que es un patron waterfall
3. Proponer correccion concreta
4. Regenerar batches corregidos

> Ver SKILL-reference.md S8 para los 5 patrones waterfall con senales y correcciones.

> Ver SKILL-reference.md S9 para tabla completa de reglas anti-waterfall.

### Paso 7: Reporte de Priorizacion

Leer `references/prioritization-framework.md` para el template completo y generar el reporte.

> Ver SKILL-reference.md S12 para template completo del reporte de priorizacion.

---

## Reglas de Generacion

1. **SIEMPRE** justificar cada score con evidencia (nunca scores sin razon)
2. **SIEMPRE** aplicar las 5 reglas anti-waterfall antes de presentar batches
3. **SIEMPRE** incluir checkpoint de dependencias con el usuario
4. **NUNCA** poner todas las stories de infraestructura en Batch 1
5. **NUNCA** crear batches sin al menos 1 story con valor usuario directo
6. **SIEMPRE** time-boxar spikes a <=3 dias
7. Las dependencias falsas ("necesitamos la base primero") deben flaggearse
8. Si todas las stories tienen Priority Score similar -> preguntar al usuario por criterio de desempate
9. **NUNCA** generar output en formato Word/Excel — siempre Notion o markdown

---

## Referencias

- **Rubricas completas, templates y patrones:** `SKILL-reference.md`
- **Rubrica completa y ejemplos:** `references/prioritization-framework.md`
