# -*- coding: utf-8 -*-
"""
run_all.py — Ejecutor secuencial de los cinco laboratorios canónicos
=====================================================================

Paquete: Laboratorios canónicos de la Teoría general de sucesos generadores y de los protocampos unificados en el Sistema Vectorial SV
DOI del laboratorio: https://doi.org/10.5281/zenodo.19863166
DOI de la publicación principal: https://doi.org/10.17613/177nb-v2465

Ejecuta los cinco laboratorios en orden canónico y devuelve código de
salida distinto de cero si alguno falla.
"""

from __future__ import annotations
import subprocess
import sys
from pathlib import Path

LABS = [
    "lab_01_banco_numerico.py",
    "lab_02_falsacion_canonica.py",
    "lab_03_absorciones_canonicas.py",
    "lab_04_morfismo_dictamen.py",
    "lab_05_configuracion_propia.py",
]


def main() -> int:
    root = Path(__file__).resolve().parent
    print("=" * 79)
    print("EJECUCIÓN SECUENCIAL DEL PAQUETE LABORATORIAL SV")
    print("DOI laboratorio: https://doi.org/10.5281/zenodo.19863166")
    print("Publicación principal: https://doi.org/10.17613/177nb-v2465")
    print("=" * 79)
    for lab in LABS:
        print(f"\n>>> Ejecutando {lab}")
        print("-" * 79)
        result = subprocess.run([sys.executable, str(root / lab)], cwd=str(root))
        if result.returncode != 0:
            print(f"\nFALLO: {lab} terminó con código {result.returncode}")
            return result.returncode
    print("\n" + "=" * 79)
    print("DICTAMEN: los cinco laboratorios han finalizado sin error de ejecución.")
    print("=" * 79)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
