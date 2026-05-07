"""
LAB-T07 — Verificador de pérdida de frontera
==============================================

Verifica computacionalmente que el residual de frontera R_F del apartado
18.5 detecta omisiones o alteraciones de la frontera factual `F` durante
el transporte.

Sin frontera declarada, la transmisión no admite cierre estructural
(condición operativa del apartado 18.2). Por tanto el laboratorio
verifica:

    Esc 1: frontera íntegra (control).
    Esc 2: frontera alterada en un atributo.
    Esc 3: frontera alterada en dos atributos.
    Esc 4: frontera ausente (no transmitida).
    Esc 5: frontera reemplazada por otra frontera distinta.

Tolerancia operativa: R_F = 0 sólo bajo frontera íntegra.

Autoría / Authorship
-------------------
© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados / All rights reserved.
ORCID: 0000-0002-6634-3351
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
IA eñ™ — La Biblia de la IA™
ISSN 2695-6411
Licencia / License: CC BY-NC-ND 4.0
"""


# Frontera origen: cierre operativo declarado
FRONTERA_ORIGEN = {
    "tipo": "frontera_factual",
    "soporte": "trayectoria_completa",
    "umbral_residual": 0.5,
    "criterio_cierre": "compuerta_ternaria",
    "extension": "compatible_con_observable",
}


def calcular_R_F(frontera_origen, frontera_recon):
    """Residual de frontera: distancia entre dos fronteras (atributos diferentes)."""
    if frontera_recon is None:
        return len(frontera_origen)  # toda la frontera perdida
    diferencias = 0
    todas_claves = set(frontera_origen.keys()) | set(frontera_recon.keys())
    for k in todas_claves:
        if frontera_origen.get(k) != frontera_recon.get(k):
            diferencias += 1
    return diferencias


def main():
    print("=" * 78)
    print(" LAB-T07 — Pérdida de frontera durante el transporte")
    print("=" * 78)
    print()
    print(" Frontera origen (5 atributos declarados):")
    for k, v in FRONTERA_ORIGEN.items():
        print(f"   {k}: {v}")
    print()

    # Esc 2: frontera con un atributo alterado
    frontera_2 = FRONTERA_ORIGEN.copy()
    frontera_2["umbral_residual"] = 1.0  # alterado

    # Esc 3: frontera con dos atributos alterados
    frontera_3 = FRONTERA_ORIGEN.copy()
    frontera_3["umbral_residual"] = 1.0
    frontera_3["criterio_cierre"] = "binario"  # alterado

    # Esc 5: frontera reemplazada por otra completamente distinta
    frontera_5 = {
        "tipo": "otra_frontera",
        "soporte": "tramo_parcial",
        "umbral_residual": 2.0,
        "criterio_cierre": "binario",
        "extension": "incompatible",
    }

    escenarios = [
        ("Esc 1: frontera íntegra (control)", FRONTERA_ORIGEN.copy(), 0),
        ("Esc 2: alteración de un atributo", frontera_2, 1),
        ("Esc 3: alteración de dos atributos", frontera_3, 2),
        ("Esc 4: frontera ausente", None, 5),
        ("Esc 5: frontera reemplazada", frontera_5, 5),
    ]

    print(f" {'Escenario':<48} | {'R_F':<4} | {'Esperado':<10} | {'OK':<3}")
    print(" " + "-" * 78)

    aciertos = 0
    for etiqueta, frontera_recon, R_esperado in escenarios:
        R_F = calcular_R_F(FRONTERA_ORIGEN, frontera_recon)
        ok = (R_F == R_esperado)
        if ok:
            aciertos += 1
        marca = "✓" if ok else "✗"
        print(f" {etiqueta:<48} | {R_F:<4} | {R_esperado:<10} | {marca:<3}")

    print()
    print(" Análisis estructural:")
    print(" - El residual R_F detecta alteraciones u omisiones de la frontera.")
    print(" - Sin frontera declarada o con frontera distinta, R_F > 0.")
    print(" - La frontera es objeto factual del corpus, no metadato.")
    print()

    if aciertos == len(escenarios):
        print("✓ LAB-T07 SUPERADO:")
        print("  - 5/5 escenarios verificados.")
        print("  - Frontera íntegra → R_F = 0; alteración → R_F > 0; ausencia → R_F máximo.")
        return 0
    else:
        print(f"✗ LAB-T07 FALLA: {len(escenarios) - aciertos} verificaciones incorrectas.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
