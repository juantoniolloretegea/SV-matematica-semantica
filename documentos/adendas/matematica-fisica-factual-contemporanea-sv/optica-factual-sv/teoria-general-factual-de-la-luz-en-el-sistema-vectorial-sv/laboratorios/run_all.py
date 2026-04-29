#!/usr/bin/env python3
"""
run_all.py — Ejecutor directo complementario de los 22 laboratorios de luz factual SV.

Este ejecutor importa cada módulo y llama a su función run() dentro del mismo
proceso. No sustituye a runner.py, que conserva la política estricta de
subprocess/fail-fast. Se proporciona como vía reproducible simple para entornos
donde el cierre de intérprete o la gestión de subprocess interfieran con NumPy.

Exit 0 sólo si los 22 laboratorios devuelven rc=0.
"""
from __future__ import annotations
import importlib.util
import json
import os
import sys
import traceback
from pathlib import Path

BASE = Path(__file__).resolve().parent
CONFIG = BASE / "runner_config.json"

def cargar_modulo(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem + "_direct", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"No se pudo cargar módulo: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def main() -> int:
    print("=" * 74)
    print("RUN_ALL — ejecución directa de laboratorios de luz factual SV")
    print("=" * 74)
    with open(CONFIG, "r", encoding="utf-8") as f:
        cfg = json.load(f)
    orden = cfg.get("orden_laboratorios", [])
    if len(orden) != 22:
        print(f"FALLO: se esperaban 22 laboratorios; hay {len(orden)}.")
        return 1
    for idx, entry in enumerate(orden, start=1):
        lab_id = entry["id"]
        archivo = entry["archivo"]
        path = BASE / archivo
        print(f"\n[{idx:02d}/22] {lab_id} — {archivo}")
        if not path.is_file():
            print(f"FALLO: archivo inexistente: {path}")
            return 1
        try:
            mod = cargar_modulo(path)
            if not hasattr(mod, "run"):
                print(f"FALLO: {archivo} no declara run().")
                return 1
            rc = mod.run()
            if rc != 0:
                print(f"FALLO: {lab_id} devuelve rc={rc}.")
                return 1
        except Exception as exc:
            print(f"FALLO: excepción en {lab_id}: {type(exc).__name__}: {exc}")
            traceback.print_exc()
            return 1
    print("\n" + "=" * 74)
    print("RUN_ALL COMPLETADO — 22/22 laboratorios PASADO.")
    print("=" * 74)
    return 0

if __name__ == "__main__":
    sys.exit(main())
