# challenge-zinobe

|  Region | City Name |  Languaje | Time  |
|---|---|---|---|
|  Africa | Angola  |  AF4F4762F9BD3F0F4A10CAF5B6E63DC4CE543724 | 0.23 ms  |
|   |   |   |   |
|   |   |   |   |


Aplicacion en Python 3 que genere la tabla anterior en consola, calcula el tiempo total, promedio, mínimo y máximo que le toma generar cada fila.

# Modelo de Datos

![entrada](https://github.com/edwargl7/challenge-zinobe/blob/develop/docs/images/Challenge%20zinobe.png)

[Modelo de Datos](https://github.com/edwargl7/challenge-zinobe/blob/develop/docs/images/Challenge%20zinobe.png)

# Especificaciones Técnicas

## Tecnologías Implementadas y Versiones

Este proyecto está desarrollado en el lenguaje Python versión 3.8 y como motor de base de datos
SQLite.

* [Python 3](https://www.python.org/downloads/release/python-380/) 3.8.7
* [Pandas](https://pandas.pydata.org/) 1.2.2
* [SQLite 3](https://www.sqlite.org/index.html) 3

## Variables de Entorno

Puede crear un archivo .env con las siguientes variables:

```bash
HOST_REGION_API=[Host del API de regiones]
TOKEN_REGION_API=[token o API KEY del API de regiones]
URL_REGION_API=[URL del API de regiones]
URL_COUNTRY_API=[URL del API de países]
DATABASE_NAME=[nombre de la base de datos]
```

## Instalación

```bash
# Clonar el proyecto,  rama master - main
git clone https://github.com/edwargl7/challenge-zinobe

# Rama develop
git clone -b development https://github.com/edwargl7/challenge-zinobe

# Moverse a la carpeta del proyecto
cd challenge-zinobe

# Instale los requerimientos
pip3 install -r requirements.txt

# Configure las variables de entorno y ejecute
python3 main.py
```
