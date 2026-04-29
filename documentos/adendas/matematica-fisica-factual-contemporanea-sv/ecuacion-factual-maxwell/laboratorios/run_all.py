#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ejecutor reproducible de los laboratorios Maxwell-SV.

Ejecuta el caso positivo de control y el banco de ataques negativos.
Termina con exit 0 sólo si los 21 bancos positivos pasan y los 15 casos
negativos son detectados con el código esperado.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from modulo.verificador_maxwell_sv import MaxwellLabError, main


def run() -> int:
    root = Path(__file__).resolve().parent
    control = root / "datos" / "caso_control_svtresnueve.json"
    negatives = root / "datos" / "casos_negativos.json"
    output = root / "resultados"
    try:
        summary = main(control, negatives, output)
    except MaxwellLabError as exc:
        print(f"[NO APTO] {exc.code}: {exc.message}", file=sys.stderr)
        if exc.payload:
            print(json.dumps(exc.payload, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1
    print("[APTO] Laboratorios Maxwell-SV completados sin pases silenciosos.")
    print(f"Bancos positivos: {summary['positive_passed']}/{summary['positive_expected']}")
    print(f"Casos negativos detectados: {summary['negative_caught']}/{summary['negative_total']}")
    print(f"Resultados escritos en: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
