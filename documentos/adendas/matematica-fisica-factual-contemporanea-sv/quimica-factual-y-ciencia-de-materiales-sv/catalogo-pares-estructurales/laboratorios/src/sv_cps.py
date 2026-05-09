# -*- coding: utf-8 -*-
# © 2026. Todos los derechos reservados. | Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351
# Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
# IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 2026
# Advertencia: esta publicación está protegida por CEDRO. Uso comercial prohibido sin autorización.
#
# Módulo: sv_cps
# Función: Catálogo de Pares Estructurales SV (CPS-SV)
#          Implementación de la función de dictamen D(A,B) sobre Ω₄₄₃ × Ω₄₄₃
#          Referencia doctrinal: §3 (criterios B.1–B.5) y §4 (aplicación al dominio completo)
#
# Códigos de error:
#   CPS-LOAD-CSV        — CSV de Tabla 2 no encontrado o no legible
#   CPS-LOAD-COLS       — Columnas requeridas ausentes en el CSV
#   CPS-LOAD-COUNT      — Número de elementos ≠ 443
#   CPS-LOAD-FLOAT-{k}-{col} — Valor no numérico en elemento k, columna col
#   CPS-LOAD-RANGE-EN-{k}    — EN_SV fuera de [0.0, 2.71]
#   CPS-LOAD-RANGE-IP-{k}    — IP_SV fuera de [355, 1800]
#   CPS-LOAD-RANGE-R-{k}     — r_SV fuera de [155, 360]
#   CPS-LOAD-RANGE-M-{k}     — M_SV fuera de [0.0, 100.0]
#   CPS-OUT-COUNT            — CSV de salida no contiene exactamente 97903 filas
#   CPS-OUT-COLS             — CSV de salida columnas incorrectas
#   CPS-OUT-DICT-{n}         — Dictamen inválido en fila n
#   CPS-INV-NOBLE            — Par noble×noble con dictamen ≠ NO-APTO (Proposición 6.1)
#   CPS-INV-MARGINAL         — Recuento de marginales B.2 ≠ 9858 (Proposición 6.2)
#   CPS-INV-FECROMO          — Fe-Cr (k=24,26) no recibe APTO-M
#   CPS-INV-CUZN             — Cu-Zn (k=29,30) no recibe APTO-M
#   CPS-INV-KCL              — KCl (k=17,19) no recibe APTO-I
#   CPS-INV-ARKR             — Ar-Kr (k=18,36) no recibe NO-APTO

from __future__ import annotations
import csv
from itertools import combinations
from pathlib import Path
from typing import Dict, List, Tuple

# ── Constantes del corpus ──────────────────────────────────────────────────────
N_ELEMENTOS  = 443
N_PARES      = N_ELEMENTOS * (N_ELEMENTOS - 1) // 2   # 97.903
COLS_SALIDA  = ['k_A','k_B','nombre_A','nombre_B','dictamen',
                'delta_EN_SV','rho_SV','M_joint','IP_suma_kJmol']

# Umbrales B.1–B.4 (§3.11)
LAMBDA_M   = 0.50    # B.1 frontera metálico/covalente
LAMBDA_C   = 1.50    # B.1 frontera covalente/iónico
LAMBDA_RHO = 1.40    # B.2 compatibilidad posicional
LAMBDA_Mj  = 40.0    # B.3 carácter metálico mínimo conjunto
LAMBDA_IP  = 1800.0  # B.4 suma de energías de ionización

# Índices de gas noble en Ω₄₄₃ (k base: EN=0, M%=2, IP máximo)
NOBLES_K    = {18, 36, 54, 72, 90, 108}

# Pares de referencia para invariantes F.1 (k_menor, k_mayor)
PAR_FECR    = (24, 26)   # Fe-Cr → APTO-M
PAR_CUZN    = (29, 30)   # Cu-Zn → APTO-M
PAR_KCL     = (17, 19)   # KCl   → APTO-I
PAR_ARKR    = (18, 36)   # Ar-Kr → NO-APTO

DICTAMENES_VALIDOS = {'APTO-M', 'APTO-C', 'APTO-I', 'NO-APTO'}

# ── Tipos ──────────────────────────────────────────────────────────────────────
Elemento = Dict[str, object]

# ── Carga y validación de la Tabla 2 ──────────────────────────────────────────
COLS_REQUERIDAS = {'k', 'nombre', 'EN_SV', 'IP_SV', 'r_SV', 'M_SV'}

def cargar_tabla2(ruta: Path) -> Tuple[Dict[int, Elemento], List[str]]:
    """Carga el CSV de Tabla 2 y valida su integridad.
    Devuelve (datos, errores). Si errores no está vacío, datos puede estar incompleto."""
    errores: List[str] = []
    datos: Dict[int, Elemento] = {}

    if not ruta.exists():
        return datos, [f"CPS-LOAD-CSV: archivo no encontrado en {ruta}"]

    try:
        with open(ruta, newline='', encoding='utf-8') as f:
            raw_lines = [l for l in f if not l.startswith('#')]
        reader = csv.DictReader(raw_lines)
        filas  = list(reader)
    except Exception as e:
        return datos, [f"CPS-LOAD-CSV: error de lectura — {e}"]

    # Verificar columnas
    if reader.fieldnames is None or not COLS_REQUERIDAS.issubset(set(reader.fieldnames)):
        faltantes = COLS_REQUERIDAS - set(reader.fieldnames or [])
        return datos, [f"CPS-LOAD-COLS: columnas ausentes — {faltantes}"]

    # Verificar recuento
    if len(filas) != N_ELEMENTOS:
        errores.append(f"CPS-LOAD-COUNT: {len(filas)} filas (esperado {N_ELEMENTOS})")

    for fila in filas:
        try:
            k = int(fila['k'])
        except (ValueError, KeyError):
            errores.append(f"CPS-LOAD-FLOAT-?-k: índice k no legible en fila {fila}")
            continue

        elem: Elemento = {'nombre': fila.get('nombre', '').strip()}
        ok = True

        for col, clave in [('EN_SV','EN'), ('IP_SV','IP'), ('r_SV','r'), ('M_SV','M')]:
            try:
                elem[clave] = float(fila[col])
            except (ValueError, KeyError):
                errores.append(f"CPS-LOAD-FLOAT-{k}-{col}")
                ok = False

        if not ok:
            continue

        # Rangos admisibles
        if not (0.0 <= elem['EN'] <= 2.71):
            errores.append(f"CPS-LOAD-RANGE-EN-{k}: EN_SV={elem['EN']:.4f} fuera de [0,2.71]")
        if not (300.0 <= elem['IP'] <= 5000.0):
            errores.append(f"CPS-LOAD-RANGE-IP-{k}: IP_SV={elem['IP']:.1f} fuera de [300,5000]")
        if not (100.0 <= elem['r'] <= 400.0):
            errores.append(f"CPS-LOAD-RANGE-R-{k}: r_SV={elem['r']:.1f} fuera de [100,400]")
        if not (0.0 <= elem['M'] <= 100.0):
            errores.append(f"CPS-LOAD-RANGE-M-{k}: M_SV={elem['M']:.1f} fuera de [0,100]")

        datos[k] = elem

    return datos, errores


# ── Función de dictamen D(A,B) ─────────────────────────────────────────────────
def dictamen(ka: int, kb: int, datos: Dict[int, Elemento]) -> Tuple[str, float, float, float, float]:
    """Aplica la función D(A,B) del §3.8.
    Devuelve (dictamen, delta_EN, rho, M_joint, IP_suma)."""
    A, B = datos[ka], datos[kb]

    dEN = abs(A['EN'] - B['EN'])
    rho = max(A['r'], B['r']) / min(A['r'], B['r'])
    Mj  = (A['M'] + B['M']) / 2.0
    IPs = A['IP'] + B['IP']

    # B.4 — filtro universal
    if IPs > LAMBDA_IP:
        return 'NO-APTO', dEN, rho, Mj, IPs

    # B.1 — carácter estructural dominante
    if dEN <= LAMBDA_M:
        chi = 'M'
    elif dEN <= LAMBDA_C:
        chi = 'C'
    else:
        chi = 'I'

    if chi == 'M':
        if rho > LAMBDA_RHO:          # B.2
            return 'NO-APTO', dEN, rho, Mj, IPs
        if Mj < LAMBDA_Mj:            # B.3 reclasifica
            return 'APTO-C', dEN, rho, Mj, IPs
        return 'APTO-M', dEN, rho, Mj, IPs

    if chi == 'C':
        return 'APTO-C', dEN, rho, Mj, IPs

    return 'APTO-I', dEN, rho, Mj, IPs


# ── Enumeración completa del dominio ──────────────────────────────────────────
def enumerar_cps(datos: Dict[int, Elemento]) -> List[tuple]:
    """Aplica D(A,B) a los 97.903 pares no ordenados de Ω₄₄₃.
    Devuelve lista de tuplas (k_A, k_B, nombre_A, nombre_B, dictamen,
    delta_EN, rho, M_joint, IP_suma)."""
    filas = []
    for ka, kb in combinations(sorted(datos.keys()), 2):
        d, dEN, rho, Mj, IPs = dictamen(ka, kb, datos)
        filas.append((
            ka, kb,
            datos[ka]['nombre'], datos[kb]['nombre'],
            d,
            round(dEN, 3), round(rho, 3),
            round(Mj, 1),  round(IPs, 1)
        ))
    return filas


# ── Verificación de invariantes (§6.4) ────────────────────────────────────────
def verificar_invariantes(filas: List[tuple]) -> List[str]:
    """Verifica las tres proposiciones de §6.4.
    Devuelve lista de errores CPS-INV-*."""
    errores: List[str] = []

    # Índice rápido
    idx = {(int(f[0]), int(f[1])): f for f in filas}

    # Proposición 6.1 — nobles×nobles → todos NO-APTO
    nobles = sorted(NOBLES_K)
    for i, j in combinations(nobles, 2):
        ka, kb = min(i,j), max(i,j)
        fila = idx.get((ka, kb))
        if fila is None or fila[4] != 'NO-APTO':
            d = fila[4] if fila else 'ausente'
            errores.append(f"CPS-INV-NOBLE: par ({ka},{kb}) tiene dictamen {d} (esperado NO-APTO)")

    # Proposición 6.2 — marginales B.2 = 9858
    marginales = sum(
        1 for f in filas
        if f[4] == 'NO-APTO'
        and float(f[5]) <= LAMBDA_M        # ΔEN ≤ 0.50
        and float(f[7]) >= LAMBDA_Mj       # M_joint ≥ 40
        and float(f[8]) <= LAMBDA_IP       # IP ≤ 1800
        and float(f[6]) > LAMBDA_RHO       # ρ > 1.40
    )
    if marginales != 9858:
        errores.append(f"CPS-INV-MARGINAL: {marginales} pares marginales B.2 (esperado 9858)")

    # F.1 — pares de referencia
    for (ka, kb), codigo, esperado in [
        (PAR_FECR, 'CPS-INV-FECROMO', 'APTO-M'),
        (PAR_CUZN, 'CPS-INV-CUZN',    'APTO-M'),
        (PAR_KCL,  'CPS-INV-KCL',     'APTO-I'),
        (PAR_ARKR, 'CPS-INV-ARKR',    'NO-APTO'),
    ]:
        fila = idx.get((min(ka,kb), max(ka,kb)))
        if fila is None or fila[4] != esperado:
            d = fila[4] if fila else 'ausente'
            errores.append(f"{codigo}: dictamen {d} (esperado {esperado})")

    return errores


# ── Escritura del CSV de salida ────────────────────────────────────────────────
def escribir_csv(filas: List[tuple], ruta_salida: Path) -> List[str]:
    """Escribe el CPS-SV como CSV. Verifica integridad del archivo escrito."""
    errores: List[str] = []
    try:
        with open(ruta_salida, 'w', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(COLS_SALIDA)
            w.writerows(filas)
    except Exception as e:
        return [f"CPS-OUT-WRITE: error al escribir {ruta_salida} — {e}"]

    # Verificar el archivo escrito
    try:
        with open(ruta_salida, newline='', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            filas_leidas = list(lector)
        if len(filas_leidas) != N_PARES:
            errores.append(f"CPS-OUT-COUNT: {len(filas_leidas)} filas (esperado {N_PARES})")
        if lector.fieldnames != COLS_SALIDA:
            errores.append(f"CPS-OUT-COLS: cabecera incorrecta")
        for i, fila in enumerate(filas_leidas, 1):
            if fila.get('dictamen') not in DICTAMENES_VALIDOS:
                errores.append(f"CPS-OUT-DICT-{i}: dictamen inválido '{fila.get('dictamen')}'")
    except Exception as e:
        errores.append(f"CPS-OUT-READ: error al releer {ruta_salida} — {e}")

    return errores
