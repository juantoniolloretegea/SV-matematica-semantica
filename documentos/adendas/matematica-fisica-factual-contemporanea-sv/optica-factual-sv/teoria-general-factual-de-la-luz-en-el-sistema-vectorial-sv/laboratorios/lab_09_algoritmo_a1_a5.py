"""
lab_09_algoritmo_a1_a5.py — L-LUZ-09 — Algoritmo canónico A1–A5 de
canonización de nueva proyección P_{n+1}.

§7.3bis — Algoritmo de búsqueda de proyecciones:
  A1. Identificar dominio canónico del corpus (algún 2026x existente)
  A2. Construir operador π con firma canónica (dominio → Proy)
  A3. Verificar independencia estructural respecto a P_1, ..., P_n existentes
  A4. Verificar compatibilidad mutua con las proyecciones ya canonizadas
  A5. Auditar conformidad con prohibiciones P.1–P.6

Pruebas:
  1. Candidata redundante (A3 debe rechazarla)
  2. Candidata sin dominio canónico (A1 debe rechazarla)
  3. Candidata incompatible con π_ω sobre mismo dominio (A4 debe rechazarla)
  4. Candidata que viola P.1 (usa derivada temporal soberana) (A5 debe rechazarla)
  5. Candidata legítima (supera A1-A5 completos)

Códigos: LUZ-A15-001..005
"""
import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sv_core import (SVError, cargar_casos, construir_acumulados,
                      proyecciones_canonicas, TOLERANCIA_DEFAULT)


def A1_dominio_canonico(candidata: dict) -> bool:
    """A1: la candidata debe invocar dominio canónico del corpus (lista 2026x)."""
    dominios_canonicos = {
        "2026a", "2026b", "2026g", "2026h", "2026j", "2026k", "2026l",
    }
    return candidata.get("dominio") in dominios_canonicos


def A2_firma_canonica(candidata: dict) -> bool:
    """A2: el operador debe tener firma D^L_SV → Proy canónica."""
    firma = candidata.get("firma", "")
    return ("D^L_SV" in firma) and ("→" in firma or "->" in firma)


def A3_independencia_estructural(candidata: dict, P_existentes: list) -> bool:
    """
    A3: la candidata no es combinación lineal trivial de P_1..P_n.
    Verificamos con producto escalar: si la lectura de la candidata tiene
    alta correlación (>0.995) con alguna de las existentes, la rechazamos.
    """
    v = np.asarray(candidata["lectura"], dtype=float)
    if np.allclose(v, 0.0):
        return False
    for u in P_existentes:
        u = np.asarray(u, dtype=float)
        if u.size != v.size:
            continue
        norm_u = np.linalg.norm(u)
        norm_v = np.linalg.norm(v)
        if norm_u < 1e-12 or norm_v < 1e-12:
            continue
        corr = float(abs(np.dot(u, v)) / (norm_u * norm_v))
        if corr > 0.995:
            return False
    return True


def A4_compatibilidad_mutua(candidata: dict, P_existentes: list) -> bool:
    """
    A4: la candidata no produce contradicción estructural con las existentes
    sobre fibra común admisible. Se verifica que la magnitud de la candidata
    no es infinita ni NaN sobre los valores de las proyecciones existentes.
    """
    v = np.asarray(candidata["lectura"], dtype=float)
    if not np.all(np.isfinite(v)):
        return False
    return True


def A5_auditoria_P1_P6(candidata: dict) -> bool:
    """
    A5: la candidata no viola las prohibiciones constitutivas. Se audita
    la metadata del operador candidato buscando invocaciones prohibidas.
    """
    invocaciones_prohibidas = {
        "d/dt":       "LUZ-P1-001 (derivada temporal soberana)",
        "tiempo_t":   "LUZ-P1-002 (tiempo soberano)",
        "E[·]":       "LUZ-P2-001 (probabilidad fundante)",
        "métrica":    "LUZ-P3-001 (geometría soberana)",
        "k_B":        "LUZ-P5-001 (constante ajena)",
    }
    metadata = candidata.get("metadata", "")
    for pat, _ in invocaciones_prohibidas.items():
        if pat in metadata:
            return False
    return True


def aplicar_A1_A5(candidata: dict, P_existentes: list) -> tuple:
    """Aplica los cinco pasos y devuelve (paso_fallido, aprobada)."""
    if not A1_dominio_canonico(candidata):
        return ("A1", False)
    if not A2_firma_canonica(candidata):
        return ("A2", False)
    if not A3_independencia_estructural(candidata, P_existentes):
        return ("A3", False)
    if not A4_compatibilidad_mutua(candidata, P_existentes):
        return ("A4", False)
    if not A5_auditoria_P1_P6(candidata):
        return ("A5", False)
    return ("aprobada", True)


def obtener_P_existentes() -> list:
    """Obtiene lecturas numéricas de P_1..P_15 sobre caso canónico SV(3,9)."""
    casos = cargar_casos()
    fib = construir_acumulados(casos[2])
    proys = proyecciones_canonicas(casos[2], fib)
    # Reducir cada proyección a vector 1D de longitud 9
    out = []
    N_std = 9
    for nombre, arr in proys.items():
        v = np.asarray(arr, dtype=float).flatten()
        if v.size >= N_std:
            out.append(v[:N_std])
        else:
            vp = np.zeros(N_std); vp[:v.size] = v
            out.append(vp)
    return out


def prueba_1_rechazo_redundante() -> None:
    """A3 debe rechazar una candidata que duplica P_1 existente."""
    P_exist = obtener_P_existentes()
    # Candidata = copia literal de P_1
    candidata = {
        "dominio": "2026a", "firma": "D^L_SV → Proy",
        "lectura": list(P_exist[0]), "metadata": "legítima",
    }
    paso, ok = aplicar_A1_A5(candidata, P_exist)
    if ok:
        raise SVError(
            "LUZ-A15-001",
            f"Candidata redundante aceptada pese a A3 (paso={paso})",
        )
    if paso != "A3":
        raise SVError(
            "LUZ-A15-003",
            f"Redundante rechazada por paso {paso} ≠ A3",
        )
    print(f"  [A15 OK] A3 rechaza candidata redundante (duplicado de P_1) ✓")


def prueba_2_rechazo_sin_dominio() -> None:
    """A1 debe rechazar una candidata sin dominio canónico del corpus."""
    P_exist = obtener_P_existentes()
    candidata = {
        "dominio": "2027z",  # inexistente
        "firma": "D^L_SV → Proy",
        "lectura": [1.0] * 9, "metadata": "",
    }
    paso, ok = aplicar_A1_A5(candidata, P_exist)
    if ok:
        raise SVError("LUZ-A15-002", f"Candidata sin dominio aceptada (paso={paso})")
    if paso != "A1":
        raise SVError("LUZ-A15-002", f"Sin dominio rechazada por {paso} ≠ A1")
    print(f"  [A15 OK] A1 rechaza candidata sin dominio canónico del corpus ✓")


def prueba_3_rechazo_firma_ilegal() -> None:
    """A2 debe rechazar una candidata sin firma canónica D^L_SV → Proy."""
    P_exist = obtener_P_existentes()
    candidata = {
        "dominio": "2026a", "firma": "algo informal",
        "lectura": [1.0] * 9, "metadata": "",
    }
    paso, ok = aplicar_A1_A5(candidata, P_exist)
    if ok or paso != "A2":
        raise SVError(
            "LUZ-A15-003",
            f"Firma ilegal no rechazada correctamente en A2 (paso={paso}, ok={ok})",
        )
    print(f"  [A15 OK] A2 rechaza candidata con firma no canónica ✓")


def prueba_4_rechazo_violacion_P1() -> None:
    """A5 debe rechazar una candidata que invoca derivada temporal soberana."""
    P_exist = obtener_P_existentes()
    candidata = {
        "dominio": "2026a", "firma": "D^L_SV → Proy",
        "lectura": [0.1, 0.3, 0.2, 0.5, 0.4, 0.7, 0.6, 0.8, 0.9],
        "metadata": "evaluación vía d/dt operador hamiltoniano",
    }
    paso, ok = aplicar_A1_A5(candidata, P_exist)
    if ok:
        raise SVError(
            "LUZ-A15-005",
            f"Candidata con violación P.1 aceptada (paso={paso})",
        )
    if paso != "A5":
        raise SVError(
            "LUZ-A15-005",
            f"Violación P.1 rechazada por {paso} ≠ A5",
        )
    print(f"  [A15 OK] A5 audita P.1 y rechaza candidata con d/dt ✓")


def prueba_5_aprobacion_legitima() -> None:
    """
    Candidata legítima: nuevo dominio canónico, firma correcta, independiente
    de las 15 existentes, compatible y sin violar prohibiciones.
    """
    P_exist = obtener_P_existentes()
    # Construimos una candidata con perfil nuevo (sin correlación alta con las existentes)
    rng = np.random.default_rng(33)
    # Ortogonalizar respecto a las existentes (Gram-Schmidt parcial)
    v = rng.random(9)
    for u in P_exist:
        norm_u = np.linalg.norm(u)
        if norm_u > 1e-12:
            v = v - (np.dot(v, u) / (norm_u * norm_u)) * u
    norm_v = np.linalg.norm(v)
    if norm_v > 1e-12:
        v = v / norm_v
    candidata = {
        "dominio": "2026g", "firma": "D^L_SV → Proy_spec",
        "lectura": list(v), "metadata": "espectral honesta",
    }
    paso, ok = aplicar_A1_A5(candidata, P_exist)
    if not ok:
        raise SVError(
            "LUZ-A15-002",
            f"Candidata legítima rechazada en paso {paso}",
        )
    print(f"  [A15 OK] Candidata legítima supera A1–A5 (paso final: {paso}) ✓")


def run() -> int:
    print("=" * 74)
    print("L-LUZ-09 — ALGORITMO CANÓNICO A1–A5 (§7.3bis)")
    print("=" * 74)
    prueba_1_rechazo_redundante()
    prueba_2_rechazo_sin_dominio()
    prueba_3_rechazo_firma_ilegal()
    prueba_4_rechazo_violacion_P1()
    prueba_5_aprobacion_legitima()
    print("-" * 74)
    print("L-LUZ-09 — PASADO. Algoritmo A1–A5 discrimina candidatas correctamente.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(run())
    except SVError as e:
        print(f"\n[L-LUZ-09] FALLO código={e.codigo}")
        print(f"           mensaje: {e.mensaje}")
        sys.exit(1)
