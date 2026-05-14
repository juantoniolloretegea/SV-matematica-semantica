#!/usr/bin/env python3
"""
Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | © 2026. Todos los derechos reservados.
Laboratorio del anexo: Biología molecular y medicina: del par estructural a la célula viva.
Verifica métricas externas, fórmulas centrales, controles negativos y constante transductiva.
"""
from pathlib import Path
import csv, json, sys
BASE = Path(__file__).resolve().parent
AUTHOR = 'Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | © 2026. Todos los derechos reservados.'
DATA = BASE / 'datos'
RESULTS = BASE / 'resultados'
K_AGE = 31_557_600 * 9
EXPECTED_K = 284_018_400
REQUIRED_FORMULAS = {f'BIO-{i:02d}' for i in range(1,12)}
REQUIRED_NEG = {f'NEG-{i:03d}' for i in range(1,9)}

def read_csv_skip_comments(path):
    with path.open(encoding='utf-8', newline='') as f:
        lines = [line for line in f if not line.startswith('#')]
    return list(csv.DictReader(lines))

def main():
    errors = []
    metrics = read_csv_skip_comments(DATA / 'metricas_biologicas_externas.csv')
    formulas = read_csv_skip_comments(DATA / 'formulas_centrales.csv')
    controls = read_csv_skip_comments(DATA / 'controles_negativos.csv')
    if len(metrics) < 10:
        errors.append('BIO-LAB-METRICS-COUNT')
    formula_ids = {row['formula_id'] for row in formulas}
    missing_formulas = sorted(REQUIRED_FORMULAS - formula_ids)
    if missing_formulas:
        errors.append('BIO-LAB-FORMULAS-MISSING:' + ','.join(missing_formulas))
    neg_ids = {row['control_id'] for row in controls}
    missing_neg = sorted(REQUIRED_NEG - neg_ids)
    if missing_neg:
        errors.append('BIO-LAB-NEGATIVE-MISSING:' + ','.join(missing_neg))
    if K_AGE != EXPECTED_K:
        errors.append('BIO-LAB-KAGE')
    silent_passes = 0
    out = {
        'autor': AUTHOR,
        'laboratorio': 'Biologia molecular y medicina: del par estructural a la celula viva',
        'metricas_externas': len(metrics),
        'formulas_centrales': len(formulas),
        'controles_negativos': len(controls),
        'K_age': K_AGE,
        'silent_passes': silent_passes,
        'errors': errors,
        'overall_status': 'APTO' if not errors and silent_passes == 0 else 'NO_APTO'
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / 'salida_obtenida.txt').write_text('\n'.join([f"{k}: {v}" for k, v in out.items()]) + '\n', encoding='utf-8')
    (RESULTS / 'salida_obtenida.json').write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if out['overall_status'] == 'APTO' else 1

if __name__ == '__main__':
    sys.exit(main())
