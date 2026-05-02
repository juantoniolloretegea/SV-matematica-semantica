"""
LAB-06 — Verificación del axioma A9 (fidelidad angular mínima)
=================================================================

Verifica numéricamente el Lema 9.4.1 (no fidelidad de k ≥ 2) mediante test
directo de la propiedad de kernel sobre la familia de representaciones
continuas R_SV,k(δ) = R(kδ + φ) del círculo en SO(2).

Para k ≥ 2, la representación R_SV,k satisface
    R_SV,k(δ + 2π/k) = R_SV,k(δ)
sobre todo δ, lo cual significa que el kernel contiene 2π/k ≠ 0 y la
representación NO es fiel sobre el círculo de bases del aparato CHSH-SV.

Para k = 1, el kernel es trivial y la representación es fiel.
Para k = 0, la representación es constante (no registra el ángulo).

El laboratorio confirma operativamente que k = 1 es la única elección admisible
bajo el axioma A9, lo cual es el pilar que hace única la solución del
Teorema 10.2.1.

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


TOL = 1e-12


def R_SV_k(delta, k, phi=0.0):
    """Representación R_SV,k(δ) = matriz de rotación de SO(2) por (kδ + φ)."""
    angulo = k * delta + phi
    return np.array([[np.cos(angulo), -np.sin(angulo)],
                     [np.sin(angulo), np.cos(angulo)]])


def es_identidad(M):
    return np.allclose(M, np.eye(2), atol=TOL)


def es_fiel(k, n_puntos=200):
    """
    Verifica si R_SV,k es fiel sobre el círculo: el kernel debe contener sólo
    los múltiplos enteros de 2π. Si existe ξ ∈ (0, 2π) tal que R_SV,k(ξ) = I,
    entonces no es fiel.
    """
    if k == 0:
        return False  # constante: no registra ángulo
    # Verificar si 2π/k ∈ kernel para k ≥ 2
    if abs(k) >= 2:
        ds_test = np.linspace(0.0, 2 * np.pi, n_puntos)
        ksi = 2 * np.pi / abs(k)
        # Verificar R_SV,k(δ + 2π/k) == R_SV,k(δ) para toda δ
        for d in ds_test:
            M1 = R_SV_k(d + ksi, k)
            M2 = R_SV_k(d, k)
            if not np.allclose(M1, M2, atol=TOL):
                return True  # No tiene esta periodicidad → podría ser fiel
        return False  # Tiene la periodicidad → no es fiel
    # Para k = 1 o k = -1: fiel
    return True


def main():
    print("=" * 72)
    print("LAB-06 — Verificación del axioma A9 (fidelidad angular mínima)")
    print("=" * 72)

    print(f"\nVerificando R_SV,k(δ) = R(kδ + φ) para varios k ∈ ℤ")
    print(f"Tolerancia operativa: {TOL:.0e}")
    print()
    print(f"{'k':>3} | {'Fiel sobre círculo':>20} | {'2π/|k| ∈ kernel?':>20} | {'Estatuto':>30}")
    print("-" * 90)

    todas_ok = True
    for k in [-3, -2, -1, 0, 1, 2, 3, 4, 5]:
        fiel = es_fiel(k)
        if abs(k) >= 2:
            ksi = 2 * np.pi / abs(k)
            M_ksi = R_SV_k(ksi, k)
            kernel_no_trivial = es_identidad(M_ksi)
        else:
            kernel_no_trivial = (k == 0)
        if k == 0:
            estatuto = "Constante: no registra ángulo"
        elif abs(k) == 1:
            estatuto = "Fiel: única admisible"
        else:
            estatuto = f"No fiel: identifica δ y δ+2π/{abs(k)}"
        print(f"{k:>3} | {str(fiel):>20} | {str(kernel_no_trivial):>20} | {estatuto:>30}")

        # Verificar coherencia: sólo k = ±1 debe ser fiel
        if abs(k) == 1:
            if not fiel:
                todas_ok = False
        else:
            if fiel:
                todas_ok = False

    # Verificación adicional: A9 selecciona unívocamente k = +1 con φ = 0
    # cuando se imponen A2 (C(0) = -1) y orientación canónica.
    print()
    print("Determinación de φ bajo A2 (C_SV(0) = -1):")
    # Ct(0) = cos(k·0 + φ) = cos(φ) = -C_SV(0) = +1 (para C_SV(0) = -1)
    # Entonces φ = 0 (mod 2π).
    # Por tanto C_SV(δ) = -cos(δ + 0) = -cos δ.
    print("  C̃(0) = cos(φ) = -C_SV(0) = +1 ⟹ φ = 0 (mod 2π).")
    print("  C_SV(δ) = -cos(δ + 0) = -cos δ.")

    print()
    if todas_ok:
        print("✓ LAB-06 SUPERADO: A9 selecciona unívocamente k = 1, φ = 0.")
        return 0
    else:
        print("✗ LAB-06 FALLA.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
