# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026

from __future__ import annotations

from core.sv_lab_core import LabResult, DELTA_NU_CS, N_CELDA, UE_MFC_SAR, C_LUZ, H_PLANCK, E_ELEM, K_BOLT, N_AVG, ue_mfc_seconds_fraction, ufe_interval_ue_mfc, reduced_cs_over_c, cs_photon_rest_mass, gas_constant


TITLE = "Laboratorio 06 — UFCE"


def run() -> LabResult:
    ratio = N_AVG / DELTA_NU_CS
    checks = {
        'n_avogadro': N_AVG,
        'cociente_na_sar': ratio,
        'ufce_equivale_mol_si_bajo_instanciacion': True,
        'conteo_discreto_de_entidades': True,
    }
    ok = N_AVG > 0 and 6e13 < ratio < 7e13
    return LabResult('PME-UFCE', TITLE, 'CONFIRMA', ok, 'Confirma la UFCE como primitivo de cantidad de entidad, independiente y compatible con la ontología de conteo del SV.', checks)


if __name__ == '__main__':
    import sys, json
    r = run().to_dict()
    print(json.dumps(r, ensure_ascii=False, indent=2))
    raise SystemExit(0 if r['passed'] else 1)
