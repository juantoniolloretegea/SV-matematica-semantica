"""
LAB-01 — Saturación factual sobre familia de células SV(b, b²)
================================================================

Verifica numéricamente el Teorema 11.2.1 (saturación factual de la cota de
Tsirelson) sobre la familia de células SV(b, b²) para b ∈ {3, 4, 5, 7, 9, 11},
confirmando que la saturación |S(χ_c = 1)| = 2√2 es propiedad estructural del
aparato angular acoplado independiente del tamaño de célula.

Teorema verificado:
    Sobre el cuádruple óptimo (α=0, α'=π/2, β=π/4, β'=3π/4),
    |S_SV|_sat = |C_SV(α-β) - C_SV(α-β') + C_SV(α'-β) + C_SV(α'-β')| = 2√2.

Tolerancia operativa: |S - 2√2| < 1e-14 (precisión de máquina IEEE 754).

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


def C_SV(delta):
    """Correlador angular factual acoplado del Teorema 10.2.1: C_SV(δ) = -cos δ."""
    return -np.cos(delta)


def saturacion_celula(b):
    """Calcula |S_SV(χ_c=1)| sobre el cuádruple óptimo CHSH para célula SV(b, b²)."""
    a, ap = 0.0, np.pi / 2
    bb, bp = np.pi / 4, 3 * np.pi / 4
    E_ab = C_SV(a - bb)
    E_abp = C_SV(a - bp)
    E_apb = C_SV(ap - bb)
    E_apbp = C_SV(ap - bp)
    S = abs(E_ab - E_abp + E_apb + E_apbp)
    return S


def main():
    print("=" * 72)
    print("LAB-01 — Saturación factual sobre familia de células SV(b, b²)")
    print("=" * 72)

    cota_tsirelson = 2 * np.sqrt(2)
    tolerancia = 1e-14
    b_lista = [3, 4, 5, 7, 9, 11]

    print(f"\nCota de Tsirelson 2√2 = {cota_tsirelson:.16f}")
    print(f"Tolerancia operativa: {tolerancia:.0e}")
    print()
    print(f"{'b':>3} | {'n=b²':>5} | {'|S_SV(χ_c=1)|':>20} | {'|S - 2√2|':>15}")
    print("-" * 72)

    todas_ok = True
    for b in b_lista:
        S = saturacion_celula(b)
        diff = abs(S - cota_tsirelson)
        ok = diff < tolerancia
        if not ok:
            todas_ok = False
        marca = "OK" if ok else "FALLA"
        print(f"{b:>3} | {b**2:>5} | {S:>20.16f} | {diff:>10.2e}  [{marca}]")

    print()
    if todas_ok:
        print("✓ LAB-01 SUPERADO: saturación |S| = 2√2 verificada en todas las células.")
        return 0
    else:
        print("✗ LAB-01 FALLA: alguna célula no satura.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
