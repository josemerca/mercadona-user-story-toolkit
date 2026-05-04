#!/usr/bin/env python3
"""Calcula Priority Score de una story (5 lentes ponderadas).

Fórmula: V*0.30 + L*0.25 + D*0.20 + R*0.15 + IC*0.10
Cada lente puntúa de 1 a 5. Priority Score resultante en rango 1.0-5.0.
"""
import argparse
import sys

WEIGHTS = {
    "value": 0.30,
    "learning": 0.25,
    "dependencies": 0.20,
    "risk": 0.15,
    "complexity": 0.10,
}


def score(value: float, learning: float, dependencies: float, risk: float, complexity: float) -> float:
    s = (
        value * WEIGHTS["value"]
        + learning * WEIGHTS["learning"]
        + dependencies * WEIGHTS["dependencies"]
        + risk * WEIGHTS["risk"]
        + complexity * WEIGHTS["complexity"]
    )
    return round(s, 2)


def band(s: float) -> str:
    if s >= 4.0:
        return "🔥 Top — entregar primero"
    if s >= 3.0:
        return "🟢 Alta — siguiente batch"
    if s >= 2.0:
        return "🟡 Media — backlog medio"
    return "⚪ Baja — backlog largo"


def validate(values: dict[str, float]) -> str | None:
    for name, v in values.items():
        if not 1 <= v <= 5:
            return f"{name} fuera de rango: {v} (debe estar entre 1 y 5)"
    return None


def main() -> int:
    p = argparse.ArgumentParser(description="Priority Score (5 lentes ponderadas).")
    p.add_argument("--value", type=float, required=True, help="Value 1-5 (peso 30%)")
    p.add_argument("--learning", type=float, required=True, help="Learning 1-5 (peso 25%)")
    p.add_argument("--dependencies", type=float, required=True, help="Dependencies 1-5 (peso 20%)")
    p.add_argument("--risk", type=float, required=True, help="Risk of Delay 1-5 (peso 15%)")
    p.add_argument("--complexity", type=float, required=True, help="Inv. Complexity 1-5 (peso 10%)")
    args = p.parse_args()
    values = {
        "value": args.value,
        "learning": args.learning,
        "dependencies": args.dependencies,
        "risk": args.risk,
        "complexity": args.complexity,
    }
    err = validate(values)
    if err:
        print(f"Error: {err}", file=sys.stderr)
        return 1
    s = score(**values)
    print(f"Priority Score: {s}")
    print(f"Banda: {band(s)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
