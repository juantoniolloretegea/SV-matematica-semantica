from __future__ import annotations
import csv
from dataclasses import dataclass
from pathlib import Path

VALID_OUTPUTS = {
    "admisibilidad olfativa suficiente",
    "admisibilidad olfativa con U",
    "inadmisibilidad para el carril de olfato",
    "reapertura obligada",
}

@dataclass(frozen=True)
class Caso:
    nombre: str
    via: str
    contexto: str
    evidencia_volatil: str
    coactivacion_gustativa: str
    coactivacion_chemestesica: str
    carga_textural_termica: str


def clasificar(c: Caso) -> str:
    via = c.via.lower()
    contexto = c.contexto.lower()
    evidencia = c.evidencia_volatil.lower()
    gusto = c.coactivacion_gustativa.lower()
    chemo = c.coactivacion_chemestesica.lower()
    carga = c.carga_textural_termica.lower()

    if evidencia in {"insuficiente", "contradictoria"}:
        return "inadmisibilidad para el carril de olfato"
    if via == "indeterminada":
        return "admisibilidad olfativa con U"
    if chemo in {"presente", "no separable"} and via != "ortonasal":
        return "admisibilidad olfativa con U"
    if gusto in {"presente", "no separable"} and contexto != "ambiental":
        return "admisibilidad olfativa con U"
    if carga == "relevante" and contexto != "ambiental":
        return "admisibilidad olfativa con U"
    return "admisibilidad olfativa suficiente"


def main() -> None:
    casos = [
        Caso("Caso 1. Café recién servido, sin ingestión", "ortonasal", "ambiental", "suficiente", "ausente", "ausente", "no relevante"),
        Caso("Caso 2. Sabor a vainilla durante ingestión de crema", "retronasal", "ingestivo", "suficiente", "presente", "ausente", "relevante"),
        Caso("Caso 3. Caramelo mentolado", "indeterminada", "ingestivo", "suficiente", "no separable", "no separable", "relevante"),
        Caso("Caso 4. Solución de tastant con componente volátil", "retronasal", "ingestivo", "suficiente", "presente", "ausente", "no relevante"),
        Caso("Caso 5. Olor ambiental en cocina con humo y picor ocular", "ortonasal", "ambiental", "suficiente", "ausente", "presente", "relevante"),
    ]
    out_dir = Path(__file__).resolve().parent
    csv_path = out_dir / "resultados_laboratorio.csv"
    md_path = out_dir / "reporte_laboratorio.md"

    rows = []
    for caso in casos:
        salida = clasificar(caso)
        assert salida in VALID_OUTPUTS
        rows.append({
            "caso": caso.nombre,
            "via": caso.via,
            "contexto": caso.contexto,
            "evidencia_volatil": caso.evidencia_volatil,
            "coactivacion_gustativa": caso.coactivacion_gustativa,
            "coactivacion_chemestesica": caso.coactivacion_chemestesica,
            "carga_textural_termica": caso.carga_textural_termica,
            "salida_modelo": salida,
        })

    with csv_path.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    lines = [
        "# Reporte del laboratorio mínimo\n",
        "Este reporte se genera a partir de `lab_minimo_olfato.py` y ofrece una verificación mínima de consistencia interna del esquema propuesto.\n",
        "## Resultados\n",
        "| Caso | Salida del modelo |",
        "|---|---|",
    ]
    for row in rows:
        lines.append(f"| {row['caso']} | {row['salida_modelo']} |")
    lines += [
        "\n## Regla de prudencia aplicada\n",
        "Ante mezcla no separable, vía indeterminada o coactivación relevante en contexto no limpio, el modelo conserva `U` antes que cierre fuerte.\n",
    ]
    md_path.write_text("\n".join(lines), encoding='utf-8')

if __name__ == '__main__':
    main()
