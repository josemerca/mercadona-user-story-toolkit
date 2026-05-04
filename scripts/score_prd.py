#!/usr/bin/env python3
"""Calcula Score Global de un PRD (3 dimensiones) y decide gate.

Fórmula: mean(D1, D2, D3), redondeado a 1 decimal.
Regla especial: D3 < 5 → FAIL automático (Discovery insuficiente).
Gate: 0-4 FAIL / 5-6 CONDICIONAL / 7-8 PASS / 9-10 PASS (modelo).
"""
import argparse
import sys


def score(d1: float, d2: float, d3: float) -> float:
    return round((d1 + d2 + d3) / 3, 1)


def gate(d1: float, d2: float, d3: float) -> tuple[str, str, str]:
    s = score(d1, d2, d3)
    if d3 < 5:
        return "FAIL", "🔴 FAIL automático", f"D3={d3} (<5): Discovery insuficiente"
    if s < 5:
        return "FAIL", "🔴 FAIL", "Requiere reescritura significativa"
    if s < 7:
        return "CONDICIONAL", "🟡 CONDICIONAL", "Iterar secciones débiles antes de research"
    if s < 9:
        return "PASS", "🟢 PASS", "Listo para research"
    return "PASS", "⭐ PASS (modelo)", "Referencia para otros PRDs"


def validate(dims: list[float]) -> str | None:
    for i, d in enumerate(dims, 1):
        if not 0 <= d <= 10:
            return f"D{i} fuera de rango: {d} (debe estar entre 0 y 10)"
    return None


def main() -> int:
    p = argparse.ArgumentParser(description="Score y gate de un PRD (3D).")
    p.add_argument("--d1", type=float, required=True, help="D1: Completitud EAC (0-10)")
    p.add_argument("--d2", type=float, required=True, help="D2: Claridad EFC + Métricas (0-10)")
    p.add_argument("--d3", type=float, required=True, help="D3: Rigor Discovery + Scope (0-10)")
    args = p.parse_args()
    err = validate([args.d1, args.d2, args.d3])
    if err:
        print(f"Error: {err}", file=sys.stderr)
        return 1
    s = score(args.d1, args.d2, args.d3)
    decision, label, reason = gate(args.d1, args.d2, args.d3)
    print(f"Score Global: {s}")
    print(f"Gate: {label}")
    print(f"Decisión: {decision}")
    print(f"Razón: {reason}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
