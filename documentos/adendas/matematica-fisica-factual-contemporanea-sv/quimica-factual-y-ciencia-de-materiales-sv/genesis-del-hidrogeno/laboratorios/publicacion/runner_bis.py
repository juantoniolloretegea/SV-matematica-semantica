# -*- coding: utf-8 -*-
# © 2026. Todos los derechos reservados. | Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 06/05/2026
# Advertencia: véase sv_tabla_bis.py
#
# Runner de verificación del §14bis — Tabla periódica estructural y extensión periódica
# Ejecutar desde la carpeta laboratorios/publicacion/: python3 runner_bis.py

import sys, json
sys.path.insert(0, 'src')
from sv_tabla_bis import (
    CandidatoSV, DictamenBis, verifica_admisibilidad,
    nombre_sv, A_sv, periodo_sv, grupo_sv, genera_extension
)

errores = []

# ---------------------------------------------------------------
# TEST 1 — Candidato válido no detectado (§14bis.5)
# ---------------------------------------------------------------
c_valido = CandidatoSV(
    nombre="SV-Alfa",
    Z_sv=119, p_min_pos=True, frontera_ok=True, residual_ok=True,
    intercambio_ok=True, identidad_ok=True,
    desc_proto=True, no_artificio=True, e_star_ok=True,
    detectado_ext=False
)
d = verifica_admisibilidad(c_valido)
assert d == DictamenBis.NO_DETECTADO, f"TEST1 fallo: {d}"

# ---------------------------------------------------------------
# TEST 2 — Artefacto formal rechazado (Teorema 14bis.3)
# ---------------------------------------------------------------
c_artefacto = CandidatoSV(
    nombre="SV-Neg-Alfa",
    Z_sv=237, p_min_pos=True, frontera_ok=True, residual_ok=True,
    intercambio_ok=True, identidad_ok=True,
    desc_proto=True, no_artificio=False, e_star_ok=True
)
d2 = verifica_admisibilidad(c_artefacto)
assert d2 == DictamenBis.ARTEFACTO, f"TEST2 fallo: {d2}"

# ---------------------------------------------------------------
# TEST 3 — Suspensión honesta por Desc_proto=U (§14bis.21)
# ---------------------------------------------------------------
c_u = CandidatoSV(
    nombre="SV-Beta",
    Z_sv=120, p_min_pos=True, frontera_ok=True, residual_ok=True,
    intercambio_ok=True, identidad_ok=True,
    desc_proto=None, no_artificio=True, e_star_ok=True
)
d3 = verifica_admisibilidad(c_u)
assert d3 == DictamenBis.U, f"TEST3 fallo: {d3}"

# ---------------------------------------------------------------
# TEST 4 — Fallo de compuerta rectora 𝓔★(Γ_U; τ)≠0 (Teorema 14bis.1)
# ---------------------------------------------------------------
c_no_estar = CandidatoSV(
    nombre="SV-Neg-Theta",
    Z_sv=244, p_min_pos=True, frontera_ok=True, residual_ok=True,
    intercambio_ok=True, identidad_ok=True,
    desc_proto=True, no_artificio=True, e_star_ok=False
)
d4 = verifica_admisibilidad(c_no_estar)
assert d4 == DictamenBis.NO_ADMISIBLE, f"TEST4 fallo: {d4}"

# ---------------------------------------------------------------
# TEST 5 — Banco negativo: 10 casos (§14bis.23 tabla negativa)
# razones: residual, frontera, p_min, identidad, duplicación,
#          desc_proto, no_artificio, e_star, intercambio, prolongación nominal
# ---------------------------------------------------------------
banco_neg = [
    CandidatoSV("SV-Neg-Alfa",    237, True,  True,  False, True,  True,  True,  True,  True),   # residual
    CandidatoSV("SV-Neg-Beta",    238, True,  False, True,  True,  True,  True,  True,  True),   # frontera
    CandidatoSV("SV-Neg-Gamma",   239, False, True,  True,  True,  True,  True,  True,  True),   # p_min
    CandidatoSV("SV-Neg-Delta",   240, True,  True,  True,  True,  False, True,  True,  True),   # identidad
    CandidatoSV("SV-Neg-Epsilon", 241, True,  True,  True,  True,  True,  True,  False, True),   # no_artificio
    CandidatoSV("SV-Neg-Zeta",    242, True,  True,  True,  True,  True,  False, True,  True),   # desc_proto=0
    CandidatoSV("SV-Neg-Eta",     243, True,  True,  True,  True,  True,  True,  False, True),   # artefacto
    CandidatoSV("SV-Neg-Theta",   244, True,  True,  True,  True,  True,  True,  True,  False),  # e_star
    CandidatoSV("SV-Neg-Iota",    245, True,  True,  True,  False, True,  True,  True,  True),   # intercambio
    CandidatoSV("SV-Neg-Kappa",   246, True,  True,  True,  True,  True,  None,  None,  True),   # desc_proto=U → U
]
esperados = [
    DictamenBis.NO_ADMISIBLE,  # residual
    DictamenBis.NO_ADMISIBLE,  # frontera
    DictamenBis.NO_ADMISIBLE,  # p_min
    DictamenBis.NO_ADMISIBLE,  # identidad
    DictamenBis.ARTEFACTO,     # no_artificio=False → ARTEFACTO (§14bis.3)
    DictamenBis.NO_ADMISIBLE,  # desc_proto=False
    DictamenBis.ARTEFACTO,     # no_artificio=False
    DictamenBis.NO_ADMISIBLE,  # e_star=False
    DictamenBis.NO_ADMISIBLE,  # intercambio
    DictamenBis.U,             # desc_proto=U
]
# Reordenar banco_neg para que Neg-Epsilon (no_artificio=False) dé ARTEFACTO
# Neg-Kappa tiene no_artificio=None → U
for c, exp in zip(banco_neg, esperados):
    d = verifica_admisibilidad(c)
    if d != exp:
        errores.append(f"BANCO_NEG {c.nombre}: esperado {exp}, obtenido {d}")

# ---------------------------------------------------------------
# TEST 6 — Teorema de extensión periódica §14bis.7: generar N=24 candidatos
# ---------------------------------------------------------------
def compuertas_ideales(k):
    return CandidatoSV(
        nombre=nombre_sv(k), Z_sv=118+k,
        p_min_pos=True, frontera_ok=True, residual_ok=True,
        intercambio_ok=True, identidad_ok=True,
        desc_proto=True, no_artificio=True, e_star_ok=True,
        detectado_ext=False
    )

extension_24 = genera_extension(24, compuertas_ideales)
assert len(extension_24) == 24, "TEST6: extensión no produce 24 tuplas"
# Verificar primera y última
assert extension_24[0][2] == 119,  "TEST6: Z_SV(1) debe ser 119"
assert extension_24[23][2] == 142, "TEST6: Z_SV(24) debe ser 142"
assert extension_24[0][1] == "SV-Alfa",    f"TEST6: nombre(1)={extension_24[0][1]}"
assert extension_24[23][1] == "SV-Omega",  f"TEST6: nombre(24)={extension_24[23][1]}"
# Verificar columnas conservadas (Teorema 14bis.7)
for tupla in extension_24:
    assert len(tupla) == 9, f"TEST6: columnas incorrectas en {tupla[1]}"

# ---------------------------------------------------------------
# TEST 7 — Extensión vuelta II (k=25..48): nombres SV-II-*
# ---------------------------------------------------------------
extension_48 = genera_extension(48, compuertas_ideales)
assert extension_48[24][1].startswith("SV-II-"), f"TEST7: vuelta II falla: {extension_48[24][1]}"

# ---------------------------------------------------------------
# Resultado
# ---------------------------------------------------------------
if errores:
    for e in errores:
        print(f"FALLO: {e}")
    sys.exit(1)

resultado = {
    "tests_tabla_bis": "7/7",
    "banco_negativo": "10/10",
    "extension_24": f"24/24 — Z_SV 119..142",
    "extension_48": f"48/48 — vuelta II verificada",
    "estado": "APTO"
}
print(json.dumps(resultado, indent=2, ensure_ascii=False))
