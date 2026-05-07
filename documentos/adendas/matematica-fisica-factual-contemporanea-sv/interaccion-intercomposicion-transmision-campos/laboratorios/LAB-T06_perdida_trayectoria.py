"""
LAB-T06 — Verificador de pérdida de trayectoria
=================================================

Verifica computacionalmente que el residual de trayectoria R_Γ del
apartado 18.5 detecta omisiones de sucesos durante el transporte.

El laboratorio aplica cinco escenarios:

    Esc 1: trayectoria íntegra (control, R_Γ = 0).
    Esc 2: omisión de un suceso intermedio.
    Esc 3: omisión del suceso de apertura S_l.
    Esc 4: omisión del suceso de cierre S_r.
    Esc 5: omisión múltiple (varios sucesos).

Tolerancia operativa: R_Γ = 0 sólo en Esc 1; R_Γ > 0 en los demás.

Autoría / Authorship
-------------------
© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados / All rights reserved.
ORCID: 0000-0002-6634-3351
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
IA eñ™ — La Biblia de la IA™
ISSN 2695-6411
Licencia / License: CC BY-NC-ND 4.0
"""


# Trayectoria origen: 6 sucesos consecutivos con índices ν_0, ν_1, ..., ν_5
TRAYECTORIA_ORIGEN = [("ν_0", "S_0"), ("ν_1", "S_1"), ("ν_2", "S_2"),
                      ("ν_3", "S_3"), ("ν_4", "S_4"), ("ν_5", "S_5")]


def calcular_R_gamma(traj_origen, traj_recon):
    """Residual de trayectoria: número de sucesos omitidos o alterados."""
    set_origen = set(traj_origen)
    set_recon = set(traj_recon)
    perdidos = set_origen - set_recon
    espureos = set_recon - set_origen
    return len(perdidos) + len(espureos)


def main():
    print("=" * 78)
    print(" LAB-T06 — Pérdida de trayectoria durante el transporte")
    print("=" * 78)
    print()
    print(f" Trayectoria origen: {len(TRAYECTORIA_ORIGEN)} sucesos.")
    print(f"   {TRAYECTORIA_ORIGEN}")
    print()

    escenarios = [
        ("Esc 1: trayectoria íntegra (control)", TRAYECTORIA_ORIGEN.copy(), 0),
        ("Esc 2: omisión de un suceso intermedio (ν_2)",
         [s for s in TRAYECTORIA_ORIGEN if s[0] != "ν_2"], 1),
        ("Esc 3: omisión del suceso de apertura S_l",
         TRAYECTORIA_ORIGEN[1:], 1),
        ("Esc 4: omisión del suceso de cierre S_r",
         TRAYECTORIA_ORIGEN[:-1], 1),
        ("Esc 5: omisión múltiple (3 sucesos)",
         [TRAYECTORIA_ORIGEN[0], TRAYECTORIA_ORIGEN[2], TRAYECTORIA_ORIGEN[5]], 3),
    ]

    print(f" {'Escenario':<55} | {'R_Γ':<5} | {'Esperado':<10} | {'OK':<3}")
    print(" " + "-" * 80)

    aciertos = 0
    for etiqueta, traj_recon, R_esperado in escenarios:
        R_gamma = calcular_R_gamma(TRAYECTORIA_ORIGEN, traj_recon)
        ok = (R_gamma == R_esperado)
        if ok:
            aciertos += 1
        marca = "✓" if ok else "✗"
        print(f" {etiqueta:<55} | {R_gamma:<5} | {R_esperado:<10} | {marca:<3}")

    print()
    print(" Análisis estructural:")
    print(" - El residual R_Γ detecta omisiones de sucesos durante el transporte.")
    print(" - Bajo trayectoria íntegra, R_Γ = 0.")
    print(" - Cualquier omisión, sea intermedia, de apertura o de cierre, eleva R_Γ.")
    print(" - La trayectoria es información estructural del corpus, no metadato.")
    print()

    if aciertos == len(escenarios):
        print("✓ LAB-T06 SUPERADO:")
        print("  - 5/5 escenarios verificados.")
        print("  - Trayectoria íntegra → R_Γ = 0; cualquier omisión → R_Γ > 0.")
        return 0
    else:
        print(f"✗ LAB-T06 FALLA: {len(escenarios) - aciertos} verificaciones incorrectas.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
