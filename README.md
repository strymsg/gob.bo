---
configs:
- config_name: default
  data_files:
  - split: train
    path:
    - "data/gobbo_tramites_pre.csv"
    - "data/2025-03-25_tramites_gobbo.raw.csv"
  default: true
  sep: ","

language:
- es
pretty_name: "Trámites Portal único de trámites de Bolivia gob.bo obtenidos por scraping."
tags:
- public
- procedures
- gobierno
- trámites
- información pública
license: "cc-by-4.0"
---

# Conjunto de datos del portal único de trámites de Bolivia (gob.bo)

Archivos generados a partir de aplicar we scraping y guardados como archivos `csv` en:

- `data/gobbo_tramites_pre.csv` (Datos pre procesados con `[notebooks/gobbo-pre.ipynb](notebooks/gobbo-pre.ipynb)`) 
- `data/2025-03-25_tramites_gobbo.raw.csv` (Datos en bruto)

Licencia: Creative Commons Attribution 4.0

## Extractor de datos plataforma gob.bo (scraping)

Extrae los trámites del portal de trámites gob.bo.

### Instalación

Se debería poder instalar con pipenv, una vez clonado el repositorio

1. `pipenv shell`
2. `pipenv install`
3. Puede que playwright pida descargar chromium, seguir las instrucciones que aparezcan en la consola.

### Ejecución

Una vez activado el entorno virtual: `python main.py`.
