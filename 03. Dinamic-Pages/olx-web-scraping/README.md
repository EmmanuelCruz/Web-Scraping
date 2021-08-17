# Web Scraping OLX con web scraping dinámico
## Emmanuel Cruz Hernández

----

## Descripción

En este ejemplo se extrae información de coches a la venta en la página de [OLX](https://www.olxautos.com.mx/autos_c84) usando la técnica de web scraping dinámico. Para esta extracción se usa _Selenium_.

## Importar

Para esta extracción de datos se importan los módulos siguientes:

        import random
        from time import sleep
        from selenium import webdriver

## Extracción de datos

Para extraer estos datos, es necesario tener descargado el driver del navegador. En este caso, el driver es _chromedriver.exe_. La ruta de su ubicación pasa como parámetro a la creacción del manejo de la página y para obtener una respuesta del servidor nuevamente se utiliza la función _get_, notése que ya no es necesario el uso de encabezados.

        driver = webdriver.Chrome("chromedriver.exe")
        driver.get("https://www.olxautos.com.mx/autos_c84")

Como se está hablando de una extracción dinámica de datos, que depende del botón denominado _Cargar más_, se debe presionar el botón para cargar más datos de la página de manera automatizada. Primero se identifica el botón y se obtiene su referencia en el HTML.

        boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')

Para este ejemplo queremos que ese botón se presione exactamente dos veces. La carga dinámica depende de dos impresiones del botón. Este comportamiento se realiza con un for.

Dentro del ciclo for, se automatiza la carga de datos con un tiempo de espera, ya que pueden ocurrir errores si no se deja pasar cierto tiempo, tales como no haber cargado el botón aún. Una vez esperado cierto tiempo aleatorio (que por cierto, no es fijo para evitar baneos por detención de bots), se presiona el botón para obtener más carga de datos.

        for i in range(2):
            print(f"Primera parte de la página {i}")

            # Dar click y buscar puede lanzar algunas excepciones
            # - Cuando se da click al botón sin que exista
            # - Que haya un cuadro de publicidad sobre el botón
            try:

                # Da click al boton para cargar más elementos
                boton.click()

                # Dormir antes de mostrar los datos mientas se cargan y Randomizar el tiempo de espera entre acciones
                sleep(random.uniform(8.0, 10.0))

                # Redefinir el boton de carga de elementos
                boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
            except:
                break

Finalmente, todos estos datos se obtienen con una expresión _XPATH_, tal cuál como se hacía en los módulos anteriores.

        autos = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

Para finalmente recorrer e imprimir la información esperada (precio e información del coche).

        for auto in autos:
            precio = auto.find_element_by_xpath('.//div[@data-aut-id="itemPrice"]').text
            print(precio)
            descripcion = auto.find_element_by_xpath('.//div[@data-aut-id="itemTitle"]').text
            print(descripcion)

## Ejecutar el proyecto

Basta con invocar

        python olx.py

en consola.

## Recursos necesarios

Instalar Selenium

        pip install selenium

Descargar el driver en la versión correspondiente al navegador y al sistema operativo. Se puede descargar [aquí](https://selenium-python.readthedocs.io/installation.html#drivers)