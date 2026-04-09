# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026

"""Registro de afirmaciones auditables para primitivos metrológicos del SV."""
from __future__ import annotations

ASSERTIONS = [
    {"id": "PME-UE_MFC", "seccion": "III", "tipo": "primitivo", "estado_esperado": "CONFIRMA", "laboratorio": "lab_01_tiempo_ue_mfc"},
    {"id": "PME-UFE", "seccion": "IV", "tipo": "primitivo", "estado_esperado": "CONFIRMA", "laboratorio": "lab_02_longitud_ufe"},
    {"id": "PME-UFM", "seccion": "V", "tipo": "primitivo", "estado_esperado": "CONFIRMA", "laboratorio": "lab_03_masa_ufm"},
    {"id": "PME-UFC", "seccion": "VI", "tipo": "primitivo", "estado_esperado": "CONFIRMA", "laboratorio": "lab_04_corriente_ufc"},
    {"id": "PME-UFT", "seccion": "VII", "tipo": "primitivo", "estado_esperado": "CONFIRMA", "laboratorio": "lab_05_temperatura_uft"},
    {"id": "PME-UFCE", "seccion": "VIII", "tipo": "primitivo", "estado_esperado": "CONFIRMA", "laboratorio": "lab_06_cantidad_ufce"},
    {"id": "PME-DERIVADAS", "seccion": "IX", "tipo": "tabla derivada", "estado_esperado": "CONFIRMA", "laboratorio": "lab_07_unidades_derivadas"},
]
