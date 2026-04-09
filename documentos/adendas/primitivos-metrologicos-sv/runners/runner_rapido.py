# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026

"""Runner rápido: ejecuta una muestra mínima de control."""
from __future__ import annotations

import importlib
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

TARGETS = [
    'laboratorios.lab_01_tiempo_ue_mfc',
    'laboratorios.lab_03_masa_ufm',
    'laboratorios.lab_07_unidades_derivadas',
]


def main() -> int:
    for name in TARGETS:
        mod = importlib.import_module(name)
        result = mod.run().to_dict()
        print(f"{name}: {result['status']} | ok={result['passed']}")
        if result['status'] != 'CONFIRMA' or result['passed'] is not True:
            return 34
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
