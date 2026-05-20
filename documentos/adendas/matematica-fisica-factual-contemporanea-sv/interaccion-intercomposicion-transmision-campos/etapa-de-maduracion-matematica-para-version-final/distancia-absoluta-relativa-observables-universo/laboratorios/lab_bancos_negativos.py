#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Laboratorio de verificación por bancos negativos duros.
Título: «Distancia absoluta y relativa entre observables del Universo».
Autor: Juan Antonio Lloret Egea (https://es.linkedin.com/in/juanantoniolloretegea/) . ORCID: 0000-0002-6634-3351 (https://orcid.org/0000-0002-6634-3351) . ITVIA (https://itvia.online) . IA eñ™ — La Biblia de la IA™ . ISSN 2695-6411 (https://portal.issn.org/resource/ISSN/2695-6411) . Licencia CC BY-NC-ND 4.0 . Madrid, 19/05/2026.

Este laboratorio somete el aparato de transducción SV<->física contemporánea
a una batería de casos negativos canónicos: construcciones deliberadamente
erróneas cuyo veredicto correcto -el rechazo- lo fija la física reconocida,
no el Sistema Vectorial SV ni quien redacta. Junto a ellos se ejecuta una
batería de casos positivos bien formados, de modo que la verificación no
premie a un aparato que se limitase a rechazarlo todo: el aparato debe
aceptar lo correcto y rechazar lo erróneo. Si algún negativo no se rechaza,
o algún positivo no se acepta, el laboratorio no está terminado, y la salida
lo declara sin maquillaje.

La lógica de cada compuerta es general: inspecciona los atributos declarados
de un caso, no su identificador. El laboratorio no contiene, por tanto,
ninguna regla escrita a la medida de un caso concreto.

Sin dependencias externas. Ejecución: python lab_bancos_negativos.py
"""

# ----------------------------------------------------------------------
# Compuertas residuales del transductor.
# Cada compuerta reconoce una forma de error de plano y, al dispararse,
# devuelve su nombre y su codigo de catalogo.
# ----------------------------------------------------------------------

def c_regimen(d):
    """Δ_reg — ecuación empleada fuera de su régimen de validez."""
    if d.get("ecuacion") == "v=cz" and (d.get("z") or 0.0) > 0.1:
        return ("Δ_reg", "E-DIST-05")
    return None


def c_identidad_magnitudes(d):
    """Δ_m — identidad afirmada entre magnitudes no intercambiables."""
    ig = d.get("afirma_igualdad")
    if ig and set(ig) == {"D_L", "D_A"} and (d.get("z") or 0.0) > 0.0:
        return ("Δ_m", "E-DIST-06")
    return None


def c_magnitud_indeclarada(d):
    """Δ_m — afirmación cinemática sin declarar la magnitud sobre la que recae."""
    if d.get("afirmacion_cinematica") and not d.get("magnitud"):
        return ("Δ_m", "E-DIST-04")
    return None


def c_redshift_como_distancia(d):
    """Δ_m — corrimiento al rojo empleado como distancia directa, sin modelo."""
    if d.get("magnitud") == "z" and d.get("usado_como") == "distancia" \
            and not d.get("modelo"):
        return ("Δ_m", "E-DIST-03")
    return None


def c_origen_físicalizado(d):
    """Δ_orig — origen formal (0,0) espacializado, dimensionado o datado."""
    if d.get("observable") == "origen_formal":
        if d.get("unidad") in ("Mpc", "m", "ly", "a") \
                or d.get("interpretacion") == "big_bang_fisico":
            return ("Δ_orig", "E-DIST-08")
    return None


def c_totalidad_como_objeto(d):
    """Δ_Ω — la totalidad tratada como observable físico medible."""
    if d.get("observable") == "totalidad" \
            and d.get("magnitud") in ("D_P", "D_L", "D_A", "D_C", "edad"):
        return ("Δ_Ω", "E-DIST-07")
    return None


def c_retorno_como_edad(d):
    """Δ_Ω — retorno luminoso identificado con una edad absoluta."""
    if d.get("identifica_retorno_con_edad"):
        return ("Δ_Ω", "E-DIST-07")
    return None


def c_dominio_ausente(d):
    """Δ_Ω — distancia declarada sin dominio de observable."""
    if d.get("magnitud") in ("D_L", "D_A", "D_C", "D_P") \
            and not d.get("observable"):
        return ("Δ_Ω", "E-DIST-01")
    return None


def c_rutas_H0_sin_tipado(d):
    """Δ_H — rutas distintas de H_0 combinadas sin declaración de tipo."""
    rutas = d.get("rutas_H0")
    if rutas and len(rutas) > 1 and not d.get("tipado_ruta"):
        return ("Δ_H", "E-DIST-09")
    return None


def c_refutacion_sin_residual(d):
    """Δ_𝓑 — observación extrema como refutación global, sin residual computado."""
    if d.get("refutacion_global") and not d.get("residual_computado"):
        return ("Δ_𝓑", "E-DIST-10")
    return None


def c_evidencia_no_cerrada(d):
    """Δ_ret — evidencia no cerrada presentada como cierre definitivo."""
    if d.get("evidencia_no_cerrada") and d.get("declara_cierre_definitivo"):
        return ("Δ_ret", "E-DIST-09")
    return None


def c_coincidencia_sin_residual(d):
    """Δ_T — coincidencia SV<->física declarada sin residual computado."""
    if d.get("declara_coincidencia_sv_fc") and not d.get("residual_computado"):
        return ("Δ_T", "E-DIST-10")
    return None


def c_unidad_ausente(d):
    """Δ_u — magnitud métrica o dimensional declarada sin unidad."""
    if d.get("magnitud") in ("D_L", "D_A", "D_C", "D_M", "D_P", "H_0",
                             "v_rec", "separacion") and not d.get("unidad"):
        return ("Δ_u", "E-DIST-02")
    return None


def c_retorno_ausente(d):
    """Δ_ret — caso proyectado al SV que no retorna al dominio físico."""
    if d.get("proyectado_a_SV") and not d.get("retorno_fisico"):
        return ("Δ_ret", "E-DIST-11")
    return None


COMPUERTAS = [
    c_regimen, c_identidad_magnitudes, c_magnitud_indeclarada,
    c_redshift_como_distancia, c_origen_físicalizado, c_totalidad_como_objeto,
    c_retorno_como_edad, c_dominio_ausente, c_rutas_H0_sin_tipado,
    c_refutacion_sin_residual, c_evidencia_no_cerrada,
    c_coincidencia_sin_residual, c_unidad_ausente, c_retorno_ausente,
]


def verificar(decl):
    """Aplica todas las compuertas. Devuelve (dictamen, lista de disparos)."""
    disparos = [r for r in (c(decl) for c in COMPUERTAS) if r is not None]
    dictamen = "NO_APTO" if disparos else "APTO"
    return dictamen, disparos


# ----------------------------------------------------------------------
# Banco positivo: casos bien formados. El aparato debe ACEPTARLOS (APTO).
# Su función es impedir que un aparato que se limitase a rechazarlo todo
# superase la batería negativa de forma trivial.
# ----------------------------------------------------------------------

POSITIVOS = [
    {"id": "P-01",
     "desc": "D_L de SN Ia calibrada, z=0.1, FLRW-LCDM, unidad declarada",
     "decl": {"observable": "SN_Ia", "magnitud": "D_L", "unidad": "Mpc",
              "modelo": "FLRW_LCDM", "z": 0.1}},
    {"id": "P-02",
     "desc": "v=cz aplicada en su regimen local, z=0.02, unidad declarada",
     "decl": {"observable": "galaxia", "magnitud": "v_rec", "ecuacion": "v=cz",
              "unidad": "km/s", "modelo": "low_z_Hubble", "regimen": "low_z",
              "z": 0.02}},
    {"id": "P-03",
     "desc": "D_A de cumulo por regla estandar BAO, modelo declarado",
     "decl": {"observable": "cumulo_BAO", "magnitud": "D_A", "unidad": "Mpc",
              "modelo": "FLRW_LCDM", "z": 0.5}},
    {"id": "P-04",
     "desc": "H_0 de ruta local unica, tipada",
     "decl": {"observable": "cefeidas", "magnitud": "H_0", "unidad": "km/s/Mpc",
              "rutas_H0": ["local"], "tipado_ruta": True}},
    {"id": "P-05",
     "desc": "Separacion relativa entre dos galaxias, metrica homogenea",
     "decl": {"observable": "par_galaxias", "magnitud": "separacion",
              "unidad": "Mpc", "modelo": "FLRW_LCDM", "z": 0.3}},
    {"id": "P-06",
     "desc": "Coincidencia SV-física con residual computado y retorno físico",
     "decl": {"observable": "SN_Ia", "magnitud": "D_L", "unidad": "Mpc",
              "modelo": "FLRW_LCDM", "z": 0.1,
              "declara_coincidencia_sv_fc": True, "residual_computado": True,
              "proyectado_a_SV": True, "retorno_fisico": True}},
]

# ----------------------------------------------------------------------
# Banco negativo: construcciones deliberadamente erroneas. El aparato debe
# RECHAZARLAS (NO_APTO) y disparar la compuerta esperada. El veredicto
# correcto de cada caso lo fija la física reconocida, no el SV.
# ----------------------------------------------------------------------

NEGATIVOS = [
    {"id": "N-01", "comp_esp": "Δ_reg",
     "desc": "v=cz aplicada a z=6 como velocidad ordinaria",
     "decl": {"observable": "galaxia", "magnitud": "v_rec", "ecuacion": "v=cz",
              "unidad": "km/s", "regimen": "high_z", "z": 6.0}},
    {"id": "N-02", "comp_esp": "Δ_m",
     "desc": "Distancia de luminosidad igualada a la angular en z=2",
     "decl": {"observable": "galaxia", "afirma_igualdad": ("D_L", "D_A"),
              "z": 2.0}},
    {"id": "N-03", "comp_esp": "Δ_orig",
     "desc": "Origen formal (0,0) interpretado como Big Bang fisico",
     "decl": {"observable": "origen_formal",
              "interpretacion": "big_bang_fisico"}},
    {"id": "N-04", "comp_esp": "Δ_Ω",
     "desc": "Distancia física atribuida a la totalidad absoluta",
     "decl": {"observable": "totalidad", "magnitud": "D_P", "unidad": "Mpc"}},
    {"id": "N-05", "comp_esp": "Δ_H",
     "desc": "H_0 local y H_0 CMB combinadas sin tipado de ruta",
     "decl": {"observable": "mixto", "magnitud": "H_0", "unidad": "km/s/Mpc",
              "rutas_H0": ["local", "CMB"], "tipado_ruta": False}},
    {"id": "N-06", "comp_esp": "Δ_m",
     "desc": "«La velocidad aumenta» sin declarar la magnitud",
     "decl": {"observable": "galaxia", "afirmacion_cinematica": True,
              "magnitud": None}},
    {"id": "N-07", "comp_esp": "Δ_𝓑",
     "desc": "Galaxia JWST como refutacion global de LCDM, sin residual",
     "decl": {"observable": "galaxia_JWST", "z": 14.0,
              "refutacion_global": True, "residual_computado": False}},
    {"id": "N-08", "comp_esp": "Δ_ret",
     "desc": "Energia oscura dinamica declarada cierre definitivo",
     "decl": {"observable": "DESI", "evidencia_no_cerrada": True,
              "declara_cierre_definitivo": True}},
    {"id": "N-09", "comp_esp": "Δ_Ω",
     "desc": "Retorno luminoso confundido con edad absoluta",
     "decl": {"observable": "galaxia", "identifica_retorno_con_edad": True}},
    {"id": "N-10", "comp_esp": "Δ_T",
     "desc": "Coincidencia SV-física declarada sin residual computado",
     "decl": {"observable": "SN_Ia", "declara_coincidencia_sv_fc": True,
              "residual_computado": False}},
    {"id": "N-11", "comp_esp": "Δ_m",
     "desc": "Corrimiento al rojo usado como distancia directa, sin modelo",
     "decl": {"observable": "galaxia", "magnitud": "z",
              "usado_como": "distancia", "modelo": None, "z": 1.2}},
    {"id": "N-12", "comp_esp": "Δ_orig",
     "desc": "Origen formal (0,0) dimensionado en megaparsecs",
     "decl": {"observable": "origen_formal", "unidad": "Mpc"}},
    {"id": "N-13", "comp_esp": "Δ_Ω",
     "desc": "Distancia de luminosidad sin dominio de observable",
     "decl": {"magnitud": "D_L", "observable": None, "unidad": "Mpc"}},
    {"id": "N-14", "comp_esp": "Δ_u",
     "desc": "Distancia de luminosidad declarada sin unidad",
     "decl": {"observable": "galaxia", "magnitud": "D_L",
              "modelo": "FLRW_LCDM", "z": 0.5}},
    {"id": "N-15", "comp_esp": "Δ_ret",
     "desc": "Caso proyectado al SV sin retorno físico al dominio observable",
     "decl": {"observable": "SN_Ia", "magnitud": "D_L", "unidad": "Mpc",
              "modelo": "FLRW_LCDM", "z": 0.1,
              "proyectado_a_SV": True, "retorno_fisico": False}},
]


# ----------------------------------------------------------------------
# Ejecución de la batería y emisión de la tabla de resultados.
# ----------------------------------------------------------------------

def ejecutar():
    filas, fallos = [], []

    for caso in POSITIVOS:
        dictamen, disparos = verificar(caso["decl"])
        codigos = ", ".join(f"{c}/{e}" for c, e in disparos) or "—"
        ok = (dictamen == "APTO")
        if not ok:
            fallos.append((caso["id"], "se esperaba APTO", dictamen, codigos))
        filas.append((caso["id"], "positivo", "APTO", dictamen, codigos,
                      "OK" if ok else "FALLO"))

    for caso in NEGATIVOS:
        dictamen, disparos = verificar(caso["decl"])
        comps = [c for c, _ in disparos]
        codigos = ", ".join(f"{c}/{e}" for c, e in disparos) or "—"
        esp = caso["comp_esp"]
        ok = (dictamen == "NO_APTO") and (esp in comps)
        if not ok:
            fallos.append((caso["id"], f"se esperaba NO_APTO con {esp}",
                           dictamen, codigos))
        filas.append((caso["id"], "negativo", f"NO_APTO/{esp}", dictamen,
                      codigos, "OK" if ok else "FALLO"))

    return filas, fallos


def imprimir(filas, fallos):
    print("=" * 80)
    print("  Autor: Juan Antonio Lloret Egea (https://es.linkedin.com/in/juanantoniolloretegea/) . ORCID: 0000-0002-6634-3351 (https://orcid.org/0000-0002-6634-3351) . ITVIA (https://itvia.online) . IA eñ™ — La Biblia de la IA™ . ISSN 2695-6411 (https://portal.issn.org/resource/ISSN/2695-6411) . Licencia CC BY-NC-ND 4.0 . Madrid, 19/05/2026")
    print("  BATERÍA DE BANCOS NEGATIVOS - TRANSDUCTOR DE DISTANCIA SV↔FÍSICA")
    print("=" * 80)
    fmt = "{:<6} {:<9} {:<15} {:<9} {:<28} {:<6}"
    print(fmt.format("CASO", "TIPO", "ESPERADO", "OBTENIDO",
                     "COMPUERTA / CÓDIGO", "JUICIO"))
    print("-" * 80)
    for f in filas:
        print(fmt.format(*f))
    print("-" * 80)

    pos = [f for f in filas if f[1] == "positivo"]
    neg = [f for f in filas if f[1] == "negativo"]
    pos_ok = sum(1 for f in pos if f[5] == "OK")
    neg_ok = sum(1 for f in neg if f[5] == "OK")
    print(f"  Positivos aceptados (APTO)                          : "
          f"{pos_ok}/{len(pos)}")
    print(f"  Negativos rechazados (NO_APTO, compuerta correcta)  : "
          f"{neg_ok}/{len(neg)}")
    print("-" * 80)
    if not fallos:
        print("  DICTAMEN DEL LABORATORIO: BATERÍA SUPERADA.")
        print("  El transductor acepta todo caso correcto y rechaza todo error")
        print("  canónico construido: error cero de plano sobre la batería.")
    else:
        print("  DICTAMEN DEL LABORATORIO: BATERÍA NO SUPERADA.")
        print("  El laboratorio NO está terminado. Discrepancias:")
        for cid, motivo, obt, cod in fallos:
            print(f"    - {cid}: {motivo}; obtenido {obt} [{cod}]")
    print("=" * 80)
    return not fallos


if __name__ == "__main__":
    import sys
    filas, fallos = ejecutar()
    superada = imprimir(filas, fallos)
    sys.exit(0 if superada else 1)
