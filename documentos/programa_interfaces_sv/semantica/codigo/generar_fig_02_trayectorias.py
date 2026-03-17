import matplotlib.pyplot as plt

traj_examples = {
    "U→0": ["U", "U", "0"],
    "U→1": ["U", "U", "1"],
    "0→U→0": ["0", "U", "0"],
    "1→U→1": ["1", "U", "1"],
}
mapping = {"0": 0, "U": 1, "1": 2}

plt.figure(figsize=(7.5, 5.5))
for name, seq in traj_examples.items():
    xs = list(range(len(seq)))
    ys = [mapping[s] for s in seq]
    plt.plot(xs, ys, marker="o", label=name)
plt.yticks([0, 1, 2], ["0", "U", "1"])
plt.xlabel("Paso discreto")
plt.ylabel("Estado")
plt.title("Trayectorias estructurales ejemplares de U")
plt.legend()
plt.tight_layout()
plt.savefig("fig_02_trayectorias_u.png", dpi=200)
