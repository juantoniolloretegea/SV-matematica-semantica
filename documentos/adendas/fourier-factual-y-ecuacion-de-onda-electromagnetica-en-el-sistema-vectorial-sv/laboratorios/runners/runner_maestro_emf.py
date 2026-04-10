from __future__ import annotations
import math
from pathlib import Path
from sv_emf_core import (
    N, COURANT_MAX, CASE_ID, C_SV, DELTA_ELL, DELTA_XI, EDGE_SET_1_INDEXED,
    PULSE_POSITION_1_INDEXED, OMEGA2,
    observable_ed_em_01, modal_transform, reconstruct, content_quadratic,
    parseval_rhs, residuals, propagate_modal, freeze_json, timestamp_utc,
    round_list, round_float,
)

BASE = Path(__file__).resolve().parents[1]
OUT = BASE / "json_congelados"
OUT.mkdir(exist_ok=True)
LABS = ["LAB-EM-01", "LAB-EM-02", "LAB-EM-03", "LAB-EM-04", "LAB-EM-05"]

TOL_EXACTA = 1e-12


def invariants(payload: dict) -> list[str]:
    errs = []
    if payload.get("dictamen_local") != "APTO":
        errs.append("dictamen_local_invalido")
    if not payload.get("passed", False):
        errs.append("passed_false")
    if "timestamp" not in payload:
        errs.append("timestamp_ausente")
    if "md5" not in payload:
        errs.append("md5_ausente")
    return errs


def lab_01():
    x = observable_ed_em_01()
    mean, alpha, beta, mod = modal_transform(x)
    xr = reconstruct(mean, alpha, beta, 4)
    max_err = max(abs(x[i] - xr[i]) for i in range(len(x)))
    passed = max_err < TOL_EXACTA
    payload = {
        "lab_id": "LAB-EM-01",
        "case_id": CASE_ID,
        "observable": "E_SV_escalarizado",
        "pulse_position_1_indexed": PULSE_POSITION_1_INDEXED,
        "input_state": round_list(x),
        "media": round_float(mean),
        "alpha": round_list(alpha),
        "beta": round_list(beta),
        "modulos": round_list(mod),
        "reconstruccion_exacta": round_list(xr),
        "error_maximo_reconstruccion": round_float(max_err),
        "tolerancia": TOL_EXACTA,
        "passed": passed,
        "dictamen_local": "APTO" if passed else "NO_APTO",
        "timestamp": timestamp_utc(),
    }
    return payload


def lab_02():
    x = observable_ed_em_01()
    mean, alpha, beta, mod = modal_transform(x)
    trunc = {f"K_{k}": round_list(reconstruct(mean, alpha, beta, k)) for k in range(0, 5)}
    # Criterio: reconstruccion K=4 exacta dentro de tolerancia
    xr4 = reconstruct(mean, alpha, beta, 4)
    max_err_k4 = max(abs(x[i] - xr4[i]) for i in range(N))
    # Criterio: ningun valor NaN o Inf en ninguna reconstruccion
    all_finite = all(
        math.isfinite(v)
        for k in range(5)
        for v in reconstruct(mean, alpha, beta, k)
    )
    # Criterio: residuos decrecen monotonamente con K (norma cuadratica)
    norms = []
    for k in range(5):
        xrk = reconstruct(mean, alpha, beta, k)
        norms.append(sum((x[i] - xrk[i]) ** 2 for i in range(N)))
    monotone = all(norms[k] >= norms[k + 1] for k in range(4))
    passed = (max_err_k4 < TOL_EXACTA) and all_finite and monotone
    payload = {
        "lab_id": "LAB-EM-02",
        "case_id": CASE_ID,
        "observable": "E_SV_escalarizado",
        "transformada_modal": {
            "media": round_float(mean),
            "alpha": round_list(alpha),
            "beta": round_list(beta),
            "modulos": round_list(mod),
        },
        "reconstrucciones": trunc,
        "error_maximo_k4": round_float(max_err_k4),
        "todos_finitos": all_finite,
        "residuos_decrecientes": monotone,
        "tolerancia": TOL_EXACTA,
        "passed": passed,
        "dictamen_local": "APTO" if passed else "NO_APTO",
        "timestamp": timestamp_utc(),
    }
    return payload


def lab_03():
    x = observable_ed_em_01()
    mean, alpha, beta, mod = modal_transform(x)
    q = content_quadratic(x)
    rhs = parseval_rhs(mean, mod)
    diff = abs(q - rhs)
    passed = diff < TOL_EXACTA
    payload = {
        "lab_id": "LAB-EM-03",
        "case_id": CASE_ID,
        "contenido_cuadratico": round_float(q),
        "lado_derecho_balance": round_float(rhs),
        "diferencia_absoluta": round_float(diff),
        "tolerancia": TOL_EXACTA,
        "passed": passed,
        "dictamen_local": "APTO" if passed else "NO_APTO",
        "timestamp": timestamp_utc(),
    }
    return payload


def lab_04():
    x = observable_ed_em_01()
    mean, alpha, beta, mod = modal_transform(x)
    res = {f"K_{k}": residuals(x, mean, alpha, beta, k) for k in range(0, 4)}
    # Criterio 1: ningun valor NaN/Inf en ningun residual
    all_finite = all(
        math.isfinite(v)
        for k in range(4)
        for v in res[f"K_{k}"]["reconstruccion_truncada"]
    )
    # Criterio 2: borde_maximo decrece con K (convergencia del residual de borde)
    borde_maximos = [res[f"K_{k}"]["borde_maximo"] for k in range(4)]
    borde_decrece = all(borde_maximos[k] >= borde_maximos[k + 1] for k in range(3))
    # Criterio 3: concentracion_borde en (0, 1] para K < 4 donde hay residual
    concentraciones_validas = all(
        0.0 <= res[f"K_{k}"]["concentracion_borde"] <= 1.0
        for k in range(4)
    )
    passed = all_finite and borde_decrece and concentraciones_validas
    payload = {
        "lab_id": "LAB-EM-04",
        "case_id": CASE_ID,
        "edge_set_1_indexed": EDGE_SET_1_INDEXED,
        "resultados_truncacion": {
            k: {
                "borde_maximo": round_float(v["borde_maximo"]),
                "borde_cuadratico": round_float(v["borde_cuadratico"]),
                "residuo_total_cuadratico": round_float(v["residuo_total_cuadratico"]),
                "concentracion_borde": round_float(v["concentracion_borde"]),
                "sobreoscilacion": round_float(v["sobreoscilacion"]),
                "suboscilacion": round_float(v["suboscilacion"]),
                "reconstruccion_truncada": round_list(v["reconstruccion_truncada"]),
            }
            for k, v in res.items()
        },
        "todos_finitos": all_finite,
        "borde_maximo_decreciente": borde_decrece,
        "concentraciones_validas": concentraciones_validas,
        "passed": passed,
        "dictamen_local": "APTO" if passed else "NO_APTO",
        "timestamp": timestamp_utc(),
    }
    return payload


def lab_05():
    x = observable_ed_em_01()
    evo = propagate_modal(x, steps=6, delta_xi=DELTA_XI)
    # Criterio 1: estabilidad de Courant
    courant_ok = COURANT_MAX < 2.0
    # Criterio 2: ningun valor NaN/Inf en ningun snapshot
    all_finite = all(
        math.isfinite(v)
        for item in evo["snapshots"]
        for v in item["estado"]
    )
    # Criterio 3: contenido cuadratico en todos los pasos es finito y positivo
    #   Nota: el contenido cuadratico NO se conserva en el esquema leapfrog
    #   discreto (la cantidad conservada es una energia escalonada distinta).
    #   Este criterio solo verifica que la propagacion no diverge.
    q_bounded = all(
        math.isfinite(item["contenido_cuadratico"]) and item["contenido_cuadratico"] >= 0.0
        for item in evo["snapshots"]
    )
    passed = courant_ok and all_finite and q_bounded
    payload = {
        "lab_id": "LAB-EM-05",
        "case_id": CASE_ID,
        "condicion_inicial": {
            "descripcion": "velocidad factual inicial nula (arranque frio: a_m(-delta_xi) = a_m(0))",
            "delta_xi": DELTA_XI,
            "delta_ell": DELTA_ELL,
            "c_sv": C_SV,
        },
        "nota_contenido_cuadratico": (
            "El contenido cuadratico sum(X_i^2) NO es la cantidad conservada del "
            "esquema leapfrog. Su variacion entre pasos es esperada y no indica "
            "inestabilidad. La cantidad conservada es la energia escalonada discreta."
        ),
        "courant_max": round_float(COURANT_MAX),
        "courant_estable": courant_ok,
        "delta_xi": DELTA_XI,
        "delta_ell": DELTA_ELL,
        "c_sv": C_SV,
        "omega2": round_list(evo["omega2"]),
        "lambdas": round_list(evo["lambdas"]),
        "snapshots": [
            {
                "paso": item["paso"],
                "xi": round_float(item["xi"]),
                "alpha": round_list(item["alpha"]),
                "beta": round_list(item["beta"]),
                "estado": round_list(item["estado"]),
                "contenido_cuadratico": round_float(item["contenido_cuadratico"]),
                "indice_maximo_1_indexed": item["indice_maximo_1_indexed"],
                "valor_maximo": round_float(item["valor_maximo"]),
            }
            for item in evo["snapshots"]
        ],
        "todos_finitos": all_finite,
        "contenido_cuadratico_acotado": q_bounded,
        "passed": passed,
        "dictamen_local": "APTO" if passed else "NO_APTO",
        "timestamp": timestamp_utc(),
    }
    return payload


RUNS = {
    "LAB-EM-01": lab_01,
    "LAB-EM-02": lab_02,
    "LAB-EM-03": lab_03,
    "LAB-EM-04": lab_04,
    "LAB-EM-05": lab_05,
}


def main() -> None:
    results = []
    for name in LABS:
        payload = RUNS[name]()
        # freeze_json ahora escribe el fichero con el campo md5 incluido
        freeze_json(OUT / f"{name.lower()}.json", payload)
        errs = invariants(payload)
        if errs:
            payload["passed"] = False
            payload["dictamen_local"] = "NO_APTO"
            payload["errores_invariantes"] = errs
            # reescribir con el dictamen actualizado
            freeze_json(OUT / f"{name.lower()}.json", payload)
        results.append(payload)
        if errs or not payload["passed"]:
            report = {
                "suite": "EMF",
                "labs": results,
                "passed": False,
                "dictamen_final": "NO_APTO",
                "fail_fast": True,
                "generated_at": timestamp_utc(),
            }
            freeze_json(OUT / "reporte_laboratorios_emf.json", report)
            raise SystemExit(1)
    report = {
        "suite": "EMF",
        "labs": results,
        "passed": True,
        "dictamen_final": "APTO",
        "fail_fast": True,
        "generated_at": timestamp_utc(),
    }
    freeze_json(OUT / "reporte_laboratorios_emf.json", report)
    print(OUT / "reporte_laboratorios_emf.json")


if __name__ == "__main__":
    main()
