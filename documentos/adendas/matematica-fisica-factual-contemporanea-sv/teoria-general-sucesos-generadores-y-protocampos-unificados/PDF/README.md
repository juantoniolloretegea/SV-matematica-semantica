# PDF firmado — Versión canónica V.1 

Esta carpeta contiene la **versión PDF firmada y verificable** de la publicación canónica:

> *Teoría general de sucesos generadores y de los protocampos unificados en el Sistema Vectorial SV* (V.1)

junto con la prueba criptográfica de fecha cierta (OpenTimestamps → blockchain Bitcoin) y los hashes canónicos.

---

## Identificación canónica

| Campo | Valor |
|---|---|
| **Título canónico (es)** | Teoría general de sucesos generadores y de los protocampos unificados en el Sistema Vectorial SV |
| **Título inglés (operativo)** | General theory of generating events and unified protofields in the Sistema Vectorial SV |
| **Autor** | Juan Antonio Lloret Egea |
| **ORCID** | [0000-0002-6634-3351](https://orcid.org/0000-0002-6634-3351) |
| **Institución** | ITVIA — Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español |
| **ISSN** | 2695-6411 |
| **Licencia** | [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) |
| **Fecha canónica** | 26 de abril de 2026 (Madrid) |
| **Versión** | V.1 (versión canónica publicada) |

---

## Contenido de esta carpeta

| Fichero | Función | Tamaño |
|---|---|---:|
| `General theory ... Sistema Vectorial SV.pdf` | Documento canónico firmado digitalmente | 2 397 618 B |
| `General theory ... Sistema Vectorial SV.pdf.ots` | Prueba OpenTimestamps anclada en blockchain Bitcoin | 514 B |
| `Hash SHA-256.md` | Hashes canónicos para verificación rápida | — |
| `README.md` | Este documento | — |

---

## Hashes SHA-256 canónicos

### PDF firmado (documento canónico)

```
c89a07102648ce2b3da7a39158db6845e5312f465faa7a321ccc75bbc8606912
```

### Prueba OpenTimestamps

```
c94e063cf8539d9e0fd9103e2735ad33c659f88c356efa517b216d2cb5c3818a
```

---

## Pruebas de autenticidad

<<<<<<< HEAD
El documento V.1 dispone de **cinco capas probatorias independientes**, ancladas a cinco infraestructuras distintas (Internet Archive, FNMT-RCM, OpenTimestamps/Bitcoin, GitHub/Git, Knowledge Commons/HCommons):
=======
El documento V.1 dispone de **cuatro capas probatorias independientes**, ancladas a cuatro infraestructuras distintas (Internet Archive, FNMT-RCM, OpenTimestamps/Bitcoin, GitHub/Git):
>>>>>>> 94f2b75c845c8753b0c70e6179e369ce30188762

### Capa 0 — Archivado público anterior a la firma (Wayback Machine / Internet Archive)

Cuatro snapshots del corpus archivados públicamente en [Internet Archive](https://archive.org) **antes** de la firma del PDF. Demuestran que el contenido canónico existía y era accesible públicamente con anterioridad a cualquier acto de firma. Los snapshots de Wayback Machine tienen valor probatorio reconocido en jurisdicciones nacionales e internacionales para acreditación de fecha cierta de contenido digital.

| Snapshot | Recurso archivado | Fecha (UTC) |
|---|---|---|
| `web/20260427101149` | [Documento canónico íntegro (`.md`)](https://web.archive.org/web/20260427101149/https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-general-sucesos-generadores-y-protocampos-unificados/teoria-general-sucesos-generadores-protocampos-unificados-sv.md) | 27/04/2026 10:11:49 |
| `web/20260426220748` | [Carpeta de Laboratorios canónicos](https://web.archive.org/web/20260426220748/https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-general-sucesos-generadores-y-protocampos-unificados/laboratorios) | 26/04/2026 22:07:48 |
| `web/20260426220045` | [Carpeta del conjunto canónico](https://web.archive.org/web/20260426220045/https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-general-sucesos-generadores-y-protocampos-unificados) | 26/04/2026 22:00:45 |
| `web/20260427101536` | [Repositorio del autor](https://web.archive.org/web/20260427101536/https://github.com/juantoniolloretegea) | 27/04/2026 10:15:36 |

### Capa 1 — Firma digital criptográfica (FNMT-RCM)

El PDF está **triplemente firmado** con el certificado oficial del autor emitido por la **FNMT-RCM** (Fábrica Nacional de Moneda y Timbre — Real Casa de la Moneda), Autoridad de Certificación cualificada española bajo Reglamento eIDAS UE 910/2014.

**Certificado del firmante**:

| Campo | Valor |
|---|---|
| Titular | LLORET EGEA JUAN ANTONIO |
| Identificador | IDCES-52813010L |
| Emisor | AC FNMT Usuarios |
| Vigencia | 08/08/2025 → 08/08/2029 |

**Cadena de certificación** (validada y embebida en el PDF):

```
AC RAIZ FNMT-RCM (raíz cualificada eIDAS, vigente hasta 2030-01-01)
  └── AC FNMT Usuarios (vigente hasta 2029-10-28)
        └── LLORET EGEA JUAN ANTONIO - 52813010L (vigente hasta 2029-08-08)
```

**Firmas presentes en el PDF**:

| Firma | Timestamp | Formato técnico | Fuente |
|---|---|---|---|
| #1 | 27/04/2026 19:18:13 +02:00 | CMS clásico (`adbe.pkcs7.detached`) | Microsoft Word 2021 |
| #2 | 27/04/2026 19:19:07 +02:00 | CMS clásico (`adbe.pkcs7.detached`) | Microsoft Word 2021 |
| #3 | 27/04/2026 19:40:53 +02:00 | **PAdES-BES** (`ETSI.CAdES.detached`) | Autofirma 1.9 |

Cualquier modificación posterior del fichero rompe la cadena de firmas y se detecta automáticamente al validarlo en cualquier visor compatible con PAdES (Adobe Acrobat Reader, Foxit, etc.).

### Capa 2 — Sello de tiempo en blockchain (OpenTimestamps → Bitcoin)

El fichero `.pdf.ots` contiene la prueba criptográfica de que el SHA-256 del PDF fue registrado en el calendario público de OpenTimestamps el **27 de abril de 2026 a las ~17:49 UTC** (~19:49 hora de Madrid). El hash queda anclado en blockchain Bitcoin de forma permanente, descentralizada y verificable por cualquier tercero independientemente de cualquier autoridad.

Esta capa, combinada con la Capa 0, demuestra que el documento **existía con este SHA-256 exacto antes de cualquier depósito posterior** en repositorios académicos (HCommons, Zenodo, engrXiv, ResearchGate, etc.).

### Capa 3 — Commit Git público (GitHub)

El commit Git con el que se depositó esta versión canónica genera un hash de commit propio (`58cec49`) y un timestamp del servidor de GitHub, ambos inmutables y públicamente verificables. Constituye una prueba adicional de fecha cierta independiente de las anteriores, soportada por la infraestructura de Git y por GitHub.
<<<<<<< HEAD

### Capa 4 — DOI académico canónico (Knowledge Commons / HCommons)

La publicación está depositada en [Knowledge Commons Works](https://works.hcommons.org/records/177nb-v2465) con DOI canónico **[10.17613/177nb-v2465](https://doi.org/10.17613/177nb-v2465)**. HCommons es una plataforma académica abierta soportada por la National Science Foundation (Grant OAC-2226271) y operada bajo la infraestructura InvenioRDM con la Michigan State University y National Endowment for the Humanities.

El depósito incluye los cuatro ficheros canónicos (PDF firmado, prueba OpenTimestamps, Hash SHA-256.md, README.md) y se ha verificado que el SHA-256 del PDF servido por HCommons coincide bit a bit con el original, confirmando que el repositorio no altera el documento.
=======
>>>>>>> 94f2b75c845c8753b0c70e6179e369ce30188762

---

## Verificación

### Comprobar SHA-256 del PDF

**Linux / macOS**:
```bash
sha256sum "General theory of generating events and unified protofields in the Sistema Vectorial SV.pdf"
```

**Windows (PowerShell)**:
```powershell
Get-FileHash "General theory of generating events and unified protofields in the Sistema Vectorial SV.pdf" -Algorithm SHA256
```

El resultado debe coincidir exactamente con:
```
c89a07102648ce2b3da7a39158db6845e5312f465faa7a321ccc75bbc8606912
```

### Verificar las firmas digitales

1. **Adobe Acrobat Reader** (recomendado): abrir el PDF y consultar el panel **Firmas** (icono de pluma a la izquierda). Mostrará las tres firmas con su certificado, vigencia y validez.
2. **Foxit Reader / PDF-XChange / cualquier visor PAdES**: equivalente.
3. **Línea de comandos** (para usuarios técnicos):
   ```bash
   pdfsig "General theory ... .pdf"
   ```

### Verificar el timestamp OpenTimestamps

**En navegador** (sin instalación):
1. Ir a [https://opentimestamps.org](https://opentimestamps.org) → STAMP & VERIFY.
2. Subir el PDF y el fichero `.ots` juntos.
3. El sistema verificará la prueba contra el calendario y, si está confirmada en blockchain, contra Bitcoin.

**Línea de comandos** (cliente oficial):
```bash
pip install opentimestamps-client
ots verify "General theory ... .pdf.ots"
```

> **Nota**: la confirmación definitiva en blockchain Bitcoin tarda entre 3 y 6 horas tras el sellado inicial. Una vez confirmada, la prueba es verificable indefinidamente y resistente a cualquier manipulación.

### Verificar los snapshots de Wayback Machine

Acceder a cualquiera de las cuatro URLs `web.archive.org/web/<timestamp>/...` listadas en la Capa 0. Internet Archive mostrará el snapshot correspondiente con su fecha de captura como texto fijo en la cabecera. Los snapshots no son alterables a posteriori por terceros.

---

## Cláusula de prevalencia / Prevalence clause

En caso de cualquier discrepancia, ambigüedad o divergencia interpretativa entre la versión española de la presente publicación y cualquier traducción a otro idioma — incluidas las traducciones automáticas — prevalece sin excepción la versión española de Lloret Egea (Madrid, ITVIA), que constituye el único original canónico del corpus del Sistema Vectorial SV protegido por CEDRO. Las traducciones a otros idiomas tienen carácter exclusivamente operativo y no canónico.

In the event of any discrepancy, ambiguity or interpretive divergence between the Spanish version of this publication and any translation into another language — including automatic translations — the Spanish version by Lloret Egea (Madrid, ITVIA) prevails without exception, as the sole canonical original of the Sistema Vectorial SV corpus protected under CEDRO. Translations into other languages have operational character only and are not canonical.

---

## Advertencia / Warning

**Advertencia**: Esta publicación está protegida por CEDRO y su aplicación en el campo de la Física, así como cualquier forma de explotación, reproducción o uso por parte de empresas, queda sujeta al copyright del autor y a los términos de la licencia indicada; la reproducción, distribución, comunicación pública o transformación de esta obra sólo puede ser realizada con la autorización de sus titulares, salvo excepción prevista por la ley, y cualquier uso comercial sin autorización expresa queda prohibido y estrictamente supeditado al licenciamiento permitido.

**Warning**: This publication is protected by CEDRO. Its application in the field of Physics, as well as any form of exploitation, reproduction, or use by corporate entities, is strictly subject to the author's copyright and the terms of the license indicated; any reproduction, distribution, public communication, or transformation of this work requires authorization from the rightsholders, except as provided by law, and any commercial use without express written consent is prohibited and strictly subject to permitted licensing.

---

## Depósitos canónicos

| Repositorio | Estado | DOI |
|---|---|---|
| **GitHub** (esta sede canónica del PDF) | ✓ Depositado | — |
| **Wayback Machine / Internet Archive** | ✓ Cuatro snapshots (Capa 0) | — |
| **OpenTimestamps / Bitcoin blockchain** | ✓ Anclado (Capa 2) | — |
<<<<<<< HEAD
| **HCommons** ([works.hcommons.org](https://works.hcommons.org/records/177nb-v2465)) | ✓ Depositado (Capa 4) | [10.17613/177nb-v2465](https://doi.org/10.17613/177nb-v2465) |
=======
| HCommons (works.hcommons.org) | *Pendiente de depósito* | *Pendiente* |
>>>>>>> 94f2b75c845c8753b0c70e6179e369ce30188762
| Zenodo | *Pendiente* | *Pendiente* |
| engrXiv | *Pendiente* | *Pendiente* |
| ResearchGate | *Pendiente* | — |

---

## Sede canónica del corpus

- **Sede canónica de la publicación (.md íntegro)**: [GitHub — teoria-general-sucesos-generadores-protocampos-unificados-sv.md](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-general-sucesos-generadores-y-protocampos-unificados/teoria-general-sucesos-generadores-protocampos-unificados-sv.md)
- **Sede canónica del conjunto**: [GitHub — teoria-general-sucesos-generadores-y-protocampos-unificados/](https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-general-sucesos-generadores-y-protocampos-unificados)
- **Colección**: [Matemática y Física Factual contemporánea del SV](https://www.itvia.online/matematica-y-fisica-factual-contemporanea-del-sv)

---

© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados.
ITVIA · IA eñ™ — La Biblia de la IA™ · ISSN 2695-6411 · Licencia CC BY-NC-ND 4.0
Madrid, 26 de abril de 2026
