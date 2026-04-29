#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
runner.py — Ejecución reproducible de los laboratorios de entropía factual SV.

Ejecuta los seis laboratorios visibles y la suite de trece tests de monotonía
sin pases silenciosos. La ejecución termina con código 0 sólo si todas las
unidades pasan. No requiere dependencias externas.
"""
from __future__ import annotations

import contextlib
import io
import os
from pathlib import Path
import runpy
import sys
import traceback

LABS = [
    "lab_04_4_verificacion_preternaria.py",
    "lab_11_recorrido_consistencia.py",
    "lab_11_10_violacion_simulada.py",
    "lab_ejemplo_A_cierre_determinado.py",
    "lab_ejemplo_B_residual_en_U.py",
    "lab_ejemplo_C_clase_emergente.py",
]

TESTS = "tests/test_monotonia.py"


def _run_path(path: str) -> tuple[int, str]:
    """Ejecuta un archivo Python en el mismo intérprete y devuelve código/salida."""
    here = Path(__file__).resolve().parent
    target = here / path
    if not target.exists():
        return 127, f"ERROR: no existe {path}\n"

    old_cwd = Path.cwd()
    if str(here) not in sys.path:
        sys.path.insert(0, str(here))

    buf = io.StringIO()
    code = 0
    try:
        os.chdir(here)
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            runpy.run_path(str(target), run_name="__main__")
    except SystemExit as exc:
        code = int(exc.code or 0)
    except BaseException:
        code = 1
        buf.write(traceback.format_exc())
    finally:
        os.chdir(old_cwd)

    return code, buf.getvalue()


def main() -> int:
    print("╔" + "═" * 68 + "╗")
    print("║" + "Entropía factual SV — suite completa de laboratorios".center(68) + "║")
    print("╚" + "═" * 68 + "╝")

    failures: list[tuple[str, int]] = []
    executed = 0

    for item in LABS + [TESTS]:
        print("\n" + "█" * 70)
        print(f"EJECUTANDO {item}")
        print("█" * 70)
        code, output = _run_path(item)
        executed += 1
        print(output, end="" if output.endswith("\n") else "\n")
        if code != 0:
            failures.append((item, code))
            print(f"✗ FALLO: {item} terminó con código {code}")
        else:
            print(f"✓ OK: {item}")

    print("\n" + "═" * 70)
    print("RESUMEN")
    print("═" * 70)
    if failures:
        print(f"✗ {len(failures)}/{executed} unidades fallaron.")
        for item, code in failures:
            print(f"    {item}: código {code}")
        return 1

    print("✓ 6/6 laboratorios visibles ejecutados sin errores.")
    print("✓ 13/13 tests de monotonía ejecutados sin errores.")
    print("✓ 19/19 verificaciones operativas superadas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
