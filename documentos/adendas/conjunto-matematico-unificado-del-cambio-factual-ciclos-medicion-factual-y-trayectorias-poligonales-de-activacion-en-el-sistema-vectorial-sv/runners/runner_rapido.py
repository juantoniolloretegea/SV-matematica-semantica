# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026

"""
Runner rápido del Hito 3.

Ejecuta un subconjunto crítico de laboratorios, pero con la misma disciplina
policial del runner maestro: si algo pasa que no debía pasar, corta con código.
"""
from __future__ import annotations

import importlib
import sys
import traceback
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from core.assertion_registry import ASSERTIONS
from core.error_codes import ERR_IMPORT, ERR_RUN_EXCEPTION, OK, describe
from core.runner_support import normalize_result, validate_result
from core.sv_lab_core import to_pretty_json

FAST = [
    'laboratorios.lab_01_cmodcf_validacion_minima',
    'laboratorios.lab_08_tpa_identidades_emergentes',
    'laboratorios.lab_11_tpa_isoperimetria_refutada',
    'laboratorios.lab_12_tpa_isoenergia_y_descriptor',
    'laboratorios.lab_15_kepler_segunda_ley_contraste',
]


def fail(code: int, message: str, details: dict[str, object] | None = None) -> int:
    payload = {
        'ok': False,
        'exit_code': code,
        'description': describe(code),
        'message': message,
        'details': details or {},
    }
    print(to_pretty_json(payload), file=sys.stderr)
    return code


def main() -> int:
    index = {f"laboratorios.{item['laboratorio']}": item for item in ASSERTIONS}
    for mod_name in FAST:
        try:
            mod = importlib.import_module(mod_name)
        except Exception as exc:
            return fail(ERR_IMPORT, f'No se pudo importar {mod_name}.', {
                'module': mod_name,
                'exception': repr(exc),
                'traceback': traceback.format_exc(),
            })

        try:
            result = normalize_result(mod.run())
        except Exception as exc:
            return fail(ERR_RUN_EXCEPTION, f'El laboratorio {mod_name} lanzó una excepción.', {
                'module': mod_name,
                'exception': repr(exc),
                'traceback': traceback.format_exc(),
            })

        issue = validate_result(result, str(index[mod_name]['estado_esperado']))
        if issue is not None:
            code, details = issue
            details = {'module': mod_name, **details}
            return fail(code, f'El laboratorio rápido {mod_name} devolvió un estado indebido.', details)

        print(f"{result['lab_id']:8s} | {result['status']:8s} | {result['title']}")
    return OK


if __name__ == '__main__':
    raise SystemExit(main())
