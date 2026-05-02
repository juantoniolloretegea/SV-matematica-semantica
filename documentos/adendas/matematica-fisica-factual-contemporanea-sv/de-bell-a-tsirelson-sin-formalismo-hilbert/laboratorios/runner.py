"""
runner.py — Runner unificado de los seis laboratorios
========================================================

Ejecuta los seis laboratorios del documento *De Bell a Tsirelson sin formalismo
de Hilbert* en orden secuencial, captura los resultados y emite un informe
global de cumplimiento.

Política de no pases silenciosos: cualquier laboratorio que devuelva código
de salida distinto de 0 activa el reporte explícito de fallo.

Uso
---
    python runner.py

Salida
------
    Código 0 si los seis laboratorios superan sus verificaciones.
    Código 1 si al menos uno falla.

Autoría
-------
© 2026. Todos los derechos reservados.
Juan Antonio Lloret Egea
ORCID: 0000-0002-6634-3351
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA)
IA eñ™ — La Biblia de la IA™
ISSN 2695-6411
Licencia: CC BY-NC-ND 4.0
"""
import subprocess
import sys
from pathlib import Path


LABORATORIOS = [
    ("LAB-01", "LAB-01_saturacion_familia_celulas.py", "Saturación factual sobre familia SV(b, b²)"),
    ("LAB-02", "LAB-02_factorizacion_R0.py", "Factorización separable y T mod 2 sobre R₀"),
    ("LAB-03", "LAB-03_monotonia_barrido.py", "Monotonía estricta sobre barrido fino de χ_c"),
    ("LAB-04", "LAB-04_equivalencia_cuantica.py", "Equivalencia SV ↔ MQ sobre cuádruples"),
    ("LAB-05", "LAB-05_unicidad_correlador.py", "Unicidad del correlador angular factual"),
    ("LAB-06", "LAB-06_fidelidad_A9.py", "Fidelidad angular mínima A9"),
]


def main():
    print("=" * 78)
    print(" RUNNER UNIFICADO DE LOS SEIS LABORATORIOS")
    print(" Documento: De Bell a Tsirelson sin formalismo de Hilbert")
    print(" Autor: Juan Antonio Lloret Egea (ORCID 0000-0002-6634-3351)")
    print("=" * 78)

    base = Path(__file__).parent
    resultados = []

    for codigo, archivo, descripcion in LABORATORIOS:
        ruta = base / archivo
        print(f"\n{'─' * 78}")
        print(f" Ejecutando {codigo} — {descripcion}")
        print(f" Fichero: {archivo}")
        print(f"{'─' * 78}\n")
        try:
            r = subprocess.run(
                [sys.executable, str(ruta)],
                capture_output=False,
                text=True,
            )
            ok = (r.returncode == 0)
        except Exception as exc:
            print(f"  ERROR de ejecución: {exc}")
            ok = False
        resultados.append((codigo, descripcion, ok))

    # Informe final
    print("\n" + "=" * 78)
    print(" INFORME GLOBAL DE CUMPLIMIENTO")
    print("=" * 78)
    print()
    print(f"{'Laboratorio':<10} | {'Descripción':<55} | {'Estado':<8}")
    print("-" * 78)
    n_ok = 0
    for codigo, descripcion, ok in resultados:
        marca = "OK" if ok else "FALLA"
        if ok:
            n_ok += 1
        print(f"{codigo:<10} | {descripcion:<55} | {marca:<8}")
    print()
    print(f"Resultados: {n_ok}/{len(resultados)} laboratorios superan sus verificaciones.")

    if n_ok == len(resultados):
        print("\n✓ RUNNER SUPERADO: los seis laboratorios cumplen sus tolerancias operativas.")
        return 0
    else:
        print("\n✗ RUNNER FALLA: revisar el catálogo de errores (CATALOGO-DE-ERRORES.md).")
        return 1


if __name__ == "__main__":
    sys.exit(main())
