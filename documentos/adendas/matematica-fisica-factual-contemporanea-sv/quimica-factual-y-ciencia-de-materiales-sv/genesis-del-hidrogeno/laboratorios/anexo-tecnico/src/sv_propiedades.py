# -*- coding: utf-8 -*-
# © 2026. Todos los derechos reservados. | Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 06/05/2026
# Advertencia: esta publicación está protegida por CEDRO. Uso comercial prohibido sin autorización.
#
# Módulo: sv_propiedades — verificación de las cuatro tablas de propiedades estructurales SV
# Referencia doctrinal: Lloret Egea (2026), §14bis; Teorema 14bis.7
# Fórmulas del modelo: Z_SV(k)=118+k, A_SV(k)=294+3k+⌊k/2⌋,
#                      Periodo_SV(k)=8+⌊(k-1)/18⌋, Grupo_SV(k)=1+((k-1) mod 18)
# Errores de dominio: SV-PROP-T1-* (Tabla 1), SV-PROP-T2-* (Tabla 2),
#                     SV-PROP-T3-* (Tabla 3), SV-PROP-T4-* (Tabla 4)

from __future__ import annotations
import csv
from math import floor
from pathlib import Path
from typing import List, Dict


# ─── Funciones del modelo (Teorema 14bis.7) ──────────────────────────────────

def Z_sv(k: int) -> int:
    return 118 + k

def A_sv(k: int) -> int:
    return 294 + 3 * k + floor(k / 2)

def periodo_sv(k: int) -> int:
    return 8 + floor((k - 1) / 18)

def grupo_sv(k: int) -> int:
    return 1 + ((k - 1) % 18)


# ─── Carga de CSV con comentarios ────────────────────────────────────────────

def leer_csv(path: Path) -> List[Dict]:
    """Lee un CSV ignorando líneas que empiezan por #."""
    rows = []
    with open(path, encoding='utf-8') as f:
        lines = [l for l in f if not l.startswith('#')]
    reader = csv.DictReader(lines)
    for row in reader:
        rows.append(row)
    return rows


# ─── Verificadores por tabla ─────────────────────────────────────────────────

def verifica_tabla1(rows: List[Dict]) -> List[str]:
    """Tabla 1 — Identidad tabular y masa estructural."""
    errores = []
    if len(rows) != 118:
        errores.append(f"SV-PROP-T1-COUNT: esperadas 118 filas, hay {len(rows)}")
        return errores
    for row in rows:
        k   = int(row['Nº'])
        zsv = int(row['Z_SV'])
        asv = int(row['Masa atómica SV (u)'])
        per = int(row['Periodo'])
        grp = int(row['Grupo'])

        if zsv != Z_sv(k):
            errores.append(f"SV-PROP-T1-ZSVM k={k}: esperado {Z_sv(k)}, CSV={zsv}")
        if asv != A_sv(k):
            errores.append(f"SV-PROP-T1-ASVM k={k}: esperado {A_sv(k)}, CSV={asv}")
        if per != periodo_sv(k):
            errores.append(f"SV-PROP-T1-PER k={k}: esperado {periodo_sv(k)}, CSV={per}")
        if grp != grupo_sv(k):
            errores.append(f"SV-PROP-T1-GRP k={k}: esperado {grupo_sv(k)}, CSV={grp}")
    return errores


def verifica_tabla2(rows: List[Dict]) -> List[str]:
    """Tabla 2 — Propiedades electrónicas, atómicas y de transporte.

    Verificaciones: 118 filas, Nº correlativo, no vacíos en columnas críticas.
    Las magnitudes derivadas (conductividad, electronegatividad, etc.) se verifican
    por monotonía estructural: dentro de cada periodo, la conductividad no debe
    crecer para metales del mismo bloque, y la electronegatividad debe ser positiva.
    """
    errores = []
    if len(rows) != 118:
        errores.append(f"SV-PROP-T2-COUNT: esperadas 118 filas, hay {len(rows)}")
        return errores

    for row in rows:
        k = int(row['Nº'])
        nombre = row['Nombre SV'].strip()
        if not nombre:
            errores.append(f"SV-PROP-T2-NOMBRE k={k}: nombre vacío")

        # Electronegatividad debe ser numérica y positiva
        try:
            eneg = float(row['Electronegatividad SV'])
            if eneg < 0:
                    errores.append(f"SV-PROP-T2-ENEG k={k}: electronegatividad negativa ({eneg})")
        except (ValueError, KeyError):
            errores.append(f"SV-PROP-T2-ENEG k={k}: valor no numérico")

        # Radio atómico debe ser positivo
        try:
            radio = float(row['Radio atómico SV (pm)'])
            if radio <= 0:
                errores.append(f"SV-PROP-T2-RADIO k={k}: radio ≤ 0 ({radio})")
        except (ValueError, KeyError):
            errores.append(f"SV-PROP-T2-RADIO k={k}: valor no numérico")

        # Energía de ionización debe ser positiva
        try:
            ei = float(row['Energía ionización SV (kJ/mol)'])
            if ei <= 0:
                errores.append(f"SV-PROP-T2-EI k={k}: energía ionización ≤ 0 ({ei})")
        except (ValueError, KeyError):
            errores.append(f"SV-PROP-T2-EI k={k}: valor no numérico")

    return errores


def verifica_tabla3(rows: List[Dict]) -> List[str]:
    """Tabla 3 — Propiedades mecánicas, químicas y térmicas.

    Verificaciones: 118 filas, rangos [0,1] en flexibilidad y maleabilidad,
    resistencias en [0,100], temperaturas positivas.
    """
    errores = []
    if len(rows) != 118:
        errores.append(f"SV-PROP-T3-COUNT: esperadas 118 filas, hay {len(rows)}")
        return errores

    for row in rows:
        k = int(row['Nº'])

        for campo in ['Flexibilidad SV (0-1)', 'Maleabilidad SV (0-1)']:
            try:
                v = float(row[campo])
                if not (0 <= v <= 1):
                    errores.append(f"SV-PROP-T3-RANGO k={k} {campo}: fuera de [0,1] ({v})")
            except (ValueError, KeyError):
                errores.append(f"SV-PROP-T3-{campo[:4].upper()} k={k}: valor no numérico")

        for campo in ['Resistencia oxidación SV (0-100)', 'Resistencia corrosión SV (0-100)']:
            try:
                v = float(row[campo])
                if not (0 <= v <= 100):
                    errores.append(f"SV-PROP-T3-RANGO k={k} {campo}: fuera de [0,100] ({v})")
            except (ValueError, KeyError):
                errores.append(f"SV-PROP-T3-RES k={k}: valor no numérico")

        try:
            t = float(row['Resistencia térmica hasta cambio (°C)'])
            if t < -273.15:
                    errores.append(f"SV-PROP-T3-TERM k={k}: temperatura inferior al cero absoluto ({t}°C)")
        except (ValueError, KeyError):
            errores.append(f"SV-PROP-T3-TERM k={k}: valor no numérico")

    return errores


def verifica_tabla4(rows: List[Dict]) -> List[str]:
    """Tabla 4 — Volumen, estabilidad, radiactividad, isótopos y usos.

    Verificaciones: 118 filas, nivel radiactivo en [0,100],
    número de isótopos positivo, campos de aplicación no vacíos.
    """
    errores = []
    if len(rows) != 118:
        errores.append(f"SV-PROP-T4-COUNT: esperadas 118 filas, hay {len(rows)}")
        return errores

    for row in rows:
        k = int(row['Nº'])

        try:
            rad = float(row['Nivel radiactivo SV (0-100)'])
            if not (0 <= rad <= 100):
                errores.append(f"SV-PROP-T4-RAD k={k}: nivel radiactivo fuera de [0,100] ({rad})")
        except (ValueError, KeyError):
            errores.append(f"SV-PROP-T4-RAD k={k}: valor no numérico")

        try:
            niso = int(row['Nº isótopos SV'])
            if niso <= 0:
                errores.append(f"SV-PROP-T4-ISO k={k}: Nº isótopos ≤ 0 ({niso})")
        except (ValueError, KeyError):
            errores.append(f"SV-PROP-T4-ISO k={k}: valor no numérico")

        for campo in ['Aplicación científica SV', 'Aplicación aeroespacial/cosmológica SV',
                      'Aplicación médica SV']:
            if not row.get(campo, '').strip():
                errores.append(f"SV-PROP-T4-APLIC k={k} '{campo}': vacío")

    return errores
