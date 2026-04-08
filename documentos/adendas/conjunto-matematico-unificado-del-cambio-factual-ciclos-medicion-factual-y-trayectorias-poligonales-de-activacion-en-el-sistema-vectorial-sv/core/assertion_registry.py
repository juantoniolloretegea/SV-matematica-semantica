# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026
"""
Registro de afirmaciones auditables del Hito 3.

Cada entrada indica:
- id: identificador estable
- seccion: localización dentro del documento canónico
- tipo: teorema / proposición / identidad / contraste / deuda
- estado_esperado: CONFIRMA / REFUTA / ABIERTO
- laboratorio: módulo Python que la audita
"""
from __future__ import annotations

ASSERTIONS = [
    {"id": "CMODCF-T1", "seccion": "Parte I, V.2-V.3", "tipo": "teorema", "estado_esperado": "CONFIRMA", "laboratorio": "lab_01_cmodcf_validacion_minima"},
    {"id": "CMODCF-P9", "seccion": "Parte I, IV.13", "tipo": "proposición", "estado_esperado": "CONFIRMA", "laboratorio": "lab_02_cmodcf_umbral_y_gravedad"},
    {"id": "CS-1-CS-2", "seccion": "Parte II, 12.5", "tipo": "proposición", "estado_esperado": "CONFIRMA", "laboratorio": "lab_03_cs_propiedades_basicas"},
    {"id": "CS-3", "seccion": "Parte II, 12.5", "tipo": "proposición condicionada", "estado_esperado": "CONFIRMA", "laboratorio": "lab_04_cs_cota_condicionada_y_contraejemplo"},
    {"id": "MFC-CESIO", "seccion": "Parte III, 13.2-13.6", "tipo": "proposición", "estado_esperado": "CONFIRMA", "laboratorio": "lab_05_mfc_escala_y_cesio"},
    {"id": "MFC-MINIMO-UNIVERSAL", "seccion": "Parte III, 13.4", "tipo": "sobreafirmación", "estado_esperado": "REFUTA", "laboratorio": "lab_06_mfc_alcance_no_universal"},
    {"id": "TPA-EJEMPLO", "seccion": "Parte IV, 4.1-4.2", "tipo": "cálculo", "estado_esperado": "CONFIRMA", "laboratorio": "lab_07_tpa_ejemplo_director"},
    {"id": "TPA-O1-O2-O3", "seccion": "Parte IV, 5", "tipo": "identidad", "estado_esperado": "CONFIRMA", "laboratorio": "lab_08_tpa_identidades_emergentes"},
    {"id": "TPA-TIPOS", "seccion": "Parte IV, 3", "tipo": "clasificación", "estado_esperado": "CONFIRMA", "laboratorio": "lab_09_tpa_doce_tipos"},
    {"id": "TPA-TVMT-EXTREMOS", "seccion": "Parte IV, 10.1-10.2", "tipo": "teorema", "estado_esperado": "CONFIRMA", "laboratorio": "lab_10_tpa_tvmtpa_extremos"},
    {"id": "TPA-ISOPERIMETRIA-LINEAL", "seccion": "Parte IV, 10.3", "tipo": "refutación", "estado_esperado": "CONFIRMA", "laboratorio": "lab_11_tpa_isoperimetria_refutada"},
    {"id": "TPA-DESCRIPTOR-CUADRUPLO", "seccion": "Parte IV, 10.4", "tipo": "refutación", "estado_esperado": "CONFIRMA", "laboratorio": "lab_12_tpa_isoenergia_y_descriptor"},
    {"id": "TPA-GRADIENTE-CURVATURA", "seccion": "Parte IV, 10.5-10.6", "tipo": "proposición", "estado_esperado": "CONFIRMA", "laboratorio": "lab_13_tpa_gradiente_y_curvatura"},
    {"id": "TPA-NLP", "seccion": "Parte IV, 10.7", "tipo": "proyección", "estado_esperado": "CONFIRMA", "laboratorio": "lab_14_tpa_nlp"},
    {"id": "KEPLER-CONTRASTE", "seccion": "Parte III, 13.8", "tipo": "contraste", "estado_esperado": "CONFIRMA", "laboratorio": "lab_15_kepler_segunda_ley_contraste"},
    {"id": "KEPLER-NO-CENTRAL", "seccion": "Parte III, 13.8", "tipo": "contraste negativo", "estado_esperado": "CONFIRMA", "laboratorio": "lab_16_contraste_no_central"},
    {"id": "ABIERTOS", "seccion": "Deudas técnicas", "tipo": "deuda", "estado_esperado": "ABIERTO", "laboratorio": "lab_17_abiertos_y_no_clausurables"},
]
