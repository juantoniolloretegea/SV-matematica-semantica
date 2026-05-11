# Runner principal de laboratorios SV-BH9
# Autor: Juan Antonio Lloret Egea
# ORCID: 0000-0002-6634-3351
# Derechos: © 2026. Todos los derechos reservados.
# Licencia: CC BY-NC-ND 4.0
# Fecha: Madrid, 10/05/2026
# Publicación: El agujero negro como cierre interno sin resto exterior formulable


from __future__ import annotations
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from src.validators import run_all


def main() -> int:
    data_path = ROOT / 'datos' / 'sv_bh9_banco.json'
    output_dir = ROOT / 'salidas'
    result = run_all(data_path, output_dir)
    summary = result['summary']
    print('SV-BH9 — laboratorio de agujero negro')
    print(f"Casos totales: {summary['total_cases']}")
    print(f"Casos aptos: {summary['passed']}")
    print(f"Casos fallidos: {summary['failed']}")
    print(f"Errores adversariales detectados: {summary['expected_errors_detected']}")
    print(f"Estado global: {summary['global_status']}")
    return 0 if summary['global_status'] == 'APTO' else 1


if __name__ == '__main__':
    raise SystemExit(main())
