from __future__ import annotations
import math
from pathlib import Path
from sv_emf_core import (
    COURANT_MAX, observable_ed_em_01, modal_transform, reconstruct,
    residuals, propagate_modal, freeze_json, timestamp_utc,
    round_list, round_float,
)

BASE = Path(__file__).resolve().parents[1]
OUT = BASE / "json_congelados"
OUT.mkdir(exist_ok=True)


def main() -> None:
    x = observable_ed_em_01()
    mean, alpha, beta, mod = modal_transform(x)
    rec = reconstruct(mean, alpha, beta, 4)
    edge = residuals(x, mean, alpha, beta, 2)
    evo = propagate_modal(x, steps=4)
    courant_ok = COURANT_MAX < 2.0
    all_finite = all(
        math.isfinite(v)
        for item in evo["snapshots"]
        for v in item["estado"]
    )
    max_err_k4 = max(abs(x[i] - rec[i]) for i in range(len(x)))
    passed = courant_ok and all_finite and (max_err_k4 < 1e-12)
    payload = {
        "runner": "ed_em_01",
        "courant_max": round_float(COURANT_MAX),
        "courant_estable": courant_ok,
        "input_state": round_list(x),
        "media": round_float(mean),
        "alpha": round_list(alpha),
        "beta": round_list(beta),
        "modulos": round_list(mod),
        "reconstruccion_exacta": round_list(rec),
        "error_maximo_k4": round_float(max_err_k4),
        "reconstruccion_truncada_k2": round_list(edge["reconstruccion_truncada"]),
        "borde_maximo_k2": round_float(edge["borde_maximo"]),
        "snapshots": [
            {
                "paso": item["paso"],
                "xi": round_float(item["xi"]),
                "valor_maximo": round_float(item["valor_maximo"]),
                "indice_maximo_1_indexed": item["indice_maximo_1_indexed"],
            }
            for item in evo["snapshots"]
        ],
        "passed": passed,
        "dictamen_local": "APTO" if passed else "NO_APTO",
        "timestamp": timestamp_utc(),
    }
    freeze_json(OUT / "runner_ed_em_01.json", payload)
    print(OUT / "runner_ed_em_01.json")


if __name__ == "__main__":
    main()
