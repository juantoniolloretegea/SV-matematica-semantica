# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026
"""
Núcleo algebraico-operativo para los laboratorios del Hito 3.

Todas las funciones de este archivo están escritas con un criterio conservador:
- distinguen entre lo confirmado, lo refutado y lo abierto;
- no elevan a teorema lo que el documento canónico no clausura;
- no usan dependencias externas fuera de la biblioteca estándar.

Convención:
- Una TPA queda dada por la secuencia de observables phi = (φ_0,...,φ_n).
- Las pendientes M se reconstruyen por diferencias sucesivas.
- La carta R^2 es auxiliar; aquí sólo se computa el observable director.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Callable, Dict, Iterable, List, Sequence, Tuple
import cmath
import json
import math


def sign(x: int) -> str:
    if x > 0:
        return "+"
    if x < 0:
        return "-"
    return "0"


def slopes(phi: Sequence[int]) -> List[int]:
    if len(phi) < 2:
        raise ValueError("Una TPA requiere al menos dos frames.")
    return [int(phi[i + 1] - phi[i]) for i in range(len(phi) - 1)]


def curvature(phi: Sequence[int]) -> List[int]:
    m = slopes(phi)
    if len(m) < 2:
        return []
    return [m[i] - m[i - 1] for i in range(1, len(m))]


def trapezoid_area(phi: Sequence[int], weights: Sequence[float] | None = None) -> float:
    n = len(phi) - 1
    if n < 1:
        raise ValueError("Una TPA necesita al menos un intervalo.")
    if weights is None:
        weights = [1.0] * n
    if len(weights) != n:
        raise ValueError("La longitud de weights debe coincidir con el número de intervalos.")
    total = 0.0
    for i in range(n):
        total += (phi[i] + phi[i + 1]) * 0.5 * weights[i]
    return total


def left_area(phi: Sequence[int], weights: Sequence[float] | None = None) -> float:
    n = len(phi) - 1
    if weights is None:
        weights = [1.0] * n
    if len(weights) != n:
        raise ValueError("La longitud de weights debe coincidir con el número de intervalos.")
    return float(sum(phi[i] * weights[i] for i in range(n)))


def weighted_path(phi: Sequence[int], weights: Sequence[float] | None = None) -> List[float]:
    n = len(phi) - 1
    if weights is None:
        weights = [1.0] * n
    if len(weights) != n:
        raise ValueError("La longitud de weights debe coincidir con el número de intervalos.")
    return [phi[i] * weights[i] for i in range(n)]


def divergence(phi: Sequence[int]) -> List[int]:
    m = slopes(phi)
    return [-x for x in m]


def balance(phi: Sequence[int]) -> int:
    d = divergence(phi)
    return sum(d)


def telescopy(phi: Sequence[int]) -> int:
    m = slopes(phi)
    return sum(m)


def l1_norm(values: Sequence[int | float]) -> float:
    return float(sum(abs(v) for v in values))


def generating_function_coefficients(phi: Sequence[int]) -> List[int]:
    return list(phi)


def generating_function_value(phi: Sequence[int], lam: complex) -> complex:
    total = 0j
    for k, val in enumerate(phi):
        total += val * (lam ** k)
    return total


def complex_integral_sv(phi: Sequence[int], weights: Sequence[float] | None = None) -> complex:
    """
    Integral compleja factual en la forma usada por el documento:
    ∫ φ dz = Σ φ_k (Δε_k + i_SV * m_k).
    Para Δε_k = 1:
    Re = área izquierda,
    Im = Σ φ_k * m_k.
    """
    m = slopes(phi)
    n = len(m)
    if weights is None:
        weights = [1.0] * n
    if len(weights) != n:
        raise ValueError("La longitud de weights debe coincidir con el número de intervalos.")
    real = sum(phi[i] * weights[i] for i in range(n))
    imag = sum(phi[i] * m[i] for i in range(n))
    return complex(real, imag)


def affine_reference_area(phi0: int, phin: int, n_intervals: int) -> float:
    return ((phi0 + phin) / 2.0) * n_intervals


def affine_deviation(phi: Sequence[int]) -> float:
    n = len(phi) - 1
    return trapezoid_area(phi) - affine_reference_area(phi[0], phi[-1], n)


def mean_trapezoidal(phi: Sequence[int]) -> float:
    return trapezoid_area(phi) / (len(phi) - 1)


def find_crossings_piecewise_linear(phi: Sequence[int], target: float) -> List[float]:
    """
    Devuelve los epsilon* donde la TPA lineal a trozos alcanza `target`.
    Se toma ε_k = k.
    """
    xs: List[float] = []
    for i in range(len(phi) - 1):
        y0, y1 = phi[i], phi[i + 1]
        low, high = min(y0, y1), max(y0, y1)
        if low <= target <= high:
            if y0 == y1 == target:
                xs.extend([float(i), float(i + 1)])
            elif y0 != y1:
                t = (target - y0) / (y1 - y0)
                xs.append(i + t)
    # quitar casi-duplicados
    out: List[float] = []
    for x in xs:
        if not any(abs(x - y) < 1e-9 for y in out):
            out.append(x)
    return out


def local_extrema(phi: Sequence[int]) -> Dict[str, List[int]]:
    m = slopes(phi)
    maxima, minima = [], []
    for k in range(1, len(phi) - 1):
        left, right = m[k - 1], m[k]
        if left >= 0 and right <= 0 and (left > 0 or right < 0):
            maxima.append(k)
        if left <= 0 and right >= 0 and (left < 0 or right > 0):
            minima.append(k)
    return {"maxima": maxima, "minima": minima}


def holonomy(phi: Sequence[int]) -> int:
    m = slopes(phi)
    if not m:
        return 0
    return m[-1] - m[0]


def classify_sign_sequence(phi: Sequence[int]) -> Tuple[str, str]:
    """
    Devuelve (codigo, etiqueta) según la tipología Σ1..Σ12.
    Es una clasificación operativa y conservadora para laboratorios.
    """
    m = slopes(phi)
    signs = [sign(x) for x in m]
    has_pos = "+" in signs
    has_neg = "-" in signs
    has_zero = "0" in signs
    changes = sum(1 for i in range(1, len(signs)) if signs[i] != signs[i-1])

    if all(s == "-" for s in signs):
        return "Σ1", "TPA-CP"
    if all(s == "+" for s in signs):
        return "Σ2", "TPA-EP"
    if all(s == "0" for s in signs):
        return "Σ5", "TPA-MI"
    if not has_pos and has_neg and has_zero:
        if signs[0] == "0" and any(s == "-" for s in signs[1:]):
            return "Σ6", "TPA-CMI"
        if changes >= 2:
            return "Σ7", "TPA-CMInt"
    if has_pos and not has_neg and has_zero:
        if signs[-1] == "0":
            return "Σ8", "TPA-ES"
    if has_pos and has_neg:
        if changes >= 3:
            return "Σ9", "TPA-MC"
        # bimodales
        first_nonzero = next((s for s in signs if s != "0"), "0")
        last_nonzero = next((s for s in reversed(signs) if s != "0"), "0")
        if first_nonzero == "+" and last_nonzero == "-":
            # asimetría si subida y bajada difieren en módulo medio
            pos = [abs(v) for v in m if v > 0]
            neg = [abs(v) for v in m if v < 0]
            if pos and neg and abs(sum(pos) / len(pos) - sum(neg) / len(neg)) > 1e-9:
                return "Σ12", "TPA-AB"
            return "Σ3", "TPA-BAC"
        if first_nonzero == "-" and last_nonzero == "+":
            return "Σ4", "TPA-BCA"
    # escalonadas y umbral tardío
    if signs.count("0") >= len(signs) // 2 and "-" in signs and "+" not in signs:
        if signs[-1] == "-":
            return "Σ10", "TPA-UT"
        return "Σ11", "TPA-ED"
    return "Σ?", "NO_CLAUSURADA"


def check_no_collinearity(phi: Sequence[int]) -> bool:
    m = slopes(phi)
    return all(m[i] != m[i + 1] for i in range(len(m) - 1))


def in_domain(phi: Sequence[int], low: int = 0, high: int = 9) -> bool:
    return all(low <= x <= high for x in phi)


def is_cycle(phi: Sequence[int]) -> bool:
    return phi[0] == phi[-1]


def cs_conditioned_lower_bound(phi: Sequence[int]) -> Tuple[bool, float, float]:
    """
    Devuelve (aplica_hipotesis, area, n*phi0).
    """
    applies = all(v >= phi[0] for v in phi)
    return applies, trapezoid_area(phi), (len(phi) - 1) * phi[0]


def area_partition(phi: Sequence[int], cuts: Sequence[int]) -> List[float]:
    out = []
    for a, b in zip(cuts[:-1], cuts[1:]):
        out.append(trapezoid_area(phi[a:b+1]))
    return out


def descriptor_quadruple(phi: Sequence[int]) -> Tuple[float, int, int, float]:
    m = slopes(phi)
    return (trapezoid_area(phi), sum(m), max(phi), l1_norm(m))


def cycle_descriptor_first_order(phi: Sequence[int]) -> Tuple[float, int, float]:
    if not is_cycle(phi):
        raise ValueError("La trayectoria no es cíclica.")
    m = slopes(phi)
    return (trapezoid_area(phi), max(phi), l1_norm(m))


def eq_cost_first_order(phi_a: Sequence[int], phi_b: Sequence[int]) -> bool:
    return cycle_descriptor_first_order(phi_a) == cycle_descriptor_first_order(phi_b)


def tpa_example_director() -> Sequence[int]:
    return [1, 3, 6, 8, 9, 9, 8, 6, 3, 2, 2]


def tpa_cycle_counterexample_same_area() -> Tuple[Sequence[int], Sequence[int]]:
    return [3, 5, 7, 5, 3], [3, 6, 5, 6, 3]


def tpa_isoperimetric_counterexample() -> Sequence[int]:
    return [4, 3, 1, 1, 0]


def tpa_cyclic_false_identity_counterexample() -> Sequence[int]:
    return [3, 5, 9, 9, 7, 3]


def tpa_descriptor_collision_pair() -> Tuple[Sequence[int], Sequence[int]]:
    a = [1, 3, 6, 8, 9, 9, 8, 6, 3, 2, 2]
    b = [1, 3, 6, 8, 9, 9, 8, 5, 3, 3, 2]
    return a, b


def mfc_reference_cycle(phi0: int = 3, n: int = 9) -> List[int]:
    return [phi0] * (n + 1)


def mfc_lower_than_plateau_counterexample(phi0: int = 3, n: int = 9) -> List[int]:
    """
    Contraejemplo a una lectura demasiado fuerte del "mínimo universal":
    misma frontera cíclica, coste por debajo de la meseta, con no-colinealidad.
    """
    phi = [3, 2, 0, 1, 0, 1, 0, 1, 0, 3]
    if len(phi) != n + 1:
        raise ValueError("La longitud del contraejemplo está fijada para n=9.")
    return phi


def kepler_sector_areas_from_areal_velocity(mu_area: float, delta_tau: float, n: int) -> List[float]:
    return [mu_area * delta_tau for _ in range(n)]


def noncentral_sector_areas_example(n: int) -> List[float]:
    return [1.0 + (0.25 if i % 2 else 0.0) for i in range(n)]


@dataclass
class LabResult:
    lab_id: str
    title: str
    status: str  # CONFIRMA / REFUTA / ABIERTO
    passed: bool
    summary: str
    details: Dict[str, object]

    def to_dict(self) -> Dict[str, object]:
        return {
            "lab_id": self.lab_id,
            "title": self.title,
            "status": self.status,
            "passed": self.passed,
            "summary": self.summary,
            "details": self.details,
        }


def to_pretty_json(data: object) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


def assert_close(a: float, b: float, tol: float = 1e-9) -> None:
    if abs(a - b) > tol:
        raise AssertionError(f"No son próximos: {a!r} vs {b!r}")


def assert_equal(a: object, b: object) -> None:
    if a != b:
        raise AssertionError(f"No coinciden: {a!r} vs {b!r}")
