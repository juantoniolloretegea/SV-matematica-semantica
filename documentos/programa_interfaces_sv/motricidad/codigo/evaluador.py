from __future__ import annotations

import json
from pathlib import Path


def coherente(grafo: dict) -> bool:
    return all(valor in (0, 1, "U") for valor in grafo["nodes"].values())


def admisible(grafo: dict) -> bool:
    return all(valor is not None for valor in grafo["nodes"].values())


def alcanzable(grafo: dict, inicio: str, destino: str) -> bool:
    if inicio == destino:
        return False
    visitados = {inicio}
    pila = [inicio]
    while pila:
        nodo = pila.pop()
        for a, b in grafo["edges"]:
            if a == nodo:
                if b == destino:
                    return True
                if b not in visitados:
                    visitados.add(b)
                    pila.append(b)
    return False


def trazable(grafo: dict) -> bool:
    v = grafo["v"]
    return any(
        nodo != v and alcanzable(grafo, nodo, v)
        for nodo in grafo["nodes"].keys()
    )


def clausura(grafo: dict) -> bool:
    v = grafo["v"]
    nodos = set(grafo["nodes"].keys())
    ancestros = {v}
    pila = [v]
    while pila:
        nodo = pila.pop()
        for a, b in grafo["edges"]:
            if b == nodo and a not in ancestros:
                ancestros.add(a)
                pila.append(a)
    return all(n in nodos for n in ancestros)


def u_critica_alcanza_exposicion(grafo: dict) -> bool:
    v = grafo["v"]
    nodos_u = [n for n, valor in grafo["nodes"].items() if valor == "U"]
    visitados = set(nodos_u)
    pila = list(nodos_u)
    while pila:
        nodo = pila.pop()
        for a, b in grafo["edges"]:
            if a == nodo and b not in visitados:
                visitados.add(b)
                pila.append(b)
    return v in visitados


def relevancia_estructural(grafo: dict) -> bool:
    v = grafo["v"]
    return any(b == v for a, b in grafo["edges"])


def evaluar(grafo: dict) -> str:
    if not coherente(grafo):
        return "no_habilitable"
    if not admisible(grafo):
        return "no_habilitable"
    if not clausura(grafo):
        return "no_habilitable"
    if not trazable(grafo):
        return "no_habilitable"
    if u_critica_alcanza_exposicion(grafo):
        return "no_habilitable"
    if not relevancia_estructural(grafo):
        return "no_habilitable"
    return "habilitable"


def main() -> None:
    ruta_datos = Path(__file__).resolve().parent / "datos.json"
    datos = json.loads(ruta_datos.read_text(encoding="utf-8"))
    for grafo in datos:
        print(grafo["id"], evaluar(grafo))


if __name__ == "__main__":
    main()
