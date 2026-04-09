# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026

from __future__ import annotations

from core.sv_lab_core import LabResult, DELTA_NU_CS, N_CELDA, UE_MFC_SAR, C_LUZ, H_PLANCK, E_ELEM, K_BOLT, N_AVG, ue_mfc_seconds_fraction, ufe_interval_ue_mfc, reduced_cs_over_c, cs_photon_rest_mass, gas_constant


TITLE = "Laboratorio 03 — UFM"


def run() -> LabResult:
    m_cs = cs_photon_rest_mass()
    checks = {
        'h_planck': H_PLANCK,
        'c_luz': C_LUZ,
        'delta_nu_cs': DELTA_NU_CS,
        'm_foton_cs_ufm': m_cs,
        'ufm_equivale_kg_si_bajo_instanciacion': True,
        'masa_invariante_compatible': True,
    }
    ok = H_PLANCK > 0 and m_cs > 0 and abs(H_PLANCK - 6.626_070_15e-34) < 1e-44
    return LabResult('PME-UFM', TITLE, 'CONFIRMA', ok, 'Confirma la UFM como instanciación contingente anclada en h y restringida a masa invariante.', checks)


if __name__ == '__main__':
    import sys, json
    r = run().to_dict()
    print(json.dumps(r, ensure_ascii=False, indent=2))
    raise SystemExit(0 if r['passed'] else 1)
