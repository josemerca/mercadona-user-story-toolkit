---
name: story-splitting
description: |
  Detecta stories demasiado grandes y aplica heurísticas de splitting para descomponerlas
  en incrementos pequeños, seguros y valiosos. Último paso antes de priorización/ejecución.

  POSICIÓN EN EL PIPELINE:
  - DESPUÉS de /validate-stories (recibe stories validadas con scoring 6D)
  - ÚLTIMO paso antes de pasar a tu issue tracker o ejecutor
  - Puede ejecutarse independientemente sobre cualquier story

  USAR CUANDO:
  - Story tiene red flags lingüísticos: "y", "o", "gestionar", "manejar", "incluyendo"
  - Story describe múltiples features bundled
  - Story parece demasiado grande o vaga (>3 días de trabajo)
  - Usuario pregunta "cómo dividir esta story" o "esta story es muy grande"
  - Después de /validate-stories para asegurar granularidad óptima
  - Comando: /split-stories

  NO USAR CUANDO:
  - Story ya es pequeña y enfocada (<1 día de trabajo)
  - Score Dim 6 (Survivable Experiment) ≥8 (ya es suficientemente pequeña)
  - Usuario pregunta CÓMO implementar (no es splitting, es diseño técnico)
---

# Story Splitting

Asiste al usuario en detectar stories demasiado grandes y propone heurísticas para descomponerlas en incrementos pequeños, seguros y valiosos.

> **Modo copiloto:** Esta skill diagnostica y PROPONE splits, pero NO los aplica automáticamente. Presenta el diagnóstico al usuario y espera confirmación antes de generar splits. Ver shared-config.md §Filosofía del Plugin.

## Principio Fundamental

**El riesgo crece más rápido que el tamaño del cambio.**

Stories pequeñas = Bajo riesgo = Feedback rápido = Aprendizaje
Stories grandes = Alto riesgo = Feedback lento = Desperdicio

---

## Integración con el Pipeline

```
quality-guard → research → stories → validate-stories → 🆕 SPLIT-STORIES
                                                              │
                                                              ▼
                                                        Stories listas
                                                        para Jira
```

### Cuándo aplicar splitting automáticamente

| Señal del pipeline | Acción |
|---|---|
| Score Dim 6 (Survivable Experiment) ≤6 | ⚠️ Splitting recomendado |
| Story tiene >3 criterios de aceptación | ⚠️ Revisar si se puede dividir |
| Story cubre >1 iteración del PRD | ⚠️ Dividir por iteración primero |
| Red flags lingüísticos detectados | 🚨 Splitting obligatorio |

### Input esperado

Stories con formato del ecosistema (template unificado de shared-config.md):
- User Story (Como/Cuando/Quiero/Para)
- JTBD Reforzado
- Criterios de Aceptación (Given-When-Then)
- Scoring 6 dimensiones

> Si las stories vienen de Jira, OBLIGATORIO leer TODOS los campos (description + custom fields). Ver shared-config.md §Lectura de Stories desde Jira.

### Output

Para cada story analizada:
1. **Diagnóstico de red flags** (si los hay)
2. **Propuesta de splits** (3-5 sub-stories concretas)
3. **Orden de entrega recomendado** (más pequeña y valiosa primero)
4. **Técnica(s) aplicada(s)**
5. **Estimación relativa** de cada split (S/M/L)

---

## Proceso

### Paso 1: Escanear Red Flags

Leer cada story buscando indicadores lingüísticos en TODOS estos campos:
- User Story (Como/Cuando/Quiero/Para)
- JTBD Reforzado (Job Principal, Struggle)
- Criterios de Aceptación

6 categorías de red flags a buscar:
1. Conjunciones coordinantes: "y", "o", "pero", "ni"
2. Conectores de acción: "gestionar", "manejar", "administrar", "procesar", "mantener"
3. Conectores de secuencia: "antes", "después", "luego", "mientras", "cuando"
4. Indicadores de alcance: "incluyendo", "además", "también", "con"
5. Indicadores de opción: "o bien", "opcionalmente", "alternativamente"
6. Indicadores de excepción: "excepto", "a menos que", "sin embargo", "aunque"

> Ver SKILL-reference.md §S1 para ejemplos detallados de cada categoría.

**Cuando detectes estas palabras, marcar la story como candidata a splitting.**

---

### Paso 2: Tabla de Decisión — Red Flag → Técnica Recomendada

> Ver SKILL-reference.md §S2 para la tabla completa de decisión Red Flag → Técnica Recomendada (10 patrones con ejemplos).

---

### CHECKPOINT: Diagnóstico con el usuario

Antes de proponer splits, presentar el diagnóstico:

> He encontrado estos red flags en la story:
> [tabla de red flags detectados con categoría y texto exacto]
>
> Técnica(s) de splitting recomendada(s): [lista]
>
> ¿Estás de acuerdo con el diagnóstico? ¿Hay algún aspecto que no deba dividirse?
> ¿Hay restricciones de entrega que deba considerar?

**Esperar confirmación antes de generar los splits.**

### Paso 3: Aplicar Heurísticas de Splitting

9 heurísticas disponibles (aplicar según red flags detectados):

| # | Heurística | Cuándo aplicar |
|---|-----------|----------------|
| 1 | Empezar por los Outputs | Output complejo (reportes, dashboards) |
| 2 | Estrechar el Segmento de Usuario | "para todos los usuarios" |
| 3 | Extraer la Utilidad Básica Primero | Feature bundling ("incluyendo", "con") |
| 4 | Empezar con Dummy, Mover a Dinámico | Múltiples fuentes de datos |
| 5 | Simplificar los Outputs | Múltiples formatos de salida |
| 6 | Dividir por Capacidad | Alcance de volumen amplio |
| 7 | Dividir por Ejemplos de Utilidad | Cambios técnicos grandes |
| 8 | Separar Aprender de Ganar | Incertidumbre técnica alta |
| 9 | Walking Skeleton en Muletas | "tiempo real" / "automatizado" |

> Ver SKILL-reference.md §S3 para ejemplos detallados de cada heurística.

---

### Paso 4: Validar los Splits

Para cada split propuesto, verificar:

- [ ] Escanear la story en busca de las 6 categorías de red flags
- [ ] Marcar la story como "demasiado grande" cuando hay red flags
- [ ] Identificar la técnica de splitting a aplicar usando la tabla de decisión
- [ ] Proponer 3-5 splits concretos (no sugerencias vagas)
- [ ] Cada split es **independientemente valioso** (se puede desplegar solo)
- [ ] Cada split es completable en **≤3 días**
- [ ] Identificar el **split más pequeño para empezar** (Survivable Experiment)
- [ ] Aplicar múltiples técnicas si la story tiene múltiples red flags
- [ ] Los splits son **verticales** (entregan valor end-to-end), no horizontales ("hacer BD, hacer API, hacer UI")

**Señales de que NO se hizo bien:**
- Aceptar la story sin cuestionar (no detectar red flags)
- Los splits siguen siendo grandes (>3 días cada uno)
- Los splits son horizontales ("construir BD, construir API, construir UI") en vez de verticales
- Los splits no entregan valor independiente (uno depende de que otro termine primero)
- Solo proponer 1-2 splits en vez de descomponer completamente

---

### Paso 5: Generar Output

> Ver SKILL-reference.md §S4 para el template completo de output (diagnóstico, red flags, splits, orden de entrega, impacto en scoring).

---

## Contexto del equipo (opcional)

> Ver SKILL-reference.md §S5 para red flags frecuentes y usuarios válidos para splits. Si tu equipo tiene un `team-context-template.md` configurado, se usa para personalizar los ejemplos.

## Tono de Coaching

> Ver SKILL-reference.md §S6 para guía de tono de coaching y frases útiles.
