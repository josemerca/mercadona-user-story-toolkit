# Principios Mom Test (Rob Fitzpatrick)

## Las 3 Reglas aplicadas a research desde PRD

### Regla 1: Habla de su vida, no del PRD
- NUNCA mostrar ni mencionar el PRD al usuario
- NUNCA preguntar "¿Te parece que el proceso actual tiene problemas?"
- NUNCA validar datos del PRD directamente ("El PRD dice que tardas 8 min, ¿es cierto?")
- El PRD es tu mapa interno. El usuario es el territorio.

### Regla 2: Pregunta por específicos del pasado
- "Cuéntame la última vez que..." > "¿Cómo sueles hacer...?"
- "¿Qué pasó?" > "¿Qué crees que pasaría?"
- "¿Cuándo fue?" > "¿Con qué frecuencia?"

### Regla 3: Habla menos, escucha más
- Objetivo: usuario habla 80%, tú 20%
- Los silencios son tu amigo. Espera 3-5 segundos antes de la siguiente pregunta.
- "Ajá", "Interesante", "Cuéntame más" son tus mejores herramientas.

---

## Tipos de Bad Data en contexto PRD

### 1. Cumplidos
**Señales:** "El proceso está bien", "La herramienta funciona", "No tengo quejas"

**Riesgo PRD:** Si preguntas "¿Qué tal el proceso de [X]?", los usuarios darán cumplidos para no ser negativos.

**Técnica:** Deflectar y volver a hechos.
```
Usuario: "El proceso va bien, no me quejo"
Tú: "Me alegro. Cuéntame cómo fue ayer. ¿A qué hora empezaste?"
```

### 2. Fluff (información vacía)
**Formas:**
- **Genéricos:** "Siempre hago lo mismo", "Normalmente no hay problemas"
- **Promesas:** "Si tuviera X, lo usaría", "Seguro que funcionaría"
- **Hipotéticos:** "Podría ser útil", "Quizás ayudaría"

**Riesgo PRD:** Las Farolas del PF pueden tentarte a preguntar genéricos ("¿Es lento el proceso?") que generan fluff.

**Técnica:** Anclar a específicos.
```
Usuario: "Siempre tardo lo mismo"
Tú: "¿Cuánto tardaste ayer? Cuéntame paso a paso"
```

### 3. Ideas y Feature Requests
**Señales:** "Deberíais hacer...", "Estaría bien si...", "¿Habéis pensado en...?"

**Riesgo PRD:** El usuario puede proponer soluciones que coinciden o no con el PRD. No importa. Tu trabajo es entender el PROBLEMA.

**Técnica:** Excavar la motivación.
```
Usuario: "Deberíais poner un dashboard en tiempo real"
Tú: "Interesante. ¿Qué información necesitas ver urgentemente? ¿Cómo la consigues ahora?"
```

---

## Preguntas Gold para descubrir JTBDs

### Para descubrir el Job (qué intenta hacer)
- "Cuéntame la última vez que [proceso]. Desde el principio."
- "¿Cómo fue? ¿Qué fue lo primero que hiciste?"
- "¿Qué estabas intentando conseguir?"

### Para descubrir el Struggle (fricción actual)
- "¿Qué es lo más pesado de [proceso]?"
- "¿Qué has intentado para hacerlo más fácil?"
- "¿Cuándo fue la última vez que algo salió mal?"

### Para descubrir el Trigger (cuándo surge)
- "¿Qué te hizo empezar [proceso] en ese momento?"
- "¿Siempre es por la misma razón?"
- "¿Qué estabas haciendo justo antes?"

### Para descubrir Desired Outcome (qué quiere lograr)
- "¿Cómo sabes que [proceso] salió bien?"
- "¿Qué significaría para ti que esto funcionara perfecto?"
- "La última vez que salió realmente bien, ¿qué fue diferente?"

### Para descubrir Motivación Emocional
- "¿Cómo te sientes cuando [situación]?"
- "¿Qué te preocupa cuando haces [proceso]?"
- "Si esto saliera perfecto, ¿cómo sería tu día?"

### Para descubrir Motivación Social
- "¿Quién se da cuenta si haces esto bien?"
- "¿Cómo se entera tu jefe/equipo?"
- "¿Qué piensan los demás cuando [situación]?"

---

## Señales de Validación vs Invalidación

### El problema es REAL cuando:
- Han buscado activamente soluciones (workarounds)
- Están pagando (tiempo, esfuerzo) por resolverlo
- Ocurre frecuentemente y recientemente
- Muestran emoción al describirlo
- Dan ejemplos con fechas y detalles específicos
- Múltiples usuarios describen lo mismo sin ser preguntados

### El problema NO es real cuando:
- Responden con genéricos ("sí, a veces")
- No han buscado soluciones
- No dan ejemplos concretos
- Lo describen sin emoción
- Solo 1 de N usuarios lo menciona
- Lo mencionan solo cuando preguntas directamente

---

## Reglas de Oro

1. **Las opiniones son inútiles** — Solo los hechos importan
2. **Todo lo del futuro es mentira optimista** — La gente sobreestima lo que haría
3. **Los cumplidos son el oro del tonto** — Brillan pero no valen nada
4. **La gente sabe sus problemas pero no las soluciones** — Tu trabajo es entender el problema
5. **Si no han buscado soluciones, no les importa lo suficiente** — El comportamiento pasado predice el futuro
6. **Cuanto más hablas, peor lo estás haciendo** — El silencio es tu amigo
7. **Los datos del PRD son hipótesis, no verdades** — Hasta que un usuario real los confirme
