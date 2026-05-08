# -*- coding: utf-8 -*-
# © 2026. Todos los derechos reservados. | Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351
# Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
# IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 08/05/2026
# Advertencia: esta publicación está protegida por CEDRO. Uso comercial prohibido sin autorización.
# Warning: this publication is protected by CEDRO. Commercial use prohibited without authorization.
#
# Módulo: sv_443
# Función: verificación del catálogo completo de 443 elementos químicos del Sistema Vectorial SV
# Referencia doctrinal: Lloret Egea (2026), Elementos químicos del SV, §7 y §13
# Referencia corpus: Teoría del TODO y de la NADA SV §14.5; Sucesos generadores §2
#
# Códigos de error: SV-443-COUNT, SV-443-HEADER, SV-443-Z-{k}, SV-443-A-{k},
#   SV-443-P-{k}, SV-443-G-{k}, SV-443-DENS-{k}, SV-443-EN-{k}, SV-443-EI-{k},
#   SV-443-RADIO-{k}, SV-443-AFIN-{k}, SV-443-METAL-{k}, SV-443-KTERM-{k},
#   SV-443-MUR-{k}, SV-443-MOHS-{k}, SV-443-RES-{k}, SV-443-ROZ-{k},
#   SV-443-FLEX-{k}, SV-443-MALE-{k}, SV-443-OXID-{k}, SV-443-CORR-{k},
#   SV-443-TMAX-{k}, SV-443-VOL-{k}, SV-443-RAD-{k}, SV-443-ISO-{k},
#   SV-443-NOMBRE-{k}, SV-443-CONFIG-{k}, SV-443-ESTADO-{k}, SV-443-FUNC-{k},
#   SV-443-APLIC-CI-{k}, SV-443-APLIC-AE-{k}, SV-443-APLIC-MED-{k},
#   SV-443-DUPZ, SV-443-FLOAT-{col}-{k}, SV-443-ORDEN

from __future__ import annotations
import csv
import math
from pathlib import Path
from typing import List

# ── Constantes del corpus ──────────────────────────────────────────────────────
N_ELEMENTOS = 443
N_COLUMNAS  = 33

ESTADOS_VALIDOS = {
    "sólido metálico", "sólido semimetálico",
    "gas reactivo pesado", "gas noble denso"
}

# Columnas numéricas y sus rangos [min, max] (None = sin límite en esa dirección)
# Índices en el CSV (0-based, tras saltar filas de comentario):
# 0=Nº 1=Nombre 2=Z_SV 3=A_SV 4=Config 5=Periodo 6=Grupo 7=Estado 8=Densidad
# 9=Conduct 10=EN 11=Eion 12=Radio 13=Afinidad 14=Metal 15=Ktérm 16=μr
# 17=Mohs 18=ResistFis 19=Roz 20=Flex 21=Male 22=Oxid 23=Corr 24=Tmax
# 25=Vol 26=TintStr 27=Radi 28=Niso 29=Func 30=CI 31=AE 32=Med

RANGOS_NUMERICOS = {
    8:  ("DENS",   0.001, 1000,    "Densidad_SV_g_cm3"),
    9:  ("CONDUCT",0.0,   200,     "Conductividad_electrica_MS_m"),
    10: ("EN",     0.0,   4.0,     "Electronegatividad_SV"),
    11: ("EI",     0.0,   5000,    "Energia_ionizacion_kJ_mol"),
    12: ("RADIO",  0.0,   1000,    "Radio_atomico_SV_pm"),
    13: ("AFIN",   0.0,   2.5,     "Afinidad_electronica_eV"),  # halógenos SV-118 alcanzan ~2.12
    14: ("METAL",  0.0,   100.0,   "Caracter_metalico_SV_pct"),
    15: ("KTERM",  0.0,   1000,    "Conductividad_termica_W_mK"),
    16: ("MUR",    0.9,   1.2,     "Permeabilidad_SV_mu_r"),
    17: ("MOHS",   0.0,   15.0,    "Dureza_SV_Mohs"),
    18: ("RES",    0.0,   10000,   "Resistencia_fisica_MPa"),
    19: ("ROZ",    0.0,   1.0,     "Coef_rozamiento_SV"),
    20: ("FLEX",   0.0,   1.0,     "Flexibilidad_SV_0_1"),
    21: ("MALE",   0.0,   1.0,     "Maleabilidad_SV_0_1"),
    22: ("OXID",   0.0,   100.0,   "Resistencia_oxidacion_SV_0_100"),
    23: ("CORR",   0.0,   100.0,   "Resistencia_corrosion_SV_0_100"),
    25: ("VOL",    0.001, 10000,   "Volumen_atomico_SV_A3"),
    27: ("RAD",    0.0,   100.0,   "Nivel_radiactivo_SV_0_100"),
    28: ("ISO",    1,     200,     "Num_isotopos_SV"),
}

COLUMNAS_TEXTO_OBLIGATORIO = {
    1:  "Nombre_SV",
    4:  "Config_electronica",
    7:  "Estado_STP_SV",
    29: "Funcion_estructural_SV",
    30: "Aplicacion_cientifica_SV",
    31: "Aplicacion_aeroespacial_SV",
    32: "Aplicacion_medica_SV",
}


# ── Fórmulas canónicas del corpus ──────────────────────────────────────────────

def Z_sv(k: int) -> int:
    return 118 + k

def A_sv(k: int) -> int:
    return 294 + 3 * k + k // 2

def periodo(k: int) -> int:
    return 8 + (k - 1) // 18

def grupo(k: int) -> int:
    return 1 + (k - 1) % 18


# ── Carga del CSV ignorando filas de metadatos ─────────────────────────────────

def cargar_csv(ruta: Path) -> tuple[list[str], list[list[str]]]:
    """Devuelve (cabecera, filas_de_datos). Lanza SV-443-COUNT si falla."""
    with open(ruta, encoding="utf-8") as f:
        lines_raw = list(f)

    # Ignorar líneas de comentario (empiezan por # o ©)
    lines = [l for l in lines_raw
             if not l.startswith('#') and not l.startswith('©')]

    reader = list(csv.reader(lines))
    if not reader:
        raise ValueError("SV-443-COUNT: archivo CSV vacío")

    cabecera = reader[0]
    filas = [r for r in reader[1:] if r and r[0].strip().isdigit()]
    return cabecera, filas


# ── Verificaciones ─────────────────────────────────────────────────────────────

def verificar_cabecera(cabecera: list[str]) -> List[str]:
    errores = []
    if len(cabecera) != N_COLUMNAS:
        errores.append(
            f"SV-443-HEADER: se esperaban {N_COLUMNAS} columnas, "
            f"se encontraron {len(cabecera)}"
        )
    return errores


def verificar_count(filas: list) -> List[str]:
    errores = []
    if len(filas) != N_ELEMENTOS:
        errores.append(
            f"SV-443-COUNT: se esperaban {N_ELEMENTOS} filas de datos, "
            f"se encontraron {len(filas)}"
        )
    return errores


def verificar_orden(filas: list) -> List[str]:
    """Los valores de Nº deben ser 1, 2, 3, …, 443 sin saltos ni repeticiones."""
    errores = []
    for i, r in enumerate(filas):
        k_esperado = i + 1
        try:
            k_real = int(r[0])
        except (ValueError, IndexError):
            errores.append(f"SV-443-ORDEN: fila {i+1} tiene Nº no numérico: {r[0]!r}")
            continue
        if k_real != k_esperado:
            errores.append(
                f"SV-443-ORDEN: posición {i+1} tiene Nº={k_real}, esperado {k_esperado}"
            )
    return errores


def verificar_formulas(filas: list) -> List[str]:
    """Comprueba Z_SV, A_SV, Periodo y Grupo para cada k."""
    errores = []
    for r in filas:
        try:
            k = int(r[0])
        except ValueError:
            continue  # ya capturado por verificar_orden

        # Z_SV
        try:
            z = int(r[2])
        except (ValueError, IndexError):
            errores.append(f"SV-443-Z-{k}: valor no entero en Z_SV: {r[2]!r}")
        else:
            if z != Z_sv(k):
                errores.append(
                    f"SV-443-Z-{k}: Z_SV={z}, esperado {Z_sv(k)} "
                    f"(fórmula 118+k)"
                )

        # A_SV
        try:
            a = int(r[3])
        except (ValueError, IndexError):
            errores.append(f"SV-443-A-{k}: valor no entero en Masa_SV_u: {r[3]!r}")
        else:
            if a != A_sv(k):
                errores.append(
                    f"SV-443-A-{k}: Masa_SV_u={a}, esperada {A_sv(k)} "
                    f"(fórmula 294+3k+k//2)"
                )

        # Periodo
        try:
            p = int(r[5])
        except (ValueError, IndexError):
            errores.append(f"SV-443-P-{k}: valor no entero en Periodo: {r[5]!r}")
        else:
            if p != periodo(k):
                errores.append(
                    f"SV-443-P-{k}: Periodo={p}, esperado {periodo(k)} "
                    f"(fórmula 8+floor((k-1)/18))"
                )

        # Grupo
        try:
            g = int(r[6])
        except (ValueError, IndexError):
            errores.append(f"SV-443-G-{k}: valor no entero en Grupo: {r[6]!r}")
        else:
            if g != grupo(k):
                errores.append(
                    f"SV-443-G-{k}: Grupo={g}, esperado {grupo(k)} "
                    f"(fórmula 1+((k-1)%18))"
                )
    return errores


def verificar_rangos(filas: list) -> List[str]:
    """Comprueba rangos numéricos de todas las columnas con límites definidos."""
    errores = []
    for r in filas:
        try:
            k = int(r[0])
        except ValueError:
            continue
        g = grupo(k)

        for col_idx, (codigo, vmin, vmax, nombre) in RANGOS_NUMERICOS.items():
            try:
                v = float(r[col_idx])
            except (ValueError, IndexError):
                errores.append(
                    f"SV-443-FLOAT-{codigo}-{k}: valor no numérico en "
                    f"{nombre} (col {col_idx}): {r[col_idx]!r}"
                )
                continue

            if vmin is not None and v < vmin:
                errores.append(
                    f"SV-443-{codigo}-{k}: {nombre}={v} < mínimo {vmin}"
                )
            if vmax is not None and v > vmax:
                errores.append(
                    f"SV-443-{codigo}-{k}: {nombre}={v} > máximo {vmax}"
                )

        # Temperatura de cambio: gases deben tener Tmax < 100 °C
        try:
            tmax = float(r[24])
            if g == 18 and tmax > 50:
                errores.append(
                    f"SV-443-TMAX-{k}: gas noble (G=18) con T_max={tmax} °C > 50 "
                    f"(esperado negativo o muy bajo)"
                )
        except (ValueError, IndexError):
            errores.append(f"SV-443-FLOAT-TMAX-{k}: Resistencia_termica_max_C no numérico: {r[24]!r}")

    return errores


def verificar_textos(filas: list) -> List[str]:
    """Comprueba que las columnas de texto obligatorio no estén vacías."""
    errores = []
    for r in filas:
        try:
            k = int(r[0])
        except ValueError:
            continue
        for col_idx, nombre in COLUMNAS_TEXTO_OBLIGATORIO.items():
            try:
                v = r[col_idx].strip()
            except IndexError:
                errores.append(
                    f"SV-443-{nombre.upper()[:6]}-{k}: columna {nombre} "
                    f"(índice {col_idx}) ausente"
                )
                continue
            if not v:
                errores.append(
                    f"SV-443-VACIO-{nombre[:6].upper()}-{k}: {nombre} vacío"
                )

    return errores


def verificar_estado(filas: list) -> List[str]:
    """Comprueba que Estado_STP_SV sea uno de los valores válidos."""
    errores = []
    for r in filas:
        try:
            k = int(r[0])
        except ValueError:
            continue
        try:
            est = r[7].strip()
        except IndexError:
            errores.append(f"SV-443-ESTADO-{k}: columna Estado_STP_SV ausente")
            continue
        if est not in ESTADOS_VALIDOS:
            errores.append(
                f"SV-443-ESTADO-{k}: valor {est!r} no es uno de "
                f"{sorted(ESTADOS_VALIDOS)}"
            )
    return errores


def verificar_duplicados_z(filas: list) -> List[str]:
    """Comprueba que no haya valores duplicados de Z_SV."""
    errores = []
    vistos: dict[int, int] = {}
    for r in filas:
        try:
            k = int(r[0])
            z = int(r[2])
        except (ValueError, IndexError):
            continue
        if z in vistos:
            errores.append(
                f"SV-443-DUPZ: Z_SV={z} aparece en k={vistos[z]} y k={k}"
            )
        else:
            vistos[z] = k
    return errores


# ── Verificación completa ──────────────────────────────────────────────────────

def verificar_todo(ruta_csv: Path) -> List[str]:
    """
    Ejecuta todas las verificaciones sobre el CSV del catálogo SV-443.
    Devuelve la lista completa de errores encontrados (vacía si APTO).
    Ningún error se captura de forma silenciosa; cada uno tiene código específico.
    """
    errores: List[str] = []

    # Carga
    try:
        cabecera, filas = cargar_csv(ruta_csv)
    except Exception as exc:
        return [f"SV-443-LOAD: no se pudo leer el CSV — {exc}"]

    errores += verificar_cabecera(cabecera)
    errores += verificar_count(filas)

    # Si el count es erróneo, algunas verificaciones posteriores pueden ser
    # inconsistentes; se continúa para reportar tantos errores como sea posible.
    errores += verificar_orden(filas)
    errores += verificar_formulas(filas)
    errores += verificar_rangos(filas)
    errores += verificar_textos(filas)
    errores += verificar_estado(filas)
    errores += verificar_duplicados_z(filas)

    return errores
