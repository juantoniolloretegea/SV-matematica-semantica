"""
sv_lib.py — Biblioteca compartida del conjunto laboratorial reproducible

Documento canónico vinculado:
  Teoría del TODO y de la NADA en el Sistema Vectorial SV
  https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-todo-nada-sv

Contiene únicamente definiciones canónicas transcritas literalmente del
documento: el alfabeto Σ = { 0, 1, U }, el operador de normalización ζ_SV,
el verificador ternario fuerte 𝓝★_SV, el código de aptitud E7, y la
estructura tipada SV_TODO_NADA_RESULT (apartado 24.2). No introduce
contenido doctrinal nuevo.

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
from dataclasses import dataclass, field, asdict
from typing import Any, Iterable, Sequence
import json
import math


# =============================================================================
# Alfabeto canónico Σ = { 0, 1, U }
# =============================================================================

# Por el §2.1 del documento canónico: alfabeto ternario Σ con tres símbolos.
# El símbolo U se representa por la cadena 'U' para distinguirlo claramente
# de cualquier valor numérico.
SIGMA = (0, 1, 'U')


def is_sigma(x: Any) -> bool:
    """Verifica si x ∈ Σ = { 0, 1, U }."""
    return x == 0 or x == 1 or x == 'U'


def alphabet_check(seq: Iterable[Any]) -> bool:
    """Verifica que toda componente de seq pertenece a Σ."""
    return all(is_sigma(x) for x in seq)


# =============================================================================
# Operador ζ_SV de normalización de defectos (apartado 13.1)
# =============================================================================

def zeta_SV(x: Any) -> Any:
    """
    Operador canónico de normalización de defectos ζ_SV.

    Por el §13.1 del documento canónico, ζ_SV : [0, ∞] ∪ { U } → { 0, 1, U }
    actúa por casos:
        ζ_SV(0)  = 0
        ζ_SV(x)  = 1   para x ∈ (0, ∞]
        ζ_SV(U)  = U
    """
    if x == 'U':
        return 'U'
    if isinstance(x, (int, float)):
        if x == 0:
            return 0
        if x > 0 or math.isinf(x):
            return 1
        raise ValueError(
            f"ζ_SV no admite valores negativos por la disciplina canónica del "
            f"§13.1 del documento canónico (recibido: {x})."
        )
    raise TypeError(
        f"ζ_SV admite x ∈ [0, ∞] ∪ {{ U }}; recibido tipo {type(x).__name__}."
    )


# =============================================================================
# Verificador ternario fuerte 𝓝★_SV (apartado 13.3)
# =============================================================================

def N_star_SV(*args: Any) -> Any:
    """
    Verificador ternario fuerte 𝓝★_SV del Sistema Vectorial SV.

    Por el §13.3 del documento canónico:
        𝓝★_SV(x_1, ..., x_m) =
            0,  si  x_j = 0 ∀j;
            1,  si  ∃ j : x_j = 1;
            U,  si  ¬∃ j : x_j = 1  ∧  ∃ j : x_j = U.

    La regla implementa la prelación canónica 1 ≻ U ≻ 0 (apartado 13.4):
    cualquier 1 fuerza el veredicto a 1; en ausencia de 1, cualquier U
    fuerza el veredicto a U; sólo ausencia total de 1 y de U produce 0.
    """
    if not args:
        raise ValueError("𝓝★_SV requiere al menos un argumento.")
    if not alphabet_check(args):
        raise ValueError(
            f"Argumentos del verificador no pertenecen al alfabeto canónico "
            f"Σ = {{ 0, 1, U }}: {args}"
        )
    if any(x == 1 for x in args):
        return 1
    if any(x == 'U' for x in args):
        return 'U'
    return 0


# =============================================================================
# Código E7 de aptitud canónica (apartado 24.2)
# =============================================================================

def passes_E7(components: Sequence[Any]) -> bool:
    """
    Código E7 — Verificación canónica de nulidad estricta sobre componentes.

    Por el §24.2 del documento canónico:
    Un laboratorio es APTO si y sólo si:
        (i)  verdict = 0 sobre la entrada del apartado correspondiente;
        (ii) passes_E7 = True, donde E7 verifica nulidad estricta sobre
             todos los componentes declarados en la sección de origen.

    E7 retorna True si y sólo si toda componente vale 0 exactamente.
    Cualquier 1 o U en componentes invalida E7.
    """
    if not components:
        return False
    if not alphabet_check(components):
        return False
    return all(x == 0 for x in components)


# =============================================================================
# Estructura tipada SV_TODO_NADA_RESULT (apartado 24.2)
# =============================================================================

@dataclass
class SV_TODO_NADA_RESULT:
    """
    Estructura canónica de salida de cada laboratorio (apartado 24.2).

    Campos:
        lab_id:     identificador del laboratorio (e.g. "lab01").
        section:    sección doctrinal de origen (e.g. "§2.1").
        verdict:    veredicto del verificador 𝓝★_SV en { 0, 1, U }.
        components: lista de componentes evaluados, cada uno ∈ { 0, 1, U }.
        trace:      lista de pasos canónicos del cómputo (auditoría).
        passes_E7:  resultado del código E7 sobre components.
    """
    lab_id: str
    section: str
    verdict: Any
    components: list[Any] = field(default_factory=list)
    trace: list[str] = field(default_factory=list)
    passes_E7: bool = False

    def is_apt(self) -> bool:
        """Aptitud canónica del laboratorio (apartado 24.2)."""
        return self.verdict == 0 and self.passes_E7 is True

    def to_dict(self) -> dict:
        return asdict(self)

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)

    def render(self) -> str:
        """Render humano-legible de la salida canónica."""
        lines = []
        lines.append(f"  lab_id     : {self.lab_id}")
        lines.append(f"  section    : {self.section}")
        lines.append(f"  verdict    : {self.verdict}")
        lines.append(f"  components : {self.components}")
        lines.append(f"  passes_E7  : {self.passes_E7}")
        lines.append(f"  APTO       : {self.is_apt()}")
        if self.trace:
            lines.append("  trace:")
            for step in self.trace:
                lines.append(f"    · {step}")
        return "\n".join(lines)


# =============================================================================
# Cabecera canónica para impresión por consola
# =============================================================================

def header(lab_id: str, lab_title: str, section: str) -> str:
    """Cabecera canónica de impresión de cada laboratorio."""
    border = "=" * 76
    return (
        f"{border}\n"
        f"  {lab_id.upper()} — {lab_title}\n"
        f"  Sección doctrinal: {section}\n"
        f"  Documento canónico: Teoría del TODO y de la NADA en el Sistema\n"
        f"  Vectorial SV (Lloret Egea, 2026).\n"
        f"{border}"
    )
