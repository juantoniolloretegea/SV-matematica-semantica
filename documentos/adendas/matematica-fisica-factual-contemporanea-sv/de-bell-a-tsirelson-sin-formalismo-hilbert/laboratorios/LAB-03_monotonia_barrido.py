"""
LAB-03 — Monotonía estricta sobre barrido fino de χ_c
========================================================

Verifica numéricamente el Teorema 11.3.1 (transición CHSH acoplada) y el
Corolario 11.1.0.1 (existencia y unicidad del cruce S = 2) sobre 10 001 puntos
del intervalo [0, 1] con paso 10⁻⁴.

Sobre célula SV(3, 9) con S_sep(3) = 0,2:
    S_SV(χ_c; 3) = (1 - χ_c)·0,2 - 2√2·χ_c

Verificaciones:
    1. Monotonía estricta de χ_c ↦ |S_SV(χ_c)| sobre [χ_c_min, 1].
    2. Cruce |S_SV| = 2 sobre el umbral crítico χ★(3) = 0,7264497078.
    3. Saturación |S_SV(1)| = 2√2.

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
import numpy as np


def main():
    print("=" * 72)
    print("LAB-03 — Monotonía estricta sobre barrido fino de χ_c en SV(3, 9)")
    print("=" * 72)

    S_sep_3 = 0.2
    cota_tsirelson = 2 * np.sqrt(2)
    chi_star_3 = (2 + S_sep_3) / (S_sep_3 + cota_tsirelson)
    print(f"\nS_sep(3) = {S_sep_3}")
    print(f"χ★(3) = (2 + S_sep) / (S_sep + 2√2) = {chi_star_3:.10f}")
    print(f"2√2 = {cota_tsirelson:.10f}")

    # Barrido fino
    chi_c_grid = np.linspace(0.0, 1.0, 10001)
    S_SV = (1 - chi_c_grid) * S_sep_3 - cota_tsirelson * chi_c_grid
    S_abs = np.abs(S_SV)

    # Localizar el cruce |S| = 2
    idx_cruce = np.argmin(np.abs(S_abs - 2.0))
    chi_cruce = chi_c_grid[idx_cruce]
    S_cruce = S_abs[idx_cruce]
    print(f"\nCruce |S_SV| = 2 localizado en χ_c ≈ {chi_cruce:.6f}")
    print(f"  Diferencia respecto a χ★(3) analítico: {abs(chi_cruce - chi_star_3):.6f}")

    # Saturación en χ_c = 1
    print(f"\nSaturación: |S_SV(χ_c=1)| = {S_abs[-1]:.10f}")
    print(f"  Diferencia respecto a 2√2: {abs(S_abs[-1] - cota_tsirelson):.2e}")

    # Verificación de monotonía estricta sobre [chi_c_min, 1]
    # Encontrar el mínimo de S_abs (donde cambia de signo el argumento)
    idx_min = np.argmin(S_abs)
    chi_min = chi_c_grid[idx_min]
    print(f"\nMínimo de |S_SV| sobre el barrido: {S_abs[idx_min]:.6f} en χ_c = {chi_min:.6f}")

    # Sobre [chi_min, 1], verificar monotonía creciente estricta
    S_post_min = S_abs[idx_min:]
    diffs = np.diff(S_post_min)
    monotona = np.all(diffs > 0)
    n_violaciones = np.sum(diffs <= 0)
    print(f"\nMonotonía estricta sobre [{chi_min:.4f}, 1]:")
    print(f"  Puntos verificados: {len(S_post_min) - 1}")
    print(f"  Violaciones de monotonía: {n_violaciones}")
    print(f"  Resultado: {'OK monótona estricta' if monotona else 'FALLA'}")

    # Resumen tabular
    print(f"\nValores selectos del barrido:")
    print(f"{'χ_c':>10} | {'|S_SV(χ_c)|':>15} | {'Régimen':>15}")
    print("-" * 50)
    for chi in [0.0, 0.1, 0.3, 0.5, 0.7, chi_star_3, 0.75, 0.9, 0.95, 1.0]:
        S_val = abs((1 - chi) * S_sep_3 - cota_tsirelson * chi)
        if chi == 0:
            reg = "R₀"
        elif chi < chi_star_3:
            reg = "R₁"
        elif chi < 1:
            reg = "R₂"
        else:
            reg = "R₂★"
        marca = " ← cruce" if abs(chi - chi_star_3) < 1e-6 else ""
        print(f"{chi:>10.6f} | {S_val:>15.10f} | {reg:>15}{marca}")

    print()
    todas_ok = monotona and abs(S_abs[-1] - cota_tsirelson) < 1e-14
    if todas_ok:
        print("✓ LAB-03 SUPERADO: monotonía estricta y saturación verificadas.")
        return 0
    else:
        print("✗ LAB-03 FALLA.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
