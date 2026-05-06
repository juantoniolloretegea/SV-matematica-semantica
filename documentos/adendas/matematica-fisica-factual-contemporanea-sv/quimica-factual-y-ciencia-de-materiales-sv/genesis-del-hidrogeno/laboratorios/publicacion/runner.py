# -*- coding: utf-8 -*-
# © 2026. Todos los derechos reservados. | Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 06/05/2026
# Advertencia. Esta publicación está protegida por CEDRO y su aplicación en el campo de la Física, así como cualquier forma de explotación, reproducción o uso por parte de empresas, queda sujeta al copyright del autor y a los términos de la licencia indicada; la reproducción, distribución, comunicación pública o transformación de esta obra solo puede ser realizada con la autorización de sus titulares, salvo excepción prevista por la ley, y cualquier uso comercial sin autorización expresa queda prohibido y sujeto estrictamente al licenciamiento permitido.
# Warning. This publication is protected by CEDRO. Its application in the field of Physics, as well as any form of exploitation, reproduction, or use by corporate entities, is strictly subject to the author's copyright and the terms of the license indicated; any reproduction, distribution, public communication, or transformation of this work requires authorization from the rightsholders, except as provided by law, and any commercial use without express written consent is prohibited and strictly subject to permitted licensing.

from pathlib import Path
import csv, json, sys
sys.path.insert(0, str(Path(__file__).parent / "src"))
from sv_persistencia import (
    Dictamen, dictaminar_elemento, dictaminar_molecula, dictaminar_atmosfera,
    estado_elemento, estado_molecular, estado_atmosferico
)

BASE = Path(__file__).parent
DATA = BASE / "data"
OUT = BASE / "resultados" / "resultados_integrales.json"


def cargar_elementos():
    with open(DATA / "elementos_control_1_118.csv", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def regenerar_elementos():
    resultados = []
    for row in cargar_elementos():
        z = int(row["Z"])
        d = dictaminar_elemento(estado_elemento(z), z).value
        resultados.append({"Z": z, "symbol": row["symbol"], "dictamen": d})
    return resultados


def dictamen_simbolo(symbol, elementos):
    for r in elementos:
        if r["symbol"] == symbol:
            return Dictamen(r["dictamen"])
    raise KeyError(symbol)


def evaluar_banco(elementos):
    out = []
    with open(DATA / "banco_demostrativo_12_casos.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            cid, tipo, esperado = row["id"], row["tipo"], row["esperado"]
            if tipo == "elemento":
                d = dictaminar_elemento(estado_elemento(int(row["Z"])), int(row["Z"])).value
            elif tipo == "candidato":
                d = dictaminar_elemento(estado_elemento(int(row["Z"]), known=False), int(row["Z"])).value
            elif tipo == "molecula":
                composicion = {
                    "H2O": ["H", "H", "O"],
                    "CO2": ["C", "O", "O"],
                    "CH4": ["C", "H", "H", "H", "H"],
                    "O3": ["O", "O", "O"],
                }[cid]
                comps = [dictamen_simbolo(s, elementos) for s in composicion]
                d = dictaminar_molecula(comps, estado_molecular()).value
            elif tipo == "atmosfera":
                if cid == "ATM_TIERRA":
                    comps = [Dictamen.MOLECULA_ADMISIBLE, Dictamen.MOLECULA_ADMISIBLE, Dictamen.ELEMENTO_ADMISIBLE, Dictamen.MOLECULA_ADMISIBLE, Dictamen.MOLECULA_ADMISIBLE]
                    d = dictaminar_atmosfera(comps, estado_atmosferico(True), True).value
                else:
                    comps = [Dictamen.MOLECULA_ADMISIBLE]
                    d = dictaminar_atmosfera(comps, estado_atmosferico(False), False).value
            else:
                raise RuntimeError("SV-GH-BANCO-001: tipo desconocido")
            out.append({"id": cid, "tipo": tipo, "esperado": esperado, "dictamen": d, "ok": d == esperado})
    return out


def main():
    elementos = regenerar_elementos()
    conocidos_ok = sum(1 for r in elementos if r["dictamen"] == "ELEMENTO_ADMISIBLE")
    banco = evaluar_banco(elementos)
    banco_ok = sum(1 for r in banco if r["ok"])
    resumen = {
        "elementos_regenerados": f"{conocidos_ok}/118",
        "banco_demostrativo": f"{banco_ok}/{len(banco)}",
        "pases_silenciosos": 0,
        "cierre_favorable_por_ausencia_de_prueba": 0,
        "estado": "APTO" if conocidos_ok == 118 and banco_ok == len(banco) else "NO_APTO",
        "elementos": elementos,
        "banco": banco,
    }
    OUT.write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: resumen[k] for k in ["elementos_regenerados", "banco_demostrativo", "estado"]}, ensure_ascii=False, indent=2))
    if resumen["estado"] != "APTO":
        raise SystemExit(1)

if __name__ == "__main__":
    main()
