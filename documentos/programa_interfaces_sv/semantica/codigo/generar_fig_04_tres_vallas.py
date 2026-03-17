import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5.5))
ax = plt.gca()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

boxes = [
    (1, 6.8, "Valla 1\nLicitud doctrinal"),
    (3.7, 6.8, "Valla 2\nCódigo exacto"),
    (6.4, 6.8, "Valla 3\nClausura con calidad"),
]
for x, y, text in boxes:
    rect = plt.Rectangle((x, y), 2.1, 1.3, fill=False)
    ax.add_patch(rect)
    ax.text(x + 1.05, y + 0.65, text, ha="center", va="center")

ax.annotate("", xy=(3.7, 7.45), xytext=(3.1, 7.45), arrowprops=dict(arrowstyle="->"))
ax.annotate("", xy=(6.4, 7.45), xytext=(5.8, 7.45), arrowprops=dict(arrowstyle="->"))

ax.text(2.05, 4.6, "Afirmación teórica", ha="center")
ax.annotate("", xy=(2.05, 6.8), xytext=(2.05, 5.1), arrowprops=dict(arrowstyle="->"))
ax.text(4.75, 4.6, "Dataset + scripts\nreproducibles", ha="center")
ax.annotate("", xy=(4.75, 6.8), xytext=(4.75, 5.1), arrowprops=dict(arrowstyle="->"))
ax.text(7.45, 4.6, "Resultado fuerte\npara el paper", ha="center")
ax.annotate("", xy=(7.45, 6.8), xytext=(7.45, 5.1), arrowprops=dict(arrowstyle="->"))

plt.title("Régimen experimental de tres vallas")
plt.tight_layout()
plt.savefig("fig_04_tres_vallas.png", dpi=200)
