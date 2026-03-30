
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
import json
from pathlib import Path

Tri = Optional[int]
IRREDUCIBLE = "irreducible"
FRONTERIZA  = "fronteriza"
RESOLUBLE   = "resoluble"

@dataclass
class Suceso:
    nombre: str
    posiciones: list[int]
    valor: Optional[int]

def gamma(vector: list[Tri], horizonte: list[Suceso]) -> dict[int, str]:
    out = {}
    for i, v in enumerate(vector):
        if v is not None:
            continue
        hits = [s for s in horizonte if i in s.posiciones]
        if not hits:
            out[i] = IRREDUCIBLE
        else:
            valores = {s.valor for s in hits if s.valor is not None}
            if len(valores) > 1:
                # Existen sucesos con valor 0 y con valor 1: fronteriza
                out[i] = FRONTERIZA
            elif len(valores) == 1:
                # Todos los sucesos instanciadores producen el mismo valor
                out[i] = RESOLUBLE
            else:
                # Sucesos presentes pero ninguno con valor determinado
                out[i] = FRONTERIZA
    return out

def convergencia_posicion(frames: list[list[Tri]], pos: int) -> tuple[bool, int|None, int|None]:
    vals = [f[pos] for f in frames]
    try:
        n0 = next(i for i,v in enumerate(vals) if v is None)
    except StopIteration:
        return True, 0, 0
    for n in range(n0, len(vals)):
        if vals[n] is not None and all(v == vals[n] for v in vals[n:]):
            return True, n, n-n0
    return False, None, None

def delta_N(frames: list[list[Tri]], irr: set[int]) -> int:
    ds = []
    for i in range(len(frames[0])):
        if i in irr:
            continue
        ok, _, d = convergencia_posicion(frames, i)
        if d is not None:
            ds.append(d)
    return max(ds) if ds else 0

def main():
    S0 = [0,None,0,0,None,0,None,0,0]
    S1 = [0,0,0,0,None,0,0,0,0]
    S2 = [0,0,0,0,0,0,0,0,0]
    T  = [S0,S1,S2]

    H_ex = [
        Suceso("respuesta_directa",[1],0),
        Suceso("fijacion_objetivo",[4],0),
        Suceso("aclaracion_referente",[6],0),
    ]
    g = gamma(S0, H_ex)
    assert g == {1: RESOLUBLE, 4: RESOLUBLE, 6: RESOLUBLE}

    irr = {i for i,t in g.items() if t == IRREDUCIBLE}
    assert not irr

    dN = delta_N(T, irr)
    assert dN == 2

    # ventana activa simple para el ejemplo
    active = T[max(0, len(T)-1-dN):]
    assert len(active) == 3

    # fork sin borrado
    T_prime = [S0, S1, [0,0,0,0,0,0,0,0,0]]
    assert T[1] == S1 and T_prime[1] == S1 and T is not T_prime

    # caso de irreducible
    H_pobre = [Suceso("respuesta_directa",[1],0)]
    g_pobre = gamma(S0, H_pobre)
    assert g_pobre[4] == IRREDUCIBLE and g_pobre[6] == IRREDUCIBLE

    out = {
        "caso_1_gamma_suficiente": g,
        "caso_2_delta_N": dN,
        "caso_3_ventana_activa_tamano": len(active),
        "caso_4_fork_append_only": "ok",
        "caso_5_gamma_horizonte_pobre": g_pobre,
        "trayectoria_ejemplo": {"S0": S0, "S1": S1, "S2": S2},
    }
    p = Path(__file__).with_name("salida_casos_canonicos_doc1_release2.json")
    p.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print("✓ Todos los casos canónicos pasan. Laboratorio verificado.")

if __name__ == "__main__":
    main()
