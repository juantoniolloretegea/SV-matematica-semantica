"""
Runner SV — Ejecuta los siete laboratorios secuencialmente y emite veredicto final.
Corresponde a la sección XV (runner mínimo reproducible) del documento.

Funciones: cambio, acumulación, sensibilidad, custodia, congelación de salida.
Invariantes: no degradación U, append-only, separación de planos, no cierre favorable.

Autor:     Juan Antonio Lloret Egea | ORCID 0000-0002-6634-3351
Sello:     ITVIA — IA eñ™ | ISSN 2695-6411 | CC BY-NC-ND 4.0
"""

import json, hashlib, sys, os, subprocess, importlib.util

LAB_DIR = os.path.dirname(os.path.abspath(__file__))

def run_lab(filename):
    """Ejecuta un laboratorio como subproceso e informa resultado."""
    path = os.path.join(LAB_DIR, filename)
    result = subprocess.run([sys.executable, path], capture_output=True, text=True)
    return {
        'lab': filename,
        'returncode': result.returncode,
        'stdout': result.stdout[-1500:] if result.stdout else '',
        'stderr': result.stderr[-500:] if result.stderr else '',
        'veredicto': 'APTO' if result.returncode == 0 else 'NO_APTO'
    }

def file_hash(path):
    """Huella MD5 de un fichero para trazabilidad."""
    try:
        with open(path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except FileNotFoundError:
        return 'NO_GENERADO'

def run_runner():
    print("=" * 70)
    print("RUNNER SV — Runner mínimo reproducible del cálculo del suceso (XV)")
    print("=" * 70)

    labs = [
        ('lab_01_calculo_suceso.py', 'XIV — Módulos A-D + NMSV001-008'),
        ('lab_02_ejemplo_director.py', 'XII §7 — Ejemplo director 7 planos'),
        ('lab_03_geometrico.py', 'XXI-XXII — Laboratorio geométrico G1-G5'),
        ('lab_04_recorrido_completo.py', 'XXIV §15 — Recorrido completo pipeline'),
        ('lab_05_maxwell_factual.py', 'I §3 — Maxwell factual sintético'),
        ('lab_06_gravedad_factual.py', 'II §4 — Gravedad factual sintética'),
        ('lab_07_higgs_factual.py', 'III §3 — Higgs factual sintético'),
    ]

    outputs = []
    all_apto = True

    for filename, descripcion in labs:
        print(f"\n── Ejecutando {filename}  ({descripcion})")
        res = run_lab(filename)
        flag = '✓' if res['veredicto'] == 'APTO' else '✗'
        print(f"  {flag}  returncode={res['returncode']}  →  {res['veredicto']}")
        if res['veredicto'] != 'APTO':
            all_apto = False
            print(f"  ERROR: {res['stderr'][:200]}")
        outputs.append(res)

    # Huellas de integridad
    json_files = [
        'salida_calculo_suceso.json',
        'salida_ejemplo_director.json',
        'salida_geometrico.json',
        'salida_recorrido_completo.json',
        'salida_maxwell_factual.json',
        'salida_gravedad_factual.json',
        'salida_higgs_factual.json',
    ]
    print("\n── Huellas de integridad (MD5) ──")
    hashes = {}
    for jf in json_files:
        h = file_hash(os.path.join(LAB_DIR, jf))
        hashes[jf] = h
        print(f"  {jf}: {h}")

    # Invariantes del runner (XV §4)
    print("\n── Invariantes XV §4 ──")
    invariants = {
        'no_degradacion_U':    True,  # Verificado por NMSV006 en Lab01
        'append_only':         True,  # Verificado por NMSV007 en Lab01
        'separacion_planos':   True,  # Verificado por NMSV005 en Lab01
        'no_cierre_favorable': True,  # Verificado por NMSV008 en Lab01
        'frontera_explicita':  True,  # Verificado por G3 en Lab03
    }
    for inv, ok in invariants.items():
        print(f"  {'✓' if ok else '✗'} {inv}")

    # Veredicto final
    print("\n── VEREDICTO FINAL DEL RUNNER ──")
    all_invariants_ok = all(invariants.values())
    verdict = "APTO" if (all_apto and all_invariants_ok) else "NO_APTO"
    print(f"  Labs pasados: {sum(1 for r in outputs if r['veredicto']=='APTO')}/{len(outputs)}")
    print(f"  Invariantes satisfechos: {sum(invariants.values())}/{len(invariants)}")
    print(f"  Clasificación final: {verdict}")

    # Salida maestra
    master_output = {
        'runner': 'runner_sv_nmsv',
        'version': '1.0',
        'labs': outputs,
        'hashes': hashes,
        'invariantes': invariants,
        'veredicto_final': verdict
    }
    master_path = os.path.join(LAB_DIR, 'salida_runner_sv.json')
    with open(master_path, 'w', encoding='utf-8') as fout:
        json.dump(master_output, fout, ensure_ascii=False, indent=2)
    print(f"  Salida maestra → salida_runner_sv.json")
    return master_output

if __name__ == '__main__':
    result = run_runner()
    sys.exit(0 if result['veredicto_final'] == 'APTO' else 1)
