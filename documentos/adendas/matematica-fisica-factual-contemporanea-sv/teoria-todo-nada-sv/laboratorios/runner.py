"""
runner.py — Runner agregado del conjunto laboratorial reproducible

Documento canónico vinculado:
  Teoría del TODO y de la NADA en el Sistema Vectorial SV
  https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-todo-nada-sv

Ejecuta los quince laboratorios canónicos y emite tabla resumen humano-legible
y, opcionalmente, salida JSON con --json.

Uso:
    python runner.py
    python runner.py --json

Author:    Juan Antonio Lloret Egea
ORCID:     https://orcid.org/0000-0002-6634-3351
ISSN:      2695-6411
Editor:    IA eñ™ — La Biblia de la IA™ (Instituto Tecnológico Virtual de la
           Inteligencia Artificial para el Español, ITVIA)
License:   CC BY-NC-ND 4.0
Copyright: © 2026 Juan Antonio Lloret Egea. Todos los derechos reservados.
Protected: CEDRO — https://www.cedro.org/english?lng=en
"""

from __future__ import annotations
import json
import sys
import importlib

LABS = [
    "lab01_alfabeto_y_celula",
    "lab02_suceso_admisible",
    "lab03_distancia_factual_fibrosa",
    "lab04_agotamiento_K3n",
    "lab05_frontera_mu_lambda",
    "lab06_componentes_ciclo_q",
    "lab07_normalizacion_zeta",
    "lab08_verificador_ternario_fuerte",
    "lab09_absorcion_canonica",
    "lab10_ley_canonica_rectora",
    "lab11_mapa_absorcion",
    "lab12_banco_diez_supuestos",
    "lab13_tabla_cruzada_once_absorciones",
    "lab14_cinco_interpretaciones",
    "lab15_validador_total",
]


def render_header():
    border = "=" * 76
    return (
        f"{border}\n"
        f"  Conjunto laboratorial reproducible — Teoría del TODO y de la NADA\n"
        f"  en el Sistema Vectorial SV\n"
        f"  Documento canónico: Lloret Egea, 2026.\n"
        f"  URL: https://github.com/juantoniolloretegea/SV-matematica-semantica/\n"
        f"       tree/main/documentos/adendas/matematica-fisica-factual-\n"
        f"       contemporanea-sv/teoria-todo-nada-sv\n"
        f"{border}"
    )


def main():
    json_mode = "--json" in sys.argv

    if not json_mode:
        print(render_header())

    resultados = []
    for lab_name in LABS:
        try:
            module = importlib.import_module(lab_name)
            r = module.run()
            resultados.append(r)
            if not json_mode:
                marca = "APTO    " if r.is_apt() else "NO APTO "
                print(f"  [{marca}] {lab_name:50s} verdict={r.verdict!s:4s}  "
                      f"section={r.section}")
        except Exception as e:
            resultados.append(None)
            if not json_mode:
                print(f"  [ERROR  ] {lab_name:50s} excepción: {e}")

    aptos = sum(1 for r in resultados if r is not None and r.is_apt())
    total = len(resultados)

    if json_mode:
        out = {
            "documento_canonico": (
                "https://github.com/juantoniolloretegea/SV-matematica-semantica/"
                "tree/main/documentos/adendas/matematica-fisica-factual-"
                "contemporanea-sv/teoria-todo-nada-sv"
            ),
            "total_laboratorios": total,
            "aptos": aptos,
            "no_aptos": total - aptos,
            "dictamen_global": (
                "𝓔★_TODO,SV = 0 (APTO)" if aptos == total else "NO APTO"
            ),
            "resultados": [
                r.to_dict() if r is not None else None
                for r in resultados
            ],
        }
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        border = "-" * 76
        print(border)
        print(f"  Total laboratorios: {total}")
        print(f"  APTOS:              {aptos}")
        print(f"  NO APTOS:           {total - aptos}")
        if aptos == total:
            print(f"  DICTAMEN GLOBAL:    𝓔★_TODO,SV = 0  (APTO)")
        else:
            print(f"  DICTAMEN GLOBAL:    NO APTO")
        print(border)

    sys.exit(0 if aptos == total else 1)


if __name__ == "__main__":
    main()
