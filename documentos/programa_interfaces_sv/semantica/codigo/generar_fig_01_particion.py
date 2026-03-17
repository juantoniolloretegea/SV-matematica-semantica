from itertools import product
import matplotlib.pyplot as plt

symbols = ["0", "1", "U"]
vectors = list(product(symbols, repeat=9))

def classify(v):
    n1 = sum(x == "1" for x in v)
    n0 = sum(x == "0" for x in v)
    if n1 >= 7:
        return "intrusion"
    if n0 >= 7:
        return "normal"
    return "u"

normal_x, normal_y, intr_x, intr_y, u_x, u_y = [], [], [], [], [], []
for v in vectors:
    n1 = sum(x == "1" for x in v)
    nU = sum(x == "U" for x in v)
    c = classify(v)
    if c == "normal":
        normal_x.append(n1); normal_y.append(nU)
    elif c == "intrusion":
        intr_x.append(n1); intr_y.append(nU)
    else:
        u_x.append(n1); u_y.append(nU)

plt.figure(figsize=(7.5, 5.5))
plt.scatter(normal_x, normal_y, s=12, label="Normal")
plt.scatter(intr_x, intr_y, s=12, label="Intrusión")
plt.scatter(u_x, u_y, s=12, label="Indeterminación U")
plt.xlabel("n₁")
plt.ylabel("n_U")
plt.title("SV(9,3)-IA: partición exhaustiva del espacio 3⁹")
plt.legend()
plt.tight_layout()
plt.savefig("fig_01_sv93_particion_exhaustiva.png", dpi=200)
