"""
LAB-01 — Verificador adversarial de la compuerta Σ = 1 / Σ = 0
==================================================================

Verifica computacionalmente el cumplimiento estricto de la compuerta de
admisibilidad del apartado 4.1 del documento principal:

    Sólo elementos del catálogo factual con lectura Σ = 1 pueden entrar como
    argumentos del operador 𝓘_SV en el dominio Π_SV^{2,ord}. Los elementos con
    lectura Σ = 0 quedan estrictamente excluidos del dominio de campos.

El laboratorio implementa un test adversarial sobre seis escenarios:
cinco intentos de violación con uno o más argumentos Σ = 0, y un escenario
limpio con dos argumentos Σ = 1 distintos. La verificación falla si:

    (Val-1) los seis primitivos métricos aparecen como argumentos del operador;
    (Val-2) la lectura espectral aparece como argumento;
    (Val-3) Fourier factual aparece como argumento;
    (Val-4) el jacobiano y la sensibilidad aparecen como argumentos;
    (Val-5) la diagonal (Φ, Φ) con un campo Σ = 1 aparece como argumento;
    (Val-6) el control limpio con dos campos Σ = 1 distintos es marcado inválido.

Tolerancia operativa: exacta sobre verificación booleana de la compuerta.

Autoría / Authorship
-------------------
© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados / All rights reserved.
ORCID: 0000-0002-6634-3351
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
IA eñ™ — La Biblia de la IA™
ISSN 2695-6411
Licencia / License: CC BY-NC-ND 4.0
"""


# Catálogo factual operativo del dominio de interacción
CATALOGO_FACTUAL = {
    # Σ = 1: campos admitidos
    "sector_electrico":          {"sigma": 1, "rol": "campo generador eléctrico"},
    "sector_magnetico":          {"sigma": 1, "rol": "campo generador magnético"},
    "sector_basal_gravitatorio": {"sigma": 1, "rol": "campo generador (m₀)"},
    "convergencia_ternaria":     {"sigma": 1, "rol": "régimen estructural generador"},
    "sector_topologico":         {"sigma": 1, "rol": "régimen estructural generador"},
    "TPA":                       {"sigma": 1, "rol": "objeto del cambio factual"},
    # régimen angular factual acoplado: ahora en Σ=0 como régimen estructural auxiliar
    "regimen_angular_factual":   {"sigma": 0, "rol": "régimen estructural auxiliar"},
    # Σ = 0: herramientas auxiliares
    "UE_MFC":                    {"sigma": 0, "rol": "herramienta de medida (periodo)"},
    "UFE":                       {"sigma": 0, "rol": "herramienta de medida (extensión)"},
    "UFM":                       {"sigma": 0, "rol": "herramienta de medida (masa)"},
    "UFC":                       {"sigma": 0, "rol": "herramienta de medida (corriente)"},
    "UFT":                       {"sigma": 0, "rol": "herramienta de medida (temperatura)"},
    "UFCE":                      {"sigma": 0, "rol": "herramienta de medida (cantidad)"},
    "lectura_espectral":         {"sigma": 0, "rol": "proyección analítica"},
    "funcion_generatriz":        {"sigma": 0, "rol": "proyección analítica"},
    "variable_compleja_factual": {"sigma": 0, "rol": "herramienta de reconstrucción"},
    "sensibilidad_factual":      {"sigma": 0, "rol": "diagnóstico de respuesta"},
    "jacobiano_estructural":     {"sigma": 0, "rol": "diagnóstico diferencial"},
    "compuerta_metrologica":     {"sigma": 0, "rol": "normalización dimensional"},
    "Fourier_factual":           {"sigma": 0, "rol": "aparato modal posterior"},
    "transformada_modal":        {"sigma": 0, "rol": "análisis modal posterior"},
}


def verifica_par_admisible(arg_a, arg_b):
    """
    Verifica si un par (arg_a, arg_b) es admisible como argumento de 𝓘_SV.
    Devuelve (admisible, motivo_si_no).
    """
    # Verificar existencia en el catálogo
    for arg, label in [(arg_a, "Φ^a"), (arg_b, "Φ^b")]:
        if arg not in CATALOGO_FACTUAL:
            return False, f"{label} = {arg} no existe en el catálogo"

    # Verificar a ≠ b (excluir diagonal)
    if arg_a == arg_b:
        return False, f"diagonal: Φ^a = Φ^b = {arg_a} (excluida del dominio)"

    # Verificar lectura Σ = 1 en ambos argumentos
    sigma_a = CATALOGO_FACTUAL[arg_a]["sigma"]
    sigma_b = CATALOGO_FACTUAL[arg_b]["sigma"]
    if sigma_a == 0:
        return False, f"Φ^a = {arg_a} tiene lectura Σ=0 (herramienta auxiliar)"
    if sigma_b == 0:
        return False, f"Φ^b = {arg_b} tiene lectura Σ=0 (herramienta auxiliar)"

    return True, "par admisible"


# Seis escenarios de prueba: cinco adversariales + uno de control limpio
ESCENARIOS = [
    {
        "etiqueta": "Val-1 — primitivos métricos como argumentos",
        "par": ("UFM", "UFE"),
        "esperado": "INADMISIBLE",
    },
    {
        "etiqueta": "Val-2 — lectura espectral como argumento",
        "par": ("sector_electrico", "lectura_espectral"),
        "esperado": "INADMISIBLE",
    },
    {
        "etiqueta": "Val-3 — Fourier factual como argumento",
        "par": ("Fourier_factual", "sector_basal_gravitatorio"),
        "esperado": "INADMISIBLE",
    },
    {
        "etiqueta": "Val-4 — jacobiano y sensibilidad como argumentos",
        "par": ("jacobiano_estructural", "sensibilidad_factual"),
        "esperado": "INADMISIBLE",
    },
    {
        "etiqueta": "Val-5 — diagonal con campo Σ=1",
        "par": ("sector_electrico", "sector_electrico"),
        "esperado": "INADMISIBLE",
    },
    {
        "etiqueta": "Val-6 — control limpio (dos Σ=1 distintos)",
        "par": ("sector_basal_gravitatorio", "sector_electrico"),
        "esperado": "ADMISIBLE",
    },
]


def main():
    print("=" * 78)
    print(" LAB-01 — Verificador adversarial de la compuerta Σ = 1 / Σ = 0")
    print("=" * 78)
    print()

    # Inventario del catálogo
    n1 = sum(1 for v in CATALOGO_FACTUAL.values() if v["sigma"] == 1)
    n0 = sum(1 for v in CATALOGO_FACTUAL.values() if v["sigma"] == 0)
    print(f" Catálogo factual: {n1} elementos Σ=1, {n0} elementos Σ=0.")
    print()

    print(f" {'Escenario':<48} | {'Esperado':<13} | {'Detectado':<13} | {'OK':<3}")
    print(" " + "-" * 80)

    aciertos = 0
    for escenario in ESCENARIOS:
        admisible, motivo = verifica_par_admisible(*escenario["par"])
        detectado = "ADMISIBLE" if admisible else "INADMISIBLE"
        ok = (detectado == escenario["esperado"])
        if ok:
            aciertos += 1
        marca = "✓" if ok else "✗"
        print(f" {escenario['etiqueta']:<48} | "
              f"{escenario['esperado']:<13} | "
              f"{detectado:<13} | "
              f"{marca:<3}")
        if not admisible and ok:
            print(f"     · {motivo}")

    print()
    print(f" Aciertos: {aciertos}/{len(ESCENARIOS)}")
    print()

    if aciertos == len(ESCENARIOS):
        print("✓ LAB-01 SUPERADO:")
        print("  - Las cinco violaciones adversariales son detectadas.")
        print("  - El control limpio con dos Σ=1 distintos es admitido.")
        print("  - Compuerta de admisibilidad verificada operativamente.")
        return 0
    else:
        print(f"✗ LAB-01 FALLA: {len(ESCENARIOS) - aciertos} escenarios incorrectos.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
