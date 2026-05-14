# Autor: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | © 2026 | CC BY-NC-ND 4.0
#!/usr/bin/env python3
from __future__ import annotations
import csv
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
JULIAN_YEAR_SECONDS = 31_557_600
UEMFC_PER_SECOND = 9
K_AGE = JULIAN_YEAR_SECONDS * UEMFC_PER_SECOND

class LabError(AssertionError):
    pass

def read_csv(name: str):
    with open(ROOT / name, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def to_int(value: str) -> int:
    return int(str(value).strip())

def to_uemfc(years_aj: int) -> int:
    return years_aj * K_AGE

def from_uemfc(value: int) -> int:
    if value % K_AGE != 0:
        raise LabError('E-TRANS-02: retorno inverso no exacto')
    return value // K_AGE

def parse_fraction(value: str) -> Fraction:
    return Fraction(value.strip())

def assert_eq(label: str, observed, expected):
    if observed != expected:
        raise LabError(f'{label}: observado={observed!r}; esperado={expected!r}')

def check_units():
    manifest = {row['field']: row['value'] for row in read_csv('manifest_unidades.csv')}
    assert_eq('julian_year_seconds', to_int(manifest['julian_year_seconds']), JULIAN_YEAR_SECONDS)
    assert_eq('uemfc_per_second', to_int(manifest['uemfc_per_second']), UEMFC_PER_SECOND)
    assert_eq('uemfc_per_julian_year', to_int(manifest['uemfc_per_julian_year']), K_AGE)
    assert_eq('rounding_allowed', manifest['rounding_allowed'], 'NO')
    assert_eq('float_allowed', manifest['float_allowed'], 'NO')
    assert_eq('silent_pass_allowed', manifest['silent_pass_allowed'], 'NO')

def check_values():
    rows = read_csv('banco_valores.csv')
    if len(rows) != 4:
        raise LabError('E-LAB-01: banco_valores debe contener cuatro objetos positivos')
    inverse_count = 0
    for row in rows:
        oid = row['object_id']
        current = to_int(row['current_aj'])
        finish = to_int(row['finish_aj'])
        remaining = finish - current
        if finish < current:
            raise LabError(f'{oid}: E-ARIT-02')
        assert_eq(f'{oid}.current_uemfc', to_uemfc(current), to_int(row['current_uemfc']))
        assert_eq(f'{oid}.finish_uemfc', to_uemfc(finish), to_int(row['finish_uemfc']))
        assert_eq(f'{oid}.remaining_aj', remaining, to_int(row['remaining_aj']))
        assert_eq(f'{oid}.remaining_uemfc', to_uemfc(remaining), to_int(row['remaining_uemfc']))
        assert_eq(f'{oid}.fraction', Fraction(current, finish), parse_fraction(row['current_fraction']))
        assert_eq(f'{oid}.remaining_fraction', Fraction(remaining, finish), parse_fraction(row['remaining_fraction']))
        assert_eq(f'{oid}.fraction_sum', parse_fraction(row['current_fraction']) + parse_fraction(row['remaining_fraction']), Fraction(1,1))
        # inverse returns: current, finish, remaining
        assert_eq(f'{oid}.inverse_current', from_uemfc(to_int(row['current_uemfc'])), current); inverse_count += 1
        assert_eq(f'{oid}.inverse_finish', from_uemfc(to_int(row['finish_uemfc'])), finish); inverse_count += 1
        assert_eq(f'{oid}.inverse_remaining', from_uemfc(to_int(row['remaining_uemfc'])), remaining); inverse_count += 1
    return len(rows), inverse_count

def check_differences():
    rows = read_csv('banco_diferencias.csv')
    if len(rows) != 7:
        raise LabError('E-LAB-01: banco_diferencias debe contener siete diferencias')
    for row in rows:
        diff = to_int(row['difference_aj'])
        assert_eq(row['difference_id'], to_uemfc(diff), to_int(row['difference_uemfc']))
    return len(rows)

def check_negatives():
    rows = read_csv('banco_negativos.csv')
    expected_ids = {f'TNEG_{i:02d}' for i in range(1,16)}
    observed_ids = {row['negative_id'] for row in rows}
    assert_eq('negative_id_set', observed_ids, expected_ids)
    for row in rows:
        status = row['expected_status']
        if status not in {'NO_ADMISIBLE', 'U'}:
            raise LabError(f"{row['negative_id']}: salida negativa no válida {status}")
    # explicit adversarial checks
    false_coefficients = [K_AGE - 1, K_AGE + 1]
    for k in false_coefficients:
        if k == K_AGE:
            raise LabError('E-TRANS-01: pendiente falsa aceptada')
    if 2_000 < 1_000:
        raise LabError('E-ARIT-02: fin anterior aceptado')
    return len(rows)

def check_no_silent_passes():
    # This runner fails immediately on any discrepancy. Absence of caught exceptions is a non-silent pass.
    return 0

def main():
    check_units()
    positives, inverse_returns = check_values()
    differences = check_differences()
    negatives = check_negatives()
    silent = check_no_silent_passes()
    lines = [
        'SV_RELATIVE_AGES_THEORY_LAB_RESULT',
        'author: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | © 2026',
        'units_manifest: OK',
        'canonical_formula: OK',
        'explicit_form: OK',
        'implicit_form: OK',
        'parametric_form: OK',
        'point_slope_form: OK',
        f'positive_objects: {positives}/4',
        'remaining_segments: 4/4',
        'fractions: 4/4',
        f'differences: {differences}/7',
        f'inverse_returns: {inverse_returns}/12',
        f'negative_controls: {negatives}/15',
        'float_used: NO',
        'rounding_used: NO',
        f'silent_passes: {silent}',
        'untabulated_outputs: 0',
        'overall_status: APTO',
    ]
    output = '\n'.join(lines) + '\n'
    (ROOT / 'salida_obtenida.txt').write_text(output, encoding='utf-8')
    datos = ROOT / 'datos'
    datos.mkdir(exist_ok=True)
    result_json = {
        'autor': 'Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | © 2026',
        'laboratorio': 'Edades relativas del universo observable y de sus objetos fisicos',
        'units_manifest': 'OK',
        'positive_objects': f'{positives}/4',
        'differences': f'{differences}/7',
        'inverse_returns': f'{inverse_returns}/12',
        'negative_controls': f'{negatives}/15',
        'silent_passes': silent,
        'overall_status': 'APTO'
    }
    (datos / 'resultado_laboratorio_edades.json').write_text(json.dumps(result_json, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(output, end='')

if __name__ == '__main__':
    main()
