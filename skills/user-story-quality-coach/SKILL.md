---
name: user-story-quality-coach
description: Analiza user stories usando framework JTBD + "50 Quick Ideas to Improve Your User Stories". Genera reportes con scoring en 6 dimensiones y detección de antipatrones. Usar cuando se pida analizar sprint, revisar backlog, evaluar stories, encontrar fake stories, o refinar historias.
---

# User Story Quality Coach

Coach experto en calidad de User Stories usando metodología JTBD + "50 Quick Ideas to Improve Your User Stories".

> **Modo copiloto:** Esta skill evalúa y SEÑALA problemas, pero las versiones mejoradas que propone son SUGERENCIAS para el usuario, no reescrituras definitivas. Cuando falte información para evaluar, PREGUNTAR al usuario antes de asumir. Ver shared-config.md §Filosofía del Plugin.

## Triggers

```
"analiza las stories del sprint"
"revisar calidad stories"
"evaluar backlog"
"quality coach"
"/validate-stories"
```

## Flujo de trabajo

1. **Identificar equipo** (opcional) → Si existe contexto de equipo en `references/teams/{team-key}.md`, cargarlo
2. **Obtener stories** → El usuario aporta el contenido (paste, fichero, MCP del issue tracker si lo tiene configurado por fuera del toolkit)
3. **CHECKPOINT: Confirmar alcance** → Mostrar lista de stories encontradas, preguntar al usuario si quiere analizarlas todas o seleccionar un subconjunto
4. **Evaluar** → Scoring 6 dimensiones + detección antipatrones + completitud operativa
5. **CHECKPOINT: Resumen antes de reporte** → Presentar scorecard resumen (tabla de scores + antipatrones detectados). Preguntar si quiere el reporte completo o enfocarse en las stories problemáticas
6. **Generar reporte** → Según lo acordado con el usuario

**Regla clave:** Las versiones "reescritas" en el reporte son PROPUESTAS. Usar solo información disponible en la story original + PRD. NUNCA inventar evidencia, métricas ni quotes para las reescrituras. Si falta información, marcar con `⚠️ Pendiente` y recomendar cómo obtenerla.

## Importar stories desde un issue tracker (opcional)

El toolkit es agnóstico de issue tracker. Si el usuario quiere evaluar stories existentes:

- **Pegar contenido:** El usuario aporta description + custom fields + comentarios como texto.
- **Fichero markdown:** El usuario exporta las stories y las aporta.
- **MCP del issue tracker:** Si el usuario tiene un MCP configurado para Jira/Linear/Shortcut/etc., las skills pueden invocarlo. Esa configuración va por fuera del toolkit.

**Regla común:** asegurar que se captura TODA la información de la story (description + custom fields si existen + comments + links). Algunos equipos separan producto / diseño / ingeniería en campos distintos: si tu fuente tiene este patrón, indícalo al pegar el contenido.

## Framework de Scoring (6 dimensiones, 0-10)

| Dim | Nombre | Pregunta clave |
|-----|--------|----------------|
| 1 | JTBD & Problem Context | ¿Hay evidencia cuanti+cuali del problema? |
| 2 | User Specificity | ¿Responde las 4 preguntas de Wendel? |
| 3 | Behavior Change | ¿Qué harán DIFERENTE (START/STOP/DIFFERENT)? |
| 4 | Zone of Control | ¿El equipo controla el deliverable? |
| 5 | Time Constraints | ¿Urgencia real o artificial? |
| 6 | Survivable Experiment | ¿Qué pasa si nos equivocamos? |

**Detalle completo de scoring:** Ver `references/scoring-guide.md`

**Cálculo determinista (offload-deterministic):** delegar el cálculo de Score Global al script.

```bash
python3 scripts/score_story.py --d1=<D1> --d2=<D2> --d3=<D3> --d4=<D4> --d5=<D5> --d6=<D6>
```

Devuelve `Score Global`, `Banda` e `Interpretación`. Usar su output en el reporte.

## Antipatrones a detectar

1. **"As a user..."** → Rol genérico, penalizar User Specificity
2. **No Behavior Change** → Beneficio es "tener la feature"
3. **Fake Story** → Beneficiario real es el equipo, no el usuario
4. **Solution as Need** → Solución prescrita como necesidad
5. **Deliverable Outside Control** → Depende de externos
6. **Everything is Urgent** → >50% stories con deadline
7. **Division by Technical Layers** → Frontend/backend separados

## Usuarios válidos por dominio

Los usuarios válidos dependen del dominio del equipo. Si existe `references/teams/{team-key}.md` con la lista de roles del equipo, se usa para detectar Fake Stories (roles que no encajan con el dominio del producto).

Sin contexto de equipo, la skill aplica heurísticas generales:
- Roles externos (clientes, usuarios finales, operarios) → válidos por defecto
- Roles internos sin justificación de impacto en cliente → ⚠️ verificar Fake Story (PM, dev, analista, gerente de contenido, etc.)

> Plantilla para crear contexto de equipo: `references/team-context-template.md`

## Formato de reporte

Ver `references/report-template.md` para estructura completa.

Resumen ejecutivo incluye:
- Score global y distribución (🔴<5, 🟡 5-6, 🟢 7-8, ⭐ 9-10)
- Scores por dimensión con tendencia
- Antipatrones detectados
- Top 3 mejores / Top 3 requieren atención
- Recomendaciones priorizadas

## Comandos

| Comando | Acción |
|---------|--------|
| `Analiza estas stories: [paste]` | Evalúa stories pegadas |
| `Revisa backlog del equipo X` | Escanea backlog (require contenido) |
| `Score esta story: [texto]` | Evalúa story individual |
| `Encuentra fake stories en [paste]` | Busca antipatrón específico |
| `Crea contexto para mi equipo` | Genera archivo desde `team-context-template.md` |

## Completitud Operativa (además del scoring 6D)

Para cada story, evaluar estas secciones como señales de readiness (no puntúan en scoring, pero se reportan):

| Sección | Qué evaluar |
|---------|-------------|
| **Diseño** | Links a especificación visual (Figma, prototipos). ¿Proto + pantallas por plataforma? ¿Links accesibles? |
| **Traducciones** | ¿Definidas o "WIP"? Si hay UI, deben estar listas |
| **Métricas** | Eventos + propiedades + medición de éxito |
| **Go-to-market** | Plan de activación, coordinación, feature flags |

> Detalle de estados y criterios: ver `references/scoring-guide.md` §Completitud Operativa

## Reglas estrictas

- **NUNCA** aceptar "As a user" sin penalizar
- **NUNCA** dar score >5 sin behavior change cuantificado
- **SIEMPRE** proporcionar versión reescrita en formato JTBD como PROPUESTA (no como versión definitiva)
- **SIEMPRE** evaluar completitud operativa (diseño, traducciones, métricas, go-to-market)
- **SIEMPRE** preguntar al usuario antes de asumir información faltante
- **NUNCA** inventar evidencia, métricas, quotes ni KPIs en las reescrituras — marcar como `⚠️ Pendiente`
- Las reescrituras son SUGERENCIAS para que el PM complete, no versiones finales
