# Código del carril de visión del Sistema Vectorial SV

**Fecha y Versión: V.1 del conjunto**  
**Fecha:** 4 de abril de 2026  
**Versión del conjunto:** V.1 del conjunto  
**Autor del corpus:** Juan Antonio Lloret Egea  
**ORCID:** 0000-0002-6634-3351  
**Institución:** ITVIA — IA eñ™  
**ISSN:** 2695-6411  
**Licencia:** CC BY-NC-ND 4.0  
**Titularidad y autoría:** © Juan Antonio Lloret Egea, 2026. Este conjunto se distribuye con atribución explícita de autoría y bajo la licencia indicada, sin autorización para apropiación de la paternidad intelectual del Sistema Vectorial SV.  

---


Este directorio contiene el cierre técnico mínimo y reproducible del carril de visión.

## Alcance real de este bloque

Este código **no** implementa una arquitectura perceptiva fuerte, ni un motor general de visión, ni la totalidad del banco experimental exhaustivo mencionado en el paper.

Su función, más sobria y precisa, es ésta:

1. **regenerar** la portada y las seis figuras publicadas del carril de visión;
2. **comprobar** que la estructura del carril es íntegra;
3. **verificar** que el manuscrito enlaza las imágenes por rutas relativas correctas.

Con ello, el directorio `codigo/` deja de ser solo nominal y pasa a ofrecer una reproducibilidad editorial mínima y una validación estructural útil.

## Archivos de este directorio

- `requisitos.txt`  
  Dependencia mínima necesaria para regenerar los activos visuales.

- `generar_figuras_vision.py`  
  Regenera en `../figuras/` la portada y las seis figuras del carril de visión.

- `validar_estructura_vision.py`  
  Comprueba la integridad del árbol `vision/` y las referencias relativas del manuscrito hacia `../figuras/...`.

## Dependencia mínima

Instale la dependencia con:

```bash
pip install -r requisitos.txt
```

## Uso

### 1. Regenerar portada y figuras

Situado en este directorio:

```bash
python generar_figuras_vision.py
```

### 2. Validar la estructura del carril

```bash
python validar_estructura_vision.py
```

## Resultado esperado

La regeneración debe escribir o sobrescribir estos archivos en `../figuras/`:

- `portada_vision_sv_1200x800.png`
- `fig_01_cadena_visual_captura_admisibilidad_ternarizacion.png`
- `fig_02_banco_visual_n9_render_canonico.png`
- `fig_03_u_visual_oclusion_ambiguedad_reapertura.png`
- `fig_04_suceso_frame_reevaluacion_trayectoria_visual.png`
- `fig_05_carta_r2_r3_auxiliar_no_ontologica.png`
- `fig_06_tres_vallas_carril_vision.png`

La validación debe comprobar además:

- existencia de `vision/README.md`;
- existencia de `manuscrito/paper_sv_vision_pubpub.md`;
- existencia de `meta/NOTA_BLOQUE_1.md`;
- existencia de `meta/NOTA_CIERRE_REPO.md`;
- existencia de las 7 imágenes esperadas;
- y presencia de las rutas relativas `../figuras/...` dentro del manuscrito.

## Nota de consistencia

Los nombres de los scripts ya están en español y no dependen internamente del nombre del archivo de dependencias. Por eso basta con reajustar este `README.md` y sustituir `requirements.txt` por `requisitos.txt`.
