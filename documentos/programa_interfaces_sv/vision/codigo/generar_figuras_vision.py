from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).resolve().parent.parent
FIG_DIR = BASE / "figuras"
FIG_DIR.mkdir(parents=True, exist_ok=True)

W, H = 1200, 800
BG = (248, 250, 252)
NAVY = (24, 56, 88)
BLUE = (49, 99, 149)
GOLD = (180, 140, 40)
GRAY = (120, 130, 145)
WHITE = (255, 255, 255)
LIGHTBLUE = (221, 234, 247)
GREENFILL = (230, 242, 230)

def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(path, size)

def wrapped(draw: ImageDraw.ImageDraw, text: str, box, fnt, fill=(0, 0, 0), line_spacing=6, align="left") -> int:
    x, y, w, h = box
    paragraphs = text.split("\n")
    yy = y
    for p in paragraphs:
        words = p.split()
        if not words:
            yy += int(fnt.size * 1.2)
            continue
        cur = ""
        lines = []
        for wd in words:
            test = (cur + " " + wd).strip()
            if draw.textbbox((0, 0), test, font=fnt)[2] <= w:
                cur = test
            else:
                lines.append(cur)
                cur = wd
        if cur:
            lines.append(cur)
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=fnt)
            tw = bbox[2] - bbox[0]
            xx = x + (w - tw) / 2 if align == "center" else x
            draw.text((xx, yy), line, font=fnt, fill=fill)
            yy += (bbox[3] - bbox[1]) + line_spacing
        yy += 4
    return yy

def save(im: Image.Image, name: str) -> None:
    path = FIG_DIR / name
    im.save(path)
    print(f"OK: {path}")

def new_fig(title: str, subtitle: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    im = Image.new("RGB", (1200, 760), BG)
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((30, 30, 1170, 730), radius=24, outline=BLUE, width=3, fill=(252, 253, 255))
    dr.rectangle((50, 50, 1150, 120), fill=NAVY)
    dr.text((80, 68), title, font=font(30, True), fill=WHITE)
    wrapped(dr, subtitle, (70, 140, 1060, 60), font(20), fill=GRAY)
    return im, dr

def portada() -> None:
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((50, 40, 1150, 760), radius=30, outline=BLUE, width=4, fill=(252, 253, 255))
    d.rectangle((80, 80, 1120, 160), fill=NAVY)
    d.text((110, 100), "Sistema Vectorial SV — Carril de visión", font=font(38, True), fill=WHITE)
    cx, cy = 290, 430
    pts = [(cx - 140, cy + 120), (cx, cy - 140), (cx + 140, cy + 120)]
    d.polygon(pts, outline=BLUE, width=6)
    d.line((cx, cy - 140, cx, cy - 260), fill=GOLD, width=6)
    d.ellipse((cx - 16, cy - 276, cx + 16, cy - 244), fill=GOLD, outline=GOLD)
    for i, (title, sub) in enumerate([("Captura", "soporte visible"), ("Ternarización", "{0,1,U}"), ("Trayectoria", "frame → trayectoria")]):
        x = 520 + i * 190
        d.rounded_rectangle((x, 320, x + 160, 450), radius=18, fill=LIGHTBLUE, outline=BLUE, width=3)
        wrapped(d, title, (x + 12, 340, 136, 40), font(24, True), fill=NAVY, align="center")
        wrapped(d, sub, (x + 12, 385, 136, 50), font(18), fill=NAVY, align="center")
    for i in range(2):
        x1 = 680 + i * 190
        d.line((x1, 385, x1 + 25, 385), fill=GRAY, width=4)
        d.polygon([(x1 + 25, 385), (x1 + 10, 377), (x1 + 10, 393)], fill=GRAY)
    wrapped(d, "Formalización de una interfaz visual estructurada en el Sistema Vectorial SV", (90, 540, 1020, 120), font(34, True), fill=NAVY)
    wrapped(d, "Portada editorial técnica · esquema inicial para GitHub / PubPub · 1200 × 800", (90, 660, 1020, 40), font(22), fill=GRAY)
    save(img, "portada_vision_sv_1200x800.png")

def fig_01() -> None:
    im, dr = new_fig("Figura 1 · Cadena visual de entrada", "Cadena mínima: configuración → soporte → captura → unidad observacional → admisibilidad → ternarización → interfaz → célula → frame → trayectoria.")
    labels = ["Configuración\nde referencia", "Soporte\nvisible", "Captura", "Unidad\nobservacional", "Admisibilidad", "Ternarización\n{0,1,U}", "Interfaz\nparamétrica", "Célula", "Frame", "Trayectoria"]
    xs = [60, 180, 300, 425, 555, 685, 840, 980, 1065, 1135]
    ws = [100, 100, 100, 110, 110, 135, 120, 75, 60, 30]
    y = 320
    h = 115
    for i, l in enumerate(labels):
        x = xs[i]
        w = ws[i]
        dr.rounded_rectangle((x, y, x + w, y + h), radius=16, fill=LIGHTBLUE if i < 6 else GREENFILL, outline=BLUE, width=2)
        wrapped(dr, l, (x + 6, y + 22, w - 12, 70), font(17, True if i in [2, 5] else False), fill=NAVY, align="center")
        if i < len(labels) - 1:
            xa = x + w
            xb = xs[i + 1] - 6
            dr.line((xa + 3, y + h / 2, xb, y + h / 2), fill=GRAY, width=4)
            dr.polygon([(xb, y + h / 2), (xb - 14, y + h / 2 - 8), (xb - 14, y + h / 2 + 8)], fill=GRAY)
    wrapped(dr, "Principio operativo: capturar no es decidir; ternarizar no es clausurar.", (100, 565, 1000, 40), font(24, True), fill=GOLD, align="center")
    save(im, "fig_01_cadena_visual_captura_admisibilidad_ternarizacion.png")

def fig_02() -> None:
    im, dr = new_fig("Figura 2 · Banco visual n=9 y render canónico", "Suelo exacto para verificar configuración ternaria, presencia de U, consistencia del render y coherencia entre figura y cierre.")
    gx, gy, cell = 120, 250, 50
    vals = ["0", "1", "U", "1", "U", "0", "U", "0", "1"]
    for idx, val in enumerate(vals):
        r, c = divmod(idx, 3)
        x = gx + c * cell
        y = gy + r * cell
        fill = {"0": (235, 245, 255), "1": (225, 245, 225), "U": (255, 241, 210)}[val]
        dr.rectangle((x, y, x + cell, y + cell), outline=NAVY, width=2, fill=fill)
        dr.text((x + 18, y + 10), val, font=font(24, True), fill=NAVY)
    wrapped(dr, "Microconfiguración\ncanónica 3×3", (90, 420, 220, 70), font(24, True), fill=NAVY, align="center")
    dr.line((330, 325, 470, 325), fill=GRAY, width=5)
    dr.polygon([(470, 325), (450, 313), (450, 337)], fill=GRAY)
    rx, ry = 620, 330
    tri = [(rx, ry + 170), (rx + 130, ry - 40), (rx + 260, ry + 170)]
    dr.polygon(tri, outline=BLUE, width=5)
    pts = [(rx + 65, ry + 65, "0"), (rx + 130, ry + 10, "U"), (rx + 195, ry + 65, "1"), (rx + 95, ry + 120, "1"), (rx + 165, ry + 120, "U"), (rx + 130, ry + 170, "0")]
    for x, y, val in pts:
        color = {"0": (220, 235, 255), "1": (225, 245, 225), "U": (255, 241, 210)}[val]
        dr.ellipse((x - 20, y - 20, x + 20, y + 20), fill=color, outline=NAVY, width=2)
        dr.text((x - 8, y - 13), val, font=font(22, True), fill=NAVY)
    wrapped(dr, "Render canónico estructural", (600, 540, 320, 40), font(24, True), fill=NAVY, align="center")
    save(im, "fig_02_banco_visual_n9_render_canonico.png")

def fig_03() -> None:
    im, dr = new_fig("Figura 3 · Estatuto visual de U", "Regímenes legitimadores: oclusión, degradación de captura y ambigüedad local no clausurable.")
    titles = ["Oclusión", "Captura degradada", "Ambigüedad local"]
    for i, tit in enumerate(titles):
        x = 90 + i * 350
        dr.rounded_rectangle((x, 230, x + 280, 540), radius=18, outline=BLUE, width=3, fill=(250, 250, 252))
        dr.rectangle((x + 20, 255, x + 120, 355), outline=NAVY, width=3, fill=LIGHTBLUE)
        if i == 0:
            dr.rectangle((x + 70, 240, x + 170, 340), fill=(190, 190, 190))
        elif i == 1:
            for dx in range(25):
                xx = x + 25 + (dx * 7) % 90
                yy = 260 + (dx * 13) % 90
                dr.ellipse((xx, yy, xx + 3, yy + 3), fill=GRAY)
        else:
            dr.line((x + 25, 350, x + 115, 260), fill=BLUE, width=3)
            dr.line((x + 25, 260, x + 115, 350), fill=BLUE, width=3)
        dr.rounded_rectangle((x + 150, 285, x + 235, 365), radius=14, fill=(255, 241, 210), outline=GOLD, width=3)
        wrapped(dr, "U", (x + 175, 307, 35, 35), font(34, True), fill=NAVY, align="center")
        wrapped(dr, tit, (x + 20, 395, 240, 30), font(22, True), fill=NAVY, align="center")
        wrapped(dr, "Persistencia legítima de indeterminación estructural.", (x + 28, 445, 225, 60), font(16), fill=GRAY, align="center")
    save(im, "fig_03_u_visual_oclusion_ambiguedad_reapertura.png")

def fig_04() -> None:
    im, dr = new_fig("Figura 4 · Suceso, reevaluación, frame y trayectoria", "El cambio visual legítimo exige suceso pertinente, nueva captura o nueva condición de admisibilidad.")
    steps = ["Suceso pertinente", "Reevaluación", "Frame", "Trayectoria"]
    sx = [110, 370, 640, 885]
    for i, st in enumerate(steps):
        x = sx[i]
        dr.rounded_rectangle((x, 310, x + 190, 430), radius=18, fill=LIGHTBLUE if i < 2 else GREENFILL, outline=BLUE, width=3)
        wrapped(dr, st, (x + 15, 343, 160, 50), font(22, True), fill=NAVY, align="center")
        if i < 3:
            dr.line((x + 190, 370, sx[i + 1] - 15, 370), fill=GRAY, width=5)
            dr.polygon([(sx[i + 1] - 15, 370), (sx[i + 1] - 30, 360), (sx[i + 1] - 30, 380)], fill=GRAY)
    dr.line((160, 560, 1040, 560), fill=NAVY, width=4)
    nodes = [(220, "U"), (430, "U"), (650, "1"), (860, "1")]
    for x, val in nodes:
        color = (255, 241, 210) if val == "U" else (225, 245, 225)
        dr.ellipse((x - 26, 534, x + 26, 586), fill=color, outline=NAVY, width=3)
        dr.text((x - 10, 546), val, font=font(24, True), fill=NAVY)
    wrapped(dr, "Persistencia de U → reapertura → clausura legítima", (250, 610, 700, 30), font(22, True), fill=GOLD, align="center")
    save(im, "fig_04_suceso_frame_reevaluacion_trayectoria_visual.png")

def fig_05() -> None:
    im, dr = new_fig("Figura 5 · Carta canónica Φ₂ y carta auxiliar Φ₃", "La carta espacial afín auxiliar aumenta legibilidad sin alterar ontología.")
    dr.rounded_rectangle((90, 220, 480, 590), radius=18, outline=BLUE, width=3, fill=(248, 252, 255))
    dr.text((215, 235), "Φ₂ canónica", font=font(26, True), fill=NAVY)
    dr.line((180, 500, 390, 500), fill=GRAY, width=3)
    dr.line((285, 560, 285, 300), fill=GRAY, width=3)
    tri = [(205, 500), (285, 360), (365, 500)]
    dr.polygon(tri, outline=BLUE, width=5)
    dr.ellipse((270, 345, 300, 375), fill=(255, 241, 210), outline=GOLD, width=3)
    dr.text((280, 347), "U", font=font(20, True), fill=NAVY)
    dr.rounded_rectangle((640, 180, 1080, 620), radius=18, outline=BLUE, width=3, fill=(248, 252, 255))
    dr.text((770, 195), "Φ₃ auxiliar", font=font(26, True), fill=NAVY)
    ox, oy = 810, 500
    dr.line((ox, oy, 980, oy), fill=GRAY, width=3)
    dr.line((ox, oy, ox, 320), fill=GRAY, width=3)
    dr.line((ox, oy, 720, 580), fill=GRAY, width=3)
    dr.line((750, 500, 840, 380), fill=BLUE, width=5)
    dr.line((840, 380, 930, 500), fill=BLUE, width=5)
    dr.line((930, 500, 750, 500), fill=BLUE, width=5)
    dr.line((840, 380, 840, 285), fill=GOLD, width=5)
    dr.ellipse((824, 266, 856, 298), fill=(255, 241, 210), outline=GOLD, width=3)
    wrapped(dr, "Separación geométrica\nauxiliar de U", (760, 545, 160, 60), font(20, True), fill=NAVY, align="center")
    dr.line((500, 400, 620, 400), fill=GRAY, width=4)
    dr.polygon([(620, 400), (605, 392), (605, 408)], fill=GRAY)
    save(im, "fig_05_carta_r2_r3_auxiliar_no_ontologica.png")

def fig_06() -> None:
    im, dr = new_fig("Figura 6 · Tres vallas del carril de visión", "Lo cerrado hoy, lo nombrado como extensión legítima y lo expresamente fuera de alcance.")
    cols = [
        ("Cierra ahora", "Célula visual simple\nPar heterogéneo visión + garantía\nTrayectoria visual\nCarta auxiliar de desopacación", (225, 245, 225), (24, 56, 88)),
        ("Extensión legítima no clausurada", "Binocularidad homogénea\nSupervisión fuerte de segundo nivel\nPuerto perceptivo fuerte", (255, 247, 220), (130, 95, 20)),
        ("Fuera de alcance", "Actuadores\nSalida motriz cerrada\nHumanoide autónomo\nEstadística opaca", (252, 230, 230), (150, 60, 60)),
    ]
    for i, (tit, body, fillc, head) in enumerate(cols):
        x = 85 + i * 355
        dr.rounded_rectangle((x, 220, x + 300, 610), radius=18, outline=BLUE, width=3, fill=fillc)
        dr.rectangle((x + 20, 245, x + 280, 305), fill=head)
        wrapped(dr, tit, (x + 25, 258, 250, 35), font(24, True), fill=WHITE, align="center")
        wrapped(dr, body, (x + 30, 340, 240, 210), font(20), fill=NAVY, align="center")
    save(im, "fig_06_tres_vallas_carril_vision.png")

def main() -> None:
    portada()
    fig_01()
    fig_02()
    fig_03()
    fig_04()
    fig_05()
    fig_06()
    print("Regeneración completada.")

if __name__ == "__main__":
    main()
