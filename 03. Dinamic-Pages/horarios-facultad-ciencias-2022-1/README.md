# Web Scraping Vertical para extraer los cursos, profesores y ayudantes de la _Facultad de Ciencias, UNAM_.
## Emmanuel Cruz Hernández

----

## Descripción

En este ejemplo se extrae información de profesores y ayudantes de la [Facultad de Ciencias](http://www.fciencias.unam.mx/docencia/horarios/indiceplan/20221/1556) usando la técnica de web scraping dinámico. Para esta extracción se usa _Selenium_.

Cabe mencionar que la extracción de datos se pudo realizar sin problema con Scrapy, sin embargo, lo hice con _Selenium_ para que el manejo automatizado del programa con la página web fuera gráfica.

## Importar

Para esta extracción de datos se importan los módulos siguientes:

        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options

## Extracción de datos

Para extraer estos datos, es necesario tener descargado el driver del navegador. En este caso, el driver es _chromedriver.exe_. La ruta de su ubicación pasa como parámetro a la creacción del manejo de la página y para obtener una respuesta del servidor nuevamente se utiliza la función _get_. Para este ejemplo, se hace uso de un encabezado para asegurar la extracción de datos automatizada.

        # Para agregar un encabezado
        opts = Options()
        opts.add_argument(
            "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
        )

        driver = webdriver.Chrome("../chromedriver.exe", options=opts)

Lo primero que se hace es tomar una lista que todos los cursos de Ciencias de la Computación, tanto obligatorias como optavas, y obtener cada uno de los links de ingreso a partir de la petición desde la URL semilla.

        driver.get('http://www.fciencias.unam.mx/docencia/horarios/indiceplan/20221/1556')

        links_courses = driver.find_elements_by_xpath('//div[@id="info-contenido"]//a')
        url_list = []

        for tag_a in links_courses:
            url_list.append(tag_a.get_attribute("href"))

Para el web scraping vertical, se accede a cada una de las URL's que contiene cada uno de los cursos con la función _get_. A partir de cada URL se obtiene el nombre de la materia de la cuál se va a extraer la información, en este caso el título.

Para obtener a profesores y ayudantes, vemos que cada elemento se encuentra en una estructura de lista en el HTML. Cada nombre se encuentra dentro de una etiqueta para referencias (_a_). Para curso lo que se obtiene es el nombre del profesor y el nombre de los ayudantes. Sabemos que el primer nombre de la lista (en la mayoría de los casos) corresponde al nombre del profesor, por lo que tenemos un contados para obtener este nombre y después enlistar a los ayudantes del mismo curso.

        # Web Scraping vertical
        for link in url_list:
            try:
                driver.get(link)

                materia = driver.find_element_by_xpath('//div[@id="info-contenido"]//h2').text

                print(f"Materia {materia}".upper())

                # Extracción de la página
                cursos = driver.find_elements_by_xpath('//div[@id="info-contenido"]/table')
                
                for curso in cursos:
                    profes = curso.find_elements_by_xpath('.//a')

                    counter = 0

                    for profe in profes:
                        if counter == 0 and profe.text!="":
                            print(f"Profesor: {profe.text}")
                        elif profe.text!="":
                            print(f"Ayudante: {profe.text}")
                        counter += 1
                    
                    print("\n")
                
                print("\n")

                driver.back()
            except Exception as e:
                driver.back()
                print(e)


## Ejecutar el proyecto

Basta con invocar

        python facultad_ciencias.py

en consola.

## Recursos necesarios

Instalar Selenium

        pip install selenium

Descargar el driver en la versión correspondiente al navegador y al sistema operativo. Se puede descargar [aquí](https://selenium-python.readthedocs.io/installation.html#drivers)