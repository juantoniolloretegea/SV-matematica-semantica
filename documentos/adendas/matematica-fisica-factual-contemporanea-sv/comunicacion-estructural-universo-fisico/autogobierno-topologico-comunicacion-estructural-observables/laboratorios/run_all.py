# -*- coding: utf-8 -*-
"""
Ejecutor común de los nueve laboratorios.
"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
OUTPUTS = ROOT / "salidas_obtenidas"
OUTPUTS.mkdir(exist_ok=True)

LABS = [
    "L1_comparador_realimentacion",
    "L2_convergencia_asintotica_U",
    "L3_regimen_ciclo_distancial",
    "L4_transito_dominios",
    "L5_gobierno_observables",
    "L6_transductores",
    "L7_canal_diccionario_diag",
    "L8_predominancia",
    "L9_matriz_integrada",
]

def main():
    resultados = []
    for lab in LABS:
        script = ROOT / lab / "runner.py"
        proc = subprocess.run([sys.executable, str(script)], cwd=str(ROOT), text=True, capture_output=True, encoding="utf-8")
        out = proc.stdout
        err = proc.stderr
        (OUTPUTS / f"{lab}.txt").write_text(out + (("\nSTDERR:\n" + err) if err else ""), encoding="utf-8")
        ok = (proc.returncode == 0 and "RESULTADO: APTO" in out)
        resultados.append((lab, ok))
        print(f"{lab}: {'APTO' if ok else 'NO_APTO'}")

    global_ok = all(ok for _, ok in resultados)
    print(f"RESULTADO_GLOBAL: {'APTO' if global_ok else 'NO_APTO'}")
    if not global_ok:
        sys.exit(1)

if __name__ == "__main__":
    main()
