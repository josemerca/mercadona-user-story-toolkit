# JTBD to Stories — Reference

Material de referencia para la skill `/jtbd-to-stories`. El procedimiento core está en `SKILL.md`.

---

## §1 Changelog v2.0

| Antes (v1.x) | Ahora (v2.0) |
|---|---|
| Hacía gap detection (Paso 0) | Gap detection movido a /research-from-prd |
| Infería JTBDs del PF (Paso 0.5) | JTBDs vienen con evidencia REAL de entrevistas |
| Aceptaba PRDs sin research | Requiere JTBDs validados como input |
| Gap detection + Inferencia + Stories | Solo generación de stories (foco) |

---

## §2 Formato de Input Esperado

Esta skill recibe **JTBDs con evidencia real** del output de `/research-from-prd`:

```markdown
## JTBDs Descubiertos (Evidencia: Entrevistas reales)

### JTBD 1: [Título]
**Confianza:** Alta (basado en N entrevistas)

**Job Performer:** [Rol específico con contexto real]
**Trigger:** Cuando [situación concreta de las entrevistas]
**Job Principal:** Quiero [motivación funcional]
**Desired Outcome:** Para [resultado esperado]

**Motivaciones:**
- Funcional: [De comportamientos observados]
- Emocional: [De quotes reales] → "[quote]"
- Social: [De contexto observado] → "[quote]"

**Evidencia:**
- Farolas confirmadas: [métricas del PF validadas]
- Penumbras confirmadas: [quotes que validan]
- Nuevos hallazgos: [no estaban en el PRD]

**Wendel Checklist:**
1. Experiencia previa: [dato real]
2. Relación con producto: [dato real]
3. Motivación situacional: [dato real]
4. Impedimento actual: [dato real]
```

Si también se proporciona el PRD original, se usa para complementar con datos de Fase 2
(Hipótesis de Solución, KPIs, Alcance del Q, Riesgo/Impacto).

---

## §3 Template de Salida Completo

Ver `references/story-generation.md` para template completo compatible con `user-story-builder`.

Secciones obligatorias:
1. **User Story** (formato JTBD: Como/Cuando/Quiero/Para)
2. **JTBD Reforzado** (Job, Struggle, Trigger, Outcome, 3 motivaciones, ansiedades)
3. **Usuario Específico** (Wendel 4/4 con datos reales)
4. **Evidencia** (Penumbras confirmadas + Farolas validadas)
5. **Cambio de Comportamiento** (AHORA → NUEVO, START/STOP/DIFFERENT)
6. **Rangos de Éxito** (min-target-over)
7. **Criterios de Aceptación** (Given-When-Then)
8. **Scoring** (6 dimensiones con justificación)

Secciones opcionales (si hay datos de Research Gap Analysis):
9. **Notas de Evidencia** — Gaps de research pendientes que afectan la story
10. **Experimento** — Feature flag, tráfico, criterios rollback (de Fase 2 del PRD)

---

## §4 Antipatrones desde JTBD/PRD

| Antipatrón | Señal | Acción |
|------------|-------|--------|
| Usuario genérico | Job Performer sin contexto | Volver a Wendel, usar datos de entrevista |
| No Behavior Change | Sin AHORA→NUEVO definido | Buscar en Struggle + Desired Outcome |
| Fake Story | Beneficiario = equipo, no usuario | Cuestionar: ¿quién es el Job Performer real? |
| Solution as Need | Job Principal = feature | Aplicar "¿Por qué?" hasta llegar al job |
| Sin 3 motivaciones | Solo motivación funcional | Buscar en quotes emocionales de entrevistas |
| Sin evidencia | JTBD sin quotes ni métricas | Recomendar más entrevistas vía /research-from-prd |
| Score inflado | Dims 4-6 altas sin datos Fase 2 | No puntuar lo que no tiene evidencia |

---

## §5 Integración con el Ecosistema de Skills

### Flujo Completo del Ecosistema

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ECOSISTEMA USER STORIES v2.0                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ENTRADA: PRD (fichero, URL o pegado)                                  │
│      │                                                                   │
│      ▼                                                                   │
│  ┌─────────────────────────────────────────┐                            │
│  │  /prd-quality-guard            │                            │
│  │  Evalúa calidad del PF (score ≥7)      │                            │
│  └─────────────────┬───────────────────────┘                            │
│                    │                                                     │
│                    ▼                                                     │
│  ┌─────────────────────────────────────────┐                            │
│  │  /research-from-prd                    │                            │
│  │                                          │                            │
│  │  • Gap Detection del PRD               │                            │
│  │  • Diseño de entrevistas (Mom Test)     │                            │
│  │  • Análisis de notas                    │                            │
│  │  • Gap Detection del Research           │                            │
│  │  • Producción de JTBDs con evidencia    │                            │
│  └─────────────────┬───────────────────────┘                            │
│                    │                                                     │
│                    │  JTBDs + evidencia real                             │
│                    │                                                     │
│                    ▼                                                     │
│  ┌─────────────────────────────────────────┐                            │
│  │  /jtbd-to-stories (ESTA SKILL)         │                            │
│  │                                          │                            │
│  │  • Mapear JTBD → Story                  │     Si falta info:         │
│  │  • Extraer 3 motivaciones              │───▶ /user-story-builder    │
│  │  • Aplicar Wendel                      │     para completar          │
│  │  • Definir Behavior Change             │     conversacionalmente     │
│  │  • Calcular Scoring                    │                             │
│  └─────────────────┬───────────────────────┘                            │
│                    │                                                     │
│                    ▼                                                     │
│  ┌─────────────────────────────────────────┐                            │
│  │  /user-story-quality-coach              │                            │
│  │                                          │                            │
│  │  - Validar scoring 6 dimensiones        │                            │
│  │  - Detectar antipatrones (7)            │                            │
│  │  - Generar reporte de calidad           │                            │
│  │  - Comparar con histórico del equipo    │                            │
│  └─────────────────┬───────────────────────┘                            │
│                    │                                                     │
│                    ▼                                                     │
│              STORIES VALIDADAS                                           │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Cuándo Usar Cada Skill

| Situación | Skill | Acción |
|-----------|-------|--------|
| JTBDs validados con research | `/jtbd-to-stories` | Generar stories directamente |
| PRD sin research previo | `/research-from-prd` → `/jtbd-to-stories` | Pipeline completo |
| Sin PRD, crear story desde cero | `/user-story-builder` | Guía conversacional 6 fases |
| Stories ya generadas, validar | `/user-story-quality-coach` | Scoring + antipatrones |
| Sprint completo, revisar calidad | `/user-story-quality-coach` | Reporte equipo |

### Consistencia Garantizada

| Elemento | Compartido Entre | Definición |
|----------|------------------|------------|
| **Scoring 6 dimensiones** | Todas | Ver `../shared-config.md` |
| **Template JTBD** | Todas | JTBD Reforzado + 3 motivaciones |
| **Wendel Checklist** | Todas | 4 preguntas específicas |
| **7 Antipatrones** | Todas | Misma definición y penalización |
| **Usuarios por dominio** | Todas | Configurable por equipo (ver team-context-template) |
| **Terminología** | Todas | Farolas, Penumbras, JTBD, etc. |

---

## §6 Referencias

- **[prd-structure.md](../prd-quality-guard/references/prd-structure.md)**: Estructura del PRD
- **[jtbd-methodology.md](references/jtbd-methodology.md)**: Metodología JTBD + 3 dimensiones
- **[story-generation.md](references/story-generation.md)**: Template completo de story compatible

---

## §7 Ejemplos de Uso

### Caso 1: JTBDs con evidencia completa (flujo ideal)

**Input:** "Genera stories con los JTBDs del research de Gestión de Oleadas"

**Proceso:**
1. Recibir JTBDs del output de `/research-from-prd`
2. Para cada JTBD:
   - Mapear a formato Story (Como/Cuando/Quiero/Para)
   - Extraer 3 motivaciones de los datos de entrevistas
   - Completar Wendel con datos reales
   - Definir AHORA→NUEVO con métricas validadas
   - Calcular scoring
3. Obtener datos de Fase 2 del PRD (si disponible)
4. Generar stories con template completo

**Output:** Stories con score esperado ≥7 en Dim 1-2 (evidencia real).

### Caso 2: JTBDs con gaps de evidencia

**Input:** JTBDs del research con Research Gap Score = 6 (Amarillo)

**Proceso:**
1. Generar stories documentando gaps de evidencia
2. Marcar dimensiones afectadas
3. Proponer acciones para resolver gaps
4. Score reflejará los gaps honestamente

**Output:** Stories con advertencias + plan de mejora.

### Caso 3: PRD directo (sin research previo)

**Input:** "Genera stories del PRD de HOME de Shop"

**Proceso:**
1. Detectar que no hay JTBDs de research
2. Advertir al usuario:
   > No hay JTBDs validados por research. Para stories de mayor calidad,
   > ejecuta primero `/research-from-prd`. ¿Proceder con datos del PRD?
3. Si el usuario confirma:
   - Extraer JTBDs directamente del PI del PRD
   - Generar stories con advertencia de "sin validación de usuarios"
   - Scoring Dim 1-2 limitado (sin evidencia de entrevistas)
