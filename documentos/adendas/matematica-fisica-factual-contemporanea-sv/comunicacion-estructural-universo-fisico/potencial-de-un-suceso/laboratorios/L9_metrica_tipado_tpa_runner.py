#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
© 2026. Todos los derechos reservados. | Juan Antonio Lloret Egea | DOI [pendiente] | ORCID: 0000-0002-6634-3351 |
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | IA eñ™ — La Biblia de la IA™ |
ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 29/05/2026 |
"""

from typing import Any
from math import floor, sqrt, ceil

CANONICAL_URL = "https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/comunicacion-estructural-universo-fisico/potencial-de-un-suceso/potencial-de-un-suceso.md"

WARNING = """Advertencia. Esta publicación está protegida por CEDRO y su aplicación en el campo de la Física y la Química, así como cualquier forma de explotación, reproducción o uso por parte de empresas, queda sujeta al copyright del autor y a los términos de la licencia indicada; la reproducción, distribución, comunicación pública o transformación de esta obra solo puede ser realizada con la autorización de sus titulares, salvo excepción prevista por la ley, y cualquier uso comercial sin autorización expresa queda prohibido y sujeto estrictamente al licenciamiento permitido.

Warning. This publication is protected by CEDRO. Its application in the field of Physics and Chemistry, as well as any form of exploitation, reproduction, or use by corporate entities, is strictly subject to the author's copyright and the terms of the license indicated; any reproduction, distribution, public communication, or transformation of this work requires authorization from the rightsholders, except as provided by law, and any commercial use without express written consent is prohibited and strictly subject to permitted licensing.

| Url canónica: https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/comunicacion-estructural-universo-fisico/potencial-de-un-suceso/potencial-de-un-suceso.md |
"""

ERROR_CATALOG = {
    "E-LAB-000": "Ejecución interrumpida por fallo no clasificado.",
    "E-LAB-001": "Caso esperado ausente o duplicado.",
    "E-LAB-002": "Resultado aritmético incompatible con el banco.",
    "E-LAB-003": "Clasificación incompatible con las restricciones del dominio.",
    "E-LAB-004": "Salida U degradada indebidamente a admisión o rechazo automático.",
    "E-LAB-005": "Caso no admisible aceptado como admisible.",
    "E-LAB-006": "Caso admisible rechazado indebidamente.",
    "E-LAB-007": "Discrepancia material sin código de error.",
    "E-LAB-008": "Precedencia ternaria incorrecta: el fallo material debe prevalecer sobre U.",
    "E-LAB-009": "Semántica de Mant_D incompatible con la definición documental.",
    "E-LAB-010": "Métrica tipada incompatible con IX.",
}

class LabFailure(AssertionError):
    def __init__(self, code: str, detail: str):
        self.code = code
        self.detail = detail
        super().__init__(f"{code}: {ERROR_CATALOG.get(code, 'Error no catalogado')} :: {detail}")

def require(condition: bool, code: str, detail: str) -> None:
    if not condition:
        raise LabFailure(code, detail)

def ternary_residual_join(values: list[Any]) -> Any:
    if any(v == 1 for v in values):
        return 1
    if any(v == "U" for v in values):
        return "U"
    return 0

def material_bool_join(values: list[Any], admissible_label: str, negative_label: str) -> str:
    if any(v is False for v in values):
        return negative_label
    if any(v == "U" for v in values):
        return "U"
    if all(v is True for v in values):
        return admissible_label
    raise LabFailure("E-LAB-007", f"valores no reconocidos: {values}")

def print_result(title: str, rows: list[dict[str, Any]]) -> None:
    print(title)
    print("=" * len(title))
    for row in rows:
        print(row)
    print("\nRESULTADO: APTO")
    print(WARNING)

def carrier_cell(r_tipo: int) -> tuple[int, int]:
    require(r_tipo >= 1, "E-LAB-003", f"soporte activo inválido: {r_tipo}")
    b = max(3, ceil(sqrt(r_tipo)))
    while b * b < r_tipo:
        b += 1
    return b * b, b

def threshold(r_tipo: int) -> int:
    require(r_tipo >= 1, "E-LAB-003", f"soporte activo inválido para umbral: {r_tipo}")
    return floor(7 * r_tipo / 9)

def typed_potential(n_pos: int, n_neg: int, n_u: int = 0) -> int:
    require(n_pos >= 0 and n_neg >= 0 and n_u >= 0, "E-LAB-003", "conteos negativos no admisibles")
    return n_pos - n_neg

def trajectory_metrics(potentials: list[float]) -> dict[str, object]:
    require(len(potentials) >= 2, "E-LAB-001", "la trayectoria tipada exige al menos dos nodos")
    deltas = [potentials[i+1] - potentials[i] for i in range(len(potentials)-1)]
    local = [abs(d) for d in deltas]
    length = sum(local)
    boundary = abs(potentials[-1] - potentials[0])
    defect = length - boundary
    return {"deltas": deltas, "distancias_locales": local, "longitud": length, "saldo_frontera": boundary, "defecto": defect}

def activation(coeffs: list[float]) -> list[float]:
    require(all(c > 0 for c in coeffs), "E-LAB-003", f"dν exige coeficientes positivos: {coeffs}")
    acc = [0.0]
    for c in coeffs:
        acc.append(acc[-1] + c)
    return acc

def tpa_areas(potentials: list[float], coeffs: list[float]) -> tuple[float, float]:
    require(len(coeffs) == len(potentials) - 1, "E-LAB-001", "coeficientes incompatibles con tramos TPA")
    require(all(c > 0 for c in coeffs), "E-LAB-003", "coeficientes TPA no positivos")
    signed = 0.0
    charge = 0.0
    for a, b, c in zip(potentials[:-1], potentials[1:], coeffs):
        signed += ((a + b) / 2.0) * c
        charge += ((abs(a) + abs(b)) / 2.0) * c
    return signed, charge

def main() -> int:
    rows = []
    for cid, r, expected_cell, expected_t in [
        ("L9-01", 9, (9, 3), 7),
        ("L9-02", 10, (16, 4), 7),
        ("L9-03", 25, (25, 5), 19),
    ]:
        cell = carrier_cell(r)
        t = threshold(r)
        require(cell == expected_cell, "E-LAB-010", f"{cid}: célula {cell} != {expected_cell}")
        require(t == expected_t, "E-LAB-010", f"{cid}: umbral {t} != {expected_t}")
        rows.append({"caso": cid, "r_tipo": r, "celula": f"SV({cell[0]},{cell[1]})", "T_tipo": t})

    for cid, pos, neg, u_count, expected in [
        ("L9-04", 8, 2, 1, 6),
        ("L9-05", 3, 7, 0, -4),
        ("L9-06", 5, 5, 4, 0),
    ]:
        p = typed_potential(pos, neg, u_count)
        require(p == expected, "E-LAB-010", f"{cid}: P_tipo {p} != {expected}")
        rows.append({"caso": cid, "N_pos": pos, "N_neg": neg, "N_U": u_count, "P_tipo": p, "unidad": "USP_SV^tipo"})

    metrics = trajectory_metrics([2, 5, 1, 6])
    require(metrics["deltas"] == [3, -4, 5], "E-LAB-010", f"L9-07 deltas: {metrics['deltas']}")
    require(metrics["distancias_locales"] == [3, 4, 5], "E-LAB-010", f"L9-07 distancias: {metrics['distancias_locales']}")
    require(metrics["longitud"] == 12, "E-LAB-010", f"L9-07 longitud: {metrics['longitud']}")
    require(metrics["saldo_frontera"] == 4, "E-LAB-010", f"L9-07 saldo: {metrics['saldo_frontera']}")
    require(metrics["defecto"] == 8, "E-LAB-010", f"L9-07 defecto: {metrics['defecto']}")
    rows.append({"caso": "L9-07", **metrics})

    nu = activation([1, 2, 3])
    require(nu == [0.0, 1.0, 3.0, 6.0], "E-LAB-010", f"L9-08 activación: {nu}")
    signed, charge = tpa_areas([2, 5, 1, 6], [1, 2, 3])
    require(signed == 20.0, "E-LAB-010", f"L9-08 área firmada: {signed}")
    require(charge == 20.0, "E-LAB-010", f"L9-08 área carga: {charge}")
    rows.append({"caso": "L9-08", "nu": nu, "A_TPA_firmada": signed, "A_TPA_carga": charge})

    signed_cancel, charge_cancel = tpa_areas([2, -2, 2], [1, 1])
    require(signed_cancel == 0.0, "E-LAB-010", f"L9-09 cancelación firmada: {signed_cancel}")
    require(charge_cancel == 4.0, "E-LAB-010", f"L9-09 carga sin cancelación: {charge_cancel}")
    rows.append({"caso": "L9-09", "A_TPA_firmada": signed_cancel, "A_TPA_carga": charge_cancel})

    print_result("L.9 Métrica tipada, unidad USP_SV^tipo y áreas TPA", rows)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
