"""
Laboratorio mínimo del frente de corpus observacional tipado del Sistema Vectorial SV.

Autor: Juan Antonio Lloret Egea
ORCID: 0000-0002-6634-3351
Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
Publicación: IA en™ – La Biblia de la IA™
ISSN: 2695-6411
Colección: Programa de interfaces del Sistema Vectorial SV
Lugar y fecha: Madrid, 20 de marzo de 2026
Estado: manuscrito v0.5 de refuerzo adversarial

Este código es demostrativo. No constituye API, módulo ni subderivado operativo del Sistema Vectorial SV.
Su función es únicamente exponer el principio conservador del patrón inaugural.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
import csv

SIGMA = {"0", "1", "U"}
ADMISIBILIDAD = {"ok", "degradado", "fallido", "U"}
SUFICIENCIA = {"suficiente", "parcial", "deficiente", "rota"}


@dataclass(frozen=True)
class ObservacionLocal:
    nombre: str
    capturada: bool
    admisibilidad: str
    sigma_local: str
    nota: str

    def validar(self) -> None:
        if self.admisibilidad not in ADMISIBILIDAD:
            raise ValueError(f"Estado de admisibilidad no válido: {self.admisibilidad}")
        if self.sigma_local not in SIGMA:
            raise ValueError(f"Valor sigma no válido: {self.sigma_local}")


@dataclass(frozen=True)
class GarantiaLocal:
    nombre: str
    avala_entrega: bool
    suficiencia: str
    nota: str

    def validar(self) -> None:
        if self.suficiencia not in SUFICIENCIA:
            raise ValueError(f"Suficiencia no válida: {self.suficiencia}")


@dataclass(frozen=True)
class ResultadoGlobal:
    caso: str
    salida: str
    decision: str
    fundamento: str


def compuerta_jerarquica_conservadora(obs: ObservacionLocal, gar: GarantiaLocal) -> ResultadoGlobal:
    """
    Núcleo axiomático del patrón inaugural:
    1. Sin observación suficiente, no hay cierre favorable.
    2. Sin garantía suficiente, no hay cierre favorable.
    3. La indeterminación material relevante preserva U.
    4. El fallo fuerte de captura o admisibilidad produce inadmisibilidad.
    """
    obs.validar()
    gar.validar()

    if not obs.capturada:
        return ResultadoGlobal(obs.nombre, "inadmisibilidad", "bloqueo", "Fallo de captura: no procede entrega semántica.")
    if obs.admisibilidad == "fallido":
        return ResultadoGlobal(obs.nombre, "inadmisibilidad", "bloqueo", "La cadena observacional es fallida; la compuerta conserva la inadmisibilidad.")
    if obs.admisibilidad == "U" or obs.sigma_local == "U":
        return ResultadoGlobal(obs.nombre, "U", "suspensión", "La observación no permite clausura legítima; se preserva la U honesta.")
    if not gar.avala_entrega or gar.suficiencia in {"deficiente", "rota"}:
        return ResultadoGlobal(obs.nombre, "U", "suspensión", "La garantía no puede avalar honestamente la entrega; no se fabrica certeza.")
    return ResultadoGlobal(obs.nombre, obs.sigma_local, "paso", "Observación suficiente y garantía válida: la compuerta autoriza la entrega.")


CASOS = [
    (
        ObservacionLocal("Caso A — Entrega favorable", True, "ok", "1", "Unidad observacional correctamente capturada y ternarizada."),
        GarantiaLocal("Garantía A", True, "suficiente", "La cadena observacional y la trazabilidad son bastante sólidas."),
    ),
    (
        ObservacionLocal("Caso B — Salida en U", True, "degradado", "1", "Existe observación, pero un punto material no queda blindado."),
        GarantiaLocal("Garantía B", False, "deficiente", "La garantía no puede avalar honestamente la entrega."),
    ),
    (
        ObservacionLocal("Caso C — Inadmisibilidad", False, "fallido", "U", "La captura falla y la cadena se corta."),
        GarantiaLocal("Garantía C", False, "rota", "No existe base suficiente para garantizar nada."),
    ),
]


def main() -> None:
    out_dir = Path(__file__).resolve().parent / "salidas"
    out_dir.mkdir(parents=True, exist_ok=True)
    resultados = [compuerta_jerarquica_conservadora(obs, gar) for obs, gar in CASOS]

    csv_path = out_dir / "resultados_laboratorio.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["caso", "salida", "decision", "fundamento"])
        writer.writeheader()
        for resultado in resultados:
            writer.writerow(asdict(resultado))

    md_path = out_dir / "reporte_laboratorio.md"
    with md_path.open("w", encoding="utf-8") as fh:
        fh.write("""# Laboratorio mínimo del frente de corpus observacional tipado

**Autor:** Juan Antonio Lloret Egea  
**ORCID:** 0000-0002-6634-3351  
**Institución:** ITVIA  
**Publicación:** IA en™ – La Biblia de la IA™  
**ISSN:** 2695-6411  
**Colección:** Programa de interfaces del Sistema Vectorial SV  
**Lugar y fecha:** Madrid, 20 de marzo de 2026

Este laboratorio no integra nada en el SV. Solo demuestra el principio conservador del patrón inaugural.

## Núcleo axiomático ensayado

1. Sin observación suficiente, no hay cierre favorable.
2. Sin garantía suficiente, no hay cierre favorable.
3. La indeterminación material relevante preserva `U`.
4. El fallo fuerte de captura o admisibilidad produce inadmisibilidad.

| Caso | Salida | Decisión | Fundamento |
|---|---|---|---|
""")
        for resultado in resultados:
            fh.write(f"| {resultado.caso} | {resultado.salida} | {resultado.decision} | {resultado.fundamento} |\n")
        fh.write("""
## Casos de entrada

""")
        for obs, gar in CASOS:
            fh.write(f"### {obs.nombre}\n")
            fh.write(f"- Observación: captura={obs.capturada}, admisibilidad={obs.admisibilidad}, sigma_local={obs.sigma_local}.\n")
            fh.write(f"- Nota observacional: {obs.nota}\n")
            fh.write(f"- Garantía: avala_entrega={gar.avala_entrega}, suficiencia={gar.suficiencia}.\n")
            fh.write(f"- Nota de garantía: {gar.nota}\n\n")

    print(f"CSV guardado en: {csv_path}")
    print(f"Reporte guardado en: {md_path}")


if __name__ == "__main__":
    main()
