# -*- coding: utf-8 -*-
"""
Runner maestro — Imperfección preformal y espacio.
Autor: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351
© 2026. Todos los derechos reservados. Licencia CC BY-NC-ND 4.0.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "validadores"))
from sv_validadores import run_all  # noqa: E402


def main() -> int:
    result = run_all(ROOT)
    out = ROOT / "registros" / "resultado_runner.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result["resultado_global"] != "APTO":
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
