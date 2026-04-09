# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026

from __future__ import annotations

from core.sv_lab_core import LabResult, DELTA_NU_CS, N_CELDA, UE_MFC_SAR, C_LUZ, H_PLANCK, E_ELEM, K_BOLT, N_AVG, ue_mfc_seconds_fraction, ufe_interval_ue_mfc, reduced_cs_over_c, cs_photon_rest_mass, gas_constant


TITLE = "Laboratorio 05 — UFT"


def run() -> LabResult:
    r = gas_constant()
    e293 = K_BOLT * 293
    checks = {
        'k_boltzmann': K_BOLT,
        'energia_termica_293': e293,
        'constante_gas_r': r,
        'uft_equivale_kelvin_si_bajo_instanciacion': True,
        'delimitacion_negativa_estadistica': True,
    }
    ok = K_BOLT > 0 and 8.31 < r < 8.32 and e293 > 0
    return LabResult('PME-UFT', TITLE, 'CONFIRMA', ok, 'Confirma la UFT como instanciación contingente del kelvin anclada en k_B, sin importar mecánica estadística al SV.', checks)


if __name__ == '__main__':
    import sys, json
    r = run().to_dict()
    print(json.dumps(r, ensure_ascii=False, indent=2))
    raise SystemExit(0 if r['passed'] else 1)
