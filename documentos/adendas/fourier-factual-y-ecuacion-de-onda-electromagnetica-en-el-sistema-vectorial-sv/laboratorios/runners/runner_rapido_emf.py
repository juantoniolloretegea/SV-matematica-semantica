from __future__ import annotations
import math
from pathlib import Path
from sv_emf_core import (
    COURANT_MAX, observable_ed_em_01, propagate_modal, freeze_json,
    timestamp_utc, round_list, round_float, DELTA_XI, DELTA_ELL, C_SV,
)

BASE = Path(__file__).resolve().parents[1]
OUT = BASE / "json_congelados"
OUT.mkdir(exist_ok=True)


def main() -> None:
    evo = propagate_modal(observable_ed_em_01(), steps=2, delta_xi=DELTA_XI)
    courant_ok = COURANT_MAX < 2.0
    all_finite = all(
        math.isfinite(v)
        for item in evo["snapshots"]
        for v in item["estado"]
    )
    passed = courant_ok and all_finite
    payload = {
        "runner": "rapido_emf",
        "courant_max": round_float(COURANT_MAX),
        "courant_estable": courant_ok,
        "delta_xi": DELTA_XI,
        "delta_ell": DELTA_ELL,
        "c_sv": C_SV,
        "snapshots": [
            {
                "paso": item["paso"],
                "xi": round_float(item["xi"]),
                "estado": round_list(item["estado"]),
                "contenido_cuadratico": round_float(item["contenido_cuadratico"]),
            }
            for item in evo["snapshots"]
        ],
        "passed": passed,
        "dictamen_local": "APTO" if passed else "NO_APTO",
        "timestamp": timestamp_utc(),
    }
    freeze_json(OUT / "runner_rapido_emf.json", payload)
    print(OUT / "runner_rapido_emf.json")


if __name__ == "__main__":
    main()
