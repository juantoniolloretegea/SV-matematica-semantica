#!/usr/bin/env python3
# © 2026. Todos los derechos reservados.
#
# Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 20/04/2026 | Advertencia: Esta publicación está protegida por CEDRO y su aplicación en el campo de la Física, así como cualquier forma de explotación, reproducción o uso por parte de empresas, queda sujeta al copyright del autor y a los términos de la licencia indicada; la reproducción, distribución, comunicación pública o transformación de esta obra solo puede ser realizada con la autorización de sus titulares, salvo excepción prevista por la ley, y cualquier uso comercial sin autorización expresa queda prohibido y supeditado estrictamente al licenciamiento permitido.
#
# Warning: This publication is protected by CEDRO. Its application in the field of Physics, as well as any form of exploitation, reproduction, or use by corporate entities, is strictly subject to the author’s copyright and the terms of the license indicated; any reproduction, distribution, public communication, or transformation of this work requires authorization from the rightsholders, except as provided by law, and any commercial use without express written consent is prohibited and strictly subject to permitted licensing.
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = ROOT / 'laboratorios' / 'modulo'
CONTROL = ROOT / 'laboratorios' / 'datos' / 'caso_control_svtresnueve.json'
RESULT = ROOT / 'laboratorios' / 'resultados' / 'runner_rapido.json'
STDOUT = ROOT / 'laboratorios' / 'resultados' / 'runner_rapido.py.stdout.txt'

if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

from verificador_maxwell_sv import MaxwellLabError, RIGHTS, load_json, verify_case


def run() -> int:
    essential = ['BANCO_01', 'BANCO_03', 'BANCO_04', 'BANCO_09', 'BANCO_10', 'BANCO_13', 'BANCO_19', 'BANCO_20', 'BANCO_21']
    try:
        control = load_json(CONTROL)
        results = verify_case(control)
    except MaxwellLabError as exc:
        print(f"[NO APTO] {exc.code}: {exc.message}")
        return 1

    selected = [r for r in results if r.bank_id in essential]
    if len(selected) != len(essential):
        print('[NO APTO] El runner rápido no ha reunido el núcleo completo exigido del laboratorio.')
        return 1
    if not all(r.passed for r in selected):
        print('[NO APTO] El runner rápido ha detectado al menos un banco crítico fallido.')
        return 1

    payload = {
        'derechos_y_autoria': {'copyright': RIGHTS},
        'banks': [r.__dict__ for r in selected],
        'count': len(selected),
        'dictamen': 'APTO'
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding='utf-8')
    STDOUT.write_text("\n".join([
        RIGHTS,
        '',
        '[APTO] Runner rápido completado sin pases silenciosos.',
        f"Bancos críticos: {len(selected)}/{len(essential)}",
        ''
    ]), encoding='utf-8')
    print('[APTO] Runner rápido completado sin pases silenciosos.')
    return 0


if __name__ == '__main__':
    raise SystemExit(run())
