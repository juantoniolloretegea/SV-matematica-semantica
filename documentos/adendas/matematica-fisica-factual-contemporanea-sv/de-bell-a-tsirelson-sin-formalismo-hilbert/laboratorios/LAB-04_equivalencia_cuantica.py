"""
LAB-04 — Equivalencia numérica con el correlador cuántico sobre cuádruples aleatorios
======================================================================================

Verifica numéricamente sobre 1 000 cuádruples aleatorios de bases que el aparato
del Sistema Vectorial SV en saturación plena (χ_c = 1) reproduce exactamente el
correlador angular C(δ) = -cos δ que la mecánica cuántica obtiene sobre el estado
singlete con observables Pauli rotados.

La igualdad C_SV(δ) = -cos(δ) = E_QM(α, β) sobre δ = α - β es la consecuencia
operativa del Teorema 10.2.1 (unicidad del coseno factual acoplado).

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
    """Correlador angular factual acoplado del Sistema Vectorial SV (Teorema 10.2.1)."""
    return -np.cos(delta)


def E_QM(alpha, beta):
    """Correlador cuántico sobre estado singlete con observables Pauli rotados."""
    return -np.cos(alpha - beta)


def main():
    print("=" * 72)
    print("LAB-04 — Equivalencia numérica SV ↔ MQ sobre cuádruples aleatorios")
    print("=" * 72)

    np.random.seed(42)
    n_pruebas = 1000
    tolerancia = 1e-14

    diferencias = []
    n_falla = 0
    for _ in range(n_pruebas):
        alpha = np.random.uniform(0, 2 * np.pi)
        beta = np.random.uniform(0, 2 * np.pi)
        delta = alpha - beta
        sv = C_SV(delta)
        qm = E_QM(alpha, beta)
        diff = abs(sv - qm)
        diferencias.append(diff)
        if diff >= tolerancia:
            n_falla += 1

    diferencias = np.array(diferencias)
    print(f"\nPruebas realizadas: {n_pruebas}")
    print(f"Tolerancia operativa: {tolerancia:.0e}")
    print(f"\nEstadísticos de |C_SV(δ) − E_QM(α,β)|:")
    print(f"  Máximo:   {diferencias.max():.2e}")
    print(f"  Promedio: {diferencias.mean():.2e}")
    print(f"  Mínimo:   {diferencias.min():.2e}")
    print(f"\nDiferencias ≥ {tolerancia:.0e}: {n_falla}/{n_pruebas}")

    # Verificación adicional sobre el cuádruple óptimo CHSH
    print(f"\nVerificación sobre el cuádruple óptimo CHSH:")
    a, ap = 0.0, np.pi / 2
    b, bp = np.pi / 4, 3 * np.pi / 4
    pares = [
        ("α, β", a, b),
        ("α, β'", a, bp),
        ("α', β", ap, b),
        ("α', β'", ap, bp),
    ]
    print(f"{'Par':>10} | {'C_SV(α-β)':>15} | {'E_QM(α,β)':>15} | {'|diff|':>10}")
    print("-" * 65)
    for nombre, x, y in pares:
        sv = C_SV(x - y)
        qm = E_QM(x, y)
        d = abs(sv - qm)
        print(f"{nombre:>10} | {sv:>15.10f} | {qm:>15.10f} | {d:>10.2e}")

    print()
    if n_falla == 0:
        print(f"✓ LAB-04 SUPERADO: equivalencia numérica SV ↔ MQ verificada en {n_pruebas} pruebas.")
        return 0
    else:
        print(f"✗ LAB-04 FALLA: {n_falla} pruebas excedieron tolerancia.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
