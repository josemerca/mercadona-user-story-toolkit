#!/usr/bin/env python3
"""Calcula Gap Score (severidad ponderada de gaps detectados en PRD/Research).

Fórmula: críticos*10 + mayores*5 + menores*2 + refinamiento*1.
Sin techo definido — interpretar por bandas relativas.
"""
import argparse
import sys


def score(criticos: int, mayores: int, menores: int, refinamiento: int) -> int:
    return criticos * 10 + mayores * 5 + menores * 2 + refinamiento * 1


def band(s: int, criticos: int) -> str:
    if criticos > 0:
        return "🔴 Bloqueante — resolver gaps críticos antes de continuar"
    if s >= 20:
        return "🟠 Alto — research adicional recomendado"
    if s >= 10:
        return "🟡 Medio — completar gaps mayores"
    if s >= 5:
        return "🟢 Bajo — refinar antes de avanzar"
    return "⭐ Mínimo — listo para avanzar"


def validate(values: dict[str, int]) -> str | None:
    for name, v in values.items():
        if v < 0:
            return f"{name} no puede ser negativo: {v}"
    return None


def main() -> int:
    p = argparse.ArgumentParser(description="Gap Score (severidad ponderada).")
    p.add_argument("--criticos", type=int, required=True, help="Nº gaps críticos")
    p.add_argument("--mayores", type=int, required=True, help="Nº gaps mayores")
    p.add_argument("--menores", type=int, required=True, help="Nº gaps menores")
    p.add_argument("--refinamiento", type=int, required=True, help="Nº gaps de refinamiento")
    args = p.parse_args()
    values = {
        "criticos": args.criticos,
        "mayores": args.mayores,
        "menores": args.menores,
        "refinamiento": args.refinamiento,
    }
    err = validate(values)
    if err:
        print(f"Error: {err}", file=sys.stderr)
        return 1
    s = score(**values)
    print(f"Gap Score: {s}")
    print(f"Interpretación: {band(s, args.criticos)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
