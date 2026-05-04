#!/usr/bin/env python3
"""Calcula Score Global de una user story (6 dimensiones).

Fórmula: mean(Dim1..Dim6), redondeado a 1 decimal.
Bandas: 🔴 0-4 / 🟡 5-6 / 🟢 7-8 / ⭐ 9-10.
"""
import argparse
import sys


def score(d1: float, d2: float, d3: float, d4: float, d5: float, d6: float) -> float:
    return round((d1 + d2 + d3 + d4 + d5 + d6) / 6, 1)


def band(s: float) -> tuple[str, str]:
    if s < 5:
        return "🔴 Deficiente", "Requiere reescritura completa"
    if s < 7:
        return "🟡 Necesita mejora", "Refinamiento necesario antes de desarrollo"
    if s < 9:
        return "🟢 Aceptable", "Lista para desarrollo con mejoras menores"
    return "⭐ Excelente", "Modelo a seguir para el equipo"


def validate(dims: list[float]) -> str | None:
    for i, d in enumerate(dims, 1):
        if not 0 <= d <= 10:
            return f"Dimensión {i} fuera de rango: {d} (debe estar entre 0 y 10)"
    return None


def main() -> int:
    p = argparse.ArgumentParser(description="Score Global de una user story (6D).")
    for i, name in enumerate(
        ["jtbd", "user", "behavior", "control", "time", "experiment"], 1
    ):
        p.add_argument(f"--d{i}", type=float, required=True, help=f"Dim {i}: {name} (0-10)")
    args = p.parse_args()
    dims = [getattr(args, f"d{i}") for i in range(1, 7)]
    err = validate(dims)
    if err:
        print(f"Error: {err}", file=sys.stderr)
        return 1
    s = score(*dims)
    label, interp = band(s)
    print(f"Score Global: {s}")
    print(f"Banda: {label}")
    print(f"Interpretación: {interp}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
