# -*- coding: utf-8 -*-
"""
================================================================================
LABORATORIO 07 — MATRIZ COMPARATIVA SV ↔ ΛCDM
================================================================================

Autor:               Juan Antonio Lloret Egea
ORCID:               https://orcid.org/0000-0002-6634-3351
Sello editorial:     Instituto Tecnológico Virtual de la Inteligencia Artificial
                     para el Español (ITVIA)
Publicación:         IA eñ — La Biblia de la IA
ISSN:                2695-6411  (https://portal.issn.org/resource/ISSN/2695-6411)
Licencia:            Creative Commons Attribution-NonCommercial-NoDerivatives 4.0
                     International (CC BY-NC-ND 4.0)
                     https://creativecommons.org/licenses/by-nc-nd/4.0/
Fecha:               25 de mayo de 2026
Lugar:               Madrid

Trabajo de referencia:
    Lloret Egea, J. A. (2026). La materia oscura no existe como sustancia:
    Demostración formal de nulidad sustancial, densidad gravitatoria efectiva
    de sutura y contraste físico escalable. ITVIA — IA eñ — La Biblia de la IA.

Banco contemporáneo de contraste:
    Planck Collaboration (2020). Planck 2018 results. VI. Cosmological parameters.
    Astronomy & Astrophysics, 641, A6.
    https://doi.org/10.1051/0004-6361/201833910

PROPÓSITO
---------
Genera la matriz comparativa entre la lectura ΛCDM contemporánea y la lectura
del trabajo presente, magnitud por magnitud, con cifras, origen y estatuto
declarados. Esta matriz es herramienta de contraste editorial para el lector
externo y replica la tabla de cierre de la conclusión del trabajo.

La comparación no es entre dos modelos físicos rivales sino entre dos lecturas
alternativas de una misma diferencia gravitatoria observada: interpretación
sustancial en ΛCDM, interpretación estructural en el desarrollo presente.

ATENCIÓN
--------
Este código forma parte de la obra protegida intelectualmente bajo licencia
CC BY-NC-ND 4.0. Cualquier referencia académica debe citar la sede canónica
original con DOI cuando esté disponible. Uso no comercial y sin obras derivadas.

================================================================================
"""

from decimal import Decimal


# ==============================================================================
# MATRIZ COMPARATIVA SV ↔ ΛCDM
# ==============================================================================

MATRIZ_COMPARATIVA = [
    {
        "magnitud": "Régimen del dominio",
        "lambda_cdm": "H₀ ≈ 67,4 km·s⁻¹·Mpc⁻¹",
        "sv": "T_obs = 4,354948800 × 10¹⁷ s",
        "origen": "corpus previo (Lloret Egea, 2026i)",
        "estatuto": "precedente canónico",
    },
    {
        "magnitud": "Curvatura cosmológica",
        "lambda_cdm": "Ω_Λ ≈ 0,685; Λ_obs ≈ 1,09 × 10⁻⁵² m⁻²",
        "sv": "Λ_SV,puro = 1,76 × 10⁻⁵² m⁻²",
        "origen": "corpus previo (Lloret Egea, 2026h)",
        "estatuto": "precedente canónico",
    },
    {
        "magnitud": "Densidad total",
        "lambda_cdm": "ρ_crit ≈ 8,5 × 10⁻²⁷ kg·m⁻³",
        "sv": "ρ_cap^SV(Ω_T) = 9,43 × 10⁻²⁷ kg·m⁻³",
        "origen": "derivación del presente trabajo",
        "estatuto": "capacidad estructural",
    },
    {
        "magnitud": "Masa total",
        "lambda_cdm": "M_obs ≈ 1,5 × 10⁵³ kg",
        "sv": "m_cap^SV(Ω_T) = 8,79 × 10⁵² kg",
        "origen": "derivación del presente trabajo",
        "estatuto": "capacidad integrada",
    },
    {
        "magnitud": "Bariones",
        "lambda_cdm": "Ω_b ≈ 0,049; ρ_b ≈ 4,2 × 10⁻²⁸ kg·m⁻³",
        "sv": "banco material en ρ_A^SV",
        "origen": "contraste material declarado",
        "estatuto": "conservado",
    },
    {
        "magnitud": "Materia oscura como sustancia",
        "lambda_cdm": "Ω_c ≈ 0,264; ρ_DM ≈ 2,3 × 10⁻²⁷ kg·m⁻³",
        "sv": "ρ_DM,sustancia^SV = 0",
        "origen": "RESULTADO NUCLEAR DEL PRESENTE TRABAJO",
        "estatuto": "NULIDAD SUSTANCIAL EXACTA",
    },
    {
        "magnitud": "Masa oscura como sustancia",
        "lambda_cdm": "m_DM ≈ 2,0 × 10⁵² kg",
        "sv": "m_DM,sustancia^SV = 0",
        "origen": "RESULTADO NUCLEAR DEL PRESENTE TRABAJO",
        "estatuto": "NULIDAD SUSTANCIAL EXACTA",
    },
    {
        "magnitud": "Inventario admitido inicial",
        "lambda_cdm": "—",
        "sv": "ρ_A^SV(Ω_T;B₀) ≈ 4,3 × 10⁻²⁸ kg·m⁻³",
        "origen": "banco inicial del presente trabajo",
        "estatuto": "inventario auditado",
    },
    {
        "magnitud": "Sutura inicial",
        "lambda_cdm": "—",
        "sv": "ρ_sut,grav^SV(Ω_T;B₀) ≈ 8,99 × 10⁻²⁷ kg·m⁻³",
        "origen": "banco inicial del presente trabajo",
        "estatuto": "indexado por refinamiento",
    },
    {
        "magnitud": "Ecuación rectora",
        "lambda_cdm": "ρ_grav,obs = ρ_bar + ρ_DM",
        "sv": "ρ_cap^SV = ρ_ret^SV + ρ_sut,grav^SV + ρ_C^SV",
        "origen": "reformulación canónica",
        "estatuto": "reidentificación ontológica",
    },
]


# ==============================================================================
# RENDERIZADO DE LA MATRIZ
# ==============================================================================

def imprimir_matriz():
    """Imprime la matriz comparativa con formato tabular legible."""
    print("=" * 80)
    print("MATRIZ COMPARATIVA SV ↔ ΛCDM")
    print("=" * 80)

    for fila in MATRIZ_COMPARATIVA:
        es_resultado = "RESULTADO NUCLEAR" in fila["origen"]
        prefijo = "  ★ " if es_resultado else "    "

        print(f"\n{prefijo}{fila['magnitud']}")
        print(f"        ΛCDM       : {fila['lambda_cdm']}")
        print(f"        SV         : {fila['sv']}")
        print(f"        Origen     : {fila['origen']}")
        print(f"        Estatuto   : {fila['estatuto']}")

    print("\n" + "=" * 80)
    print("CIERRE INTERPRETATIVO")
    print("=" * 80)
    print("""
  La comparación no autoriza decir que una cifra contemporánea esté
  equivocada como parámetro de modelo ΛCDM. Una cifra cosmológica puede
  estar correctamente determinada como parámetro de ajuste y resultar,
  sin embargo, inadecuada como ontología sustancial si se interpreta
  como masa de sustancia material independiente.

  La materia oscura, como sustancia material, no existe; lo que la
  cosmología contemporánea midió y nombró así es estructura del dominio
  físico realizado.
""")
    print("=" * 80)


def exportar_a_markdown():
    """Exporta la matriz en formato markdown para PubPub / GitHub."""
    lineas = []
    lineas.append("| Magnitud | Lectura ΛCDM | Lectura SV | Origen | Estatuto |")
    lineas.append("|---|---|---|---|---|")
    for fila in MATRIZ_COMPARATIVA:
        es_resultado = "RESULTADO NUCLEAR" in fila["origen"]
        m = f"**{fila['magnitud']}**" if es_resultado else fila['magnitud']
        cdm = f"**{fila['lambda_cdm']}**" if es_resultado else fila['lambda_cdm']
        sv = f"**{fila['sv']}**" if es_resultado else fila['sv']
        o = f"**{fila['origen']}**" if es_resultado else fila['origen']
        e = f"**{fila['estatuto']}**" if es_resultado else fila['estatuto']
        lineas.append(f"| {m} | {cdm} | {sv} | {o} | {e} |")
    return "\n".join(lineas)


if __name__ == "__main__":
    imprimir_matriz()
    print("\n\nVERSIÓN MARKDOWN PARA PUBPUB / GITHUB:")
    print("-" * 80)
    print(exportar_a_markdown())
