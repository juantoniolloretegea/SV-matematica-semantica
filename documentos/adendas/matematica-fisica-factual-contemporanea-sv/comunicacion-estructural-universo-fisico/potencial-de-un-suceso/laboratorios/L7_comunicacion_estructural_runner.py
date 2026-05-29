#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
© 2026. Todos los derechos reservados. | Juan Antonio Lloret Egea | DOI [pendiente] | ORCID: 0000-0002-6634-3351 |
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | IA eñ™ — La Biblia de la IA™ |
ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 29/05/2026 |
"""

from typing import Any

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
    # Residual: 0 cierra; 1 falla materialmente; U conserva indeterminación sólo si no hay fallo material.
    if any(v == 1 for v in values):
        return 1
    if any(v == "U" for v in values):
        return "U"
    return 0

def material_bool_join(values: list[Any], admissible_label: str, negative_label: str) -> str:
    # Booleanos de condición: False prevalece sobre U; sólo sin False puede conservarse U.
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

def r_com(r_delta: Any, r_canal: Any, r_frontera: Any, r_traza: Any, r_ret: Any, r_id: Any) -> Any:
    return ternary_residual_join([r_delta, r_canal, r_frontera, r_traza, r_ret, r_id])

def communication(r_delta: Any, r_canal: Any, r_frontera: Any, r_traza: Any, r_ret: Any, r_id: Any) -> str:
    residual = r_com(r_delta, r_canal, r_frontera, r_traza, r_ret, r_id)
    if residual == 0:
        return "comunicacion_estructural_admisible"
    if residual == "U":
        return "U"
    return "no_admisible"

def mant(tramos: list[tuple[Any, Any, Any, Any]]) -> Any:
    # Mant_D = 1: mantenimiento admisible; Mant_D = 0: no admisible; Mant_D = U: indeterminación honesta.
    tramo_outputs = []
    for adm_delta, canal, ret, residual_com in tramos:
        # adm_delta/canal/ret usan 1 como cierre positivo; residual_com usa 0 como cierre positivo.
        if adm_delta == 0 or canal == 0 or ret == 0 or residual_com == 1:
            tramo_outputs.append(0)
        elif "U" in (adm_delta, canal, ret, residual_com):
            tramo_outputs.append("U")
        elif adm_delta == 1 and canal == 1 and ret == 1 and residual_com == 0:
            tramo_outputs.append(1)
        else:
            raise LabFailure("E-LAB-007", f"tramo no reconocido: {(adm_delta, canal, ret, residual_com)}")
    if any(v == 0 for v in tramo_outputs):
        return 0
    if any(v == "U" for v in tramo_outputs):
        return "U"
    return 1

def main() -> int:
    cases = [
        ("L7-01", (0, 0, 0, 0, 0, 0), "comunicacion_estructural_admisible"),
        ("L7-02", (1, 0, 0, 0, 0, 0), "no_admisible"),
        ("L7-03", (0, 1, 0, 0, 0, 0), "no_admisible"),
        ("L7-04", (0, 0, 1, 0, 0, 0), "no_admisible"),
        ("L7-05", (0, 0, 0, 1, 0, 0), "no_admisible"),
        ("L7-06", (0, 0, 0, 0, 1, 0), "no_admisible"),
        ("L7-07", (0, 0, 0, 0, 0, "U"), "U"),
        ("L7-08", (0, "U", 0, 0, 0, 0), "U"),
        ("L7-09", (1, "U", 0, 0, 0, 0), "no_admisible"),
        ("L7-10", (0, 0, 0, 1, "U", 0), "no_admisible"),
    ]
    rows = []
    for cid, comps, expected in cases:
        status = communication(*comps)
        require(status == expected, "E-LAB-003", f"{cid}: {status} != {expected}")
        if any(v == 1 for v in comps):
            require(status == "no_admisible", "E-LAB-008", f"{cid}: fallo material no prevalece sobre U")
        rows.append({"caso": cid, "componentes": comps, "salida": status})
    require(mant([(1, 1, 1, 0), (1, 1, 1, 0)]) == 1, "E-LAB-009", "Mant_D admisible debe devolver 1")
    require(mant([(1, 1, 1, 0), (1, "U", 1, 0)]) == "U", "E-LAB-004", "Mant_D con U no conservada")
    require(mant([(1, 1, 1, 0), (1, 0, 1, 0)]) == 0, "E-LAB-009", "Mant_D no admisible debe devolver 0")
    require(mant([(1, 1, 1, 0), (1, "U", 1, 1)]) == 0, "E-LAB-008", "fallo material en Mant_D no prevalece sobre U")
    print_result("L.7 Comunicación estructural", rows)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
