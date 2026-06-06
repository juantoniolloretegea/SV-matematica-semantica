#!/usr/bin/env python3
from pathlib import Path
import csv, json, math, re
ROOT = Path(__file__).resolve().parents[1]

def read_csv(rel):
    with open(ROOT / rel, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))

def write_output(name, data):
    out = ROOT / 'salidas' / name
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(data, ensure_ascii=False, indent=2))

def fnum(x):
    return float(str(x).replace('−','-'))

main = read_csv('datos/tabla_principal_control.csv')
kt = read_csv('datos/tabla_KTheta.csv')
mp = read_csv('datos/contraste_externo_materials_project_metricas.csv')
errors = []

def verify(rows, table_name):
    for r in rows:
        k=int(r['k']); z=int(r['Z_SV']); a=int(r['A_SV']); zfis=int(r['Z_fis'])
        sigma_z=int(r['Sigma_Z']); sigma_a=int(r['Sigma_A_ref']); nres=int(r['N_res']); n=int(r['N'])
        checks = {
            'Z_SV': z == 118+k,
            'A_SV': a == 294+3*k+(k//2),
            'Periodo': int(r['Periodo']) == 8+((k-1)//18),
            'Grupo': int(r['Grupo']) == 1+((k-1)%18),
            'Z_fis': zfis == z,
            'Sigma_Z': sigma_z == zfis,
            'N': n == a-zfis,
            'N_res': nres == a-sigma_a,
            'R_ZSV': r['R_ZSV'] == '0',
            'R_ASV': r['R_ASV'] == '0',
            'R_Zfis': r['R_Zfis'] == '0',
            'R_A': r['R_A'] == '0',
        }
        if table_name == 'KTheta':
            theta=int(r['Theta_max_C']); margin=int(r['Margen_C'])
            checks.update({'Theta': theta == 700+10*k, 'Margen': margin == theta-4500, 'Umbral': theta > 4500, 'R_Theta': r['R_Theta']=='0'})
        for key, ok in checks.items():
            if not ok:
                errors.append(f'{table_name}:{r["Elemento"]}:{key}')
verify(main, 'principal_control')
verify(kt, 'KTheta')
expected = list(range(381,395))+list(range(397,413))+list(range(415,431))+list(range(433,444))
if [int(r['k']) for r in kt] != expected: errors.append('KTheta:secuencia')
if len(kt) != 57: errors.append('KTheta:cardinal')
if min(int(r['Theta_max_C']) for r in kt) != 4510: errors.append('KTheta:theta_min')
if max(int(r['Theta_max_C']) for r in kt) != 5130: errors.append('KTheta:theta_max')
if any(('F11' in str(r) or 'F12' in str(r)) for r in mp): errors.append('MP:F11_F12_presente')
result = {'verificador':'verificador_pliego_final.py','errores':errors,'dictamen':'APTO_COMPLETO_GITHUB' if not errors else 'NO_APTO'}
write_output('salida_verificador_pliego_final.json', result)
if errors: raise SystemExit(1)
