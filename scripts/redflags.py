#!/usr/bin/env python3
"""Detecta red flags lingüísticos en una user story (story-splitting).

6 categorías:
1. Conjunciones coordinantes
2. Conectores de acción
3. Conectores de secuencia
4. Indicadores de alcance
5. Indicadores de opción
6. Indicadores de excepción

Lee texto desde --text "..." o stdin. Hace match palabra completa, case-insensitive.
"""
import argparse
import re
import sys

CATEGORIES = {
    "1. Conjunciones coordinantes": ["y", "o", "pero", "ni"],
    "2. Conectores de acción": [
        "gestionar",
        "manejar",
        "administrar",
        "procesar",
        "mantener",
    ],
    "3. Conectores de secuencia": [
        "antes",
        "después",
        "luego",
        "mientras",
        "cuando",
    ],
    "4. Indicadores de alcance": ["incluyendo", "además", "también", "con"],
    "5. Indicadores de opción": [
        "o bien",
        "opcionalmente",
        "alternativamente",
    ],
    "6. Indicadores de excepción": [
        "excepto",
        "a menos que",
        "sin embargo",
        "aunque",
    ],
}


def detect(text: str) -> dict[str, list[str]]:
    findings: dict[str, list[str]] = {}
    lower = text.lower()
    for cat, words in CATEGORIES.items():
        hits = []
        for w in words:
            pattern = r"\b" + re.escape(w.lower()) + r"\b"
            if re.search(pattern, lower):
                hits.append(w)
        if hits:
            findings[cat] = hits
    return findings


def main() -> int:
    p = argparse.ArgumentParser(description="Detector de red flags lingüísticos.")
    p.add_argument("--text", type=str, help="Texto de la story. Si se omite, lee de stdin.")
    args = p.parse_args()
    text = args.text if args.text is not None else sys.stdin.read()
    if not text.strip():
        print("Error: texto vacío", file=sys.stderr)
        return 1
    findings = detect(text)
    if not findings:
        print("Sin red flags detectados.")
        print("Recomendación: la story no requiere splitting por red flags lingüísticos.")
        return 0
    print(f"Red flags detectados: {sum(len(v) for v in findings.values())}")
    for cat, hits in findings.items():
        print(f"  {cat}: {', '.join(hits)}")
    print()
    print("Recomendación: consultar tabla de decisión Red Flag → Técnica en SKILL-reference.md §S2.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
