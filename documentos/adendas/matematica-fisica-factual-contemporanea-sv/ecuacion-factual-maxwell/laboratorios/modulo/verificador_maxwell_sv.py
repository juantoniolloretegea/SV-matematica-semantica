# © 2026. Todos los derechos reservados. 
#
# Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 20/04/2026 | Advertencia: Esta publicación está protegida por CEDRO y su aplicación en el campo de la Física, así como cualquier forma de explotación, reproducción o uso por parte de empresas, queda sujeta al copyright del autor y a los términos de la licencia indicada; la reproducción, distribución, comunicación pública o transformación de esta obra solo puede ser realizada con la autorización de sus titulares, salvo excepción prevista por la ley, y cualquier uso comercial sin autorización expresa queda prohibido y supeditado estrictamente al licenciamiento permitido.
#
# Warning: This publication is protected by CEDRO. Its application in the field of Physics, as well as any form of exploitation, reproduction, or use by corporate entities, is strictly subject to the author’s copyright and the terms of the license indicated; any reproduction, distribution, public communication, or transformation of this work requires authorization from the rightsholders, except as provided by law, and any commercial use without express written consent is prohibited and strictly subject to permitted licensing.
from __future__ import annotations

import copy
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Sequence


RIGHTS = '© 2026. Todos los derechos reservados.\n\nJuan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 20/04/2026 | Advertencia: Esta publicación está protegida por CEDRO y su aplicación en el campo de la Física, así como cualquier forma de explotación, reproducción o uso por parte de empresas, queda sujeta al copyright del autor y a los términos de la licencia indicada; la reproducción, distribución, comunicación pública o transformación de esta obra solo puede ser realizada con la autorización de sus titulares, salvo excepción prevista por la ley, y cualquier uso comercial sin autorización expresa queda prohibido y supeditado estrictamente al licenciamiento permitido.\n\nWarning: This publication is protected by CEDRO. Its application in the field of Physics, as well as any form of exploitation, reproduction, or use by corporate entities, is strictly subject to the author’s copyright and the terms of the license indicated; any reproduction, distribution, public communication, or transformation of this work requires authorization from the rightsholders, except as provided by law, and any commercial use without express written consent is prohibited and strictly subject to permitted licensing.'


class MaxwellLabError(RuntimeError):
    def __init__(self, code: str, message: str, payload: Dict[str, Any] | None = None):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message
        self.payload = payload or {}


@dataclass
class BankResult:
    bank_id: str
    description: str
    observed: Any
    expected: Any
    passed: bool
    error_code: str | None = None


def load_json(path: Path) -> Dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise MaxwellLabError("MAXWELL900", "No se encuentra el archivo de datos del laboratorio.", {"path": str(path)}) from exc
    except json.JSONDecodeError as exc:
        raise MaxwellLabError("MAXWELL901", "El archivo JSON del laboratorio no es válido.", {"path": str(path), "error": str(exc)}) from exc


def ensure_mapping(value: Any, code: str, name: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise MaxwellLabError(code, f"Se esperaba un objeto de mapeo para '{name}'.", {"name": name, "type": type(value).__name__})
    return value


def ensure_numeric(value: Any, code: str, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise MaxwellLabError(code, f"Se esperaba un valor numérico para '{name}'.", {"name": name, "value": value})
    return float(value)


def ensure_bool(value: Any, code: str, name: str) -> bool:
    if not isinstance(value, bool):
        raise MaxwellLabError(code, f"Se esperaba un valor booleano para '{name}'.", {"name": name, "value": value})
    return value


def ensure_vector(value: Any, length: int, code: str, name: str) -> List[float]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes)):
        raise MaxwellLabError(code, f"Se esperaba una secuencia numérica para '{name}'.", {"name": name, "value": value})
    if len(value) != length:
        raise MaxwellLabError(code, f"Longitud inválida para '{name}'.", {"name": name, "expected_length": length, "observed_length": len(value)})
    return [ensure_numeric(item, code, f"{name}[{idx}]") for idx, item in enumerate(value)]


def ensure_matrix_3x3(value: Any, code: str, name: str) -> List[List[float]]:
    if not isinstance(value, Sequence) or len(value) != 3:
        raise MaxwellLabError(code, f"Se esperaba una matriz 3x3 para '{name}'.", {"name": name, "value": value})
    rows = [ensure_vector(row, 3, code, f"{name}[{idx}]") for idx, row in enumerate(value)]
    return rows


def almost_equal(a: float, b: float, tol: float) -> bool:
    return math.isclose(a, b, rel_tol=0.0, abs_tol=tol)


def vector_almost_equal(a: Sequence[float], b: Sequence[float], tol: float) -> bool:
    if len(a) != len(b):
        return False
    return all(almost_equal(x, y, tol) for x, y in zip(a, b))


def dot(u: Sequence[float], v: Sequence[float]) -> float:
    if len(u) != len(v):
        raise MaxwellLabError("MAXWELL932", "No se puede calcular el producto escalar con vectores de distinta longitud.", {"len_u": len(u), "len_v": len(v)})
    return sum(x * y for x, y in zip(u, v))


def cross(u: Sequence[float], v: Sequence[float]) -> List[float]:
    if len(u) != 3 or len(v) != 3:
        raise MaxwellLabError("MAXWELL932", "No se puede calcular el producto vectorial fuera de dimensión tres.", {"len_u": len(u), "len_v": len(v)})
    return [
        u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v[0],
    ]


def determinant_3x3(m: List[List[float]]) -> float:
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def clean_dim(dim: Mapping[str, int]) -> Dict[str, int]:
    return {k: v for k, v in dim.items() if v != 0}


def dim_mul(a: Mapping[str, int], b: Mapping[str, int]) -> Dict[str, int]:
    out = dict(a)
    for key, val in b.items():
        out[key] = out.get(key, 0) + val
    return clean_dim(out)


def dim_div(a: Mapping[str, int], b: Mapping[str, int]) -> Dict[str, int]:
    out = dict(a)
    for key, val in b.items():
        out[key] = out.get(key, 0) - val
    return clean_dim(out)


def dim_pow(a: Mapping[str, int], power: int) -> Dict[str, int]:
    return clean_dim({k: v * power for k, v in a.items()})


def ensure_dim_map(value: Any, code: str, name: str) -> Dict[str, int]:
    mapping = ensure_mapping(value, code, name)
    out: Dict[str, int] = {}
    for key, val in mapping.items():
        if not isinstance(key, str) or not isinstance(val, int):
            raise MaxwellLabError(code, f"Dimensión inválida en '{name}'.", {"name": name, "key": key, "value": val})
        out[key] = val
    return clean_dim(out)


def set_nested_value(data: Dict[str, Any], dotted_key: str, value: Any) -> None:
    parts = dotted_key.split('.')
    if not parts:
        raise MaxwellLabError("MAXWELL935", "La mutación negativa no contiene una ruta válida.", {"route": dotted_key})
    if parts[0] == 'constitutivas':
        obj: Any = data['constitutivas']
        parts = parts[1:]
    elif parts[0] == 'bancos':
        obj = data['bancos']
        parts = parts[1:]
    elif parts[0] == 'metrologia':
        obj = data['bancos']['metrologia']
        parts = parts[1:]
    else:
        obj = data['bancos']
    for part in parts[:-1]:
        if not isinstance(obj, Mapping) or part not in obj:
            raise MaxwellLabError("MAXWELL935", "La mutación negativa referencia una ruta inexistente.", {"route": dotted_key, "missing": part})
        obj = obj[part]
    if not isinstance(obj, Mapping) or parts[-1] not in obj:
        raise MaxwellLabError("MAXWELL935", "La mutación negativa no puede aplicarse en la ruta solicitada.", {"route": dotted_key})
    obj[parts[-1]] = value


def validate_control_case(data: Dict[str, Any]) -> None:
    ensure_mapping(data, "MAXWELL930", "raíz del caso de control")
    meta = ensure_mapping(data.get("meta"), "MAXWELL930", "meta")
    if int(ensure_numeric(meta.get("bancos_positivos_esperados"), "MAXWELL931", "meta.bancos_positivos_esperados")) != 21:
        raise MaxwellLabError("MAXWELL920", "El caso de control no fija los veintiún bancos positivos exigidos.")
    ensure_mapping(data.get("constitutivas"), "MAXWELL930", "constitutivas")
    bancos = ensure_mapping(data.get("bancos"), "MAXWELL930", "bancos")
    required = [
        "gauss_electrica", "gauss_magnetica", "faraday", "ampere_maxwell", "balance", "carga",
        "contorno_D", "contorno_B", "contorno_E", "contorno_H", "frontera", "reconfiguracion",
        "operatorial", "onda", "metrologia"
    ]
    for key in required:
        if key not in bancos:
            raise MaxwellLabError("MAXWELL930", "Falta un banco obligatorio en el caso de control.", {"missing": key})


def validate_negative_cases(negatives: Dict[str, Any]) -> None:
    ensure_mapping(negatives, "MAXWELL935", "casos negativos")
    cases = negatives.get("cases")
    if not isinstance(cases, list) or len(cases) != 15:
        raise MaxwellLabError("MAXWELL922", "El lote negativo no contiene los quince ataques obligatorios.", {"count": 0 if not isinstance(cases, list) else len(cases)})
    seen: set[str] = set()
    for idx, item in enumerate(cases):
        mapping = ensure_mapping(item, "MAXWELL935", f"cases[{idx}]")
        case_id = mapping.get("id")
        expected = mapping.get("expected_error")
        mutations = mapping.get("mutations")
        if not isinstance(case_id, str) or not case_id:
            raise MaxwellLabError("MAXWELL935", "Un caso negativo carece de identificador canónico.", {"index": idx})
        if case_id in seen:
            raise MaxwellLabError("MAXWELL935", "Existe un identificador de ataque negativo duplicado.", {"id": case_id})
        seen.add(case_id)
        if not isinstance(expected, str) or not expected.startswith("MAXWELL"):
            raise MaxwellLabError("MAXWELL935", "Un caso negativo carece de código de error esperado válido.", {"id": case_id, "expected_error": expected})
        ensure_mapping(mutations, "MAXWELL935", f"mutations de {case_id}")


def verify_case(data: Dict[str, Any]) -> List[BankResult]:
    validate_control_case(data)
    tol = ensure_numeric(data["meta"]["tolerancia"], "MAXWELL931", "meta.tolerancia")
    c = ensure_mapping(data["constitutivas"], "MAXWELL930", "constitutivas")
    b = ensure_mapping(data["bancos"], "MAXWELL930", "bancos")
    results: List[BankResult] = []

    def record(bank_id: str, description: str, observed: Any, expected: Any, passed: bool, error_code: str | None = None) -> None:
        results.append(BankResult(bank_id, description, observed, expected, passed, error_code))
        if not passed and error_code:
            raise MaxwellLabError(error_code, description, {"observed": observed, "expected": expected, "bank_id": bank_id})

    ge = ensure_mapping(b["gauss_electrica"], "MAXWELL930", "gauss_electrica")
    observed = sum(ensure_vector(ge["boundary_D"], 4, "MAXWELL932", "gauss_electrica.boundary_D"))
    expected = ensure_numeric(ge["rho"], "MAXWELL931", "gauss_electrica.rho") * ensure_numeric(ge["volume"], "MAXWELL931", "gauss_electrica.volume")
    record("BANCO_01", "Gauss eléctrica factual (forma integral)", observed, expected, almost_equal(observed, expected, tol), "MAXWELL001")

    gm = ensure_mapping(b["gauss_magnetica"], "MAXWELL930", "gauss_magnetica")
    observed = sum(ensure_vector(gm["boundary_B"], 4, "MAXWELL932", "gauss_magnetica.boundary_B"))
    expected = 0.0
    record("BANCO_02", "Gauss magnética factual (forma integral)", observed, expected, almost_equal(observed, expected, tol), "MAXWELL002")

    f = ensure_mapping(b["faraday"], "MAXWELL930", "faraday")
    observed = sum(ensure_vector(f["gamma_E"], 4, "MAXWELL932", "faraday.gamma_E"))
    expected = -(ensure_numeric(f["dnu_B"], "MAXWELL931", "faraday.dnu_B") * ensure_numeric(f["area"], "MAXWELL931", "faraday.area"))
    record("BANCO_03", "Faraday factual (forma integral)", observed, expected, almost_equal(observed, expected, tol), "MAXWELL003")

    a = ensure_mapping(b["ampere_maxwell"], "MAXWELL930", "ampere_maxwell")
    observed = sum(ensure_vector(a["gamma_H"], 4, "MAXWELL932", "ampere_maxwell.gamma_H"))
    expected = (ensure_numeric(a["J"], "MAXWELL931", "ampere_maxwell.J") + ensure_numeric(a["dnu_D"], "MAXWELL931", "ampere_maxwell.dnu_D")) * ensure_numeric(a["area"], "MAXWELL931", "ampere_maxwell.area")
    record("BANCO_04", "Ampère–Maxwell factual (forma integral)", observed, expected, almost_equal(observed, expected, tol), "MAXWELL004")

    bal = ensure_mapping(b["balance"], "MAXWELL930", "balance")
    observed = -(ensure_numeric(bal["dnu_u"], "MAXWELL931", "balance.dnu_u") + ensure_numeric(bal["div_S"], "MAXWELL931", "balance.div_S"))
    expected = ensure_numeric(bal["expected_EJ"], "MAXWELL931", "balance.expected_EJ")
    record("BANCO_05", "Balance electromagnético factual", observed, expected, almost_equal(observed, expected, tol), "MAXWELL005")

    ch = ensure_mapping(b["carga"], "MAXWELL930", "carga")
    observed = ensure_numeric(ch["dnu_rho"], "MAXWELL931", "carga.dnu_rho") + ensure_numeric(ch["div_J"], "MAXWELL931", "carga.div_J")
    expected = 0.0
    record("BANCO_06", "Conservación factual de la carga", observed, expected, almost_equal(observed, expected, tol), "MAXWELL006")

    cd = ensure_mapping(b["contorno_D"], "MAXWELL930", "contorno_D")
    observed = dot([x - y for x, y in zip(ensure_vector(cd["D2"], 3, "MAXWELL932", "contorno_D.D2"), ensure_vector(cd["D1"], 3, "MAXWELL932", "contorno_D.D1"))], ensure_vector(cd["normal"], 3, "MAXWELL932", "contorno_D.normal"))
    expected = ensure_numeric(cd["rho_s"], "MAXWELL931", "contorno_D.rho_s")
    record("BANCO_07", "Condición de contorno: componente normal de D", observed, expected, almost_equal(observed, expected, tol), "MAXWELL007")

    cb = ensure_mapping(b["contorno_B"], "MAXWELL930", "contorno_B")
    observed = dot([x - y for x, y in zip(ensure_vector(cb["B2"], 3, "MAXWELL932", "contorno_B.B2"), ensure_vector(cb["B1"], 3, "MAXWELL932", "contorno_B.B1"))], ensure_vector(cb["normal"], 3, "MAXWELL932", "contorno_B.normal"))
    expected = ensure_numeric(cb["expected"], "MAXWELL931", "contorno_B.expected")
    record("BANCO_08", "Condición de contorno: componente normal de B", observed, expected, almost_equal(observed, expected, tol), "MAXWELL008")

    ce = ensure_mapping(b["contorno_E"], "MAXWELL930", "contorno_E")
    observed = cross(ensure_vector(ce["normal"], 3, "MAXWELL932", "contorno_E.normal"), [x - y for x, y in zip(ensure_vector(ce["E2"], 3, "MAXWELL932", "contorno_E.E2"), ensure_vector(ce["E1"], 3, "MAXWELL932", "contorno_E.E1"))])
    expected = ensure_vector(ce["expected"], 3, "MAXWELL932", "contorno_E.expected")
    record("BANCO_09", "Condición de contorno: componente tangencial de E", observed, expected, vector_almost_equal(observed, expected, tol), "MAXWELL016")

    chh = ensure_mapping(b["contorno_H"], "MAXWELL930", "contorno_H")
    observed = cross(ensure_vector(chh["normal"], 3, "MAXWELL932", "contorno_H.normal"), [x - y for x, y in zip(ensure_vector(chh["H2"], 3, "MAXWELL932", "contorno_H.H2"), ensure_vector(chh["H1"], 3, "MAXWELL932", "contorno_H.H1"))])
    expected = ensure_vector(chh["J_s"], 3, "MAXWELL932", "contorno_H.J_s")
    record("BANCO_10", "Condición de contorno: componente tangencial de H", observed, expected, vector_almost_equal(observed, expected, tol), "MAXWELL017")

    fr = ensure_mapping(b["frontera"], "MAXWELL930", "frontera")
    observed = determinant_3x3(ensure_matrix_3x3(fr["jacobian"], "MAXWELL933", "frontera.jacobian"))
    expected = 0.0
    record("BANCO_11", "Criterio absoluto de frontera factual: determinante del jacobiano", observed, expected, almost_equal(observed, expected, tol), "MAXWELL009")
    frontier_state = almost_equal(observed, 0.0, tol)
    expected_state = ensure_bool(fr["frontier_active"], "MAXWELL934", "frontera.frontier_active")
    record("BANCO_12", "Criterio absoluto de frontera factual: activación de frontera", frontier_state, expected_state, frontier_state == expected_state, "MAXWELL009")

    rec = ensure_mapping(b["reconfiguracion"], "MAXWELL930", "reconfiguracion")
    observed = (1.0 if frontier_state else 0.0) * ensure_numeric(rec["lambda"], "MAXWELL931", "reconfiguracion.lambda") * ensure_numeric(rec["B_reg"], "MAXWELL931", "reconfiguracion.B_reg")
    expected = ensure_numeric(rec["expected_Rf"], "MAXWELL931", "reconfiguracion.expected_Rf")
    record("BANCO_13", "Operador exacto de reconfiguración factual", observed, expected, almost_equal(observed, expected, tol), "MAXWELL010")

    observed = ensure_numeric(c["eps_sv"], "MAXWELL931", "constitutivas.eps_sv") * ensure_numeric(c["E_const"], "MAXWELL931", "constitutivas.E_const")
    expected = ensure_numeric(c["D_const"], "MAXWELL931", "constitutivas.D_const")
    record("BANCO_14", "Relación constitutiva eléctrica factual", observed, expected, almost_equal(observed, expected, tol), "MAXWELL011")

    observed = ensure_numeric(c["mu_sv"], "MAXWELL931", "constitutivas.mu_sv") * ensure_numeric(c["H_const"], "MAXWELL931", "constitutivas.H_const")
    expected = ensure_numeric(c["B_const"], "MAXWELL931", "constitutivas.B_const")
    record("BANCO_15", "Relación constitutiva magnética factual", observed, expected, almost_equal(observed, expected, tol), "MAXWELL011")

    observed = ensure_numeric(c["sigma_sv"], "MAXWELL931", "constitutivas.sigma_sv") * ensure_numeric(c["E_const"], "MAXWELL931", "constitutivas.E_const") + ensure_numeric(c["J_ext"], "MAXWELL931", "constitutivas.J_ext")
    expected = ensure_numeric(c["J_const"], "MAXWELL931", "constitutivas.J_const")
    record("BANCO_16", "Relación constitutiva de conducción factual", observed, expected, almost_equal(observed, expected, tol), "MAXWELL011")

    op = ensure_mapping(b["operatorial"], "MAXWELL930", "operatorial")
    observed_vec = [
        ensure_numeric(op["div_D"], "MAXWELL931", "operatorial.div_D") - ensure_numeric(op["rho"], "MAXWELL931", "operatorial.rho"),
        ensure_numeric(op["div_B"], "MAXWELL931", "operatorial.div_B"),
        ensure_numeric(op["rot_E"], "MAXWELL931", "operatorial.rot_E") + ensure_numeric(op["dnu_B"], "MAXWELL931", "operatorial.dnu_B"),
        ensure_numeric(op["rot_H"], "MAXWELL931", "operatorial.rot_H") - ensure_numeric(op["dnu_D"], "MAXWELL931", "operatorial.dnu_D") - ensure_numeric(op["J"], "MAXWELL931", "operatorial.J"),
    ]
    expected_vec = [0.0, 0.0, 0.0, 0.0]
    record("BANCO_17", "Forma maestra operatoria factual", observed_vec, expected_vec, vector_almost_equal(observed_vec, expected_vec, tol), "MAXWELL013")

    observed_vec = [
        sum(ensure_vector(ge["boundary_D"], 4, "MAXWELL932", "gauss_electrica.boundary_D")) - ensure_numeric(ge["rho"], "MAXWELL931", "gauss_electrica.rho") * ensure_numeric(ge["volume"], "MAXWELL931", "gauss_electrica.volume"),
        sum(ensure_vector(gm["boundary_B"], 4, "MAXWELL932", "gauss_magnetica.boundary_B")),
        sum(ensure_vector(f["gamma_E"], 4, "MAXWELL932", "faraday.gamma_E")) + ensure_numeric(f["dnu_B"], "MAXWELL931", "faraday.dnu_B") * ensure_numeric(f["area"], "MAXWELL931", "faraday.area"),
        sum(ensure_vector(a["gamma_H"], 4, "MAXWELL932", "ampere_maxwell.gamma_H")) - (ensure_numeric(a["J"], "MAXWELL931", "ampere_maxwell.J") + ensure_numeric(a["dnu_D"], "MAXWELL931", "ampere_maxwell.dnu_D")) * ensure_numeric(a["area"], "MAXWELL931", "ampere_maxwell.area"),
    ]
    expected_vec = [0.0, 0.0, 0.0, 0.0]
    record("BANCO_18", "Forma maestra integral factual", observed_vec, expected_vec, vector_almost_equal(observed_vec, expected_vec, tol), "MAXWELL014")

    observed = {
        "M": vector_almost_equal([ensure_numeric(op["div_D"], "MAXWELL931", "operatorial.div_D") - ensure_numeric(op["rho"], "MAXWELL931", "operatorial.rho"), ensure_numeric(op["div_B"], "MAXWELL931", "operatorial.div_B"), ensure_numeric(op["rot_E"], "MAXWELL931", "operatorial.rot_E") + ensure_numeric(op["dnu_B"], "MAXWELL931", "operatorial.dnu_B"), ensure_numeric(op["rot_H"], "MAXWELL931", "operatorial.rot_H") - ensure_numeric(op["dnu_D"], "MAXWELL931", "operatorial.dnu_D") - ensure_numeric(op["J"], "MAXWELL931", "operatorial.J")], [0.0, 0.0, 0.0, 0.0], tol),
        "K": all(almost_equal(x, y, tol) for x, y in [
            (ensure_numeric(c["eps_sv"], "MAXWELL931", "constitutivas.eps_sv") * ensure_numeric(c["E_const"], "MAXWELL931", "constitutivas.E_const"), ensure_numeric(c["D_const"], "MAXWELL931", "constitutivas.D_const")),
            (ensure_numeric(c["mu_sv"], "MAXWELL931", "constitutivas.mu_sv") * ensure_numeric(c["H_const"], "MAXWELL931", "constitutivas.H_const"), ensure_numeric(c["B_const"], "MAXWELL931", "constitutivas.B_const")),
            (ensure_numeric(c["sigma_sv"], "MAXWELL931", "constitutivas.sigma_sv") * ensure_numeric(c["E_const"], "MAXWELL931", "constitutivas.E_const") + ensure_numeric(c["J_ext"], "MAXWELL931", "constitutivas.J_ext"), ensure_numeric(c["J_const"], "MAXWELL931", "constitutivas.J_const")),
        ]),
        "F": frontier_state == expected_state and almost_equal((1.0 if frontier_state else 0.0) * ensure_numeric(rec["lambda"], "MAXWELL931", "reconfiguracion.lambda") * ensure_numeric(rec["B_reg"], "MAXWELL931", "reconfiguracion.B_reg"), ensure_numeric(rec["expected_Rf"], "MAXWELL931", "reconfiguracion.expected_Rf"), tol),
    }
    expected = {"M": True, "K": True, "F": True}
    record("BANCO_19", "Ecuación única factual electromagnética", observed, expected, observed == expected, "MAXWELL015")

    dims = ensure_mapping(ensure_mapping(b["metrologia"], "MAXWELL930", "metrologia")["dimensions"], "MAXWELL930", "metrologia.dimensions")
    dims_c = {key: ensure_dim_map(value, "MAXWELL931", f"metrologia.dimensions.{key}") for key, value in dims.items()}
    checks = {
        "gauss_electrica": dim_div(dims_c["D"], dims_c["UFE"]) == dims_c["rho"],
        "faraday": dim_div(dims_c["E"], dims_c["UFE"]) == dim_div(dims_c["B"], dims_c["UE_MFC"]),
        "ampere_maxwell": dim_div(dims_c["H"], dims_c["UFE"]) == dim_div(dims_c["D"], dims_c["UE_MFC"]) == dims_c["J"],
        "balance": dim_div(dims_c["u_SV"], dims_c["UE_MFC"]) == dim_div(dims_c["S_SV"], dims_c["UFE"]) == dim_mul(dims_c["E"], dims_c["J"]),
        "onda": dim_div(dims_c["E"], dim_pow(dims_c["UFE"], 2)) == dim_div(dim_mul(dim_mul(dims_c["eps"], dims_c["mu"]), dims_c["E"]), dim_pow(dims_c["UE_MFC"], 2)),
    }
    record("BANCO_20", "Cosido dimensional soberano", checks, {k: True for k in checks}, all(checks.values()), "MAXWELL012")

    onda = ensure_mapping(b["onda"], "MAXWELL930", "onda")
    observed = ensure_numeric(onda["rotrot_E"], "MAXWELL931", "onda.rotrot_E") + ensure_numeric(onda["eps_mu_d2nu2_E"], "MAXWELL931", "onda.eps_mu_d2nu2_E")
    expected = 0.0
    record("BANCO_21", "Identidad de onda factual", observed, expected, almost_equal(observed, expected, tol), "MAXWELL018")

    return results


def verify_negative_cases(control_case: Dict[str, Any], negatives: Dict[str, Any]) -> List[Dict[str, Any]]:
    validate_negative_cases(negatives)
    out: List[Dict[str, Any]] = []
    for item in negatives["cases"]:
        mutated = copy.deepcopy(control_case)
        for key, value in item["mutations"].items():
            set_nested_value(mutated, key, value)
        try:
            verify_case(mutated)
            out.append({"id": item["id"], "status": "unexpected-pass", "expected_error": item["expected_error"]})
        except MaxwellLabError as exc:
            out.append({
                "id": item["id"],
                "status": "caught",
                "expected_error": item["expected_error"],
                "observed_error": exc.code,
                "message": exc.message,
                "matches": exc.code == item["expected_error"],
            })
        except (TypeError, ValueError, KeyError, IndexError) as exc:  # defensa estructural no silenciosa
            out.append({
                "id": item["id"],
                "status": "crash",
                "expected_error": item["expected_error"],
                "observed_error": type(exc).__name__,
                "message": str(exc),
                "matches": False,
            })
    return out


def _write_result_files(output_dir: Path, summary: Dict[str, Any]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / 'runner_maestro.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding='utf-8')
    lines = [RIGHTS, '', '# Resultado del runner maestro del bloque electromagnético factual', '', f"- Bancos positivos superados: {summary['positive_passed']}/{summary['positive_expected']}", f"- Casos negativos detectados correctamente: {summary['negative_caught']}/{summary['negative_total']}", '', '## Bancos positivos', '', '| Banco | Descripción | Observado | Esperado | Dictamen |', '|---|---|---|---|---|']
    for r in summary['positive_results']:
        lines.append(f"| {r['bank_id']} | {r['description']} | `{r['observed']}` | `{r['expected']}` | {'Pasa' if r['passed'] else 'No pasa'} |")
    lines += ['', '## Casos negativos', '', '| Caso | Error esperado | Error observado | Dictamen |', '|---|---|---|---|']
    for r in summary['negative_results']:
        lines.append(f"| {r['id']} | `{r['expected_error']}` | `{r.get('observed_error', 'ninguno')}` | {'Pasa' if r.get('matches', False) else 'No pasa'} |")
    (output_dir / 'runner_maestro_resumen.md').write_text("\n".join(lines) + "\n", encoding='utf-8')
    stdout = [RIGHTS, '', '[APTO] Runner maestro completado sin pases silenciosos.', f"Bancos positivos: {summary['positive_passed']}/{summary['positive_expected']}", f"Casos negativos detectados: {summary['negative_caught']}/{summary['negative_total']}", '']
    (output_dir / 'runner_maestro.py.stdout.txt').write_text("\n".join(stdout), encoding='utf-8')


def main(control_path: Path, negatives_path: Path, output_dir: Path) -> Dict[str, Any]:
    control = load_json(control_path)
    negatives = load_json(negatives_path)
    results = verify_case(control)
    negative_results = verify_negative_cases(control, negatives)
    expected_positive = int(control['meta']['bancos_positivos_esperados'])
    if len(results) != expected_positive:
        raise MaxwellLabError("MAXWELL920", "El runner maestro no produjo los bancos positivos exigidos.", {"count": len(results), "expected": expected_positive})
    if not all(r.passed for r in results):
        raise MaxwellLabError("MAXWELL921", "Existe al menos un banco positivo no superado.")
    unexpected = [r for r in negative_results if r['status'] != 'caught' or not r.get('matches', False)]
    if unexpected:
        raise MaxwellLabError("MAXWELL922", "Existe al menos un ataque negativo sin detección correcta.", {"unexpected": unexpected})
    summary = {
        'derechos_y_autoria': {'copyright': RIGHTS},
        'meta': control['meta'],
        'positive_results': [r.__dict__ for r in results],
        'negative_results': negative_results,
        'positive_passed': sum(1 for r in results if r.passed),
        'positive_expected': expected_positive,
        'negative_caught': sum(1 for r in negative_results if r.get('matches', False)),
        'negative_total': len(negative_results),
    }
    _write_result_files(output_dir, summary)
    return summary
