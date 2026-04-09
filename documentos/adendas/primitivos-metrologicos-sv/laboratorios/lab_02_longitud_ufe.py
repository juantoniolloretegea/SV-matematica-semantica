# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026

from __future__ import annotations

from core.sv_lab_core import LabResult, DELTA_NU_CS, N_CELDA, UE_MFC_SAR, C_LUZ, H_PLANCK, E_ELEM, K_BOLT, N_AVG, ue_mfc_seconds_fraction, ufe_interval_ue_mfc, reduced_cs_over_c, cs_photon_rest_mass, gas_constant


TITLE = "Laboratorio 02 — UFE"


def run() -> LabResult:
    num, den = reduced_cs_over_c()
    interval = ufe_interval_ue_mfc()
    checks = {
        'c_luz': C_LUZ,
        'intervalo_ue_mfc_num': interval.numerator,
        'intervalo_ue_mfc_den': interval.denominator,
        'gcd_reducido_num': num,
        'gcd_reducido_den': den,
        'c_mod_9': C_LUZ % 9,
        'ufe_equivale_metro_si_bajo_instanciacion': True,
    }
    ok = interval.numerator == 9 and interval.denominator == C_LUZ and num == 656_616_555 and den == 21_413_747 and checks['c_mod_9'] == 1
    return LabResult('PME-UFE', TITLE, 'CONFIRMA', ok, 'Confirma la UFE como instanciación contingente de longitud anclada en c, sin sustrato discreto entero propio.', checks)


if __name__ == '__main__':
    import sys, json
    r = run().to_dict()
    print(json.dumps(r, ensure_ascii=False, indent=2))
    raise SystemExit(0 if r['passed'] else 1)
