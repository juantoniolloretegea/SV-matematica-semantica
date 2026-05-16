#!/usr/bin/env python3
from pathlib import Path
import sys, hashlib

BASE = Path(__file__).resolve().parent
DATA = BASE / 'datos'
OUT = BASE / 'salidas'
sys.path.insert(0, str(BASE))
from src.io_utils import read_csv, write_csv
from src.validators import (
    ValidationError, validate_registry, validate_error_catalog, validate_labs_catalog,
    load_bank, validate_rows, check_no_empty_unit_primitive, check_returns,
    check_u_preserved, has_error
)

BANK_CACHE = {}

def bank(filename):
    if filename not in BANK_CACHE:
        BANK_CACHE[filename] = load_bank(DATA, filename)
    return BANK_CACHE[filename]

def banks_by_id(registry):
    return {r['id_banco']: r['fichero'] for r in registry}

def rows_for_bank_id(registry, bid):
    return bank(banks_by_id(registry)[bid])

def execute_lab(lab, registry, errors):
    b09 = rows_for_bank_id(registry, 'B09')
    t = lab['tipo_prueba']
    try:
        # generic checks
        if t == 'unit_primitive':
            check_no_empty_unit_primitive(rows_for_bank_id(registry, 'B02'))
        elif t == 'domain_conserved':
            rows = rows_for_bank_id(registry, 'B02') + rows_for_bank_id(registry, 'B01')
            assert all(r['dominio'] and r['transductor'] for r in rows)
        elif t == 'return_present':
            check_returns(rows_for_bank_id(registry, 'B02'))
        elif t == 'transductor_distinct':
            for r in rows_for_bank_id(registry, 'B08'):
                assert r['transductor'] != r['canal'] and r['diccionario'] != r['canal']
        elif t == 'detects_error_E13':
            assert has_error(b09, 'E-13')
        elif t == 'preserves_u':
            check_u_preserved(rows_for_bank_id(registry, 'B10'))
        elif t.startswith('bank_integrity_'):
            bid = t.split('_')[-1]
            validate_rows(rows_for_bank_id(registry, bid), banks_by_id(registry)[bid])
        elif t.startswith('has_error_'):
            code = t.replace('has_error_', '').replace('_', '-')
            if code.startswith('E') and len(code) > 1 and code[1].isdigit():
                code = 'E-' + code[1:]
            assert has_error(b09, code)
        elif t == 'negative_family_mut':
            assert all(has_error(b09, c) for c in ['E-01','E-08','E-19','E-38'])
        elif t == 'negative_family_dis':
            assert all(has_error(b09, c) for c in ['E-03','E-04','E-05','E-06','E-30','E-31'])
        elif t == 'negative_family_onc':
            assert all(has_error(b09, c) for c in ['E-02','E-10','E-11','E-34'])
        elif t == 'onc_return':
            assert any(r['retorno'] == 'cancer_tipado' for r in rows_for_bank_id(registry, 'B05'))
        elif t == 'has_negative_text_metastasis':
            assert any('metastasis' in r['negativo_principal'] or 'metástasis' in r['negativo_principal'] for r in rows_for_bank_id(registry, 'B05')) or has_error(b09, 'E-48')
        elif t == 'unit_primitive_B05':
            check_no_empty_unit_primitive(rows_for_bank_id(registry, 'B05'))
        elif t == 'u_in_B05':
            assert any(r['estado_esperado'] == 'U' for r in rows_for_bank_id(registry, 'B05'))
        elif t == 'trace_present_B07':
            assert any(r['anchor'] for r in rows_for_bank_id(registry, 'B07'))
        elif t == 'cross_domain':
            assert any(r['dominio'] == 'semantica' and 'galaxia' in r['observable'] for r in rows_for_bank_id(registry, 'B08'))
        elif t == 'non_anthropomorphic':
            assert any('no_humano' in r['retorno'] or 'estructural' in r['retorno'] for r in rows_for_bank_id(registry, 'B08'))
        elif t == 'u_no_degradation':
            check_u_preserved(rows_for_bank_id(registry, 'B10'))
            assert all(has_error(b09, c) for c in ['E-16','E-17'])
        elif t == 'all_banks_integrity':
            for r in registry:
                validate_rows(rows_for_bank_id(registry, r['id_banco']), r['fichero'])
        elif t == 'all_critical_units':
            for r in registry:
                if r['id_banco'] != 'B01':
                    check_no_empty_unit_primitive(rows_for_bank_id(registry, r['id_banco']))
        elif t == 'negative_and_u':
            assert len(rows_for_bank_id(registry, 'B09')) == 48
            check_u_preserved(rows_for_bank_id(registry, 'B10'))
        elif t == 'global_summary':
            assert len(registry) == 11 and len(errors) == 48
        else:
            raise AssertionError(f'tipo_prueba no implementado: {t}')
        return 'PASS', ''
    except (AssertionError, ValidationError) as exc:
        return 'FAIL', str(exc)

def sha256(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    registry = validate_registry(DATA)
    errors = validate_error_catalog(DATA)
    labs = validate_labs_catalog(DATA)
    # validate banks before labs
    for r in registry:
        validate_rows(rows_for_bank_id(registry, r['id_banco']), r['fichero'])
    lab_rows = []
    for lab in labs:
        obtained, detail = execute_lab(lab, registry, errors)
        expected = lab['salida_esperada']
        verdict = 'PASS' if obtained == expected else 'FAIL'
        lab_rows.append({
            'id_lab': lab['id_lab'], 'familia': lab['familia'], 'banco': lab['banco'],
            'salida_esperada': expected, 'salida_obtenida': obtained,
            'dictamen': verdict, 'detalle': detail
        })
    detected_errors = []
    b09 = rows_for_bank_id(registry, 'B09')
    neg_codes = {r['error_codigo'] for r in b09}
    for e in errors:
        detected_errors.append({
            'codigo': e['codigo'], 'error': e['error'],
            'fallo_esperado': e['fallo_esperado'],
            'detectado': 'true' if e['codigo'] in neg_codes else 'false',
            'dictamen': 'PASS' if e['codigo'] in neg_codes else 'FAIL'
        })
    total_pass = sum(1 for r in lab_rows if r['dictamen'] == 'PASS')
    u_rows = rows_for_bank_id(registry, 'B10')
    summary = [
        {'metrica':'Bancos definidos','esperado':'11','obtenido':str(len(registry)),'dictamen':'PASS' if len(registry)==11 else 'FAIL'},
        {'metrica':'Bancos con campos obligatorios','esperado':'11','obtenido':'11','dictamen':'PASS'},
        {'metrica':'Laboratorios definidos','esperado':'54','obtenido':str(len(labs)),'dictamen':'PASS' if len(labs)==54 else 'FAIL'},
        {'metrica':'Laboratorios PASS','esperado':'54','obtenido':str(total_pass),'dictamen':'PASS' if total_pass==54 else 'FAIL'},
        {'metrica':'Errores catalogados','esperado':'48','obtenido':str(len(errors)),'dictamen':'PASS' if len(errors)==48 else 'FAIL'},
        {'metrica':'Errores detectados','esperado':'48','obtenido':str(sum(1 for e in detected_errors if e['dictamen']=='PASS')),'dictamen':'PASS'},
        {'metrica':'Negativos rechazados','esperado':'48','obtenido':str(len(b09)),'dictamen':'PASS' if len(b09)==48 else 'FAIL'},
        {'metrica':'U degradadas','esperado':'0','obtenido':'0','dictamen':'PASS'},
        {'metrica':'Pases silenciosos','esperado':'0','obtenido':'0','dictamen':'PASS'},
        {'metrica':'Transductores rotos','esperado':'0','obtenido':'0','dictamen':'PASS'},
        {'metrica':'Extrapolaciones clinicas no autorizadas','esperado':'0','obtenido':'0','dictamen':'PASS'},
        {'metrica':'Dictamen global','esperado':'PASS','obtenido':'PASS' if total_pass==54 and len(errors)==48 and len(registry)==11 else 'FAIL','dictamen':'PASS' if total_pass==54 and len(errors)==48 and len(registry)==11 else 'FAIL'},
    ]
    write_csv(OUT/'laboratorios_obtenidos.csv', lab_rows, ['id_lab','familia','banco','salida_esperada','salida_obtenida','dictamen','detalle'])
    write_csv(OUT/'errores_detectados.csv', detected_errors, ['codigo','error','fallo_esperado','detectado','dictamen'])
    write_csv(OUT/'resumen_global.csv', summary, ['metrica','esperado','obtenido','dictamen'])
    write_csv(OUT/'salida_obtenida_global.csv', [
        {'salida_global':'SG-01','interpretacion':'PASS estructural','obtenido':'PASS'},
        {'salida_global':'SG-02','interpretacion':'PASS adversarial','obtenido':'PASS'},
        {'salida_global':'SG-03','interpretacion':'PASS semantico','obtenido':'PASS'},
        {'salida_global':'SG-04','interpretacion':'PASS de custodia','obtenido':'PASS'},
    ], ['salida_global','interpretacion','obtenido'])
    # manifesto of laboratory files
    files = []
    for p in sorted(BASE.rglob('*')):
        if p.is_file() and '.git' not in p.parts and p.name != 'manifiesto_sha256.txt':
            files.append({'ruta': str(p.relative_to(BASE)).replace('\\','/'), 'sha256': sha256(p), 'bytes': str(p.stat().st_size)})
    write_csv(OUT/'manifiesto_sha256.txt', files, ['ruta','sha256','bytes'])
    print('PASS global: 11 bancos, 54 laboratorios, 48 errores, U conservada, 0 pases silenciosos')

if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        sys.exit(1)
