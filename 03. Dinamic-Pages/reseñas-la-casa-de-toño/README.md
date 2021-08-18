# Web Scraping a reseñas de _La casa de Toño_ con web scraping dinámico
## Emmanuel Cruz Hernández

----

## Descripción

En este ejemplo se extrae información de reseñas de [La casa de toño, sucursal Cuajimalpa](https://www.google.com.mx/maps/place/La+Casa+de+To%C3%B1o/@19.3460137,-99.2731642,12z/data=!4m11!1m2!2m1!1sla+casa+de+to%C3%B1o!3m7!1s0x0:0x3466b88c477ff25c!8m2!3d19.3643183!4d-99.2872466!9m1!1b1!15sChBsYSBjYXNhIGRlIHRvw7FvIgOIAQFaEiIQbGEgY2FzYSBkZSB0b8Oxb5IBEm1leGljYW5fcmVzdGF1cmFudA?hl=es) desde Google Maps, usando la técnica de web scraping dinámico. Para esta extracción se usa _Selenium_.

## Importar

Para esta extracción de datos se importan los módulos siguientes:

                import random
                from time import sleep
                from selenium import webdriver
                from selenium.webdriver.common.by import By
                from selenium.webdriver.chrome.options import Options

## Extracción de datos

Para extraer estos datos, es necesario tener descargado el driver del navegador. En este caso, el driver es _chromedriver.exe_. La ruta de su ubicación pasa como parámetro a la creacción del manejo de la página y para obtener una respuesta del servidor nuevamente se utiliza la función _get_. Nótese que con el parámetro _options_, se puede agregar un encabezado a la extracción de datos.

                opts = Options()
                opts.add_argument(
                        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
                )

                driver = webdriver.Chrome("chromedriver.exe", options=opts)
                driver.get('https://www.google.com.mx/maps/place/La+Casa+de+To%C3%B1o/@19.3460137,-99.2731642,12z/data=!4m11!1m2!2m1!1sla+casa+de+to%C3%B1o!3m7!1s0x0:0x3466b88c477ff25c!8m2!3d19.3643183!4d-99.2872466!9m1!1b1!15sChBsYSBjYXNhIGRlIHRvw7FvIgOIAQFaEiIQbGEgY2FzYSBkZSB0b8Oxb5IBEm1leGljYW5fcmVzdGF1cmFudA?hl=es')


Para realizar la carga dinámica de datos, se define con una expresión en JavaScript el comportamiento. La función que permite hacer el scroll con Js es tal cual _scroll_. Esta función estará asociada al cuadro donde se encuentran todas las reseñas. Se carga con un número grande para que pueda tomar en cuenta la cantidad de pixeles necesarios para realizar el scroll.

                scrolling_script = """
                        document.getElementsByClassName('section-layout section-scrollbox cYB2Ge-oHo7ed cYB2Ge-ti6hGc')[0].scroll(0, 100000)
                """

Para este ejemplo se hicieron 2 scrolls para cargar información antes de extraerla. El manejo de la cantidad de scrolls está controlado por un while y su condición de término.

                SCROLLS = 0
                while SCROLLS!=2:
                # Se realiza el scroll
                driver.execute_script(scrolling_script)

                # Esperar antes de realizar la acción
                sleep(random.uniform(7.0, 13.0))

                # Se aumenta la cantidad de scrolls actuales
                SCROLLS += 1

                        for auto in autos:
                        precio = auto.find_element_by_xpath('.//div[@data-aut-id="itemPrice"]').text
                        print(precio)
                        descripcion = auto.find_element_by_xpath('.//div[@data-aut-id="itemTitle"]').text
                        print(descripcion)

Finalmente, una vez que están cargados los datos necesarios, basta con recorrer la lista de elementos y extraer la información que es de nuestro interes. En este caso, lo que nos interesa de las reseñas son el nombre de usuario, el tiempo que tiene la reseña y el contenido de la reseña del restaurante.

                restaurant_review = driver.find_elements(By.XPATH, '//div[@jstcache="435"]')

                print(f"Elementos encontrados: {len(restaurant_review)}")

                for review in restaurant_review:

                        client = review.find_element_by_xpath('.//span[@jstcache="408"]').text
                        tiempo = review.find_element_by_xpath('.//span[@jstcache="242"]').text
                        resena = review.find_element_by_xpath('.//span[@jstcache="246"]').text

                        print(f"""
                                Nombre: {client}
                                Fecha: {tiempo}
                                Reseña:
                                {resena}
                        """)

## Ejecutar el proyecto

Basta con invocar

        python casa_de_tono.py

en consola.

## Recursos necesarios

Instalar Selenium

        pip install selenium

Descargar el driver en la versión correspondiente al navegador y al sistema operativo. Se puede descargar [aquí](https://selenium-python.readthedocs.io/installation.html#drivers)