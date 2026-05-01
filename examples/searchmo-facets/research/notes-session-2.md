# Notas de Research — Sesión 2

**Fecha:** 2026-04-23
**Tipo:** Entrevista (sin observación previa — sesión remota)
**Participante:** Cliente recurrente, hombre, 45 años, mobile + web, 14 meses de uso, compra ~2x/semana
**Entorno:** Llamada por video, despacho del cliente
**Duración:** 30 min

---

## Entrevista — quotes literales

> "Si pudiera filtrar por tipo de café como en otras apps, sería más rápido"

> "Cuando no encuentro lo que quiero rápido, me voy y compro otra cosa"

> "El truco que tengo es: pongo la marca primero y luego el producto, así sale más concreto. Por ejemplo, 'Hacendado leche desnatada' en lugar de 'leche desnatada'"

> "En el ordenador tengo más paciencia, pero en el móvil quiero que sea rápido — si no, dejo la app abierta y vuelvo más tarde"

> "Lo que más me cabrea es cuando busco algo simple y me sale media tienda"

> "[Mostrando los dos mockups] Los chips por arriba están bien, lo otro es muy de PC, en móvil sobra"

## Hechos (resumen, sin interpretación)

- Reconoce explícitamente el patrón de queries ambiguas problemáticas
- Workaround: añadir marca al principio de la query
- Diferencia experiencia mobile vs web: en mobile pide más rapidez, en web tolera más fricción
- Coincide con sesión 1 en preferencia chips > sidebar
- Cuando no encuentra, abandona y compra otra cosa o pospone — comportamiento confirmatorio del search abandon medido

## Aprendizajes (interpretación en clave JTBD)

**JTBD reforzado** (mismo job que sesión 1, con matiz adicional):

- **Trigger** (refinado): Búsqueda ambigua **en mobile** devuelve resultados poco claros
- **Struggle** (nuevo): "Pereza de escribir más en mobile" + "abandono cuando no es rápido"
- **Motivación social** (nueva): —
- **Anxiedad detectada:** "Cabrearse" cuando los resultados no son claros — reactivo emocional fuerte
- **Conexión con feature:** la propuesta de chips inline encaja con la expectativa de "rápido en mobile" — los chips son menos esfuerzo que escribir más

## Validación cruzada con PRD

| Sección PRD | Confirma | Contradice | Emerge nuevo |
|-------------|----------|------------|--------------|
| Hipótesis principal | ✓ Confirma; el cliente verbaliza directamente la propuesta ("filtrar por tipo de café") | — | — |
| Mobile-first decisión | ✓ Mobile demanda más rapidez explícitamente | — | — |
| Decisión chips vs sidebar | ✓ Confirma | — | — |
| — | — | — | **Diferencia mobile vs web emocional**: en web hay más tolerancia. Sugiere que el feature es PRIORITARIO en mobile, secundario en web. Implementación debe priorizar mobile. |
| Farolas (search abandon 28%) | ✓ "Compro otra cosa o pospone" es consistente con search abandon | — | — |
