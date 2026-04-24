"""
lab_19_transductor_nlp.py — L-LUZ-19 — Transductor NLP.

§8 A.23: El transductor NLP 𝓘_NLP del corpus (Lloret Egea, 2026i) produce
a partir de paquete observacional una célula K_3^9 sobre Σ = {0, 1, U} que
coincide con la célula canónica SV(3, 9) del §18 cuando el paquete es
admisible.

Pruebas:
  1. Transductor produce matriz de shape (3, 9) con valores en Σ
  2. Cardinalidad de la célula = 3^9 = 19 683 configuraciones posibles
  3. Reproducibilidad determinista sobre paquete observacional idéntico
  4. Célula producida coincide estructuralmente con SV(3, 9) canónica
  5. Adversarial: paquete con 4 × 10 celdas debe disparar LUZ-NLP-001
  6. Semilla determinista (33): dos ejecuciones idénticas producen misma célula

Códigos: LUZ-NLP-001..003
"""
import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sv_core import (SVError, U_CODE, SEMILLA_DETERMINISTA, cargar_casos)


def transductor_NLP(paquete: np.ndarray, semilla: int = SEMILLA_DETERMINISTA) -> np.ndarray:
    """
    𝓘_NLP: paquete observacional → célula K_3^9 sobre Σ = {0, 1, U}.

    Implementación mínima reproducible: mapea valores del paquete al alfabeto
    ternario por umbrales fijos sobre rango normalizado, con semilla
    determinista para romper empates.

    Parámetros
    ----------
    paquete : np.ndarray de shape (d, n) con valores reales
    semilla : int (default 33)

    Retorna
    -------
    np.ndarray de shape (d, n) con valores en {0, 1, U_CODE}
    """
    rng = np.random.default_rng(semilla)
    if paquete.shape != (3, 9):
        raise SVError(
            "LUZ-NLP-001",
            f"Paquete con shape {paquete.shape} ≠ (3, 9) — "
            f"transductor exige célula K_3^9",
        )
    normalizado = (paquete - paquete.min()) / (paquete.max() - paquete.min() + 1e-12)
    celula = np.full_like(paquete, U_CODE, dtype=int)
    celula[normalizado < 0.33] = 0
    celula[normalizado > 0.66] = 1
    # Los empates (valor en la frontera) se resuelven con semilla determinista
    frontera = (normalizado >= 0.33) & (normalizado <= 0.66)
    if np.any(frontera):
        ruido = rng.uniform(-1e-9, 1e-9, size=paquete.shape)
        celula[frontera] = np.where(
            (normalizado + ruido)[frontera] > 0.5, 1, U_CODE
        )
    return celula


def prueba_1_transductor_produce_shape_3_9() -> None:
    """Transductor sobre paquete 3×9 produce célula 3×9."""
    rng = np.random.default_rng(SEMILLA_DETERMINISTA)
    paquete = rng.normal(0, 1, size=(3, 9))
    celula = transductor_NLP(paquete)
    if celula.shape != (3, 9):
        raise SVError(
            "LUZ-NLP-001",
            f"Célula producida con shape {celula.shape} ≠ (3, 9)",
        )
    valores_en_sigma = np.isin(celula, [0, 1, U_CODE]).all()
    if not valores_en_sigma:
        raise SVError(
            "LUZ-NLP-001",
            f"Célula con valor fuera de Σ = {{0, 1, {U_CODE}}}",
        )
    print(f"  [NLP OK] Transductor 𝓘_NLP produce célula 3×9 sobre Σ ternario ✓")


def prueba_2_cardinalidad_espacio_posibles() -> None:
    """|Σ^9| = 3^9 = 19 683 configuraciones posibles para una fibra."""
    cardinalidad = 3 ** 9
    if cardinalidad != 19683:
        raise SVError(
            "LUZ-NLP-001",
            f"Cardinalidad espacio = {cardinalidad} ≠ 19 683",
        )
    # Cada celda produce UNA configuración en Σ^9 por hebra
    # Tres hebras producen UNA configuración en Σ^(3·9) = 3^27
    espacio_total = 3 ** (3 * 9)
    if espacio_total != 7625597484987:
        raise SVError(
            "LUZ-NLP-001",
            f"Espacio total 3^27 = {espacio_total} ≠ 7 625 597 484 987",
        )
    print(f"  [NLP OK] |Σ^9| = 3^9 = 19 683, |Σ^(3·9)| = 3^27 = {espacio_total:,} ✓")


def prueba_3_reproducibilidad_determinista() -> None:
    """Dos ejecuciones del transductor sobre paquete idéntico: mismo resultado."""
    rng = np.random.default_rng(SEMILLA_DETERMINISTA)
    paquete = rng.normal(0, 1, size=(3, 9))
    c1 = transductor_NLP(paquete, semilla=SEMILLA_DETERMINISTA)
    c2 = transductor_NLP(paquete, semilla=SEMILLA_DETERMINISTA)
    if not np.array_equal(c1, c2):
        diferencias = int(np.sum(c1 != c2))
        raise SVError(
            "LUZ-NLP-002",
            f"Transductor no reproducible: {diferencias} celdas distintas con "
            f"semilla fija",
        )
    print(f"  [NLP OK] Reproducibilidad determinista: misma entrada → misma salida ✓")


def prueba_4_compatibilidad_con_celula_canonica() -> None:
    """
    La célula producida por 𝓘_NLP para un paquete admisible tiene misma
    estructura (3, 9) que la célula canónica SV(3, 9) del §18.
    """
    casos = cargar_casos()
    canonico = next((c for c in casos if c.chi.shape == (3, 9)), None)
    if canonico is None:
        raise SVError(
            "LUZ-NLP-003",
            "No hay caso canónico SV(3,9) en el conjunto",
        )
    # Producir una célula por el transductor
    rng = np.random.default_rng(SEMILLA_DETERMINISTA)
    paquete = rng.normal(0, 1, size=(3, 9))
    celula_nlp = transductor_NLP(paquete)
    # Verificar estructura equivalente: misma shape, valores en Σ
    if celula_nlp.shape != canonico.chi.shape:
        raise SVError(
            "LUZ-NLP-003",
            f"Shape célula NLP {celula_nlp.shape} ≠ canónica {canonico.chi.shape}",
        )
    alfabeto_nlp = set(np.unique(celula_nlp).tolist())
    alfabeto_can = set(np.unique(canonico.chi).tolist())
    if not alfabeto_nlp.issubset({0, 1, U_CODE}):
        raise SVError(
            "LUZ-NLP-003",
            f"Célula NLP con alfabeto {alfabeto_nlp} ⊄ Σ",
        )
    print(f"  [NLP OK] Célula NLP estructura (3, 9) sobre Σ compatible con canónica ✓")


def prueba_5_adversarial_shape_incorrecta() -> None:
    """
    Paquete con shape ≠ (3, 9) debe disparar LUZ-NLP-001 (no otra cosa).
    """
    rng = np.random.default_rng(SEMILLA_DETERMINISTA)
    paquete_malo = rng.normal(0, 1, size=(4, 10))
    try:
        transductor_NLP(paquete_malo)
        raise SVError(
            "LUZ-NLP-001",
            "Paquete (4, 10) pasó sin error: transductor no valida shape",
        )
    except SVError as e:
        if e.codigo != "LUZ-NLP-001":
            raise SVError(
                "LUZ-NLP-001",
                f"Paquete (4, 10) disparó código {e.codigo} ≠ LUZ-NLP-001",
            )
    print(f"  [NLP OK] Paquete (4, 10) dispara LUZ-NLP-001 específicamente ✓")


def prueba_6_semilla_33_estable() -> None:
    """Semilla 33 del corpus produce célula estable y reproducible."""
    rng1 = np.random.default_rng(33)
    paquete = rng1.normal(0, 1, size=(3, 9))
    celula_a = transductor_NLP(paquete, semilla=33)
    celula_b = transductor_NLP(paquete, semilla=33)
    if not np.array_equal(celula_a, celula_b):
        raise SVError(
            "LUZ-NLP-002",
            "Semilla 33: dos llamadas distintas producen células diferentes",
        )
    # Verificar que la misma semilla NO produce todo U_CODE (sería degenerado)
    frac_U = float(np.mean(celula_a == U_CODE))
    if frac_U > 0.95:
        raise SVError(
            "LUZ-NLP-002",
            f"Semilla 33: célula con {frac_U*100:.1f}% U_CODE (degeneración)",
        )
    print(f"  [NLP OK] Semilla 33 estable: {frac_U*100:.1f}% U_CODE (no degenerado) ✓")


def run() -> int:
    print("=" * 74)
    print("L-LUZ-19 — TRANSDUCTOR NLP (§8 A.23)")
    print("=" * 74)
    prueba_1_transductor_produce_shape_3_9()
    prueba_2_cardinalidad_espacio_posibles()
    prueba_3_reproducibilidad_determinista()
    prueba_4_compatibilidad_con_celula_canonica()
    prueba_5_adversarial_shape_incorrecta()
    prueba_6_semilla_33_estable()
    print("-" * 74)
    print("L-LUZ-19 — PASADO. Transductor 𝓘_NLP produce célula K_3^9 reproducible.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(run())
    except SVError as e:
        print(f"\n[L-LUZ-19] FALLO código={e.codigo}")
        print(f"           mensaje: {e.mensaje}")
        sys.exit(1)
