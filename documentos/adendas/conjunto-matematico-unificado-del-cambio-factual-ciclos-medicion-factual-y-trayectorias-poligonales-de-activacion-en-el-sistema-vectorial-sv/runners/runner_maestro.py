# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026

"""
Runner maestro del Hito 3.

Uso local:
    python runners/runner_maestro.py

Efectos:
- valida registro, autoría y consistencia de la suite,
- ejecuta todos los laboratorios registrados,
- corta con códigos de salida explícitos si algo pasa que no debe pasar,
- escribe informe JSON en ../reporte_laboratorios_hito3.json.
"""
from __future__ import annotations

import importlib
import json
import sys
import traceback
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from core.assertion_registry import ASSERTIONS
from core.error_codes import (
    OK,
    ERR_IMPORT,
    ERR_REPORT_WRITE,
    ERR_RUN_EXCEPTION,
    describe,
)
from core.runner_support import (
    ensure_author_metadata,
    normalize_result,
    validate_registry,
    validate_result,
)
from core.sv_lab_core import to_pretty_json


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
    registry_issue = validate_registry(ASSERTIONS, BASE_DIR)
    if registry_issue is not None:
        code, details = registry_issue
        return fail(code, 'Fallo de registro del Hito 3.', details)

    metadata_issue = ensure_author_metadata(BASE_DIR)
    if metadata_issue is not None:
        code, details = metadata_issue
        return fail(code, 'Falta la línea obligatoria de autoría en la suite.', details)

    results = []
    summary = {'CONFIRMA': 0, 'REFUTA': 0, 'ABIERTO': 0}

    for item in ASSERTIONS:
        module_name = f"laboratorios.{item['laboratorio']}"
        try:
            module = importlib.import_module(module_name)
        except Exception as exc:
            return fail(ERR_IMPORT, f'No se pudo importar {module_name}.', {
                'module': module_name,
                'exception': repr(exc),
                'traceback': traceback.format_exc(),
            })

        try:
            raw_result = module.run()
        except Exception as exc:
            return fail(ERR_RUN_EXCEPTION, f'El laboratorio {module_name} lanzó una excepción.', {
                'module': module_name,
                'exception': repr(exc),
                'traceback': traceback.format_exc(),
            })

        try:
            result = normalize_result(raw_result)
        except Exception as exc:
            from core.error_codes import ERR_INVALID_RESULT
            return fail(ERR_INVALID_RESULT, f'El laboratorio {module_name} devolvió un resultado no normalizable.', {
                'module': module_name,
                'exception': repr(exc),
            })

        validation_issue = validate_result(result, str(item['estado_esperado']))
        if validation_issue is not None:
            code, details = validation_issue
            details = {'module': module_name, **details}
            return fail(code, f'El laboratorio {module_name} devolvió un estado indebido.', details)

        summary[str(result['status'])] += 1
        results.append({
            'assertion_id': item['id'],
            'section': item['seccion'],
            'expected': item['estado_esperado'],
            'result': result,
        })

    out = {'ok': True, 'exit_code': OK, 'summary': summary, 'results': results}
    out_path = BASE_DIR / 'reporte_laboratorios_hito3.json'
    try:
        out_path.write_text(to_pretty_json(out), encoding='utf-8')
    except Exception as exc:
        return fail(ERR_REPORT_WRITE, 'No se pudo escribir el informe JSON final.', {
            'path': str(out_path),
            'exception': repr(exc),
        })

    print('== HITO 3 — MATRIZ RESUMIDA ==')
    for entry in results:
        r = entry['result']
        print(f"{entry['assertion_id']:24s} | esperado={entry['expected']:8s} | estado={r['status']:8s} | ok={r['passed']}")
    print()
    print(f"Informe escrito en: {out_path}")
    return OK


if __name__ == '__main__':
    raise SystemExit(main())
