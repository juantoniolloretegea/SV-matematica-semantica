from itertools import product
import matplotlib.pyplot as plt

symbols = ["0", "1", "U"]
vectors = list(product(symbols, repeat=9))

def k_transitions(v):
    k = 0
    n = len(v)
    for i in range(n):
        a = (v[i] == "U")
        b = (v[(i + 1) % n] == "U")
        if a != b:
            k += 1
    return k

def ez_from_edges(v, h=1.0):
    z = [h if x == "U" else 0.0 for x in v]
    n = len(z)
    return sum((z[(i + 1) % n] - z[i]) ** 2 for i in range(n))

ks = []
ezs = []
for v in vectors:
    ks.append(k_transitions(v))
    ezs.append(ez_from_edges(v, h=1.0))

plt.figure(figsize=(7.5, 5.5))
plt.scatter(ks, ezs, s=12)
plt.xlabel("k(v): transiciones U / no-U")
plt.ylabel("E_z calculada por aristas (h=1)")
plt.title("Verificación geométrica auxiliar: E_z = k(v)·h²")
plt.tight_layout()
plt.savefig("fig_03_verificacion_geometrica_auxiliar.png", dpi=200)
