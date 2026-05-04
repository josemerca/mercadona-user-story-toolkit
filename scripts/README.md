# Scripts deterministas

Cálculos puros que NO se delegan al LLM. Las skills llaman a estos scripts vía `Bash` y usan su output directamente.

Patrón Lada Kesseler: `offload-deterministic` — la matemática y los regex son cosa de código, no del modelo.

## Inventario

| Script | Fórmula | Usado por |
|---|---|---|
| `score_story.py` | `mean(D1..D6)` | `jtbd-to-stories`, `user-story-quality-coach`, `user-story-builder` |
| `score_prd.py` | `mean(D1,D2,D3)` + regla `D3<5 → FAIL` | `prd-quality-guard` |
| `score_priority.py` | `V*0.30 + L*0.25 + D*0.20 + R*0.15 + IC*0.10` | `story-prioritization` |
| `gap_score.py` | `críticos*10 + mayores*5 + menores*2 + refinamiento*1` | `prd-quality-guard`, `research-from-prd` |
| `redflags.py` | regex con boundaries, 6 categorías | `story-splitting` |

## Uso desde una skill

Cada script imprime un bloque human-readable a stdout. La skill lo invoca, lee el output y lo cita en su reporte. Ejemplo:

```
python3 scripts/score_story.py --d1=8 --d2=7 --d3=9 --d4=8 --d5=6 --d6=7
```

Output:
```
Score Global: 7.5
Banda: 🟢 Aceptable
Interpretación: Lista para desarrollo con mejoras menores
```

## Tests

```bash
cd scripts && python3 -m unittest discover tests/ -v
```

Cobertura: 32 tests (boundaries, casos críticos, regla D3, regex word-boundary).

## Reglas

1. **Stdlib only** — sin `pip install`, portable.
2. **Lógica pura separada de CLI** — `score()` y `band()` son funciones testables.
3. **Validación en boundary** — rangos validados, errores a stderr con exit code 1.
4. **Una fórmula = un script** — no agregar lógica de presentación.
