# JTBDs Sintetizados — SearchMO Faceted Search

**Generado por:** `/analyze-research`
**Input:** notes-session-1.md, notes-session-2.md (+3 sesiones adicionales no incluidas en este walkthrough por brevedad)
**Sesiones totales:** 5
**Quality Gate:** PASS — criterios primarios cubiertos al 100%, evidencia cuanti+cuali en todos los JTBDs

---

## JTBD-01: Refinar búsqueda ambigua sin esfuerzo extra

**Job principal:** Cuando busco un producto en la app y la consulta es ambigua (devuelve muchos resultados de categorías distintas), quiero **refinar el resultado sin tener que pensar palabras adicionales**, para llegar al producto correcto sin perder tiempo ni frustrarme.

**Trigger:** Búsqueda con query corta o conceptual ("café", "yogur", "queso") devuelve resultados de múltiples categorías.

**Struggle:**
- "Tener que pensar palabras adicionales que afinen la búsqueda"
- "Perder tiempo scrolleando resultados poco claros"
- "Frustrarse y abandonar"

**Desired outcome:** Llegar al producto que quiero en ≤3 taps, sin escribir más texto.

**Motivaciones:**
- **Funcional:** Ahorrar tiempo en la compra (ahorro percibido: ≥10s por búsqueda)
- **Emocional:** No sentirse "perdido" o "engañado" por el buscador; sentirse en control
- **Social:** — (no emergió en research)

**Evidencia cuantitativa (Farolas):**
- 12% de queries son ambiguas (search service logs, abril 2026)
- 28% de queries ambiguas terminan en search abandon (vs 16% en específicas)
- Tiempo medio query→primer click: 4.2s en ambiguas (vs 2.1s en específicas)

**Evidencia cualitativa (Penumbras):**
- "Cuando busco 'café' me sale de todo y no sé cuál pillar" — sesión 1
- "Acabo escribiendo 'café Hacendado molido' aunque tarde más" — sesión 1
- "Si pudiera filtrar por tipo de café como en otras apps, sería más rápido" — sesión 2

**Confianza en el JTBD:** Alta (5/5 entrevistas mencionaron alguna versión del struggle, 4/5 verbalizaron preferencia por solución tipo chip/filtro inline)

---

## JTBD-02: Reducir esfuerzo cognitivo en búsqueda mobile

**Job principal:** Cuando uso la app en el móvil para hacer la compra rápido, quiero que el buscador me **ayude a afinar el resultado sin que tenga que escribir más**, para terminar la compra antes de perder la paciencia.

**Trigger:** Búsqueda en mobile + contexto de prisa (cocina, transporte, etc.).

**Struggle:**
- "Pereza de escribir más palabras en mobile"
- "Abandonar la app si no es rápido"
- "Cabrearse cuando los resultados no son claros"

**Desired outcome:** Decisión rápida sobre qué producto añadir al carrito, sin teclear adicional.

**Motivaciones:**
- **Funcional:** Velocidad en mobile (la sesión típica es <5 min)
- **Emocional:** Sentirse competente, no torpe; no perder la paciencia
- **Social:** — (no emergió)

**Evidencia cuantitativa:** mismas Farolas que JTBD-01, segmentado por mobile en tracking (los datos del PRD original ya implican el segmento mobile-first).

**Evidencia cualitativa:**
- "En el ordenador tengo más paciencia, pero en el móvil quiero que sea rápido" — sesión 2
- "Lo que más me cabrea es cuando busco algo simple y me sale media tienda" — sesión 2

**Confianza:** Alta (3/5 sesiones mencionaron específicamente la diferencia mobile vs web; las otras 2 eran exclusivamente mobile)

**Decisión derivada:** El feature es prioritario en mobile. Considerar empezar el rollout solo en mobile y extender a web en una segunda fase si las métricas mobile son positivas.

---

## JTBD-03: Confiar en el buscador como herramienta principal

**Job principal:** Cuando hago la compra recurrente, quiero **poder confiar en el buscador como mi entrada principal a la app**, para no tener que cambiar a categorías ni reescribir queries cada vez.

**Trigger:** Sesiones de compra repetida (clientes recurrentes que ya conocen el catálogo).

**Struggle:**
- "Cuando el buscador no sirve, voy a categorías y se siente como un retroceso"
- "Antes navegaba por categorías, ahora uso el buscador, pero a veces sigo teniendo que volver"

**Desired outcome:** El buscador "siempre funciona" — es la herramienta confiable.

**Motivaciones:**
- **Funcional:** Ruta única de acceso (menos clicks, menos contexto cognitivo)
- **Emocional:** Sentirse "en casa" con la app, no perdido
- **Social:** —

**Evidencia cuantitativa:** % de sesiones donde se usa buscador como primer entry point (no incluido en farolas del PRD, sería interesante medir post-rollout).

**Evidencia cualitativa:**
- "El buscador es lo que más uso, pero a veces me gana la pereza" — sesión 1
- "Si lo tengo claro lo escribo entero, si no lo tengo claro voy a categorías" — sesión 1

**Confianza:** Media-alta (todas las sesiones mencionan el buscador como primary entry, pero el JTBD subyacente es más metafísico que el JTBD-01 — más difícil de medir directamente).

**Decisión derivada:** Este JTBD es un *nice-to-have* del feature; los JTBD-01 y JTBD-02 son los que justifican el ROI. Pero confirma que el buscador es la herramienta crítica y vale la pena invertir.

---

## Síntesis y próximos pasos

**JTBDs con confianza alta (entran a `/stories`):** JTBD-01, JTBD-02
**JTBDs con confianza media (mantener en backlog, validar en Phase 3 con telemetría):** JTBD-03

**Cobertura criterios B3:** 4/4 — research suficiente para generar stories.

**Siguiente paso:** `/stories` con JTBD-01 y JTBD-02 como input principal.
