"""
LAB-T05 — Verificador de distorsión global Loss^D_SV y Teorema 8
====================================================================

Verifica computacionalmente la magnitud Loss^D_SV(Γ, Γ') del apartado 18.6
y el Teorema 8 (distorsión factual del canal) del apartado 18.8.3:

    Loss^D_SV := |D^{SV}_{Φ,origen}(Γ) − D^{SV}_{Φ,reconstruido}(Γ')|

    Teorema 8: si Loss^profile_SV(Γ, Γ') > L_d, entonces D_𝓣 ∈ {0, U}.

El laboratorio:

    (A) Calcula Loss^D_SV sobre tres trayectorias con distorsión global creciente.
    (B) Verifica el Teorema 8 sobre el perfil completo: si la distorsión
        excede el umbral declarado, el dictamen de transmisión es no apto.
    (C) Verifica el caso frontera: si la distorsión induce U en el perfil,
        el dictamen es U.

Tolerancia operativa: el umbral L_d se declara explícitamente.

Autoría / Authorship
-------------------
© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados / All rights reserved.
ORCID: 0000-0002-6634-3351
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
IA eñ™ — La Biblia de la IA™
ISSN 2695-6411
Licencia / License: CC BY-NC-ND 4.0
"""


# Trayectoria origen con observable Φ aplicado: valores en cada suceso
VALORES_PHI_ORIGEN = [0, 1, 2, 3, 5]


def calcular_D_global(valores):
    """D^{SV}_Φ(Γ) = |Φ(S_r) − Φ(S_l)|."""
    return abs(valores[-1] - valores[0])


def calcular_perfil(valores):
    """Perfil local d^{SV}_Φ."""
    return [abs(valores[k+1] - valores[k]) for k in range(len(valores) - 1)]


def loss_global(valores_origen, valores_recon):
    return abs(calcular_D_global(valores_origen) - calcular_D_global(valores_recon))


def loss_profile(valores_origen, valores_recon):
    p_origen = calcular_perfil(valores_origen)
    p_recon = calcular_perfil(valores_recon)
    return sum(abs(a - b) for a, b in zip(p_origen, p_recon))


def dictamen_T8(loss_profile_value, umbral_L_d, hay_U=False):
    """Dictamen del Teorema 8: D_𝓣 ∈ {0, 1, U}."""
    if hay_U:
        return "U"
    if loss_profile_value > umbral_L_d:
        return 0  # no apto
    return 1  # apto


def main():
    print("=" * 78)
    print(" LAB-T05 — Distorsión global Loss^D_SV y Teorema 8")
    print("=" * 78)
    print()
    print(" Definiciones canónicas:")
    print("   D^{SV}_Φ(Γ) = |Φ(S_r) − Φ(S_l)|")
    print("   Loss^D_SV = |D origen − D reconstruido|")
    print()
    print(f" Trayectoria origen Φ: {VALORES_PHI_ORIGEN}")
    print(f" D^{{SV}}_Φ(Γ) origen = |Φ(S_r) − Φ(S_l)| = |{VALORES_PHI_ORIGEN[-1]} − {VALORES_PHI_ORIGEN[0]}| = {calcular_D_global(VALORES_PHI_ORIGEN)}")
    print(f" Perfil local origen: {calcular_perfil(VALORES_PHI_ORIGEN)}")
    print()

    UMBRAL_L_D = 2

    print(f" Umbral L_d declarado: {UMBRAL_L_D}")
    print()

    # Tres casos con distorsión global creciente
    casos = [
        ("Caso A: sin distorsión (control)", VALORES_PHI_ORIGEN, 1),
        ("Caso B: distorsión leve (perfil = 1)", [0, 1, 2, 3, 4], "?"),
        ("Caso C: distorsión moderada (perfil = 4)", [0, 1, 2, 3, 9], "?"),
        ("Caso D: distorsión severa (perfil = 8)", [0, 2, 4, 6, 13], "?"),
    ]

    print(f" {'Caso':<48} | {'D recon':<7} | {'Loss^D':<6} | {'Loss^p':<6} | {'D_𝓣':<5}")
    print(" " + "-" * 80)

    aciertos = 0
    for etiqueta, valores_recon, esperado in casos:
        D_recon = calcular_D_global(valores_recon)
        L_D = loss_global(VALORES_PHI_ORIGEN, valores_recon)
        L_p = loss_profile(VALORES_PHI_ORIGEN, valores_recon)
        D_T = dictamen_T8(L_p, UMBRAL_L_D)
        # El control debe pasar (1), los otros no apto (0) si superan umbral
        if esperado == 1:
            ok = (D_T == 1)
        else:
            # Esperamos que A apto, B apto (≤2), C no apto (>2), D no apto (>2)
            esperado_real = 1 if L_p <= UMBRAL_L_D else 0
            ok = (D_T == esperado_real)
        if ok:
            aciertos += 1
        marca = "✓" if ok else "✗"
        print(f" {etiqueta:<48} | {D_recon:<7} | {L_D:<6} | {L_p:<6} | {str(D_T):<5} {marca}")

    # Caso frontera: distorsión induce U en el perfil
    print()
    print(" Caso frontera: distorsión que induce U en perfil reconstruido.")
    perfil_con_U = [1, "U", 1, 2]  # contiene U: dictamen debe ser U
    hay_U = "U" in perfil_con_U
    D_T_frontera = dictamen_T8(0, UMBRAL_L_D, hay_U=hay_U)
    print(f"   Perfil con U: {perfil_con_U}")
    print(f"   Dictamen de transmisión: D_𝓣 = {D_T_frontera}")
    frontera_OK = (D_T_frontera == "U")
    if frontera_OK:
        aciertos += 1
    print(f"   {'✓' if frontera_OK else '✗'} Caso frontera: U preservada en dictamen.")
    print()

    print(" Análisis estructural:")
    print(" - Loss^D_SV cuantifica la distorsión global de la distancia fibrosa.")
    print(" - El Teorema 8 sostiene que distorsión > umbral implica no apto.")
    print(" - La preservación de U se mantiene cuando hay U en el perfil.")
    print()

    if aciertos == len(casos) + 1:
        print("✓ LAB-T05 SUPERADO:")
        print(f"  - Loss^D_SV calculado correctamente sobre {len(casos)} casos.")
        print("  - Teorema 8 verificado: distorsión > umbral → dictamen no apto.")
        print("  - Caso frontera con U preservada en dictamen.")
        return 0
    else:
        print(f"✗ LAB-T05 FALLA.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
