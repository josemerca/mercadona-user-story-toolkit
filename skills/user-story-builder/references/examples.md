# Ejemplos de User Stories Excelentes

## Ejemplo 1: Limpieza de Novedades en e-commerce (Score: 9.8/10)

### 🎯 USER STORY

**Como** cliente recurrente de un supermercado online
**Cuando** busco **novedades** en la App para descubrir productos nuevos
**quiero** que lo que veo sean realmente **productos que no existían antes** (ni antes agotados, ni promociones temporales)
**para** confiar en la recomendación, no perder tiempo revisando cosas que ya conozco, y sentirme informado sobre lo nuevo de verdad

---

### 🧩 JTBD REFORZADO

**Job principal:** Descubrir productos genuinamente nuevos que encajen con mis preferencias, sin dedicar tiempo extra a filtrar ruido.

**Struggle:**
- Hoy "Novedades" mezcla productos realmente nuevos con recuperados y campañas temporales
- Esta mezcla diluye el significado de "novedad" y erosiona la confianza
- No existe una vía clara para descubrir qué es realmente nuevo vs qué es familiar

**Trigger:** Quiero ver qué hay de nuevo sin que me "vendan" lo de siempre con otro nombre.

**Desired outcome:** Un catálogo de novedades limpio donde cada producto sea una novedad real.

**Motivación funcional:** Reducir tiempo explorando falsos positivos.

**Motivación emocional:** Sentir que la app me respeta, no me manipula.

**Motivación social:** Poder recomendar novedades reales a amigos/familia.

**Ansiedades:** Sentirse "engañado" si una novedad resulta ser algo que ya conocía.

---

### 👤 USUARIO ESPECÍFICO (Wendel Checklist)

| Pregunta | Respuesta |
|----------|-----------|
| **Experiencia previa** | Usuario recurrente, explora novedades regularmente |
| **Relación con producto** | Confía en la app pero ha notado ruido en la sección "novedades" |
| **Motivación situacional** | Descubrir algo nuevo sin perder tiempo |
| **Impedimento actual** | Mezcla de recuperados/campañas diluye las novedades reales |

---

### 📊 EVIDENCIA

**Cuantitativa:**
- Coeficientes del modelo de scoring:
  - is_new_arrival: +0.15 (sin definición estricta actual)
  - is_recovered: +0.08 (compite con novedades genuinas)
  - is_campaign: +0.05 (relevancia efímera)

**Cualitativa:**
- "¿Por qué me sale como novedad algo que ya conocía?"
- Feedback interno: "Recuperados y campañas no deberían convivir con novedades"

---

### 🔄 CAMBIO DE COMPORTAMIENTO

**AHORA:** El Jefe ve "Novedades" mezcladas con recuperados y campañas → desconfianza, scroll largo, abandono de sección.

**NUEVO:**
- **START:** Confiar en que cada ítem de Novedades es realmente nuevo
- **STOP:** Ignorar la sección por exceso de ruido
- **DIFFERENT:** Interactuar más con Novedades, mayor add-to-cart

**Rango min-target-over:**
| Nivel | Métrica | Valor |
|-------|---------|-------|
| Mínimo | add2cart/impresión en Novedades | +2% |
| Target | add2cart/impresión en Novedades | +5% |
| Over-top | add2cart/impresión en Novedades | +8-10% |

---

### ✅ CRITERIOS DE ACEPTACIÓN

**Dado** que un producto está marcado como novedad
**Cuando** el backend evalúa su elegibilidad
**Entonces** se excluye si is_recovered=true O is_campaign=true

**Dado** que el Jefe accede a la sección Novedades
**Cuando** se renderizan los productos
**Entonces** ninguno debe tener tags de recuperado ni campaña

---

### 🔬 PLAN A/B TEST

- **Plataforma:** GrowthBook
- **Experiment_id:** shop_new_vs_recovered
- **Variantes:**
  - control: novedades_mezcladas
  - variante: novedades_limpias
- **Tráfico:** 50/50
- **Métricas:** add2cart/impresión, CTR sección, tiempo en sección
- **Guardrails:** Sin degradación en GMV global
- **Duración:** 2 semanas

---

## Ejemplo 2: IS-Story - Visualización de Pedidos (Score: 7.1/10)

### 🎯 USER STORY

**Como** Coordinador de Preparación (CP)
**Cuando** gestiono las oleadas de pedidos en el centro de preparación durante picos de demanda
**quiero** visualizar el estado de todos los pedidos de la oleada en tiempo real con indicadores claros de progreso y alertas
**para** identificar cuellos de botella antes de que impacten la entrega, reasignar pickers proactivamente, y mantener el SLA de preparación

---

### 🧩 JTBD REFORZADO

**Job principal (funcional):** Mantener el flujo de preparación dentro de SLA durante picos de demanda.

**Job emocional:** Sentir control sobre la operación, no estar "apagando fuegos" constantemente.

**Job social:** Ser reconocido como un CP que anticipa problemas, no solo reacciona.

**Struggle:**
- Hoy tengo que consultar múltiples pantallas para entender el estado real
- Las alertas llegan tarde, cuando el retraso ya impactó
- No tengo visibilidad de qué picker está saturado hasta que se queja

**Trigger:** Inicio de oleada con >50 pedidos y equipo limitado.

---

### 👤 USUARIO ESPECÍFICO (Wendel Checklist)

| Pregunta | Respuesta |
|----------|-----------|
| **Experiencia previa** | CP con 2+ años de experiencia, conoce bien la operación |
| **Relación con producto** | Usuario diario del sistema de gestión |
| **Motivación situacional** | Evitar retrasos que escalen a incidencias |
| **Impedimento actual** | Información fragmentada y alertas tardías |

---

### 📊 EVIDENCIA

**Cuantitativa:**
- 23% de oleadas con >50 pedidos experimentan retrasos >15 min
- Tiempo medio de detección de cuello de botella: 8 minutos (vs 2 min objetivo)
- 34% de reasignaciones de picker son reactivas (después del retraso)

**Cualitativa:**
- "Cuando veo el problema ya es tarde, el pedido está retrasado"
- "Necesito una vista que me diga dónde intervenir, no solo datos"

---

### 🔄 CAMBIO DE COMPORTAMIENTO

**AHORA:** CP revisa múltiples pantallas → detecta problema tarde → reasigna reactivamente → impacto en SLA

**NUEVO:**
- **START:** Usar dashboard unificado con alertas predictivas
- **STOP:** Consultar múltiples fuentes de información
- **DIFFERENT:** Intervenir proactivamente antes del retraso

**Rango min-target-over:**
| Nivel | Métrica | Valor |
|-------|---------|-------|
| Mínimo | Reducción tiempo detección | -30% (de 8 a 5.6 min) |
| Target | Reducción tiempo detección | -50% (de 8 a 4 min) |
| Over-top | Reducción tiempo detección | -75% (de 8 a 2 min) |

---

## Ejemplo 3: Story con Debilidades (Score: 4.2/10) - ANTES de mejora

### ❌ User Story Original (Problemática)

```
Como usuario,
quiero un botón de filtros en la búsqueda
para poder filtrar los resultados.
```

**Problemas detectados:**
- ❌ "Como usuario" - genérico
- ❌ Beneficio es "tener la feature"
- ❌ Sin contexto situacional
- ❌ Sin behavior change
- ❌ Sin evidencia
- ❌ Sin dimensiones emocionales/sociales

### ✅ User Story Reescrita (JTBD)

```
Como Jefe cazador de ofertas que compra 1-2x/mes buscando los
mejores precios,

Cuando busco un producto específico y obtengo +50 resultados
mezclando marcas, tamaños y precios,

quiero poder filtrar rápidamente por precio (menor a mayor) y
formato/tamaño para encontrar la mejor relación calidad-precio
sin revisar todos los resultados,

para completar mi búsqueda en <2 minutos vs los 6 min actuales,
sentir que estoy haciendo una compra inteligente,
y poder justificar a mi familia que elegí la mejor opción.
```

**Mejoras aplicadas:**
- ✅ Usuario específico con comportamiento definido
- ✅ Contexto situacional claro (trigger)
- ✅ Behavior change cuantificado (6 min → 2 min)
- ✅ Dimensiones funcional + emocional + social
- ✅ Beneficio medible

---

## Patrones de Stories Excelentes

### Patrón 1: Triple Motivación
Siempre incluir las tres dimensiones:
```
para [beneficio funcional],
[beneficio emocional],
y [beneficio social].
```

### Patrón 2: Cuantificación del Cambio
```
Reducir [métrica] de [valor actual] a [valor objetivo] ([X]% mejora)
Rango: Min [A]% / Target [B]% / Over [C]%
```

### Patrón 3: Evidencia Mixta
```
Evidencia cuantitativa:
- [Dato 1 de analytics]
- [Dato 2 de métricas]

Evidencia cualitativa:
- "[Quote textual de usuario]"
- [Observación de comportamiento]
```

### Patrón 4: Criterios Given-When-Then
```
Dado que [precondición específica]
Cuando [acción del usuario]
Entonces [resultado observable y verificable]
```
