# Guión de Entrevista — SearchMO Faceted Search

**Generado por:** `/research source_type=PRD`
**Modo:** Validar (hay hipótesis y evidencia inicial; queremos confirmar JTBDs)
**Perfil objetivo:** Cliente recurrente de la app, ≥3 meses de uso, ≥1 compra/semana
**Muestra:** 5 entrevistas (3 mobile, 2 web)
**Duración:** 30 min/entrevista
**Modalidad:** Presencial cuando sea posible (incluye Field Study), remoto cuando no

---

## Bloque 1: Propósito (interno, no compartir con cliente)

**Entender qué TRABAJO** intenta lograr un cliente recurrente cuando busca un producto en la app, qué fricciones experimenta cuando la query es ambigua, y qué motivaciones (funcional/emocional/social) lo mueven. En particular, validar:

- ¿La frustración con queries ambiguas es real o anecdótica?
- ¿Los clientes ya tienen workarounds (queries más largas, navegación por categorías)?
- ¿La idea de "filtros inline" encaja con su mental model?

## Bloque 2: Plan

### 2a. Plan de observación (Field Study)

**Qué observar (sin intervenir):**
- ¿Cómo escribe la query inicial? ¿Larga o corta?
- ¿Pulsa "buscar" inmediatamente o duda?
- ¿Qué hace cuando ve los resultados? ¿Scrollea? ¿Cambia la query?
- ¿Cuánto tiempo pasa entre query y primer tap en resultado?
- Workarounds: ¿añade marca al principio? ¿escribe categoría primero? ¿usa filtros existentes (si los hay)?

**Dónde:** casa del cliente (preferencia), durante una compra real
**Duración:** 30-45 min observación silenciosa antes de la entrevista

### 2b. Guión de entrevista (Mom Test)

#### Warm-up (3 min)
- "¿Cuándo fue la última vez que hiciste la compra en la app?"
- "¿Qué buscaste? ¿Encontraste todo?"

#### Su vida — comportamiento actual (10 min)
- "Cuéntame cómo haces la compra normalmente. ¿Vas con lista? ¿Vas descubriendo?"
- "Cuéntame la última vez que buscaste algo y NO lo encontraste rápido. ¿Qué pasó?"
- "¿Tienes algún truco para encontrar lo que buscas más rápido?"
- "Cuando no encuentras algo, ¿qué haces? ¿Cambias la query? ¿Vas a categorías? ¿Te rindes?"

#### Validación de JTBDs (8 min)
- "Si te digo 'búsqueda ambigua' — ¿te suena el problema? ¿Cómo lo describirías tú?"
- "[Mostrar mockup A: chips inline + B: sidebar] ¿Cuál te parece más útil? ¿Por qué?"
- *Nota: NO mencionar "facetas" ni "filtros" antes de que el cliente los nombre. Si los nombra, profundizar.*

#### Exploración abierta (5 min)
- "¿Hay algo del buscador que te gustaría que funcionara distinto?"
- "Si pudieras pedirle algo al equipo del buscador, ¿qué sería?"

#### Cierre (3 min)
- Agradecer
- Preguntar si conoce a otros clientes recurrentes que puedan estar disponibles para entrevistar (snowball)

---

## Reglas anti-sesgo (Modo Validar)

- ❌ NO mencionar "facetas", "filtros sugeridos", "categorías inline" antes de que el cliente los nombre
- ❌ NO validar la solución directamente ("¿Te gustaría que apareciera...?")
- ✅ Habla de su vida, no del feature
- ✅ Pregunta por específicos del pasado, no opiniones futuras
- ✅ Si el cliente NO menciona el problema espontáneamente, es un hallazgo válido — registrar
- ✅ Habla menos, escucha más

## Quality Gate

- ≥4/5 entrevistas mencionan algún tipo de fricción con queries ambiguas → CONFIRMA hipótesis
- 4/5 prefieren chips inline a sidebar → CONFIRMA decisión arquitectural
- Si <3/5 mencionan el problema espontáneamente → repensar si el problema es real o solo anecdótico
