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

rows = read_csv('datos/contraste_externo_materials_project_metricas.csv')
errors=[]
expected={
 "`Y_SV` como clasificador MP": {'TP':1730,'FP':313,'TN':4,'FN':51,'F1':0.905,'Exactitud':0.827,'Especificidad':0.013,'Exactitud balanceada':0.492,'MCC':-0.036},
 'Sello trivial: todo estable': {'TP':1781,'FP':317,'TN':0,'FN':0,'F1':0.918,'Exactitud':0.849,'Especificidad':0.000,'Exactitud balanceada':0.500,'MCC':0.000},
}
for r in rows:
    name=r['Lectura evaluada']
    if name not in expected: errors.append(f'lectura_no_esperada:{name}'); continue
    for key,val in expected[name].items():
        if key in ['TP','FP','TN','FN']:
            if int(r[key])!=val: errors.append(f'{name}:{key}')
        else:
            if abs(fnum(r[key])-val)>0.001: errors.append(f'{name}:{key}')
result={'verificador':'verificador_contraste_externo_mp.py','errores':errors,'dictamen':'APTO_CON_CONTRASTE_EXTERNO_NEGATIVO_REPORTADO' if not errors else 'NO_APTO'}
write_output('salida_contraste_externo_mp.json', result)
if errors: raise SystemExit(1)
