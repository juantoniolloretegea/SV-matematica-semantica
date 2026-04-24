"""
lab_10_cuarenta_y_cuatro_operadores.py — L-LUZ-10 — Los 44 operadores canónicos
del aparato luminoso factual.

§8 del documento: inventario canónico de 44 operadores distribuidos como:
  • 24 heredados del corpus (invocados con rango canónico desde 2026a, 2026g,
    2026h, 2026j, 2026k, 2026l)
  • 12 propios del régimen luminoso (B.1–B.12 del documento)
  • 8 emergentes del cruce heredado × propio (C.1–C.8)

Pruebas:
  1. Cardinal total exacto = 44
  2. Partición en (24, 12, 8) sin solapamiento ni pérdida
  3. Cada operador con firma canónica (dominio, codominio, prefijo)
  4. Ausencia de operadores duplicados
  5. Ningún operador invoca axioma ajeno al corpus (prohibición P.5)
  6. Cada operador propio o emergente tiene referencia al documento

Códigos: LUZ-OPE-001..004
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sv_core import SVError


# ---------------------------------------------------------------------------
# INVENTARIO CANÓNICO DE LOS 44 OPERADORES
# ---------------------------------------------------------------------------

OPERADORES_HEREDADOS_24 = {
    # Del corpus 2026a (convergencia ternaria, 5)
    "A.1 Π_3^H":              {"dom": "Ω_pre", "cod": "Σ", "fuente": "2026j"},
    "A.2 Γ_ℋ":                {"dom": "{(α_i,β_i)}", "cod": "clases", "fuente": "2026j"},
    "A.3 ε_SV":                {"dom": "[0,1]^{d×N}", "cod": "ℝ", "fuente": "2026a"},
    "A.4 μ_SV":                {"dom": "[0,1]^{d×N}", "cod": "ℝ", "fuente": "2026a"},
    "A.5 K_3":                 {"dom": "Σ", "cod": "{0,1,2}", "fuente": "2026j"},
    # Del corpus 2026b (TPA, 7)
    "A.6 O1_NM":               {"dom": "mosaico", "cod": "defecto", "fuente": "2026h"},
    "A.7 O2_Gauss":            {"dom": "celda", "cod": "flujo", "fuente": "2026h"},
    "A.8 O3_continuidad":      {"dom": "frontera", "cod": "defecto", "fuente": "2026h"},
    "A.9 dictamen_TPA":        {"dom": "trayectoria", "cod": "{m_0,χ_α,U}", "fuente": "2026h"},
    "A.10 Σ_1..12":            {"dom": "configuración", "cod": "clase", "fuente": "2026h"},
    "A.11 m_0":                {"dom": "configuración cerrada", "cod": "ℝ⁺", "fuente": "2026h"},
    "A.12 M_mat":              {"dom": "región", "cod": "ℝ⁺", "fuente": "2026h"},
    # Del corpus 2026k (Maxwell factual, 8)
    "A.13 Div_SV":             {"dom": "campo", "cod": "escalar", "fuente": "2026k"},
    "A.14 Rot_SV":             {"dom": "campo", "cod": "campo", "fuente": "2026k"},
    "A.15 ∂_ν^SV":             {"dom": "magnitud(ν)", "cod": "Δmagnitud", "fuente": "2026k"},
    "A.16 c_SV":               {"dom": "triplet", "cod": "velocidad", "fuente": "2026k"},
    "A.17 𝔼_SV":               {"dom": "config_em", "cod": "defecto", "fuente": "2026k"},
    "A.18 σ_SV":               {"dom": "material", "cod": "cond", "fuente": "2026k"},
    "A.19 J_ext":              {"dom": "fuente_ext", "cod": "corriente", "fuente": "2026k"},
    "A.20 dic_Maxwell":        {"dom": "SV", "cod": "Maxwell", "fuente": "2026k"},
    # Del corpus 2026l (termodinámica, 4)
    "A.21 𝒜_SV":               {"dom": "trayectoria", "cod": "acum", "fuente": "2026l"},
    "A.22 𝓗_SV":               {"dom": "trayectoria", "cod": "entropía", "fuente": "2026l"},
    "A.23 𝒥_SV":               {"dom": "trayectoria", "cod": "jacob", "fuente": "2026l"},
    "A.24 Θ_SV":                {"dom": "trayectoria", "cod": "Θ", "fuente": "2026l"},
}

OPERADORES_PROPIOS_12 = {
    "B.1 generador_fibra_L":   {"dom": "sec_act", "cod": "D^L_SV", "ref": "§8"},
    "B.2 activador_L":         {"dom": "par polar", "cod": "activ", "ref": "§8"},
    "B.3 modalidad_proyectiva":{"dom": "D^L_SV", "cod": "Proy^{15+}", "ref": "§8"},
    "B.4 cuanto_h_SV":         {"dom": "trayectoria", "cod": "ℝ⁺", "ref": "§3.6"},
    "B.5 umbral_gr":           {"dom": "umbrales", "cod": "umbrales_def", "ref": "A.1"},
    "B.6 polarizacion_SV":     {"dom": "fibra", "cod": "{δ_i^res}", "ref": "§8"},
    "B.7 coherencia_SV":       {"dom": "hebras", "cod": "coh∈[0,1]", "ref": "§8"},
    "B.8 fourier_SV_L":        {"dom": "fibra", "cod": "espectro", "ref": "A.4"},
    "B.9 transmutacion_SV":    {"dom": "trayectoria", "cod": "clase_χ", "ref": "A.7"},
    "B.10 criticidad_SV":      {"dom": "configuración", "cod": "umbral", "ref": "§8"},
    "B.11 correlacion_SV":     {"dom": "par_fibras", "cod": "𝔈^corr", "ref": "A.6"},
    "B.12 NLP_SV":             {"dom": "paquete_obs", "cod": "K_3^9", "ref": "§8"},
}

OPERADORES_EMERGENTES_8 = {
    "C.1 cruce_𝕏×𝕋":           {"dom": "E × TPA", "cod": "dict", "ref": "§8"},
    "C.2 cruce_𝕄×𝕊":           {"dom": "B × espectro", "cod": "band", "ref": "§8"},
    "C.3 cruce_𝔾×ℂ":           {"dom": "grav × conv", "cod": "deform", "ref": "§8"},
    "C.4 cruce_𝕋×𝕃":           {"dom": "TPA × top", "cod": "sing", "ref": "§8"},
    "C.5 cruce_ℂ×𝕊":           {"dom": "conv × esp", "cod": "res", "ref": "§8"},
    "C.6 cruce_𝕃×𝕏":           {"dom": "top × eléct", "cod": "vórt", "ref": "§8"},
    "C.7 cruce_𝔾×𝕋":           {"dom": "grav × TPA", "cod": "sem", "ref": "§8"},
    "C.8 cruce_𝕄×𝔾":           {"dom": "mag × grav", "cod": "lente", "ref": "§8"},
}


def prueba_1_cardinal_total_44() -> None:
    total = len(OPERADORES_HEREDADOS_24) + len(OPERADORES_PROPIOS_12) + len(OPERADORES_EMERGENTES_8)
    if total != 44:
        raise SVError(
            "LUZ-OPE-001",
            f"Cardinal total de operadores = {total} ≠ 44",
        )
    print(f"  [OPE OK] Cardinal total = 44 operadores ✓")


def prueba_2_particion_24_12_8() -> None:
    n24 = len(OPERADORES_HEREDADOS_24)
    n12 = len(OPERADORES_PROPIOS_12)
    n8  = len(OPERADORES_EMERGENTES_8)
    if (n24, n12, n8) != (24, 12, 8):
        raise SVError(
            "LUZ-OPE-001",
            f"Partición ({n24}, {n12}, {n8}) ≠ (24, 12, 8)",
        )
    print(f"  [OPE OK] Partición (24, 12, 8) canónica ✓")


def prueba_3_firmas_canonicas() -> None:
    """Cada operador debe tener 'dom' y 'cod' (firma canónica)."""
    for fuente, dicc in [
        ("heredado", OPERADORES_HEREDADOS_24),
        ("propio", OPERADORES_PROPIOS_12),
        ("emergente", OPERADORES_EMERGENTES_8),
    ]:
        for nombre, info in dicc.items():
            if "dom" not in info or "cod" not in info:
                raise SVError(
                    "LUZ-OPE-002",
                    f"Operador {fuente} '{nombre}' sin firma canónica (dom/cod)",
                )
    print(f"  [OPE OK] Los 44 operadores con firma canónica (dom, cod) ✓")


def prueba_4_ausencia_duplicados() -> None:
    """Ningún operador aparece en dos categorías distintas."""
    nombres_h = set(OPERADORES_HEREDADOS_24.keys())
    nombres_p = set(OPERADORES_PROPIOS_12.keys())
    nombres_e = set(OPERADORES_EMERGENTES_8.keys())
    if nombres_h & nombres_p:
        raise SVError("LUZ-OPE-003", f"Operador en heredados y propios: {nombres_h & nombres_p}")
    if nombres_h & nombres_e:
        raise SVError("LUZ-OPE-003", f"Operador en heredados y emergentes: {nombres_h & nombres_e}")
    if nombres_p & nombres_e:
        raise SVError("LUZ-OPE-003", f"Operador en propios y emergentes: {nombres_p & nombres_e}")
    total = len(nombres_h | nombres_p | nombres_e)
    if total != 44:
        raise SVError(
            "LUZ-OPE-003",
            f"Total de operadores únicos = {total} ≠ 44 (duplicados detectados)",
        )
    print(f"  [OPE OK] 44 operadores únicos (sin duplicados entre categorías) ✓")


def prueba_5_sin_axiomas_ajenos() -> None:
    """Ningún operador invoca axioma ajeno al corpus (P.5)."""
    patrones_prohibidos = ["hamiltoniano_soberano", "espacio_Hilbert",
                           "probabilidad_Kolmogorov", "métrica_soberana"]
    for dicc in [OPERADORES_HEREDADOS_24, OPERADORES_PROPIOS_12, OPERADORES_EMERGENTES_8]:
        for nombre, info in dicc.items():
            descriptor = str(info)
            for pat in patrones_prohibidos:
                if pat in descriptor:
                    raise SVError(
                        "LUZ-OPE-004",
                        f"Operador {nombre} invoca axioma ajeno: '{pat}'",
                    )
    print(f"  [OPE OK] Ningún operador invoca axioma ajeno al corpus (P.5 respetada) ✓")


def prueba_6_operadores_propios_con_referencia() -> None:
    """Los operadores propios deben apuntar a referencia del documento."""
    for nombre, info in OPERADORES_PROPIOS_12.items():
        if "ref" not in info:
            raise SVError(
                "LUZ-OPE-002",
                f"Operador propio '{nombre}' sin referencia al documento",
            )
    for nombre, info in OPERADORES_EMERGENTES_8.items():
        if "ref" not in info:
            raise SVError(
                "LUZ-OPE-002",
                f"Operador emergente '{nombre}' sin referencia al documento",
            )
    print(f"  [OPE OK] 12+8 operadores propios/emergentes con referencia al documento ✓")


def run() -> int:
    print("=" * 74)
    print("L-LUZ-10 — CUARENTA Y CUATRO OPERADORES DEL APARATO (§8)")
    print("=" * 74)
    prueba_1_cardinal_total_44()
    prueba_2_particion_24_12_8()
    prueba_3_firmas_canonicas()
    prueba_4_ausencia_duplicados()
    prueba_5_sin_axiomas_ajenos()
    prueba_6_operadores_propios_con_referencia()
    print("-" * 74)
    print("L-LUZ-10 — PASADO. 44 operadores canónicos inventariados sin duplicados.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(run())
    except SVError as e:
        print(f"\n[L-LUZ-10] FALLO código={e.codigo}")
        print(f"           mensaje: {e.mensaje}")
        sys.exit(1)
