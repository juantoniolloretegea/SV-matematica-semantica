"""
run_all.py — Ejecuta todos los laboratorios y la suite de tests en orden.

Uso:
    python3 run_all.py
"""
import subprocess
import sys
import os

LABS = [
    'lab_04_4_verificacion_preternaria.py',
    'lab_11_recorrido_consistencia.py',
    'lab_11_10_violacion_simulada.py',
    'lab_ejemplo_A_cierre_determinado.py',
    'lab_ejemplo_B_residual_en_U.py',
    'lab_ejemplo_C_clase_emergente.py',
]
TESTS = 'tests/test_monotonia.py'


def run(path):
    print(f"\n{'█' * 70}")
    print(f"EJECUTANDO {path}")
    print('█' * 70)
    result = subprocess.run(['python3', path],
                            capture_output=False,
                            cwd=os.path.dirname(os.path.abspath(__file__)))
    return result.returncode


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)

    failures = []

    print("╔" + "═" * 68 + "╗")
    print("║" + "  2026l Entropía factual SV — suite completa de laboratorios  ".center(68) + "║")
    print("╚" + "═" * 68 + "╝")

    for lab in LABS:
        rc = run(lab)
        if rc != 0:
            failures.append(lab)

    rc = run(TESTS)
    if rc != 0:
        failures.append(TESTS)

    print("\n" + "═" * 70)
    print("RESUMEN")
    print("═" * 70)
    if not failures:
        print(f"✓ {len(LABS) + 1} laboratorios/tests ejecutados sin errores.")
    else:
        print(f"✗ {len(failures)}/{len(LABS) + 1} fallaron:")
        for f in failures:
            print(f"    {f}")
    return len(failures)


if __name__ == '__main__':
    sys.exit(main())
