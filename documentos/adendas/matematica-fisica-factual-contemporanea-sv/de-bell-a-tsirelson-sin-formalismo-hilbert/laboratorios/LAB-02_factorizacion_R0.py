"""
LAB-02 — Verificación explícita de la factorización separable sobre R₀
========================================================================

Verifica numéricamente el Lema 7.3.1 (factorización separable sobre R₀) y el
Teorema 6.2.1 (Bell exacto) sobre las configuraciones binarias del régimen R₀
sobre la célula SV(3, 9) con bases CHSH óptimas.

Codificación de marcas (apartado 4.1 del documento)
---------------------------------------------------
Sobre el alfabeto ternario Σ = {0, 1, U}, la codificación a reales del aparato
del Sistema Vectorial SV es: 0 ↦ 0, 1 ↦ +1, U ↦ −1. Bajo esta codificación, la
marca 0 no contribuye al aparato angular Z(v; θ).

Bajo esta codificación, sobre las 2⁹ = 512 configuraciones binarias en {0, 1}⁹,
exactamente 260 satisfacen la pertenencia a R₀(Q): tienen los cuatro dictámenes
binarios y las cuatro coincidencias en {0, 1}.

Las 252 configuraciones restantes producen al menos un Z(v; θ) = 0 sobre alguna
base del cuádruple óptimo, lo cual genera dictamen U y excluye la configuración
de R₀(Q).

Para cada v ∈ R₀(Q) ⊂ {0, 1}⁹, se computa:
    1. Los cuatro dictámenes 𝔡(v; θ) sobre las bases del cuádruple.
    2. Las cuatro coincidencias r(v; α_p, β_q).
    3. El observable T(v; Q) mod 2 sobre 𝔽₂.
    4. La cantidad CHSH X(v) bajo κ:{0,1}→{−1,+1}.

Resultados esperados:
    - |R₀(Q)| sobre {0, 1}⁹ bajo la codificación del SV = 260.
    - T(v; Q) ≡ 0 (mod 2) sobre las 260 configuraciones (cumplimiento exacto).
    - |X(v)| ≤ 2 sobre cada configuración individual.

Nota técnica
------------
El parámetro S_sep(b) del Postulado 11.1.1 (mezcla factual mínima) se computa
bajo otra codificación: la binaria pura {−1, +1} del régimen separable estándar
de la literatura CHSH, donde 0 ↦ −1 y 1 ↦ +1. Bajo esa codificación, sobre la
célula SV(3, 9) las 320 configuraciones no degeneradas producen S_sep(3) = 0,2.
La distinción técnica entre los cardinales 260 (R₀ bajo codificación del SV) y
320 (no degeneradas bajo codificación binaria pura) está explicitada en el
apartado 13.9 del documento.

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


N = 9
J = np.arange(1, N + 1)
A_BASE, AP_BASE = 0.0, np.pi / 2
B_BASE, BP_BASE = np.pi / 4, 3 * np.pi / 4


def Z(v_real, theta):
    """Aparato angular Z(v;θ) = Σⱼ ṽⱼ cos(θj)."""
    return float(v_real @ np.cos(theta * J))


def codifica(v_sim):
    """Codificación canónica 0→0, 1→+1, U→-1 (representada como 2)."""
    return np.where(v_sim == 2, -1.0, np.where(v_sim == 1, +1.0, 0.0))


def dictamen(v_sim, theta):
    """Dictamen 𝔡(v;θ) ∈ {0, 1, U} (representado como {0, 1, 2})."""
    if np.any(v_sim == 2):
        return 2
    z = Z(codifica(v_sim), theta)
    if abs(z) < 1e-12:
        return 2
    return 0 if z > 0 else 1


def coincidencia(v_sim, ta, tb):
    """r(v; α_p, β_q) ∈ {0, 1, U}."""
    dA, dB = dictamen(v_sim, ta), dictamen(v_sim, tb)
    if dA == 2 or dB == 2:
        return 2
    return 0 if dA == dB else 1


def kappa(r):
    """Aplicación κ:{0,1}→{−1,+1} del apartado 7.6."""
    if r == 0:
        return +1
    if r == 1:
        return -1
    raise ValueError("κ no definido sobre U")


def main():
    print("=" * 72)
    print("LAB-02 — Factorización separable y T mod 2 sobre R₀ en SV(3, 9)")
    print("=" * 72)

    en_R0 = 0
    T_cero = 0
    T_uno = 0
    X_cumple = 0
    X_falla = 0
    distribucion_X = {}

    for k in range(2 ** 9):
        bits = np.array([(k >> i) & 1 for i in range(9)])
        # Coincidencias ternarias
        rs = [
            coincidencia(bits, A_BASE, B_BASE),
            coincidencia(bits, A_BASE, BP_BASE),
            coincidencia(bits, AP_BASE, B_BASE),
            coincidencia(bits, AP_BASE, BP_BASE),
        ]
        # Dictámenes individuales
        ds = [
            dictamen(bits, A_BASE),
            dictamen(bits, AP_BASE),
            dictamen(bits, B_BASE),
            dictamen(bits, BP_BASE),
        ]
        if all(r in [0, 1] for r in rs) and all(d in [0, 1] for d in ds):
            en_R0 += 1
            T = sum(rs) % 2
            if T == 0:
                T_cero += 1
            else:
                T_uno += 1
            X = kappa(rs[0]) - kappa(rs[1]) + kappa(rs[2]) + kappa(rs[3])
            distribucion_X[X] = distribucion_X.get(X, 0) + 1
            if abs(X) <= 2:
                X_cumple += 1
            else:
                X_falla += 1

    print(f"\nConfiguraciones en R₀(Q) sobre SV(3, 9): {en_R0}")
    print(f"  T mod 2 = 0: {T_cero}")
    print(f"  T mod 2 = 1: {T_uno}")
    cumplimiento_T = (T_cero / en_R0 * 100) if en_R0 > 0 else 0
    print(f"  Cumplimiento Teorema 6.2.1: {cumplimiento_T:.4f}%")
    print()
    print(f"Distribución de X(v) sobre R₀:")
    for x in sorted(distribucion_X.keys()):
        print(f"  X = {x:+d}: {distribucion_X[x]} casos")
    print()
    print(f"  |X(v)| ≤ 2 cumple: {X_cumple}/{en_R0}")
    print(f"  |X(v)| ≤ 2 falla : {X_falla}/{en_R0}")

    if en_R0 > 0:
        promedio_X = sum(x * count for x, count in distribucion_X.items()) / en_R0
        S_R0 = abs(promedio_X)
        print(f"\nPromedio ⟨X⟩ sobre R₀ = {promedio_X:+.10f}")
        print(f"|S|_R₀ = |⟨X⟩| = {S_R0:.10f} ≤ 2: {'OK' if S_R0 <= 2 else 'FALLA'}")

    print()
    todas_ok = (en_R0 == 260 and T_uno == 0 and X_falla == 0)
    if todas_ok:
        print("✓ LAB-02 SUPERADO: 260 configuraciones en R₀, T mod 2 = 0 al 100%, |X|≤2 al 100%.")
        return 0
    else:
        print("✗ LAB-02 FALLA: revisar.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
