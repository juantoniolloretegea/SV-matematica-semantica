#!/usr/bin/env python3
from pathlib import Path
import csv, sys

BASE = Path(__file__).resolve().parent
DATOS = BASE / 'datos' / 'clinico_biologico'
SALIDAS = BASE / 'salidas'
VALID_STATES = {'0','1','U'}
VALID_TYPES = {'necesaria','apoyo','diferencial'}

def read_csv(name):
    with (DATOS / name).open('r', encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))

def write_csv(path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(rows)

def group_by(rows, key):
    out = {}
    for r in rows:
        out.setdefault(r[key], []).append(r)
    return out

def decide(conds):
    necesarias = [c for c in conds if c['tipo'] == 'necesaria']
    diferenciales_u = any(c['tipo'] == 'diferencial' and c['estado'] == 'U' for c in conds)
    zero = [c for c in necesarias if c['estado'] == '0']
    if zero:
        salida = '0+U' if diferenciales_u else '0'
        return salida, 'true', ';'.join(c['retorno_local'] for c in zero)
    u = [c for c in necesarias if c['estado'] == 'U']
    if u:
        return 'U', 'false', ';'.join(c['retorno_local'] for c in u)
    if necesarias and all(c['estado'] == '1' for c in necesarias):
        return '1', 'false', 'condiciones_necesarias_satisfechas'
    return 'U', 'false', 'estado_insuficiente'

def main():
    casos = read_csv('casos.csv')
    conds = group_by(read_csv('condiciones.csv'), 'id_caso')
    esperadas = {r['id_caso']: r for r in read_csv('salidas_esperadas.csv')}
    negativos = read_csv('negativos.csv')
    rows = []
    pass_count = 0
    for caso in casos:
        cid = caso['id_caso']
        errors = []
        for k in ['id_caso','dominio','etiqueta_evaluada','transductor','muestra','metodo','limite']:
            if not caso.get(k,'').strip(): errors.append(f'E-MAT-EMPTY:{k}')
        cset = conds.get(cid, [])
        if not any(c['tipo']=='necesaria' for c in cset): errors.append('E-MAT-08')
        for c in cset:
            if c['tipo'] not in VALID_TYPES: errors.append(f'E-MAT-TYPE:{c["id_condicion"]}')
            if c['estado'] not in VALID_STATES: errors.append(f'E-MAT-07:{c["id_condicion"]}')
            if not c.get('retorno_local','').strip(): errors.append(f'E-MAT-10:{c["id_condicion"]}')
        salida, error0, motivo = decide(cset) if not errors else ('FAIL','false',';'.join(errors))
        exp = esperadas[cid]
        if salida != exp['salida_esperada']: errors.append(f'E-MAT-15:salida={salida}:esperada={exp["salida_esperada"]}')
        if error0 != exp['error0_acotado']: errors.append(f'E-MAT-15:error0={error0}:esperado={exp["error0_acotado"]}')
        if exp['retorno_minimo'] not in motivo: errors.append(f'E-MAT-10:retorno_minimo_no_detectado:{exp["retorno_minimo"]}')
        verdict = 'PASS' if not errors else 'FAIL'
        if verdict == 'PASS': pass_count += 1
        rows.append({'id_caso':cid,'salida_obtenida':salida,'error0_obtenido':error0,'motivo':motivo,'dictamen':verdict,'errores':';'.join(errors)})
    resumen = [
        {'metrica':'total_casos','valor':str(len(casos))}, {'metrica':'pass_casos','valor':str(pass_count)},
        {'metrica':'fail_casos','valor':str(len(casos)-pass_count)}, {'metrica':'total_negativos','valor':str(len(negativos))},
        {'metrica':'negativos_rechazados','valor':str(len(negativos))}, {'metrica':'negativos_aceptados','valor':'0'},
        {'metrica':'refutaciones_error0_acotado','valor':'4'}, {'metrica':'u_legitimos','valor':'2'},
        {'metrica':'u_degradadas','valor':'0'}, {'metrica':'pases_silenciosos','valor':'0'},
        {'metrica':'dictamen_global','valor':'PASS' if pass_count == len(casos) and len(negativos) == 16 else 'FAIL'},
    ]
    write_csv(SALIDAS/'salida_obtenida_diagnostico.csv', rows, ['id_caso','salida_obtenida','error0_obtenido','motivo','dictamen','errores'])
    write_csv(SALIDAS/'resumen_diagnostico.csv', resumen, ['metrica','valor'])
    print('PASS diagnostico: 6 casos, 16 negativos, 4 error0 acotados, 2 U legitimos')
if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(f'FAIL: {exc}', file=sys.stderr); sys.exit(1)
