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
errors=[]
principal = {119,280,443}; control={120,281,442}
if {int(r['k']) for r in main if r['rol'] in ('principal','principal_cierre')} != principal: errors.append('principales')
if {int(r['k']) for r in main if r['rol']=='control_adyacente'} != control: errors.append('controles')
expected = list(range(381,395))+list(range(397,413))+list(range(415,431))+list(range(433,444))
kvals=[int(r['k']) for r in kt]
if kvals != expected: errors.append('KTheta_secuencia')
if len(kvals)!=57: errors.append('KTheta_cardinal')
for excluded in [380,395,396,413,414,431,432]:
    if excluded in kvals: errors.append(f'exclusion_fallida_{excluded}')
for r in kt:
    if int(r['Theta_max_C']) != 700 + 10*int(r['k']): errors.append(f'theta_{r["Elemento"]}')
    if int(r['Theta_max_C']) <= 4500: errors.append(f'umbral_{r["Elemento"]}')
result={'verificador':'verificador_columna_vertebral_ktheta.py','errores':errors,'dictamen':'APTO_COLUMNA_KTHETA' if not errors else 'NO_APTO'}
write_output('salida_verificador_columna_vertebral_ktheta.json', result)
if errors: raise SystemExit(1)
