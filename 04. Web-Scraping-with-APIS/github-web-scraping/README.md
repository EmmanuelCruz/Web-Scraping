# Extracción de datos de GitHub con su API
## Emmanuel Cruz Hernández

----

## Descripción

GitHub cuenta con un sistema de API para la extracción de datos. La documentación del _endpoint_ para el uso de la API se encuentra [aquí](https://docs.github.com/en/rest).

Por otro lado, cada endpoint API de GitHub que utiliza BASIC OUTH se puede encontrar en la
siguiente URL: [https://api.github.com/](https://api.github.com/).

----

## Módulos necesarios

        import requests
        import json

## Extracción de datos

El API de extracción de datos de GitHub está basado en un API definida por la propia plataforma. Permite extraer información como el nombre de repositorios, url's, lenguaje de programación más usado, etc.

En este caso no es necesario tener headers porque la información la provee GitHub, pero no está de más definirlos para hacer un mejor trabajo.

        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
        }

El _endpoint_ es el punto de comienzo de la extracción de datos, la cuál se obtiene desde el API de GitHub.

        endpoint = "https://api.github.com/user/repos?page=1"

Posteriomente se define el usuario, contraseña y la petición

        usuario = 'Aquí va usuario GitHub'
        password = open('./password.txt').readline().strip()

        response = requests.get(endpoint, headers=headers, auth=(usuario, password))

Transformación a formato JSON

    repositorios = response.json()

Se recorre el JSON y se imprime cada uno de los nombres de los repositorios

        for repo in repositorios:
            print(repo['name'])