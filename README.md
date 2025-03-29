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

Archivos generados a partir de aplicar web scraping y guardados como archivos `csv` en:

- [gobbo_tramites_pre.csv](data/gobbo_tramites_pre.csv)` (Datos pre procesados con [notebooks/gobbo-pre.ipynb](notebooks/gobbo-pre.ipynb)) 
- [2025-03-25_tramites_gobbo.raw.csv](data/2025-03-25_tramites_gobbo.raw.csv) (Datos en bruto)

Licencia: Creative Commons Attribution 4.0

## Diccionario de datos

Del archivo [data/gobbo_tramites_pre.csv](data/gobbo_tramites_pre.csv).

| Columna              | Descripción                                                                | Tipo   |
|----------------------|----------------------------------------------------------------------------|--------|
| titulo               | Título del trámite.                                                        | string |
| institucion          | Institución estatal encargada del trámite.                                 | string |
| descripcion          | Descripción del trámite.                                                   | string |
| contacto             | Email de contacto.                                                         | string |
| web                  | Sitio web de la institución encargada del trámite.                         | string |
| es_presencial        | 1 si el trámite se hace de forma presencial.                               | int    |
| es_en_linea          | 1 si el trámite se hace en línea.                                          | int    |
| requisitos           | Lista de requisitos mostrados para este trámite.                           | string |
| procedimiento        | Procedimiento para el trámite.                                             | string |
| num_ubicaciones      | Número de ubicaciones físicas para realizar el trámite.                    | int    |
| ubicaciones          | Ubicaciones o direcciones físicas para realizar el trámite.                | string |
| info_adicional       | Texto con información adicional mostrado para el trámite.                  | string |
| ultima_actualización | Fecha en la que se hizo la última actualización. Formato DD-MM-AAAA hh:mm. | string |
| observaciones        | Texto con observaciones mostradas para el trámite.                         | string |
| costo_descripcion    | Descripción completa mostrada en la sección de costos del trámite.         | string |
| costo_montos         | Montos + Monedas mostrados en el portal en la sección de costos.           | string |
| costo_forma          | Forma de pago mostrada en la sección de costos.                            | string |
| costo_conceptos      | Concepto de pago mostrado en la sección de costos.                         | string |
| costo_ctas_bancarias | Números de cuentas bancarias mostrados en la sección de costos.            | string |
| calificación         | Valoración promedia hecha al trámite.                                      | string |
| url                  | URL para acceder al trámite.                                               | string |
| categoria            | Clasificación categórica del trámite.                                      | string |
| duracion             | Tiempo de duración mostrado.                                               | string |
| marco_legal          | Ley, Decreto o documento legal que respalda al trámite.                    | string |
| costo_bancos         | Nombre de bancos mostrados en la sección de costos.                        | sring  |
| horarios_atencion    | Horarios de atención para el trámite en formato Hora inicio : Hora Fin.    | string |

## Extractor de datos plataforma gob.bo (scraping)

Extrae los trámites del portal de trámites gob.bo.

### Instalación

Se debería poder instalar con pipenv, una vez clonado el repositorio

1. `pipenv shell`
2. `pipenv install`
3. Puede que playwright pida descargar chromium, seguir las instrucciones que aparezcan en la consola.

### Ejecución

Una vez activado el entorno virtual: `python main.py`.
