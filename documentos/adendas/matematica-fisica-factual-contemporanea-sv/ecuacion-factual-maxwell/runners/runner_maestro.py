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
OUTPUT_DIR = ROOT / 'laboratorios' / 'resultados'
CONTROL = ROOT / 'laboratorios' / 'datos' / 'caso_control_svtresnueve.json'
NEGATIVES = ROOT / 'laboratorios' / 'datos' / 'casos_negativos.json'

if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

from verificador_maxwell_sv import MaxwellLabError, main


def run() -> int:
    try:
        summary = main(CONTROL, NEGATIVES, OUTPUT_DIR)
    except MaxwellLabError as exc:
        print(f"[NO APTO] {exc.code}: {exc.message}")
        if exc.payload:
            print(json.dumps(exc.payload, ensure_ascii=False, indent=2))
        return 1
    print('[APTO] Runner maestro completado sin pases silenciosos.')
    print(f"Bancos positivos: {summary['positive_passed']}/{summary['positive_expected']}")
    print(f"Casos negativos detectados: {summary['negative_caught']}/{summary['negative_total']}")
    return 0


if __name__ == '__main__':
    raise SystemExit(run())
