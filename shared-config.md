# Configuración Compartida — Mercadona User Story Toolkit (OSS)

Documento de referencia compartido por todas las skills del toolkit.

## Filosofía del Plugin: Copiloto Conversacional (OBLIGATORIO)

Las skills del toolkit operan en **modo copiloto**: diagnostican, proponen y guían — pero NO completan ni inventan contenido por el usuario.

### Principios fundamentales

1. **Preguntar antes de generar** — Si falta información clave, preguntar primero
2. **Guiar, no automatizar** — La skill propone, el usuario decide
3. **Foco en lo que falta** — Señalar gaps, no rellenarlos
4. **Checkpoints obligatorios** — Antes de generar output extenso, confirmar enfoque
5. **Transparencia sobre incertidumbre** — Si no hay evidencia, decirlo

### Comportamiento por defecto en TODAS las skills

- Si el PRD tiene huecos → listarlos como preguntas para el PM, no rellenarlos
- Si no hay datos cuantitativos → recomendar qué tipo de métrica sería útil, no fabricar valores
- Si el research no se ha hecho → diseñar el plan, no inventar conclusiones
- Si una decisión es ambigua → preguntar al usuario, no asumir

### Anti-patrón: Generación Autónoma Excesiva

NO hacer:
- Rellenar farolas/penumbras con datos inventados
- Generar JTBDs sin evidencia real de entrevistas
- Asumir alcance que no está en el PRD
- Decidir priorización sin checkpoint con el usuario

---

## Skills del Ecosistema

| Skill | Rol | Trigger ejemplo |
|-------|-----|-----------------|
| `prd-quality-guard` | Quality gate: evaluar PRD antes de research | "Analizar calidad de este PRD" |
| `gsd-to-prd` | Mapear artefactos GSD (.planning/) → PRD sintético | "/from-gsd" |
| `research-from-prd` | Gap detection + Research Mom Test desde PRD | "Research para el PRD de..." |
| `user-story-builder` | Crear stories desde cero (sin PRD) | "Ayúdame a escribir una story" |
| `jtbd-to-stories` | Generar stories estructuradas desde JTBDs | "Convertir JTBDs en stories" |
| `user-story-quality-coach` | Validar stories con scoring 6 dimensiones + antipatrones | "Validar estas stories" |
| `story-splitting` | Detectar stories grandes y proponer splits incrementales | "¿Cómo divido esta story?" |
| `story-prioritization` | Priorización con 5 lentes + grafo de dependencias | "Prioriza el batch del sprint" |

---

## Pipeline Unificado (3 vías de entrada)

```
┌─────────────────────────────────────────────────────────────────────┐
│                         FUENTES DE ENTRADA                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   PRD               GSD              Sin documento                  │
│    │                 │                    │                         │
│    │           /from-gsd                  │                         │
│    │                 │                    │                         │
│    │     [completar GAPs marcados]        │                         │
│    │                 │                    │                         │
│    └────────┬────────┘                    │                         │
│             │                             │                         │
│             ▼                             ▼                         │
│   /prd-quality-guard            /user-story-builder                 │
│             │                             │                         │
│             ▼                             │                         │
│       /research                           │                         │
│   (entrevistas reales)                    │                         │
│             │                             │                         │
│             ▼                             │                         │
│    /analyze-research                      │                         │
│             │                             │                         │
│             ▼                             │                         │
│        /stories                           │                         │
│             │                             │                         │
│             └──────────────┬──────────────┘                         │
│                            ▼                                        │
│                  /validate-stories                                  │
│                            │                                        │
│                            ▼                                        │
│                  /split-stories (opcional)                          │
│                            │                                        │
│                            ▼                                        │
│                    /prioritize                                      │
│                            │                                        │
│                            ▼                                        │
│            Stories priorizadas en batches                           │
│         → tu issue tracker / Superpowers / equipo                   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Bridge a ejecución:** `bridge/gsd-bridge.py` mantiene consistencia entre `.planning/` (GSD) y commits del ejecutor (p. ej. Superpowers). Ver `bridge/README.md`.

---

## Estilo de Escritura (OBLIGATORIO)

| # | Regla | Detalle |
|---|-------|---------|
| 1 | Frases ≤30 palabras | Frases largas pierden foco |
| 2 | Sin adjetivos sin datos | "Muy lento" → "45 min vs 30 min objetivo" |
| 3 | Bullet points ≤3 niveles | Anidación excesiva confunde |
| 4 | Cada sección con encabezado | Navegación clara |
| 5 | Datos con fuente | "45 min (analytics, Ene 2026)" |
| 6 | Citas textuales entrecomilladas | Diferenciar observación de interpretación |
| 7 | Métricas con baseline → target | "De 45 min a 30 min" |
| 8 | NUNCA inventar métricas/KPIs | Solo incluir métricas explícitas. Si no hay: placeholder `[⚠️ Pendiente: definir con PM/Data]` |

---

## Sistema de Scoring Unificado (6 Dimensiones)

Todas las skills generadoras aplican este scoring a cada story:

| Dim | Nombre | Pregunta clave |
|-----|--------|----------------|
| 1 | Clarity | ¿Es la story específica y testeable? |
| 2 | Independence | ¿Se puede entregar sin esperar a otra story? |
| 3 | Negotiability | ¿Hay flexibilidad en el "cómo"? |
| 4 | Value | ¿Aporta valor observable al usuario? |
| 5 | Estimability | ¿Se puede estimar con confianza? |
| 6 | Survivable Experiment | ¿Es lo bastante pequeña para fallar barato? |

### Escala de Scoring

- **9-10:** Excelente — proceder sin cambios
- **7-8:** Bueno — proceder con observaciones menores
- **5-6:** Mejorable — splittear o refinar antes de proceder
- **<5:** Insuficiente — rehacer

---

## Antipatrones Compartidos

Las skills detectan estos antipatrones al validar stories:

1. **Fake Story** — No es una story de usuario, es una tarea técnica disfrazada
2. **Story-as-spec** — La story describe el cómo en lugar del qué + por qué
3. **Compound story** — Múltiples necesidades mezcladas (necesita splitting)
4. **Acceptance overload** — >7 criterios de aceptación sugieren story demasiado grande
5. **Vague valor** — "para mejorar la experiencia" sin métrica observable
6. **Missing JTBD** — La story no se ata a un Job-to-be-Done explícito
7. **Solution-first** — La solución va antes que el problema/contexto

---

## Gap Detection (dos niveles)

### Gap Detection del PRD (en `prd-quality-guard`)

Evalúa completitud del PRD antes de diseñar research. Identifica secciones débiles o vacías.

### Gap Detection del Research (en `research-from-prd`)

Tras analizar las notas de entrevistas, evalúa cobertura y calidad de evidencia. Identifica si los hallazgos son suficientes para generar JTBDs sólidos.

---

## Terminología

| Término | Definición |
|---------|------------|
| **PRD** | Product Requirements Document. Documento que define problema, solución, métricas y scope |
| **JTBD** | Job-to-be-Done. Trabajo funcional + emocional + social que el usuario "contrata" la solución para hacer |
| **Farola** | Evidencia cuantitativa. Métrica con valor + fuente + fecha |
| **Penumbra** | Evidencia cualitativa. Cita o observación de campo con fuente y contexto. NO es una incertidumbre |
| **Mom Test** | Técnica de entrevista (Rob Fitzpatrick): preguntar sobre comportamientos pasados, no opiniones futuras |
| **Behavior Change** | Comportamiento concreto que cambia con la solución (AHORA → NUEVO) |
| **Gap Score** | Completitud del PRD (0-100), output de prd-quality-guard |
| **Anti-waterfall** | Reglas que impiden batches que solo entregan valor al final (infra-first, etc.) |

---

## Lectura de Stories desde Issue Tracker (opcional)

El toolkit es agnóstico de issue tracker. Cuando el usuario quiere leer stories existentes (de Jira, Linear, Shortcut, etc.) las opciones son:

1. **Pegar contenido directamente:** El usuario aporta el contenido de la story como texto.
2. **Fichero markdown:** El usuario exporta la story como markdown.
3. **MCP del issue tracker:** Si el usuario tiene un MCP configurado para su herramienta, las skills pueden invocarlo. Esa configuración va por fuera del toolkit.

**Regla común:** asegurar que se captura TODA la información (no solo summary). Si tu fuente separa producto/diseño/ingeniería en campos distintos, indícalo al pegar el contenido.

---

## Fuentes de PRDs

El toolkit es agnóstico de la herramienta de almacenamiento. El usuario aporta el documento como:
- Ruta a un fichero local (`.md`, `.docx` previamente convertido a markdown)
- URL pública del documento
- Contenido pegado directamente en el chat

Cada equipo configura su integración con la herramienta de documentos por fuera del toolkit.

---

## Versiones

| Skill | Versión | Notas |
|-------|---------|-------|
| prd-quality-guard | 1.0 | Quality gate del PRD |
| gsd-to-prd | 1.0 | Mapeo GSD → PRD (Ruta D) |
| research-from-prd | 1.0 | Gap detection + research design |
| jtbd-to-stories | 2.0 | Generación de stories con scoring |
| user-story-builder | 1.0 | Stories desde cero |
| user-story-quality-coach | 1.0 | Validación 6D + antipatrones |
| story-splitting | 1.0 | Splits incrementales |
| story-prioritization | 1.0 | Priorización con 5 lentes |

---

*Plugin v0.1.0 — MIT License — https://github.com/josemerca/mercadona-user-story-toolkit*
