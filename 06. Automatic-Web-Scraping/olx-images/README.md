# Web scraping de imágenes
## Emmanuel Cruz Hernández

----

## Descripción

Extracción de datos de [OLXAutos](https://www.olxautos.com.mx/autos_c84) para obtener las imágenes de los coches en venta. Se hace una combinación de web scraping dinánico para poder obtener acceso a la página y comportamiento dentro del servidor y request para la obtención de las imágenes.

## Módulos necesarios

        from os import path
        import requests
        from PIL import Image
        import io
        import random
        from time import sleep
        from selenium import webdriver

----

## Extracción de datos

Este ejemplo está basado en la extracción de datos a [OLX vista en web scraping dinámico](https://github.com/EmmanuelCruz/Web-Scraping/tree/master/03.%20Dinamic-Pages/olx-web-scraping)

Las líneas que se agregaron son las siguientes:

Se hace scroll por 5 segundo hacia arriba y hacia abajo dentro de la página para la carga de imágenes

        # Realiza Scroll
        driver.execute_script("window.scrollTo({top:0, behavior: 'smooth'});")
        sleep(5)
        driver.execute_script("window.scrollTo({top:20000, behavior: 'smooth'});")
        sleep(5)

Dentro de cada div de los autos, se encuentra una imagen, a la cual se accede por una expresión XPATH. La URL de cada imagen se encuentra en particular en cada atributo llamado _src_, el cual se obtiene y hace un requerimiento al servidor para el acceso a la imagen.

Portesiormente, la imagen que se regresa en forma de bytes es tranformada a una imagen con los formatos requeritos, que en este caso, es una imagen con extensión JPG y calidad del 70%.

        # Extracción de imagen

        url_image = auto.find_element_by_xpath('.//img').get_attribute('src')
        image_content = requests.get(url_image).content

        image_file = io.BytesIO(image_content)
        imagen = Image.open(image_file).convert('RGB')

        path = './images/' + str(img_num) + ".jpg"

        with open(path, 'wb') as f:
            imagen.save(f, "JPEG", quality = 70)

        img_num += 1

Todas las imágenes son almacenadas en el directorio _images_.