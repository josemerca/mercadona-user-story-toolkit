# Notas de Research — Sesión 1

**Fecha:** 2026-04-22
**Tipo:** Observación + Entrevista
**Participante:** Cliente recurrente, mujer, 38 años, mobile-first, 8 meses de uso de la app, compra ~1.5x/semana
**Entorno:** Casa del cliente, comida del miércoles
**Duración:** 50 min (20 observación, 30 entrevista)

---

## Observación (hechos, sin interpretación)

- Empieza la app y va directo al buscador (no a Home)
- Primera búsqueda: "yogur" → ve listado largo, scrollea 3 pantallas → cambia a "yogur natural griego"
- Segunda búsqueda: "café" → ve resultados → duda 4-5 segundos mirando la pantalla → escribe encima "café molido"
- Workaround visible: cuando los resultados no son claros, **añade especificación adicional a la query** sin volver al search bar — escribe encima de la query original
- Tercera búsqueda: "Pan de molde" → resultados claros → tap en primer resultado en <2 segundos
- Cuarta búsqueda: "queso" → ve resultados → mueve el dedo arriba/abajo varios segundos → cierra el buscador → va a categorías → entra en "Lácteos y huevos > Quesos"
- En total: 4 búsquedas en 20 minutos. 2 fueron ambiguas. En las 2 ambiguas hizo workaround o abandonó.

## Entrevista — quotes literales

> "Cuando busco 'café' me sale de todo y no sé cuál pillar"

> "Acabo escribiendo 'café Hacendado molido' aunque tarde más, porque sale más limpio"

> "Si lo tengo claro lo escribo entero, si no lo tengo claro voy a categorías"

> "El buscador es lo que más uso, pero a veces me gana la pereza"

> "[Mostrando mockup chips] Esto está bien, te ayuda. [Mostrando sidebar] Esto se ve más típico de web, en el móvil molesta."

> "Lo que necesito es que cuando escribo poquito el buscador me ayude a afinar, no que tenga yo que hacerlo todo"

## Hechos (resumen, sin interpretación)

- 4 búsquedas, 2 ambiguas, 2 con workaround/abandono
- Workaround principal: extender la query
- Workaround alternativo: ir a categorías
- Reconoce explícitamente el problema cuando se le pregunta
- Prefiere chips a sidebar en mobile

## Aprendizajes (interpretación en clave JTBD)

**JTBD candidato:** "Cuando busco un producto en la app y la consulta es ambigua, quiero refinar el resultado sin tener que pensar más palabras, para llegar al producto correcto sin perder tiempo y sin frustrarme."

- **Trigger:** Búsqueda ambigua devuelve resultados poco claros
- **Struggle:** "Tener que pensar palabras adicionales que afinen", "perder tiempo scrolleando", "frustrarse y abandonar"
- **Desired outcome:** Llegar al producto correcto en menos pasos
- **Motivación funcional:** Ahorrar tiempo en la compra
- **Motivación emocional:** No sentirse "perdida" en el buscador
- **Motivación social:** —

## Validación cruzada con PRD

| Sección PRD | Confirma | Contradice | Emerge nuevo |
|-------------|----------|------------|--------------|
| Hipótesis principal (facetas reducen fricción) | ✓ Cliente reconoce problema y prefiere chips a sidebar | — | — |
| Farolas (28% search abandon en queries ambiguas) | ✓ Indirectamente: 1 abandono en 2 queries ambiguas observadas | — | — |
| Decisión chips vs sidebar | ✓ Cliente prefiere chips explícitamente | — | — |
| Multi-faceta out of scope v1 | — | — | Cliente no mencionó multi-faceta espontáneamente — sostiene la decisión |
| — | — | — | **Workaround "extender query"**: el cliente ya hace algo parecido a aplicar una faceta. Las facetas son explícitas pero el comportamiento subyacente ya existe. Refuerza la hipótesis. |
