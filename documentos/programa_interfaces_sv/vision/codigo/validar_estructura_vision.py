from __future__ import annotations

from pathlib import Path
import sys

BASE = Path(__file__).resolve().parent.parent
FIG_DIR = BASE / "figuras"
MANUSCRITO = BASE / "manuscrito" / "paper_sv_vision_pubpub.md"
META_1 = BASE / "meta" / "NOTA_BLOQUE_1.md"
META_2 = BASE / "meta" / "NOTA_CIERRE_REPO.md"
README_RAIZ = BASE / "README.md"

EXPECTED = [
    "portada_vision_sv_1200x800.png",
    "fig_01_cadena_visual_captura_admisibilidad_ternarizacion.png",
    "fig_02_banco_visual_n9_render_canonico.png",
    "fig_03_u_visual_oclusion_ambiguedad_reapertura.png",
    "fig_04_suceso_frame_reevaluacion_trayectoria_visual.png",
    "fig_05_carta_r2_r3_auxiliar_no_ontologica.png",
    "fig_06_tres_vallas_carril_vision.png",
]

def check(condition: bool, ok: str, fail: str, errors: list[str]) -> None:
    if condition:
        print(f"OK: {ok}")
    else:
        print(f"ERROR: {fail}")
        errors.append(fail)

def main() -> int:
    errors: list[str] = []

    check(README_RAIZ.exists(), "Existe vision/README.md", "Falta vision/README.md", errors)
    check(MANUSCRITO.exists(), "Existe manuscrito/paper_sv_vision_pubpub.md", "Falta el manuscrito principal", errors)
    check(META_1.exists(), "Existe meta/NOTA_BLOQUE_1.md", "Falta meta/NOTA_BLOQUE_1.md", errors)
    check(META_2.exists(), "Existe meta/NOTA_CIERRE_REPO.md", "Falta meta/NOTA_CIERRE_REPO.md", errors)
    check(FIG_DIR.exists(), "Existe el directorio figuras/", "Falta el directorio figuras/", errors)

    for name in EXPECTED:
        path = FIG_DIR / name
        check(path.exists(), f"Existe {name}", f"Falta {name}", errors)

    if MANUSCRITO.exists():
        text = MANUSCRITO.read_text(encoding="utf-8", errors="replace")
        refs = [f"../figuras/{name}" for name in EXPECTED]
        for ref in refs:
            check(ref in text, f"Referencia encontrada en manuscrito: {ref}", f"No aparece en el manuscrito la referencia {ref}", errors)

    if errors:
        print("\nValidación fallida.")
        return 1

    print("\nValidación correcta del carril de visión.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
