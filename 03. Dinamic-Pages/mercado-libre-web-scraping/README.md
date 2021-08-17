# Web Scraping Horizontal y Vertical a Mercado Libre con web scraping dinámico
## Emmanuel Cruz Hernández

----

## Descripción

En este ejemplo se extrae información de [mercado libre](https://autos.mercadolibre.com.mx/refacciones-autos-camionetas/) usando la técnica de web scraping dinámico. Para esta extracción se usa _Selenium_.

## Importar

Para esta extracción de datos se importan los módulos siguientes:

        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.chrome.options import Options

## Extracción de datos

Para extraer estos datos, es necesario tener descargado el driver del navegador. En este caso, el driver es _chromedriver.exe_. La ruta de su ubicación pasa como parámetro a la creacción del manejo de la página y para obtener una respuesta del servidor nuevamente se utiliza la función _get_. Para este ejemplo, se hace uso de un encabezado para asegurar la extracción de datos automatizada.

        opts = Options()
        opts.add_argument(
            "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
        )

        driver = webdriver.Chrome("chromedriver.exe", chrome_options=opts)

Para realizar web Scraping vertical, se debe acceder a cada uno de los links de los productos por medio de un click para redireccionar la página y ubicar al driver en el nivel actual de la extracción de datos.

        while(True):
            links_products = driver.find_elements(By.XPATH, '//a[@class="ui-search-link"]')
            url_list = []

            for tag_a in links_products:
                url_list.append(tag_a.get_attribute("href"))

            # Web Scraping vertical

            for link in url_list:
                try:
                    driver.get(link)

                    # Extracción de la página
                    titulo = driver.find_element_by_xpath('//h1').text
                    precio = driver.find_element_by_xpath('//span[@class="price-tag-fraction"]').text

                    print(titulo)
                    print(precio)

                    driver.back()
                except Exception as e:
                    driver.back()
                    print(e)
                
                try:
                    boton_next = driver.find_element(By.XPATH, '//span[text()="Siguiente"]')
                    boton_next.click()
                except:
                    print("Ya no hay más páginas por recorrer")
                    break

Este comportamiento se estará realizando siempre y cuando no ocurra un problema con la extracción de datos, o que ya no haya más páginas co el botón _Siguiente_ por visitar, es decir terminar la extracción de datos hasta la última página.

## Nota importante
El trabajo que realizar _Seleium_ es más pesdo al realizar varias peticiones al servidor, por lo que la extracción de datos se puede volver muy lenta.

## Ejecutar el proyecto

Basta con invocar

        python mercado-libre-web-scraping.py

en consola.

## Recursos necesarios

Instalar Selenium

        pip install selenium

Descargar el driver en la versión correspondiente al navegador y al sistema operativo. Se puede descargar [aquí](https://selenium-python.readthedocs.io/installation.html#drivers)