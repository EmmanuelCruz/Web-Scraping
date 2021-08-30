# Descarga automática de archivos con Web Scraping
## Emmanuel Cruz Hernández

----

## Descripción

Extraccción de archivos de una página con archivos de ejemplo llamada [File Examples](https://file-examples.com/index.php/sample-documents-download/sample-doc-download/), en este caso, archivos con extensión _DOC_.

## Módulos necesarios

        import requests
        from bs4 import BeautifulSoup

----

## Extracción de datos

En realidad es más fácil de lo que parece, primero se define la URL semilla de la que se van a extraer los datos, así como inicializar la sopa (llamaré así al ejemplar de _Beautiful Soup_ que permite la extracción de datos desde el HTML de la URL semilla).

        url = 'https://file-examples.com/index.php/sample-documents-download/sample-doc-download/'

        response = requests.get(url)
        soup = BeautifulSoup(response.text, features="lxml")

Como el mismo caso de las imágenes, los archivos también están asociados a una URL que corresponde al archivo. En particular, para este caso, se encuentran en el atributo _ref_ de cada etiqueta _a_. Cada uno de estos los almacenamos en una lista de URL's.

        urls = []

        files = soup.find_all('a', class_="download-button")

        # Obtener las url's de los archivos
        for file in files:
            urls.append(file['href'])

Una vez extraídas las URL, procedemos a realizar la petición a estas a través de un request y un _GET_ hacia el recurso. Una vez teniendo los datos, sólo es cuestión de escribirlos en un archivo.

        # Hacer el requerimiento de descarga de los archivos
        i = 0
        for url in urls:
            response_file = requests.get(url, allow_redirects=True)

            file_name = f'./archivos/file{i}.doc'
            i+=1

            out = open(file_name, 'wb')
            out.write(response_file.content)
            out.close()

## Instalación de los recursos necesarios

        pip install requests
        
		pip install beautifulsoup4