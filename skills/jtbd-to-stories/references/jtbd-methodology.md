# Metodología JTBD (Jobs to be Done)

**Compatible con:** `/user-story-builder` - misma filosofía y estructura

## Filosofía JTBD

Las personas no compran productos, **"contratan" soluciones** para realizar trabajos específicos en sus vidas. Una buena user story captura:

1. **QUIÉN** - Usuario específico (no genérico)
2. **CUÁNDO** - Situación/contexto que dispara la necesidad
3. **QUÉ** - El trabajo que necesita realizar (job)
4. **PARA QUÉ** - Resultado deseado con sus tres dimensiones

## Fórmula Job Story

```
Cuando [SITUACIÓN + CONTEXTO],
quiero [MOTIVACIÓN/CAPACIDAD],
para [RESULTADO ESPERADO].
```

## Las 3 Dimensiones de Motivación

Toda necesidad tiene tres capas de motivación:

### 1. Funcional (Obligatoria)
**Pregunta:** ¿Qué tarea práctica necesita realizar?

- Verbos de acción: completar, verificar, registrar, consultar
- Medible y observable
- Es lo que el PRD captura en "Motivación"

**Ejemplo:** "Añadir los productos de siempre al carrito sin buscarlos uno a uno"

### 2. Emocional (Recomendada)
**Pregunta:** ¿Cómo quiere sentirse el usuario durante y después?

- Seguridad, confianza, tranquilidad, control
- Reduce ansiedad, aumenta satisfacción
- Es lo que el PRD captura en "Jobs Emocionales"

**Ejemplo:** "Sentirse organizado, en control, sin estrés por olvidar algo"

### 3. Social (Cuando aplique)
**Pregunta:** ¿Cómo quiere ser percibido por otros?

- Eficiente, profesional, cumplidor
- Imagen que proyecta
- También en "Jobs Emocionales" del PRD

**Ejemplo:** "Ser visto como alguien eficiente que gestiona bien el hogar"

## Mapeo PRD → 3 Dimensiones

| Campo PRD | Dimensión | Notas |
|------------|-----------|-------|
| Motivación | Funcional | Tarea práctica principal |
| Jobs Emocionales | Emocional | Cómo quiere sentirse |
| Jobs Emocionales | Social | Cómo quiere ser percibido |
| Limitaciones actuales | Ansiedades | Miedos y barreras |

## JTBD Reforzado (Estructura Completa)

```markdown
### Job Principal (core job)
[La tarea fundamental - de Motivación del PRD]

### Struggle (fricción actual)
- [Limitación 1 del PRD]
- [Limitación 2 del PRD]

### Trigger (disparador)
[Momento/situación - de Contexto Situacional del PRD]

### Desired Outcome (resultado deseado)
[Qué espera conseguir - de Criterio de Éxito del PRD]

### Motivación Funcional
- [De Motivación del PRD]

### Motivación Emocional
- [De Jobs Emocionales del PRD]

### Motivación Social
- [De Jobs Emocionales del PRD]

### Ansiedades / Barreras
- [De Limitaciones actuales del PRD]
```

## Técnica del "¿Por qué?"

Para descubrir el job real cuando el PRD tiene una solución disfrazada:

```
PRD dice: "Quiero añadir filtros de búsqueda"
¿Por qué? → "Para encontrar productos más rápido"
¿Por qué? → "Porque ahora tardan mucho y abandonan"
¿Por qué? → "Quieren completar su compra sin perder tiempo"
→ JOB REAL: "Completar la compra habitual de forma eficiente"
```

## Wendel Checklist - Usuario Específico

4 preguntas obligatorias para validar especificidad:

| # | Pregunta | Fuente PRD | Ejemplo |
|---|----------|-------------|---------|
| 1 | ¿Qué **experiencia previa** tiene? | Job Performer + Contexto | "Recurrente, 1-2x/semana" |
| 2 | ¿Qué **relación** tiene con producto? | Contexto del Usuario | "Cliente 2 años, confía" |
| 3 | ¿Qué le **motiva** en esta situación? | Motivación | "Rapidez, 15 min antes del reparto" |
| 4 | ¿Qué le **impide** conseguirlo? | Limitaciones actuales | "Buscar uno a uno" |

## Red Flags - Antipatrones

| Antipatrón | Señal | Corrección |
|------------|-------|------------|
| Usuario genérico | "Como usuario..." | Aplicar Wendel 4 preguntas |
| Verbo débil | "Gestionar" | Especificar: "Registrar", "Verificar" |
| Sin contexto | "Quiero ver datos" | Añadir "Cuando [situación]" |
| Solución disfrazada | "Quiero un botón de..." | "¿Por qué?" hasta llegar al job |
| Sin "para qué" | Solo funcional | Añadir emocional + beneficio |
| Sin evidencia | Job sin datos | Buscar Penumbras/Farolas en PRD |

## Validación: ¿Es un JOB o una SOLUCIÓN?

| ✅ Es un JOB | ❌ Es una SOLUCIÓN |
|--------------|-------------------|
| "Completar mi compra sin olvidar nada" | "Tener una lista de favoritos" |
| "Saber cuándo llega mi pedido" | "Ver el tracking en tiempo real" |
| "No perder tiempo buscando productos" | "Tener filtros de búsqueda" |

**Regla:** Si puedes implementarlo de varias formas, es un JOB. Si es específico, es una solución.

## Estructura de Salida del JTBD

```yaml
JTBD:
  actor: [Job Performer del PRD]
  trigger: [Contexto Situacional]
  job_principal: [Motivación transformada]
  desired_outcome: [Criterio de Éxito]
  motivaciones:
    funcional: [Tarea práctica]
    emocional: [Cómo quiere sentirse]
    social: [Cómo quiere ser percibido]
  struggle: [Limitaciones actuales]
  ansiedades: [Miedos/barreras]
  evidencia:
    penumbras: [Feedback cualitativo]
    farolas: [Datos cuantitativos]
```

## Integración con Skills

- **Si el PRD tiene Jobs Emocionales completos:** Extraer directamente
- **Si el PRD solo tiene Motivación funcional:** Usar `/user-story-builder` para completar conversacionalmente las dimensiones emocional y social
- **Después de generar:** Validar con `/user-story-quality-coach`
