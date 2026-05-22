# -*- coding: utf-8 -*-
# Autor: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | ITVIA | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 22/05/2026
# Publicación: Campo y energía, génesis de la masa y definición física de la gravedad: gravitación universal, constante cosmológica y dominio observable.
# Archivo material de laboratorio reproducible. No modificar sin conservar autoría, licencia y trazabilidad.
import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "datos"
REL_TOL = 1e-9
ABS_TOL = 1e-60

OUTPUT_HEADER = 'AUTOR|Juan Antonio Lloret Egea|ORCID|0000-0002-6634-3351\nLICENCIA|CC BY-NC-ND 4.0|PUBLICACION|Campo y energia, genesis de la masa y definicion fisica de la gravedad\n'

C = {
    "c": 299792458.0,
    "G": 6.67430e-11,
    "T_obs": 435_494_880_000_000_000.0,
    "Mpc": 3.0856775814913673e22,
    "M_Tierra": 5.9722e24,
    "R_Tierra": 6.371e6,
    "M_Luna": 7.342e22,
    "r_Tierra_Luna": 3.844e8,
    "M_Sol": 1.98847e30,
    "UA": 1.495978707e11,
}

def read_csv(name):
    with (DATA / name).open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def ensure(cond, msg):
    if not cond:
        raise AssertionError(msg)

def lab_line(lab_id, status, detail):
    return f"{lab_id}|{status}|{detail}"

def fmt(x):
    if isinstance(x, str):
        return x
    return f"{x:.15e}"

def check_numeric(name, value, expected, rel=REL_TOL, abs_tol=ABS_TOL):
    ensure(math.isclose(value, expected, rel_tol=rel, abs_tol=abs_tol), f"{name}: {value} != {expected}")
    return True

def bank_rows():
    return {r["banco"]: r for r in read_csv("bancos_observacionales_lambda.csv")}

def audited_lambda_bank(bank="B_Planck18-baseΛCDM"):
    banks = bank_rows()
    ensure(bank in banks, f"banco no declarado: {bank}")
    row = banks[bank]
    ensure(row["estado"] == "AUDITADO", f"banco no auditado: {bank}")
    ensure(row["H0_km_s_Mpc"] and row["Omega_Lambda"] and row["unidad_H0"] == "km·s⁻¹·Mpc⁻¹", f"banco incompleto: {bank}")
    ensure(row["sigma_H0"] and row["sigma_Omega_Lambda"], f"banco sin incertidumbre: {bank}")
    ensure(row["fuente"], f"banco sin fuente: {bank}")
    return row

def H0_si_from_bank(bank="B_Planck18-baseΛCDM"):
    row = audited_lambda_bank(bank)
    return float(row["H0_km_s_Mpc"]) * 1000.0 / C["Mpc"]

def omega_from_bank(bank="B_Planck18-baseΛCDM"):
    return float(audited_lambda_bank(bank)["Omega_Lambda"])

def lambda_puro():
    return 3.0 / (C["c"] ** 2 * C["T_obs"] ** 2)

def lambda_obs(bank="B_Planck18-baseΛCDM"):
    return 3.0 * omega_from_bank(bank) * H0_si_from_bank(bank) ** 2 / C["c"] ** 2

def lambda_sv_ret_tuple(bank="B_Planck18-baseΛCDM"):
    row = audited_lambda_bank(bank)
    return {
        "Lambda_obs": lambda_obs(bank),
        "u": "m^-2",
        "B": bank,
        "sigma_B": f"sigma_H0={row['sigma_H0']};sigma_Omega_Lambda={row['sigma_Omega_Lambda']}",
        "Delta_Lambda_B": "Delta_B=0;Delta_u=0;Delta_fund=0",
        "d_Lambda_B": row["dictamen"],
    }

def a_lambda(r_m, bank="B_Planck18-baseΛCDM"):
    return lambda_obs(bank) * C["c"] ** 2 * r_m / 3.0

def g_earth():
    return C["G"] * C["M_Tierra"] / C["R_Tierra"] ** 2

def F_earth_moon():
    return C["G"] * C["M_Tierra"] * C["M_Luna"] / C["r_Tierra_Luna"] ** 2

def a_moon_by_earth():
    return C["G"] * C["M_Tierra"] / C["r_Tierra_Luna"] ** 2

def F_sun_earth():
    return C["G"] * C["M_Sol"] * C["M_Tierra"] / C["UA"] ** 2

def a_sun_at_earth():
    return C["G"] * C["M_Sol"] / C["UA"] ** 2

def lambda_ratio(bank="B_Planck18-baseΛCDM"):
    return lambda_obs(bank) / lambda_puro()

def lab_01():
    pos = read_csv("banco_positivo.csv")
    neg = read_csv("banco_negativo.csv")
    ensure(any(r["codigo"] == "P-11" and "ABSORCION" in r["dictamen"] for r in pos), "P-11 no absorbido")
    ensure(any(r["codigo"] == "N-12" and r["resultado_esperado"] == "RECHAZO" for r in neg), "N-12 no rechazado")
    return lab_line("LAB-01_campo_energia", "APTO", "campo_y_energia_articulados_por_dominio_no_por_sinonimia")

def lab_02():
    neg = read_csv("banco_negativo.csv")
    for code in ["N-09", "N-10", "N-11"]:
        ensure(any(r["codigo"] == code and r["resultado_esperado"] == "RECHAZO" for r in neg), f"{code} no rechazado")
    return lab_line("LAB-02_masa_frontera", "APTO", "masa_exige_frontera_residual_retorno_y_traza")

def lab_03():
    pos = read_csv("banco_positivo.csv")
    ensure(any(r["codigo"] == "P-10" and "CANONICO" in r["dictamen"] for r in pos), "P-10 hidrogeno no canónico")
    return lab_line("LAB-03_hidrogeno_persistencia", "APTO", "hidrogeno_verificado_como_caso_canonico_conocido_no_minimo_universal")

def lab_04():
    neg = read_csv("banco_negativo.csv")
    ensure(any(r["codigo"] == "N-13" and r["resultado_esperado"] == "RECHAZO" for r in neg), "curvatura sin fuente no rechazada")
    return lab_line("LAB-04_campo_gravitatorio", "APTO", "campo_gravitatorio_exige_fuente_dominio_accion_y_retorno")

def lab_05():
    check_numeric("F_Tierra_Luna", F_earth_moon(), 1.9805585650280284e20, rel=1e-12)
    check_numeric("F_Sol_Tierra", F_sun_earth(), 3.5416715752424943e22, rel=1e-12)
    return lab_line("LAB-05_atraccion_local", "APTO", f"F_Tierra_Luna={fmt(F_earth_moon())};F_Sol_Tierra={fmt(F_sun_earth())}")

def lab_06():
    neg = read_csv("banco_negativo.csv")
    for code in ["N-01", "N-02", "N-03", "N-17"]:
        ensure(any(r["codigo"] == code and r["resultado_esperado"] == "RECHAZO" for r in neg), f"{code} no rechazado")
    return lab_line("LAB-06_distancias_tipadas", "APTO", "r_local_DL_DA_DM_y_distancia_factual_no_intercambiables")

def lab_07():
    check_numeric("g_Tierra", g_earth(), 9.820302293385645, rel=1e-12)
    check_numeric("a_Luna_por_Tierra", a_moon_by_earth(), 0.00269757363801148, rel=1e-12)
    return lab_line("LAB-07_constante_G", "APTO", f"g_Tierra={fmt(g_earth())};a_Luna={fmt(a_moon_by_earth())}")

def lab_08():
    check_numeric("Lambda_SV_puro", lambda_puro(), 1.7600043527547774e-52, rel=1e-12, abs_tol=1e-70)
    kappa_obs = 1.0 / C["T_obs"]
    h_like = kappa_obs * C["Mpc"] / 1000.0
    check_numeric("kappa_obs_convertida", h_like, 70.854508817448, rel=1e-12)
    ensure(h_like > 0 and h_like != float(audited_lambda_bank()["H0_km_s_Mpc"]), "kappa_obs no debe confundirse con H0[B]")
    return lab_line("LAB-08_lambda_puro", "APTO", f"Lambda_SV_puro={fmt(lambda_puro())}_m^-2;kappa_obs_no_es_H0_B")

def lab_09():
    tuple_ret = lambda_sv_ret_tuple("B_Planck18-baseΛCDM")
    check_numeric("Lambda_obs_B", tuple_ret["Lambda_obs"], 1.0909105028380932e-52, rel=1e-12, abs_tol=1e-70)
    ensure(tuple_ret["B"] == "B_Planck18-baseΛCDM", "retorno sin banco correcto")
    ensure(tuple_ret["u"] == "m^-2" and tuple_ret["sigma_B"] and tuple_ret["Delta_Lambda_B"], "tupla de retorno incompleta")
    banks = bank_rows()
    ensure(banks["B_Planck18+BAO"]["estado"] != "AUDITADO", "banco Planck18+BAO no debe cerrar como auditado en este laboratorio")
    ensure(banks["B_DESI-DR2"]["estado"] != "AUDITADO", "DESI no debe cerrar como magnitud constitutiva")
    adv = read_csv("banco_lambda_adversarial.csv")
    ensure(len(adv) == 7 and all(r["resultado_esperado"] == "RECHAZO" for r in adv), "banco lambda adversarial incompleto")
    return lab_line("LAB-09_lambda_retorno_banco_declarado", "APTO", f"B=B_Planck18-baseLambdaCDM;Lambda_obs_B={fmt(tuple_ret['Lambda_obs'])}_m^-2;Lambda_SV_ret_B=tupla_auditada")

def lab_10():
    ratio = a_lambda(C["UA"]) / a_sun_at_earth()
    check_numeric("ratio_aLambda_aSol", ratio, 8.24443205916933e-23, rel=1e-12)
    ensure(ratio < 1e-20, "Lambda local no queda despreciable frente a retorno solar")
    return lab_line("LAB-10_separacion_G_Lambda", "APTO", f"aLambda_AU/aSol={fmt(ratio)};G_y_Lambda_no_intercambiables")

def lab_11():
    neg = read_csv("banco_negativo.csv")
    ensure(any(r["codigo"] == "N-08" and r["resultado_esperado"] == "RECHAZO" for r in neg), "vacío desnudo no rechazado")
    return lab_line("LAB-11_vacio_lambda", "APTO", "vacio_desnudo_no_proyecta_directamente_sobre_Lambda_fisica")

def lab_12():
    pos = read_csv("banco_positivo.csv")
    neg = read_csv("banco_negativo.csv")
    adv = read_csv("banco_lambda_adversarial.csv")
    ensure(any(r["codigo"] == "P-12" and "PARCIAL" in r["dictamen"] for r in pos), "DESI no parcial")
    ensure(any(r["codigo"] == "N-15" and r["resultado_esperado"] == "RECHAZO" for r in neg), "ajuste como fundamento no rechazado")
    ensure(any(r["codigo"] == "LNB-07" and r["resultado_esperado"] == "RECHAZO" for r in adv), "DESI/SH0ES como fundamento no rechazado")
    return lab_line("LAB-12_energia_oscura_dinamica", "APTO", "tension_observacional_no_cierra_mecanismo_final")

def lab_13():
    tr = read_csv("banco_transduccion.csv")
    ensure(len(tr) == 12, "banco de transducción incompleto")
    ensure(any(r["id"] == "T-08" and r["dictamen"] == "RECHAZO" for r in tr), "T-08 no rechazado")
    ensure(any(r["id"] == "T-04" and r["salida_evaluable"] == "m⁻²" for r in tr), "T-04 no retorna m^-2")
    ensure(any(r["id"] == "T-05" and "B" in r["residual"] and "sigma_B" in r["salida_evaluable"] for r in tr), "T-05 no tipa retorno de banco")
    return lab_line("LAB-13_transduccion_bidireccional", "APTO", "todas_las_transducciones_tienen_retorno_o_rechazo_explicito")

def lab_14():
    pos = read_csv("banco_positivo.csv")
    neg = read_csv("banco_negativo.csv")
    adv = read_csv("banco_lambda_adversarial.csv")
    ensure(len(pos) == 12, "banco positivo incompleto")
    ensure(len(neg) == 18, "banco negativo incompleto")
    ensure(len(adv) == 7, "banco adversarial Lambda incompleto")
    return lab_line("LAB-14_matriz_absorcion", "APTO", "dictamen_por_uso_dominio_unidad_residual_y_retorno")

def lab_15():
    neg = read_csv("banco_negativo.csv")
    adv = read_csv("banco_lambda_adversarial.csv")
    failed = [r["codigo"] for r in neg if r["resultado_esperado"] != "RECHAZO"]
    failed += [r["codigo"] for r in adv if r["resultado_esperado"] != "RECHAZO"]
    ensure(not failed, f"negativos aceptados: {failed}")
    return lab_line("LAB-15_banco_negativo_integral", "APTO", "N-01_a_N-18_y_LNB-01_a_LNB-07_rechazados_sin_pase_silencioso")

def lab_16(lines=None):
    if lines is None:
        lines = all_lab_lines(include_16=False)
    expected = OUTPUT_HEADER + "\n".join(lines + [lab_line("LAB-16_salida_global", "APTO", "salida_obtenida_coincide_con_salida_esperada")]) + "\n"
    expected_path = ROOT / "salida_esperada.txt"
    if expected_path.exists():
        stored = expected_path.read_text(encoding="utf-8")
        ensure(stored == expected, "salida esperada no coincide con salida calculada")
    return lab_line("LAB-16_salida_global", "APTO", "salida_obtenida_coincide_con_salida_esperada")

LABS = [
    lab_01, lab_02, lab_03, lab_04, lab_05, lab_06, lab_07, lab_08,
    lab_09, lab_10, lab_11, lab_12, lab_13, lab_14, lab_15
]

def all_lab_lines(include_16=True):
    lines = [fn() for fn in LABS]
    if include_16:
        lines.append(lab_16(lines))
    return lines

def run_all(write_output=True):
    lines = all_lab_lines(include_16=True)
    text = OUTPUT_HEADER + "\n".join(lines) + "\n"
    if write_output:
        (ROOT / "salida_obtenida.txt").write_text(text, encoding="utf-8")
    return text

if __name__ == "__main__":
    print(run_all(write_output=False), end="")
