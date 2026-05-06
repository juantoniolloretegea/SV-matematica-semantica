# -*- coding: utf-8 -*-
# © 2026. Todos los derechos reservados. | Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 06/05/2026
# DOI del laboratorio canónico: 10.5281/zenodo.20058612.

from pathlib import Path
import subprocess
import json
import sys

PUBLICACION = Path(__file__).resolve().parent
LAB_ROOT = PUBLICACION.parent
ANEXO = LAB_ROOT / "anexo-tecnico"

commands = [
    (PUBLICACION, [sys.executable, "runner.py"]),
    (PUBLICACION, [sys.executable, "runner_bis.py"]),
    (ANEXO, [sys.executable, "runner_prop.py"]),
]

resultados = []
for cwd, cmd in commands:
    p = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, timeout=60)
    resultados.append({
        "cwd": str(cwd.relative_to(LAB_ROOT)),
        "cmd": " ".join(cmd),
        "returncode": p.returncode,
        "stdout": p.stdout.strip(),
        "stderr": p.stderr.strip(),
    })
    if p.returncode != 0:
        print(json.dumps({"estado":"NO_APTO", "resultados":resultados}, ensure_ascii=False, indent=2))
        raise SystemExit(p.returncode)

out = {"estado":"APTO_PUBLICACION_INTEGRAL", "resultados":resultados}
print(json.dumps(out, ensure_ascii=False, indent=2))
