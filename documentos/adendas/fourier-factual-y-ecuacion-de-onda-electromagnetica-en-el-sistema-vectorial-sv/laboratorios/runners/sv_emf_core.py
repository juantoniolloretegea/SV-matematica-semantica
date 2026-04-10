from __future__ import annotations
import math, json, hashlib, datetime
from pathlib import Path

N = 9
THETAS = [2.0 * math.pi * i / N for i in range(N)]
CASE_ID = "ED-EM-01"
AMPLITUDE_E = 1.0
PULSE_POSITION_1_INDEXED = 2
PULSE_INDEX = PULSE_POSITION_1_INDEXED - 1
EDGE_SET_1_INDEXED = [1, 2, 3]
EDGE_SET = [i - 1 for i in EDGE_SET_1_INDEXED]
DELTA_ELL = 1.0
DELTA_XI = 0.5
C_SV = 1.0
OMEGA2 = [4.0 * (C_SV ** 2) / (DELTA_ELL ** 2) * math.sin(math.pi * m / N) ** 2 for m in range(1, 5)]
LAMBDAS = [2.0 * math.cos(2.0 * math.pi * m / N) - 2.0 for m in range(1, 5)]

# Courant maximo para los parametros canonicos del documento.
# Condicion de estabilidad del leapfrog: delta_xi * Omega_m <= 2 para todo m.
COURANT_MAX = DELTA_XI * max(math.sqrt(o) for o in OMEGA2)   # 0.9848... < 2.0


def timestamp_utc() -> str:
    return datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def md5_text(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def round_list(values, digits=12):
    """Redondea lista a `digits` decimales. Normaliza -0.0 a 0.0."""
    result = []
    for v in values:
        r = round(v, digits)
        if r == 0.0:
            r = 0.0   # eliminar cero negativo (-0.0 == 0.0 pero repr distinto)
        result.append(r)
    return result


def round_float(value, digits=12):
    r = round(value, digits)
    if r == 0.0:
        r = 0.0
    return r


def observable_ed_em_01(amplitude: float = AMPLITUDE_E, pulse_index: int = PULSE_INDEX):
    x = [0.0] * N
    x[pulse_index] = float(amplitude)
    return x


def modal_transform(x):
    mean = sum(x) / N
    alpha, beta, mod = [], [], []
    for m in range(1, 5):
        a = (2.0 / N) * sum(x[i] * math.cos(m * THETAS[i]) for i in range(N))
        b = (2.0 / N) * sum(x[i] * math.sin(m * THETAS[i]) for i in range(N))
        alpha.append(a)
        beta.append(b)
        mod.append(math.sqrt(a * a + b * b))
    return mean, alpha, beta, mod


def reconstruct(mean, alpha, beta, k=4):
    x = []
    for i in range(N):
        val = mean
        for m in range(1, k + 1):
            val += alpha[m - 1] * math.cos(m * THETAS[i]) + beta[m - 1] * math.sin(m * THETAS[i])
        x.append(val)
    return x


def content_quadratic(x):
    return sum(v * v for v in x)


def parseval_rhs(mean, mod):
    return N * mean * mean + (N / 2.0) * sum(m * m for m in mod)


def residuals(x, mean, alpha, beta, k):
    xr = reconstruct(mean, alpha, beta, k=k)
    delta = [x[i] - xr[i] for i in range(N)]
    edge_max = max(abs(delta[i]) for i in EDGE_SET)
    edge_quadratic = sum(delta[i] * delta[i] for i in EDGE_SET)
    total_quadratic = sum(d * d for d in delta)
    concentration = edge_quadratic / total_quadratic if total_quadratic else 0.0
    local_min = min(x[i] for i in EDGE_SET)
    local_max = max(x[i] for i in EDGE_SET)
    overshoot = max(max(xr[i] - local_max, 0.0) for i in EDGE_SET)
    undershoot = max(max(local_min - xr[i], 0.0) for i in EDGE_SET)
    return {
        "reconstruccion_truncada": xr,
        "residuo_puntual": delta,
        "borde_maximo": edge_max,
        "borde_cuadratico": edge_quadratic,
        "residuo_total_cuadratico": total_quadratic,
        "concentracion_borde": concentration,
        "sobreoscilacion": overshoot,
        "suboscilacion": undershoot,
    }


def propagate_modal(initial_x, steps=6, delta_xi=DELTA_XI):
    """
    Propaga la configuracion factual inicial mediante el esquema leapfrog discreto.

    Condicion inicial canonica (declarada):
      a_m(xi=0) = coeficiente modal inicial
      velocidad factual inicial: da_m/dxi|_{xi=0} = 0

    La velocidad nula se impone via arranque frio: a_m(-delta_xi) := a_m(0),
    lo que en el primer paso da:
      a_m(delta_xi) = a_m(0) * (1 - delta_xi^2 * Omega_m^2)

    Estabilidad: delta_xi * Omega_m <= 2 para todo m.
    Courant_max canonico = {:.6f} < 2.0 => ESTABLE.
    """
    mean, alpha0, beta0, mod0 = modal_transform(initial_x)
    alpha_hist = [[a] for a in alpha0]
    beta_hist = [[b] for b in beta0]
    for idx, a0 in enumerate(alpha0):
        prev = a0   # arranque frio: a(-delta_xi) = a(0)
        cur = a0
        om2 = OMEGA2[idx]
        for _ in range(steps):
            nxt = 2.0 * cur - prev - (delta_xi ** 2) * om2 * cur
            alpha_hist[idx].append(nxt)
            prev, cur = cur, nxt
    for idx, b0 in enumerate(beta0):
        prev = b0
        cur = b0
        om2 = OMEGA2[idx]
        for _ in range(steps):
            nxt = 2.0 * cur - prev - (delta_xi ** 2) * om2 * cur
            beta_hist[idx].append(nxt)
            prev, cur = cur, nxt
    snapshots = []
    for s in range(steps + 1):
        alpha = [alpha_hist[idx][s] for idx in range(4)]
        beta = [beta_hist[idx][s] for idx in range(4)]
        x = reconstruct(mean, alpha, beta, 4)
        snapshots.append({
            "paso": s,
            "xi": s * delta_xi,
            "alpha": alpha,
            "beta": beta,
            "estado": x,
            "contenido_cuadratico": content_quadratic(x),
            "indice_maximo_1_indexed": x.index(max(x)) + 1,
            "valor_maximo": max(x),
        })
    return {
        "media": mean,
        "alpha_inicial": alpha0,
        "beta_inicial": beta0,
        "modulos_iniciales": mod0,
        "omega2": OMEGA2,
        "lambdas": LAMBDAS,
        "courant_max": COURANT_MAX,
        "delta_xi": delta_xi,
        "delta_ell": DELTA_ELL,
        "c_sv": C_SV,
        "snapshots": snapshots,
    }


def freeze_json(path: Path, payload: dict) -> str:
    """
    Serializa payload a JSON autosellado con campo 'md5'.

    La huella se calcula sobre el JSON SIN el campo 'md5' (payload limpio).
    Luego se inserta 'md5' y el fichero se escribe una sola vez con la huella
    ya presente. El fichero en disco es autoverificable:

      Protocolo de verificacion externa:
        1. Leer el fichero JSON.
        2. Eliminar el campo 'md5'.
        3. Serializar: json.dumps(d, ensure_ascii=False, indent=2)
        4. md5(texto.encode('utf-8')) debe coincidir con el valor del campo 'md5'.
    """
    payload_clean = {k: v for k, v in payload.items() if k != "md5"}
    text_clean = json.dumps(payload_clean, ensure_ascii=False, indent=2)
    digest = md5_text(text_clean)
    payload["md5"] = digest
    text_final = json.dumps(payload, ensure_ascii=False, indent=2)
    path.write_text(text_final, encoding="utf-8")
    return digest
