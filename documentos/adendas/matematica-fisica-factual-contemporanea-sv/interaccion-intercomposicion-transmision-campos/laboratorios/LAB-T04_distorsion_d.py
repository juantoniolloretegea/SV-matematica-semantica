"""
LAB-T04 — Verificador de distorsión local Loss^d_SV
========================================================

Verifica computacionalmente la magnitud Loss^d_SV(S_{k+1}, S_k) del
apartado 18.6:

    Loss^d_SV(S_{k+1}, S_k) := |d^{SV}_{Φ,origen}(S_{k+1}, S_k) − d^{SV}_{Φ,reconstruido}(S'_{k+1}, S'_k)|

El laboratorio aplica tres niveles de distorsión inducida sobre el perfil
local de distancia factual fibrosa y verifica que Loss^d_SV detecta
correctamente cada nivel:

    Nivel 0: sin distorsión (control).
    Nivel 1: distorsión leve sobre un paso.
    Nivel 2: distorsión moderada sobre dos pasos.
    Nivel 3: distorsión severa sobre todos los pasos.

Tolerancia operativa: la distorsión Loss^d_SV debe ser monótona creciente
con el nivel de distorsión inducida.

Autoría / Authorship
-------------------
© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados / All rights reserved.
ORCID: 0000-0002-6634-3351
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
IA eñ™ — La Biblia de la IA™
ISSN 2695-6411
Licencia / License: CC BY-NC-ND 4.0
"""


# Perfil local de distancia factual fibrosa origen sobre 5 pasos consecutivos
PERFIL_ORIGEN = [1, 2, 1, 3, 2]


def perfil_distorsionado(perfil_origen, nivel):
    """Aplica distorsión según el nivel."""
    p = list(perfil_origen)
    if nivel == 0:
        return p  # sin distorsión
    if nivel == 1:
        p[0] = p[0] + 1  # distorsión leve sobre el paso 0
        return p
    if nivel == 2:
        p[0] = p[0] + 1
        p[2] = p[2] + 2  # distorsión sobre paso 0 y paso 2
        return p
    if nivel == 3:
        return [v * 2 for v in p]  # distorsión severa sobre todos
    raise ValueError("Nivel de distorsión no soportado")


def loss_local(perfil_origen, perfil_reconstruido, k):
    """Loss^d_SV en el paso k."""
    return abs(perfil_origen[k] - perfil_reconstruido[k])


def loss_perfil_total(perfil_origen, perfil_reconstruido):
    """Suma de Loss^d_SV sobre todos los pasos."""
    return sum(abs(a - b) for a, b in zip(perfil_origen, perfil_reconstruido))


def main():
    print("=" * 78)
    print(" LAB-T04 — Distorsión local Loss^d_SV de d^{SV}_Φ")
    print("=" * 78)
    print()
    print(" Definición canónica:")
    print("   Loss^d_SV(S_{k+1}, S_k) := |d^{SV}_{Φ,origen} − d^{SV}_{Φ,reconstruido}|")
    print()
    print(f" Perfil origen: {PERFIL_ORIGEN}")
    print()

    casos = [
        ("Nivel 0: sin distorsión (control)", 0, 0),  # esperado total = 0
        ("Nivel 1: distorsión leve (1 paso)", 1, 1),
        ("Nivel 2: distorsión moderada (2 pasos)", 2, 3),
        ("Nivel 3: distorsión severa (todos)", 3, sum(PERFIL_ORIGEN)),
    ]

    print(f" {'Nivel':<35} | {'Perfil reconstruido':<25} | {'Total':<6} | {'OK':<3}")
    print(" " + "-" * 78)

    aciertos = 0
    losses = []
    for etiqueta, nivel, esperado in casos:
        perfil_recon = perfil_distorsionado(PERFIL_ORIGEN, nivel)
        total = loss_perfil_total(PERFIL_ORIGEN, perfil_recon)
        losses.append(total)
        ok = (total == esperado)
        if ok:
            aciertos += 1
        marca = "✓" if ok else "✗"
        print(f" {etiqueta:<35} | {str(perfil_recon):<25} | {total:<6} | {marca:<3}")

    # Verificar monotonía
    monotonia = all(losses[i] <= losses[i+1] for i in range(len(losses) - 1))
    print()
    print(f" Monotonía Loss^d_SV creciente con nivel de distorsión: {'✓' if monotonia else '✗'}")
    print(f"   Valores obtenidos: {losses}")
    print()

    print(" Análisis estructural:")
    print(" - Loss^d_SV cuantifica la distorsión local del eje rector P0.")
    print(" - Es magnitud factual, no probabilística.")
    print(" - Debe ser detectable y monótona con el nivel de distorsión inducida.")
    print()

    todo_OK = (aciertos == len(casos)) and monotonia

    if todo_OK:
        print("✓ LAB-T04 SUPERADO:")
        print("  - Loss^d_SV detecta cada nivel de distorsión.")
        print("  - Comportamiento monótono creciente verificado.")
        print("  - Cuatro niveles (0 a 3) verificados correctamente.")
        return 0
    else:
        print(f"✗ LAB-T04 FALLA.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
