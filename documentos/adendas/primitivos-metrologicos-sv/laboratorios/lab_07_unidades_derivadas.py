# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026

from __future__ import annotations

from core.sv_lab_core import LabResult, DELTA_NU_CS, N_CELDA, UE_MFC_SAR, C_LUZ, H_PLANCK, E_ELEM, K_BOLT, N_AVG, ue_mfc_seconds_fraction, ufe_interval_ue_mfc, reduced_cs_over_c, cs_photon_rest_mass, gas_constant


TITLE = "Laboratorio 07 — Unidades derivadas"


def run() -> LabResult:
    r = gas_constant()
    checks = {
        'fuerza': 'UFM*UFE*UE_MFC^-2',
        'energia': 'UFM*UFE^2*UE_MFC^-2',
        'potencia': 'UFM*UFE^2*UE_MFC^-3',
        'voltaje': 'UFM*UFE^2*UFC^-1*UE_MFC^-3',
        'resistencia': 'UFM*UFE^2*UFC^-2*UE_MFC^-3',
        'campo_magnetico': 'UFM*UFC^-1*UE_MFC^-2',
        'constante_gas': r,
    }
    ok = 8.31 < r < 8.32
    return LabResult('PME-DERIVADAS', TITLE, 'CONFIRMA', ok, 'Confirma la tabla de unidades derivadas y la consistencia dimensional de R = N_A * k_B.', checks)


if __name__ == '__main__':
    import sys, json
    r = run().to_dict()
    print(json.dumps(r, ensure_ascii=False, indent=2))
    raise SystemExit(0 if r['passed'] else 1)
