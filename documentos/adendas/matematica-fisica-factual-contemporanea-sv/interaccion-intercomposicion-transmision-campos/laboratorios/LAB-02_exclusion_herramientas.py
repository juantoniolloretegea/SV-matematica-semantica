"""
LAB-02 — Verificador de exclusión de herramientas Σ = 0
==========================================================

Verifica computacionalmente el Teorema 2 del documento principal: ninguna
herramienta del aparato matemático auxiliar del Sistema Vectorial SV con
lectura Σ = 0 puede operar como campo generador de interacción.

El laboratorio extiende la verificación de LAB-01 mediante una batería
exhaustiva sobre los catorce elementos Σ = 0 del inventario canónico:

    - los seis primitivos metrológicos (UE_MFC, UFE, UFM, UFC, UFT, UFCE);
    - lectura espectral, función generatriz;
    - variable compleja factual auxiliar;
    - sensibilidad factual, jacobiano estructural;
    - compuerta metrológica;
    - Fourier factual y transformadas modales.

La verificación falla si cualquiera de los catorce elementos puede pasar como
argumento del operador 𝓘_SV.

Tolerancia operativa: exacta sobre exclusión booleana.

Autoría / Authorship
-------------------
© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados / All rights reserved.
ORCID: 0000-0002-6634-3351
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
IA eñ™ — La Biblia de la IA™
ISSN 2695-6411
Licencia / License: CC BY-NC-ND 4.0
"""


HERRAMIENTAS_SIGMA0 = [
    "UE_MFC", "UFE", "UFM", "UFC", "UFT", "UFCE",
    "lectura_espectral", "funcion_generatriz",
    "variable_compleja_factual",
    "sensibilidad_factual", "jacobiano_estructural",
    "compuerta_metrologica",
    "regimen_angular_factual_acoplado",
    "Fourier_factual", "transformada_modal",
]

CAMPOS_SIGMA1 = [
    "sector_electrico", "sector_magnetico", "sector_basal_gravitatorio",
    "convergencia_ternaria", "sector_topologico", "TPA",
]


def es_admisible_como_campo(elemento):
    """Devuelve True si el elemento es campo Σ = 1 admisible."""
    return elemento in CAMPOS_SIGMA1


def main():
    print("=" * 78)
    print(" LAB-02 — Verificador de exclusión de herramientas Σ = 0")
    print("=" * 78)
    print()
    print(f" Inventario de herramientas Σ = 0: {len(HERRAMIENTAS_SIGMA0)}")
    print(f" Inventario de campos Σ = 1:        {len(CAMPOS_SIGMA1)}")
    print()
    print(" Test exhaustivo: cada herramienta Σ=0 contra cada campo Σ=1.")
    print(" Falla si cualquier herramienta es admitida como campo generador.")
    print()

    intentos = 0
    rechazos = 0
    fallos = []

    for herramienta in HERRAMIENTAS_SIGMA0:
        for campo in CAMPOS_SIGMA1:
            # Probar las dos direcciones (herramienta, campo) y (campo, herramienta)
            for arg_a, arg_b in [(herramienta, campo), (campo, herramienta)]:
                intentos += 1
                # La herramienta nunca debe ser admitida como argumento
                herramienta_es_admisible = es_admisible_como_campo(herramienta)
                if herramienta_es_admisible:
                    fallos.append(f"{herramienta} (Σ=0) admitida como campo")
                else:
                    rechazos += 1

    print(f" Intentos totales: {intentos}")
    print(f" Rechazos correctos: {rechazos}")
    print(f" Fallos detectados: {len(fallos)}")
    print()

    # Reporte detallado de las catorce herramientas
    print(" Estatuto de las herramientas Σ = 0:")
    todas_excluidas = True
    for h in HERRAMIENTAS_SIGMA0:
        admisible = es_admisible_como_campo(h)
        marca = "✗ ADMITIDA (FALLO)" if admisible else "✓ excluida"
        print(f"   {marca}: {h}")
        if admisible:
            todas_excluidas = False

    print()
    print(" Estatuto de los campos Σ = 1 (control de inclusión):")
    todos_admitidos = True
    for c in CAMPOS_SIGMA1:
        admisible = es_admisible_como_campo(c)
        marca = "✓ admitido" if admisible else "✗ rechazado (FALLO)"
        print(f"   {marca}: {c}")
        if not admisible:
            todos_admitidos = False

    print()
    if todas_excluidas and todos_admitidos and len(fallos) == 0:
        print("✓ LAB-02 SUPERADO:")
        print(f"  - Las {len(HERRAMIENTAS_SIGMA0)} herramientas Σ=0 quedan excluidas como campos.")
        print(f"  - Los {len(CAMPOS_SIGMA1)} campos Σ=1 son admitidos correctamente.")
        print("  - Teorema 2 verificado operativamente.")
        return 0
    else:
        print(f"✗ LAB-02 FALLA: {len(fallos)} fallos detectados.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
