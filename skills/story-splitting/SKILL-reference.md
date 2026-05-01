# Story Splitting — Reference

Material de referencia para el skill `story-splitting`. El procedimiento core esta en [SKILL.md](SKILL.md).

---

## S1 Detalle de Red Flags por Categoria

### 1.1 Conjunciones coordinantes: "y", "o", "pero", "ni"
- "Los usuarios pueden subir **y** descargar archivos" -> 2 stories
- "El admin puede ver **o** editar usuarios" -> 2 stories

### 1.2 Conectores de accion: "gestionar", "manejar", "administrar", "procesar", "mantener"
- "El admin puede **gestionar** usuarios" -> Oculta crear, editar, eliminar, listar
- "El sistema **procesa** pagos" -> Oculta iniciar, procesar, reembolsar, reportar

### 1.3 Conectores de secuencia: "antes", "despues", "luego", "mientras", "cuando"
- "Guardar trabajo **antes** de enviar" -> 2 stories separadas
- "Procesar pago **y luego** enviar recibo" -> 2 pasos, 2 stories

### 1.4 Indicadores de alcance: "incluyendo", "ademas", "tambien", "con"
- "Notificaciones por email **y** SMS" -> Dividir por canal
- "Reporte **incluyendo** graficos y exportacion" -> Dividir por output

### 1.5 Indicadores de opcion: "o bien", "opcionalmente", "alternativamente"
- "Login con contrasena **o** Google" -> 2 metodos de autenticacion
- "Exportar a CSV **o** PDF" -> 2 stories de formato

### 1.6 Indicadores de excepcion: "excepto", "a menos que", "sin embargo", "aunque"
- "Eliminar cuenta **a menos que** sea admin" -> Caso base + excepcion

---

## S2 Tabla de Decision — Red Flag a Tecnica Recomendada

| Red Flag Detectado | Problema Probable | Tecnica Recomendada | Ejemplo |
|---|---|---|---|
| **"gestionar"** / **"manejar"** | Oculta multiples operaciones CRUD | #1 (Empezar por outputs) + Dividir por accion | "Gestionar usuarios" -> Crear, Editar, Eliminar |
| **"y"** | Multiples features independientes | Dividir por conjuncion | "Subir y descargar" -> (1) Subir, (2) Descargar |
| **"o"** / **"o bien"** | Multiples opciones/alternativas | #5 (Simplificar outputs) o Dividir por opcion | "Exportar CSV o PDF" -> (1) CSV, (2) PDF |
| **"para todos los usuarios"** | Alcance demasiado amplio | #2 (Estrechar segmento) | "Todos exportan" -> (1) Admins, (2) Power users, (3) Todos |
| **"incluyendo"** / **"con"** | Feature bundling | #3 (Extraer utilidad basica) | "Upload con drag-drop y progress" -> (1) Upload basico, (2) Drag-drop, (3) Progress |
| **"antes/despues/luego"** | Pasos secuenciales bundled | Dividir por paso del workflow | "Guardar antes de enviar" -> (1) Guardar, (2) Enviar |
| **Output complejo** (reportes, dashboards) | Demasiados outputs | #1 (Empezar por outputs) | "Reporte financiero con graficos" -> (1) Resumen basico, (2) Graficos |
| **Multiples fuentes de datos** | Complejidad de integracion | #4 (Dummy a dinamico) | "Dashboard de 3 BDs" -> (1) Dummy, (2) BD 1, (3) BD 2+3 |
| **"tiempo real"** / **"automatizado"** | Solucion sobre-ingenieriada | #4 + #9 (Muletas) | "Sync tiempo real" -> (1) Manual, (2) Script, (3) Automatizado |
| **Alcance grande** (subsistema entero) | Demasiado grande conceptualmente | #7 (Ejemplos de utilidad) | "Auth API" -> (1) Auth lectura, (2) Auth escritura |

---

## S3 Ejemplos por Heuristica

### Heuristica #1: Empezar por los Outputs

**Ejemplo:** "Generar reporte de cancelaciones masivas"
- Split 1: "Generar resumen basico (totales por estado)"
- Split 2: "Anadir detalle por pedido"
- Split 3: "Anadir exportacion a CSV"

### Heuristica #2: Estrechar el Segmento de Usuario

**Ejemplo:** "Todos los empleados pueden consultar horarios"
- Split 1: "Empleados de tienda pueden consultar horarios"
- Split 2: "Empleados de almacen pueden consultar horarios"
- Split 3: "Todos los empleados pueden consultar horarios"

### Heuristica #3: Extraer la Utilidad Basica Primero

**Ejemplo:** "Cancelar pedidos masivamente con filtros, validacion y resumen"
- Split 1: "Cancelar pedidos subiendo lista de IDs (sin filtros UI)"
- Split 2: "Anadir filtro por centro/CP"
- Split 3: "Anadir validacion previa de estado"
- Split 4: "Anadir resumen visual de resultados"

### Heuristica #4: Empezar con Dummy, Mover a Dinamico

**Ejemplo:** "Dashboard con metricas de reparto en tiempo real"
- Split 1: "Dashboard con datos estaticos de ejemplo"
- Split 2: "Integrar datos reales de una fuente"
- Split 3: "Hacer refresh automatico"

### Heuristica #5: Simplificar los Outputs

**Ejemplo:** "Generar y enviar informe PDF por email"
- Split 1: "Generar CSV descargable"
- Split 2: "Convertir a formato PDF"
- Split 3: "Enviar por email automaticamente"

### Heuristica #6: Dividir por Capacidad

**Ejemplo:** "Soportar cancelacion masiva de cualquier volumen"
- Split 1: "Soportar hasta 100 pedidos por batch"
- Split 2: "Soportar hasta 1.000 pedidos"
- Split 3: "Soportar volumen ilimitado con procesamiento paralelo"

### Heuristica #7: Dividir por Ejemplos de Utilidad

**Ejemplo:** "Implementar sistema de comunicaciones post-cancelacion"
- Split 1: "Enviar email para pedidos web estandar"
- Split 2: "Enviar SMS para pedidos movil"
- Split 3: "Generar ticket Zendesk para casos NSD"

### Heuristica #8: Separar Aprender de Ganar

**Ejemplo:** "Implementar recomendaciones ML en la tienda"
- Learning: "Spike: Evaluar opciones ML (3 dias max)"
- Earning 1: "Implementar recomendaciones basadas en reglas simples"
- Earning 2: "Evolucionar a modelo ML"

### Heuristica #9: Olvidar el Walking Skeleton — Ponerlo en Muletas

**Ejemplo:** "Sincronizacion automatica de inventario entre sistemas"
- Split 1: "Export/import manual CSV entre sistemas"
- Split 2: "Script semi-automatizado"
- Split 3: "Sincronizacion totalmente automatica"

---

## S4 Template de Output

Para cada story analizada, generar este formato:

```markdown
## Analisis de Splitting — [ID Story]

### Diagnostico

| Aspecto | Resultado |
|---------|-----------|
| Red flags detectados | [lista] |
| Tecnica(s) recomendada(s) | [lista] |
| Splits propuestos | [numero] |
| Estimacion original | [S/M/L/XL] |

### Red Flags Detectados

**[palabra]** en [campo]: "[texto exacto]"
> Problema: [descripcion]
> Tecnica: [numero y nombre]

### Splits Propuestos

#### Split 1 (Empezar aqui)
**Como** [actor]
**Cuando** [trigger]
**quiero** [capacidad minima]
**para** [beneficio]

- **Estimacion:** S (1-2 dias)
- **Valor independiente:** Si — [por que]
- **Tecnica aplicada:** #[N] [nombre]

#### Split 2
[mismo formato]

#### Split 3
[mismo formato]

### Orden de Entrega Recomendado

| Orden | Split | Estimacion | Dependencia |
|-------|-------|------------|-------------|
| 1 | Split 1 | S | Ninguna |
| 2 | Split 2 | M | Split 1 |
| 3 | Split 3 | S | Ninguna |

### Impacto en Scoring

| Dimension | Score Original | Score post-split (Split 1) |
|-----------|---------------|---------------------------|
| Dim 6: Survivable Experiment | X/10 | [nuevo]/10 |
```

---

## S5 Patrones frecuentes

### Red Flags frecuentes en stories grandes

| Patron Comun | Ejemplo | Splitting Recomendado |
|---|---|---|
| "Gestionar X masivamente" | "Cancelar y comunicar masivamente" | Separar cancelacion de comunicacion |
| "Para todos los canales" | "Comunicar por email, SMS y push" | Un canal por story |
| "Con trazabilidad completa" | "Cancelar con resumen e historico" | Cancelar -> Resumen -> Historico |
| "Integracion con X e Y" | "Conectar con dos servicios externos" | Una integracion por story |
| "Para P0/P1/P2" | "Gestionar incidentes P0, P1 y P2" | Empezar con P0 (mas critico) |

### Usuarios validos para splits

Usar los perfiles definidos en `team-context-template.md` del equipo (si existe). Al estrechar segmento, elegir el más crítico primero.

---

## S6 Tono de Coaching

- **Ser directo**: Senalar stories "demasiado grandes" inmediatamente
- **Desafiar**: "Podemos hacerlo mas pequeno?"
- **Provocar**: "Que enviariamos si tuvieramos la mitad del tiempo?"
- Frases utiles:
  - "Que es lo peor que podria pasar si enviamos la version mas simple?"
  - "Podemos evitar hacerlo completamente?"
  - "Eliminemoslo y midamos el impacto"
