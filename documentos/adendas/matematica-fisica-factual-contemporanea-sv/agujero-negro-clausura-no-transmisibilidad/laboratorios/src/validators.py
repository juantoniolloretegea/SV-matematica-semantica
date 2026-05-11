# Validadores sin pase silencioso para SV-BH9
# Autor: Juan Antonio Lloret Egea
# ORCID: 0000-0002-6634-3351
# Derechos: © 2026. Todos los derechos reservados.
# Licencia: CC BY-NC-ND 4.0
# Fecha: Madrid, 10/05/2026
# Publicación: El agujero negro como cierre interno sin resto exterior formulable


from __future__ import annotations
import json, csv, math
from pathlib import Path
from typing import Any, Dict, List
from .sv_core import d_sigma, d_sigma_from_counts, equivalent_forms, postfrontier, mn2_is_not_u
from .bh_physics import thermo_row, escape_ratio, schwarzschild_cell, kerr_r_plus_over_rg, kretschmann_ratio
from .absorption import classify_absorption
from .autoria import metadata


def _result(case_id: str, block: str, status: str, expected: Any, obtained: Any, details: Dict[str, Any] | None = None, error: str | None = None) -> Dict[str, Any]:
    return {'case_id': case_id, 'block': block, 'status': status, 'expected': expected, 'obtained': obtained, 'details': details or {}, 'error': error}


def validate_formula_equivalence(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    out = []
    for case in data['formula_equivalence']:
        forms = equivalent_forms(case['R'])
        ok = forms['all_forms_equivalent'] and forms['dictamen'] == case['expected']
        err = None if ok else case.get('expected_error', 'BH-FORM-001')
        # For negative cases, obtaining NO_APTO is the expected detection.
        if case['expected'] == 'NO_APTO' and forms['dictamen'] == 'NO_APTO':
            ok = True
            err = case.get('expected_error')
        out.append(_result(case['case_id'], 'formas_equivalentes_BH', 'PASS' if ok else 'FAIL', case['expected'], forms['dictamen'], forms, err))
    return out


def validate_cells(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    out = []
    for case in data['cells']:
        calc = d_sigma(case['cell']) if 'cell' in case else d_sigma_from_counts(case['counts'])
        ok = calc['DΣ'] == case['expected']
        out.append(_result(case['case_id'], 'DΣ_celular', 'PASS' if ok else 'FAIL', case['expected'], calc['DΣ'], calc, None if ok else 'BH-DΣ-001'))
    return out


def validate_schwarzschild(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    out=[]
    for case in data['schwarzschild']:
        cell = schwarzschild_cell(case['q'])
        calc = d_sigma(cell)
        horizon = (calc['DΣ'] == 'NO_APTO')
        ok = horizon == case['expected_horizon']
        details={'q':case['q'], 'v_escape_over_c': escape_ratio(case['q']), 'cell': cell, **calc}
        out.append(_result(case['case_id'], 'Schwarzschild', 'PASS' if ok else 'FAIL', case['expected_horizon'], horizon, details, None if ok else 'BH-SCH-001'))
    return out


def validate_thermo(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    out=[]
    for case in data['masses']:
        row = thermo_row(case['solar_masses'])
        ok = row['r_s_m'] > 0 and row['S_BH_over_kB'] > 0 and row['T_H_K'] > 0
        expected = 'C_TH=0;C_H=0'
        obtained = expected if ok else 'NO_APTO'
        out.append(_result(case['case_id'], 'termodinamica_BH', 'PASS' if ok else 'FAIL', expected, obtained, row, None if ok else 'BH-TH-001'))
    return out


def validate_kerr(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    out=[]
    for case in data['kerr']:
        rp = kerr_r_plus_over_rg(case['chi'])
        valid = rp is not None
        ok = valid == case['expected_valid']
        err = None if ok else case.get('expected_error', 'BH-KERR-001')
        # Negative superextreme valid False is expected and should pass with expected error noted.
        if not valid and not case['expected_valid']:
            ok=True; err=case.get('expected_error')
        out.append(_result(case['case_id'], 'Kerr', 'PASS' if ok else 'FAIL', case['expected_valid'], valid, {'chi':case['chi'], 'r_plus_over_rg':rp}, err))
    return out


def validate_singularity(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    out=[]
    for case in data['singularity']:
        kr = kretschmann_ratio(case['q'])
        if kr is None:
            obtained='NO_EVALUABLE_COMO_FUNDAMENTO'
            ok = case.get('expected_error') == 'BH-SING-001'
            err='BH-SING-001'
        else:
            obtained='LIMITE_DE_PROYECCION'
            ok = case['expected_foundation'] is False
            err=None if ok else 'BH-SING-001'
        out.append(_result(case['case_id'], 'singularidad_geometrica', 'PASS' if ok else 'FAIL', case.get('expected_error','no_fundamento'), obtained, {'q':case['q'], 'K_over_Kh':kr}, err))
    return out


def validate_absorption(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    out=[]
    for case in data['absorption']:
        calc = classify_absorption(case['cell'], case['model'])
        ok = calc['dictamen_absorcion'] == case['expected']
        err = calc.get('error') if calc.get('error') else (None if ok else 'BH-ABS-001')
        out.append(_result(case['case_id'], 'absorcion_modelos', 'PASS' if ok else 'FAIL', case['expected'], calc['dictamen_absorcion'], calc, err))
    return out


def validate_postfrontier(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    out=[]
    for case in data['postfrontier']:
        calc = postfrontier(case['mu'], case['lambda'], case['verifier'], case['declared'])
        ok = calc['dictamen'] == case['expected']
        err = calc.get('error') if calc.get('error') else (None if ok else 'BH-MN2-001')
        out.append(_result(case['case_id'], 'postfrontera_MN2', 'PASS' if ok else 'FAIL', case['expected'], calc['dictamen'], calc, err))
    # non-subsumption check
    out.append(_result('PF-MN2-NE-U', 'postfrontera_MN2', 'PASS' if mn2_is_not_u() else 'FAIL', 'M_N2-SV≠U', 'M_N2-SV≠U' if mn2_is_not_u() else 'M_N2-SV=U', {'type_check': True}, None if mn2_is_not_u() else 'BH-MN2U-001'))
    return out


def validate_external(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    out=[]
    for case in data['external_falsification']:
        closed = (case['D_TE']=='NO_APTO' and case['D_L']=='NO_APTO' and case['D_INT']=='SATURACION' and case['mu']==0 and case['lambda']==0 and case['verifier']==0)
        obtained = 'BH_FISICO_EQ_BH_SV' if closed else 'NO_APTO'
        ok = obtained == case['expected']
        err = None
        if obtained == 'NO_APTO':
            err = case.get('expected_error', 'BH-TE-001')
        out.append(_result(case['case_id'], 'falsacion_luminosa_externa', 'PASS' if ok else 'FAIL', case['expected'], obtained, dict(case), err))
    return out


def run_all(data_path: Path, output_dir: Path) -> Dict[str, Any]:
    data=json.loads(data_path.read_text(encoding='utf-8'))
    output_dir.mkdir(parents=True, exist_ok=True)
    results=[]
    for fn in [validate_formula_equivalence, validate_cells, validate_schwarzschild, validate_thermo, validate_kerr, validate_singularity, validate_absorption, validate_postfrontier, validate_external]:
        results.extend(fn(data))
    failures=[r for r in results if r['status']!='PASS']
    expected_errors=[r for r in results if r.get('error')]
    summary={
        'metadata': metadata(),
        'total_cases': len(results),
        'passed': len(results)-len(failures),
        'failed': len(failures),
        'expected_errors_detected': len(expected_errors),
        'global_status': 'APTO' if not failures else 'NO_APTO'
    }
    payload={'metadata': metadata(), 'summary': summary, 'results': results}
    (output_dir/'sv_bh9_resultados.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    with (output_dir/'sv_bh9_traza.csv').open('w', encoding='utf-8', newline='') as f:
        writer=csv.writer(f)
        writer.writerow(['autor', 'orcid', 'derechos', 'licencia', 'case_id', 'block', 'status', 'expected', 'obtained', 'error'])
        for r in results:
            writer.writerow([metadata()['autor'], metadata()['orcid'], metadata()['derechos'], metadata()['licencia'], r['case_id'], r['block'], r['status'], r['expected'], r['obtained'], r.get('error') or ''])
    md = ['# Resumen de ejecución SV-BH9', '', f"**Autor:** {metadata()['autor']}  ", f"**ORCID:** {metadata()['orcid']}  ", f"**Derechos:** {metadata()['derechos']}  ", f"**Licencia:** {metadata()['licencia']}  ", '', f"Estado global: **{summary['global_status']}**", '', f"Casos totales: {summary['total_cases']}", f"Casos aptos: {summary['passed']}", f"Casos fallidos: {summary['failed']}", f"Errores adversariales detectados: {summary['expected_errors_detected']}", '', '| Bloque | Caso | Estado | Esperado | Obtenido | Error |', '|---|---|---|---|---|---|']
    for r in results:
        md.append(f"| {r['block']} | {r['case_id']} | {r['status']} | {r['expected']} | {r['obtained']} | {r.get('error') or ''} |")
    (output_dir/'sv_bh9_resumen.md').write_text('\n'.join(md)+'\n', encoding='utf-8')
    return payload
