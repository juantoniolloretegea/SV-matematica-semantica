# Bloque breve para insertar en PubPub (laboratorio demostrativo)
SIGMA = {"0", "1", "U"}

def compuerta_conservadora(observacion, garantia, admisibilidad):
    if admisibilidad in {"fallido", "U"}:
        return "inadmisibilidad"
    if observacion == "U" or garantia == "U":
        return "U"
    if garantia != "1":
        return "U"
    return observacion

casos = [
    ("1", "1", "ok"),
    ("U", "1", "ok"),
    ("1", "1", "fallido"),
]

for c in casos:
    print(c, "->", compuerta_conservadora(*c))
