#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Autor: Juan Antonio Lloret Egea
# ORCID: 0000-0002-6634-3351
# Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
# Publicación: IA eñ™ — La Biblia de la IA™
# ISSN: 2695-6411
# Licencia: CC BY-NC-ND 4.0
# Madrid, 2026
"""
Runner determinista del Banco de Contraste de Admisibilidad Material H–He (BCAM-HHe).
Materializa la matriz BCAM-HHe en ejecución reproducible: aplica reglas declaradas, conserva salidas explícitas y permite verificar esperado/obtenido.
"""
from __future__ import annotations
import argparse, csv, json, hashlib
from pathlib import Path
from datetime import datetime, timezone

ALLOWED = {"ADMISION", "DEFECTO", "U", "APTO-M", "APTO-C", "APTO-I", "NO-APTO"}
REQUIRED_FIELDS = ["id", "familia", "objeto", "dominio", "condicion_aplicada", "regla", "residual_controlado", "salida_esperada", "motivo"]
METADATA = {
    "autor": "Juan Antonio Lloret Egea",
    "orcid": "0000-0002-6634-3351",
    "institucion": "Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)",
    "publicacion": "IA eñ™ — La Biblia de la IA™",
    "issn": "2695-6411",
    "licencia": "CC BY-NC-ND 4.0",
    "lugar_fecha": "Madrid, 2026",
}


def b(v) -> bool:
    return str(v).strip().lower() in {"1", "true", "sí", "si", "yes"}


def num(v, default=0.0) -> float:
    try:
        if v is None or str(v).strip() == "":
            return default
        return float(v)
    except ValueError:
        return default


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def cps_decision(row: dict) -> str:
    if not b(row.get('in_omega')):
        return 'NO-APTO'
    delta_en = num(row.get('delta_en'))
    m_joint = num(row.get('m_joint'))
    rho = num(row.get('rho'))
    ip_suma = num(row.get('ip_suma'))
    if ip_suma > 1800:
        return 'NO-APTO'
    if delta_en <= 0.50 and m_joint >= 0.40 and rho <= 1.40:
        return 'APTO-M'
    if delta_en <= 1.70:
        return 'APTO-C'
    return 'APTO-I'


def decide(row: dict) -> str:
    rule = row.get('regla', '').strip()
    if rule == 'CPS':
        return cps_decision(row)
    if rule == 'DEFECTO':
        return 'DEFECTO' if b(row.get('defecto')) else 'U'
    if rule == 'U':
        return 'U' if b(row.get('u_flag')) else 'DEFECTO'
    if rule == 'ADMISION_H':
        ok = all(b(row.get(k)) for k in ['has_domain','has_frontier','has_trace','has_return','no_plane_confusion','h_admit'])
        return 'ADMISION' if ok else 'U'
    if rule == 'ADMISION_HE':
        ok = all(b(row.get(k)) for k in ['has_domain','has_frontier','has_trace','has_return','no_plane_confusion','he_stabilization'])
        return 'ADMISION' if ok else 'U'
    if rule == 'ADMISION_HHE':
        ok = all(b(row.get(k)) for k in ['has_domain','has_frontier','has_trace','has_return','no_plane_confusion','h_admit','he_stabilization','hhe_pair'])
        return 'ADMISION' if ok else 'U'
    if rule == 'ADMISION_SOL':
        ok = all(b(row.get(k)) for k in ['has_domain','has_frontier','has_trace','has_return','no_plane_confusion','solar_reference']) and not b(row.get('sol_origin_claim'))
        return 'ADMISION' if ok else 'DEFECTO'
    if rule == 'ADMISION_SV443_BASE':
        ok = all(b(row.get(k)) for k in ['has_domain','has_frontier','has_trace','has_return','no_plane_confusion','in_omega','empirical_detected'])
        return 'ADMISION' if ok else 'U'
    return 'DEFECTO'


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--cases', default='datos/bcam_hhe_casos.csv')
    ap.add_argument('--out', default='salidas/bcam_hhe_salidas_obtenidas.csv')
    ap.add_argument('--summary', default='', help='Ruta opcional para guardar resumen JSON. Si se omite, no se crea archivo de resumen.')
    args = ap.parse_args()
    cases_path = Path(args.cases)
    out_path = Path(args.out)
    summary_path = Path(args.summary) if args.summary else None if args.summary else None
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with cases_path.open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    output_rows = []
    incomplete = 0
    out_of_catalog_expected = 0
    out_of_catalog_obtained = 0
    matches = 0
    mismatches = 0
    empty_outputs = 0

    for row in rows:
        missing = [k for k in REQUIRED_FIELDS if not str(row.get(k, '')).strip()]
        if missing:
            incomplete += 1
        expected = row.get('salida_esperada','').strip()
        if expected not in ALLOWED:
            out_of_catalog_expected += 1
        obtained = decide(row)
        if not obtained:
            empty_outputs += 1
        if obtained not in ALLOWED:
            out_of_catalog_obtained += 1
        match = (expected == obtained) and expected in ALLOWED and obtained in ALLOWED and not missing
        if match:
            matches += 1
        else:
            mismatches += 1
        output_row = dict(METADATA)
        output_row.update({
            'id': row.get('id',''),
            'familia': row.get('familia',''),
            'regla': row.get('regla',''),
            'residual_controlado': row.get('residual_controlado',''),
            'salida_esperada': expected,
            'salida_obtenida': obtained,
            'coincide': '1' if match else '0',
            'campos_faltantes': ';'.join(missing),
            'motivo': row.get('motivo','')
        })
        output_rows.append(output_row)

    with out_path.open('w', newline='', encoding='utf-8') as f:
        fieldnames = list(METADATA.keys()) + ['id','familia','regla','residual_controlado','salida_esperada','salida_obtenida','coincide','campos_faltantes','motivo']
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader(); w.writerows(output_rows)

    counts_by_output = {}
    for r in output_rows:
        counts_by_output[r['salida_obtenida']] = counts_by_output.get(r['salida_obtenida'], 0) + 1

    summary = {
        'metadata': METADATA,
        'runner': 'runner_bcam_hhe.py',
        'run_utc': datetime.now(timezone.utc).isoformat(),
        'cases_file': str(cases_path),
        'output_file': str(out_path),
        'sha256_cases': sha256(cases_path),
        'sha256_output': sha256(out_path),
        'total_cases': len(rows),
        'complete_rows': len(rows) - incomplete,
        'incomplete_rows': incomplete,
        'empty_outputs': empty_outputs,
        'out_of_catalog_expected': out_of_catalog_expected,
        'out_of_catalog_obtained': out_of_catalog_obtained,
        'matches_expected_obtained': matches,
        'mismatches_expected_obtained': mismatches,
        'counts_by_obtained_output': counts_by_output,
        'allowed_outputs': sorted(ALLOWED),
        'verdict': 'APTO' if (incomplete == 0 and empty_outputs == 0 and out_of_catalog_expected == 0 and out_of_catalog_obtained == 0 and mismatches == 0) else 'NO_APTO'
    }
    if summary_path is not None:
        summary_path.parent.mkdir(parents=True, exist_ok=True)
        with summary_path.open('w', encoding='utf-8') as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary['verdict'] == 'APTO' else 2

if __name__ == '__main__':
    raise SystemExit(main())
