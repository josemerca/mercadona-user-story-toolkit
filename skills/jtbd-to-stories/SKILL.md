---
name: jtbd-to-stories
description: |
  Genera User Stories de alta calidad a partir de JTBDs con evidencia real.

  POSICIÓN EN EL PIPELINE:
  - DESPUÉS de /research-from-prd (recibe JTBDs con evidencia de entrevistas)
  - ANTES de /user-story-quality-coach (entrega stories para validación)
  - NO hace gap detection (eso es /research-from-prd)
  - NO infiere JTBDs (eso es /research-from-prd)
  - SÍ mapea PRD → campos de story cuando hay datos directos

  TRIGGERS - Usar cuando el usuario pida:
  - Generar user stories desde JTBDs
  - Convertir JTBDs a backlog
  - Crear historias a partir de JTBDs validados
  - "Dame las stories del research de..."
  - "Genera stories con estos JTBDs"
  - Pasar de JTBDs a épicas/features/stories

  CONSISTENCIA GARANTIZADA:
  - Scoring: Compatible con /user-story-quality-coach (6 dimensiones, 0-10)
  - Template: Compatible con /user-story-builder (JTBD Reforzado, 3 motivaciones)
version: 2.0.0
---

# JTBD to Stories v2.0

Asiste al usuario en convertir JTBDs con evidencia real en User Stories de alta calidad, aplicando el framework JTBD Reforzado, Wendel Checklist y scoring de 6 dimensiones.

> **Modo copiloto:** Esta skill NO genera stories de forma autónoma. Guía al usuario paso a paso, señala información faltante y pregunta antes de rellenar. Ver shared-config.md §Filosofía del Plugin.

## Posición en el Pipeline

```
/prd-quality-guard  →  /research-from-prd  →  /jtbd-to-stories (ESTA)  →  /user-story-quality-coach
                              │                        │
                         JTBDs + evidencia        Stories + scoring
```

> Ver SKILL-reference.md §1 para changelog v2.0 (qué cambió respecto a v1.x)

## Framework Unificado

- **Scoring:** `/user-story-quality-coach` (6 dimensiones, escala 0-10)
- **Template:** `/user-story-builder` (JTBD Reforzado, 3 motivaciones)

---

## Input Esperado

JTBDs con evidencia real del output de `/research-from-prd` (obligatorio).
PRD original opcional para datos de Fase 2.

> Ver SKILL-reference.md §2 para formato detallado del input con ejemplo de template

Si el usuario intenta generar stories SIN haber pasado por research:
> **Recomendación:** Para stories de alta calidad, ejecuta primero `/research-from-prd`
> para obtener JTBDs con evidencia real de entrevistas.

---

## Mapeo JTBD + PRD → Story

### Desde JTBDs (input principal)

| Campo JTBD | Elemento Story | Template |
|------------|---------------|----------|
| Job Performer | Actor ("Como...") | Usuario Específico |
| Trigger | "Cuando..." | Trigger (disparador) |
| Job Principal | "Quiero..." | Job Principal (core job) |
| Desired Outcome | "Para..." | Desired Outcome |
| Struggle | Fricción | Struggle + Ansiedades/Barreras |
| Motivación Funcional | Motivación F | Tarea práctica |
| Motivación Emocional | Motivación E | Cómo quiere sentirse |
| Motivación Social | Motivación S | Cómo quiere ser percibido |
| Evidencia - Farolas | Evidencia cuanti | Métricas validadas |
| Evidencia - Penumbras | Evidencia cuali | Quotes reales |
| Wendel 1-4 | Usuario Específico | 4 respuestas reales |

### Desde PRD (complemento)

| Sección PRD | Uso en Story |
|-------------|--------------|
| Hipótesis de Solución | Comportamiento NUEVO (START) |
| Métricas | Rangos min-target-over |
| Dimensionamiento | Time Constraints (Dim 5) |
| Riesgos identificados | Survivable Experiment (Dim 6) |

---

## Proceso de Conversión (6 Pasos + 2 Checkpoints)

### Paso 1: Obtener Input

**Fuentes:**
- **JTBDs de research:** Output de `/research-from-prd` (obligatorio)
- **PRD original:** Fichero, URL o pegado (opcional, para enriquecer secciones de la story)
- **Research Gap Analysis:** Si disponible, usar para documentar gaps de evidencia

### CHECKPOINT 1: Inventario de información disponible

Antes de generar nada, comunicar al usuario:

> He revisado los JTBDs y el PRD. Este es el inventario de lo que tengo:
> - JTBDs: [listar con completitud de cada campo]
> - Evidencia: [cuanti: X datos | cuali: X quotes]
> - Métricas/KPIs: [disponibles o ⚠️ ausentes]
> - Wendel: [X/4 preguntas con datos]
>
> Información que FALTA y necesito para generar stories de calidad:
> [lista de gaps concretos con preguntas]
>
> ¿Tienes esta información? ¿Procedo con lo que hay y marco lo pendiente?

**Esperar respuesta del usuario antes de continuar.**

### Paso 2: Mapear JTBD → Story (formato JTBD Reforzado)

Para cada JTBD, construir:

```markdown
### Job Principal (core job)
[Job Principal del JTBD — la tarea fundamental]

### Struggle (fricción actual)
[Struggle del JTBD — con quotes reales si disponibles]

### Trigger (disparador)
[Trigger del JTBD — momento específico de las entrevistas]

### Desired Outcome
[Desired Outcome del JTBD — resultado esperado concreto]
```

**Validación:** El Job Principal debe ser un JOB, no una solución.
- OK: "Completar mi compra sin olvidar nada" (implementable de múltiples formas)
- MAL: "Tener una lista de favoritos" (es una solución específica)

Si detectas que el Job es una solución, aplicar técnica del "¿Por qué?" hasta llegar al job real.

### Paso 3: Extraer 3 Dimensiones de Motivación

| Dimensión | Fuente en JTBD | Pregunta clave |
|-----------|----------------|----------------|
| **Funcional** | Motivación Funcional | ¿Qué tarea práctica necesita realizar? |
| **Emocional** | Motivación Emocional | ¿Cómo quiere sentirse? |
| **Social** | Motivación Social | ¿Cómo quiere ser percibido? |

**Ansiedades/Barreras:** Extraer del Struggle del JTBD.

Si alguna motivación falta en el JTBD:
- Documentar como gap pendiente
- Si hay PRD disponible, intentar extraer de Jobs Emocionales
- Si no hay fuente, recomendar usar `/user-story-builder` para completar conversacionalmente

### Paso 4: Aplicar Wendel Checklist

| # | Pregunta | Fuente | Ejemplo |
|---|----------|--------|---------|
| 1 | ¿Experiencia previa? | Wendel 1 del JTBD | "Recurrente, 1-2x/semana" |
| 2 | ¿Relación con producto? | Wendel 2 del JTBD | "Cliente 2 años, confía" |
| 3 | ¿Motivación situacional? | Wendel 3 del JTBD | "Rapidez, 15 min antes del reparto" |
| 4 | ¿Impedimento actual? | Wendel 4 del JTBD | "Buscar uno a uno, sin historial" |

**Wendel Score:** X/4 — Si <4, documentar qué falta.

### Paso 5: Definir Cambio de Comportamiento

```markdown
### AHORA (comportamiento actual)
[Del Struggle del JTBD + observaciones de entrevistas]

### NUEVO (comportamiento objetivo)
| Tipo | Comportamiento |
|------|----------------|
| **START** | [De Hipótesis de Solución del PRD, o inferir del Desired Outcome] |
| **STOP** | [Lo que dejará de hacer — del Struggle] |
| **DIFFERENT** | [Mejora cuantificada — de métricas validadas] |

### Rangos (min-target-over)
[De KPIs Esperados del PRD, o de métricas de entrevistas]
```

Si no hay datos de Fase 2 del PRD:
- Documentar como limitación con `⚠️ Pendiente: definir con PM/Data`
- Usar métricas de las entrevistas como baseline SI EXISTEN
- **NUNCA inventar valores numéricos** — recomendar qué tipo de métrica sería útil

### CHECKPOINT 2: Revisión antes de scoring

Presentar al usuario un BORRADOR de cada story (§1 User Story + §3 Comportamiento) y preguntar:

> Aquí tienes el borrador de las stories. Antes de calcular scoring y completar:
> - ¿El Job Principal refleja bien el trabajo real del usuario?
> - ¿El cambio de comportamiento (START/STOP/DIFFERENT) es correcto?
> - ¿Hay algo que corregir o completar?
> [Listar secciones con ⚠️ Pendiente si las hay]

**Esperar confirmación antes de generar el output final.**

### Paso 6: Calcular Scoring (6 Dimensiones)

| Dim | Nombre | Fuente principal | Escala |
|-----|--------|-----------------|--------|
| 1 | JTBD & Problem Context | Evidencia cuali + cuanti del JTBD | 0-10 |
| 2 | User Specificity | Job Performer + Wendel 4/4 | 0-10 |
| 3 | Behavior Change | AHORA→NUEVO + rangos | 0-10 |
| 4 | Zone of Control | Hipótesis Solución del PRD | 0-10 |
| 5 | Time Constraints | Alcance del Q del PRD | 0-10 |
| 6 | Survivable Experiment | Riesgo/Impacto del PRD | 0-10 |

**Score Global = Promedio(Dim1...Dim6)**

Interpretación: 0-4 requiere reescritura | 5-6 necesita refinamiento | 7-8 lista para desarrollo | 9-10 modelo a seguir.

**Nota:** Stories desde JTBDs con evidencia real típicamente alcanzan Dim1 y Dim2 ≥7.

---

## Template de Salida

> Ver SKILL-reference.md §3 para secciones obligatorias y opcionales del template completo

---

## Niveles de Salida

| Nivel | Contenido | Cuándo usar |
|-------|-----------|-------------|
| **Épica** | JTBD alto nivel + métricas generales | Vista estratégica |
| **Features** | Jobs Principales desglosados (2-5 por épica) | Planificación Q |
| **Stories** | Desglose implementable (1-2 sprints cada una) | Sprint planning |

---

> Ver SKILL-reference.md §4 para antipatrones desde JTBD/PRD (7 antipatrones con señales y acciones)

> Ver SKILL-reference.md §5 para integración con el ecosistema de skills (diagrama completo + cuándo usar cada skill)

> Ver SKILL-reference.md §6 para referencias (jtbd-methodology, story-generation)

> Ver SKILL-reference.md §7 para ejemplos de uso (3 casos: evidencia completa, gaps, PRD directo)

---

## Comandos Rápidos

| Comando | Acción |
|---------|--------|
| `Genera stories con estos JTBDs` | Flujo completo desde JTBDs |
| `Genera stories del PRD de [X]` | Extracción directa del PRD (con advertencia) |
| `Stories del research de [X]` | Buscar output de research y generar |
| `Desglose a nivel [épica/feature/story]` | Ajustar granularidad de salida |
