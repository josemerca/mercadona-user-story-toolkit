# Guía Completa de Jobs To Be Done (JTBD)

## ¿Qué es JTBD?

Jobs To Be Done es una metodología que parte de una premisa simple pero transformadora: **las personas no compran productos, "contratan" soluciones para realizar trabajos específicos en sus vidas**.

### El Origen: La Historia del Batido

Clayton Christensen (Harvard Business School) fue contratado por una cadena de comida rápida para mejorar las ventas de batidos. Después de estudios demográficos sin resultados, observó directamente a los compradores.

**Descubrimiento:** El 40% de los batidos se vendían temprano en la mañana a personas con largo viaje al trabajo. No estaban "comprando un batido" - estaban **contratando** algo que:
- Los mantuviera entretenidos durante el viaje
- Pudieran consumir con una mano mientras conducían
- Les llenara hasta el almuerzo

**El batido competía con bananas, barras de cereales y bagels**, no con otros batidos.

---

## Las Tres Dimensiones de un Job

Un trabajo tiene siempre tres dimensiones:

### 1. Dimensión Funcional
La tarea práctica que necesita realizarse.

**Ejemplo app navegación:** "Llegar a mi destino de la manera más eficiente posible"

### 2. Dimensión Emocional
Cómo quiere sentirse el usuario antes, durante y después.

**Ejemplo:** "Sentirme seguro y confiado de que llegaré a tiempo a mi reunión"

### 3. Dimensión Social
Cómo quiere ser percibido por otros.

**Ejemplo:** "Ser visto como un profesional confiable que siempre llega puntual"

---

## Estructura Completa de un Job

Un job bien definido incluye:

| Componente | Pregunta | Ejemplo |
|------------|----------|---------|
| **Contexto situacional** | ¿Cuándo y dónde surge la necesidad? | "Al planificar la compra semanal, domingo por la noche" |
| **Motivación** | ¿Qué dispara la necesidad? | "El refrigerador está vacío y la familia necesita comida" |
| **Limitaciones** | ¿Qué factores impiden completarlo? | "Tiempo disponible limitado, habilidades culinarias básicas" |
| **Criterios de éxito** | ¿Cómo sabe que completó el job? | "Lista completa, sin olvidar nada, pedido confirmado" |
| **Consecuencias deseadas** | ¿Qué beneficios espera? | "Familia alimentada, ahorro de tiempo, tranquilidad" |

---

## JTBD vs User Stories Tradicionales

### User Story Tradicional
```
Como usuario, quiero poder agregar productos al carrito
para comprarlos más tarde.
```
**Problemas:** Usuario genérico, sin contexto, beneficio vago.

### User Story con JTBD
```
Cuando estoy planificando las compras de la semana mientras
reviso mi refrigerador por la noche,
quiero poder guardar productos que encuentro
para asegurarme de no olvidar nada importante,
optimizar mi tiempo de compra y evitar múltiples viajes
al supermercado durante la semana.
```

**La versión JTBD proporciona:**
- Momento específico de necesidad
- Contexto situacional completo
- Consecuencias negativas a evitar
- Múltiples beneficios esperados

---

## El Formato "Cuando-Quiero-Para"

El formato JTBD reemplaza el tradicional "Como-Quiero-Para":

### Tradicional (centrado en rol)
```
Como [tipo de usuario]
quiero [acción]
para [beneficio]
```

### JTBD (centrado en situación)
```
Cuando [situación específica con contexto]
quiero [capacidad/resultado]
para [outcome medible]
```

### ¿Por qué "Cuando" es mejor que "Como"?

| "Como..." | "Cuando..." |
|-----------|-------------|
| Define un rol estático | Define un momento dinámico |
| Puede ser genérico | Obliga a ser específico |
| No indica cuándo surge la necesidad | Indica el trigger exacto |
| "Como usuario" no dice nada | "Cuando reviso mi nevera vacía" lo dice todo |

---

## Identificando Jobs: La Técnica del "¿Por qué?"

Para encontrar el job real, profundizar 3-5 niveles:

```
"Quiero filtros de búsqueda"
    ↓ ¿Por qué?
"Para encontrar productos más rápido"
    ↓ ¿Por qué es importante?
"Porque ahora tardo mucho y abandono"
    ↓ ¿Qué intentas lograr cuando buscas?
"Completar mi compra semanal sin perder tiempo"
    ↓ JOB REAL
```

### Validar que es un Job (no solución)

| ✅ Es un JOB | ❌ Es una SOLUCIÓN |
|-------------|-------------------|
| "Completar mi compra sin olvidar nada" | "Tener una lista de favoritos" |
| "Sentirme seguro de que llegaré a tiempo" | "Ver el tráfico en tiempo real" |
| "No perder tiempo buscando productos" | "Tener filtros de búsqueda" |

**Test:** Si puedes resolverlo de múltiples formas diferentes, es un job. Si describe una implementación específica, es una solución.

---

## Struggling Moments: Donde Nacen los Jobs

Los "Struggling moments" son situaciones donde el usuario experimenta fricción. Son la fuente de los mejores insights JTBD.

### Señales de Struggling Moment
- "Siempre tengo que..."
- "Es frustrante cuando..."
- "Ojalá pudiera..."
- "No entiendo por qué..."
- "Pierdo mucho tiempo en..."

### Preguntas para Descubrir Struggling Moments
1. "Cuéntame la última vez que hiciste [tarea]. ¿Qué fue lo más difícil?"
2. "¿Qué workarounds has creado para resolver esto?"
3. "¿Cuándo fue la última vez que cambiaste cómo haces [tarea]? ¿Por qué?"

---

## Aplicación en E-commerce (ejemplo)

### Job: Planificación de Compra Semanal

**Contexto:** Domingo noche, planificando la semana, nevera semivacía.

**Struggle:**
- "Siempre olvido algo y tengo que volver a comprar"
- "No sé qué tengo en casa, compro duplicados"
- "Tardo mucho decidiendo qué vamos a comer"

**Dimensiones:**
- **Funcional:** Tener todos los ingredientes para la semana sin olvidar nada
- **Emocional:** Sentir control y tranquilidad, no estrés por la compra
- **Social:** Ser visto como organizado por la familia

**User Story JTBD:**
```
Cuando planifico las comidas de la semana el domingo por la noche
y reviso qué tengo en la nevera,
quiero ver mis productos habituales organizados y poder completar
mi lista sin tener que buscar cada uno,
para asegurarme de no olvidar nada importante,
reducir el tiempo de planificación de 30 a 10 minutos,
y sentirme organizado y en control de la alimentación de mi familia.
```

---

## Errores Comunes

### 1. Confundir Features con Jobs
❌ "El job es tener filtros de búsqueda"
✅ "El job es encontrar productos específicos rápidamente"

### 2. Jobs Demasiado Amplios
❌ "El job es comprar comida"
✅ "El job es completar la compra semanal habitual en menos de 15 minutos"

### 3. Jobs Demasiado Estrechos
❌ "El job es hacer click en el botón de añadir"
✅ "El job es añadir productos al carrito sin interrumpir mi flujo de navegación"

### 4. Olvidar Dimensiones Emocionales/Sociales
❌ Solo describir la tarea funcional
✅ Incluir cómo quiere sentirse y cómo quiere ser percibido

### 5. No Capturar el Contexto
❌ "Cuando un usuario quiere comprar..."
✅ "Cuando un jefe recurrente abre la app durante su pausa del trabajo para hacer la compra semanal..."

---

## Recursos Adicionales

- **Libro:** "Competing Against Luck" - Clayton Christensen
- **Libro:** "Jobs to be Done" - Anthony Ulwick
- **Libro:** "Designing for Behavior Change" - Stephen Wendel
- **Framework:** "Outcome-Driven Innovation" - Tony Ulwick
