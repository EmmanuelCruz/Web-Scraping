# Web Scraping Vertical en Amazon
## Emmanuel Cruz Hernández

----

## Descripción

En este ejemplo se extrae información de las ofertas del día de [Amazon](https://www.amazon.com/-/es/international-sales-offers/b/?ie=UTF8&node=15529609011&ref_=nav_cs_gb_intl_52df97a2eee74206a8343034e85cd058&nocache=1630981248280) usando la técnica de web scraping dinámico. Para esta extracción se usa _Selenium_.

## Importar

Para esta extracción de datos se importan los módulos siguientes:

        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.chrome.options import Options

## Extracción de datos

Definidmos el user agent para especificar navegador y equipo de cómputo específico para la extracción de datos, así como el driver para manejar Selenium y controlar el navegador.

        # Para agregar un encabezado
        opts = Options()
        opts.add_argument(
            "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
        )

        driver = webdriver.Chrome("../chromedriver.exe", options=opts)

Definimos la URL semilla

        # Se obtiene la página de la URL semilla
        driver.get('https://www.amazon.com/-/es/international-sales-offers/b/?ie=UTF8&node=15529609011&ref_=nav_cs_gb_intl_52df97a2eee74206a8343034e85cd058&nocache=1630981248280')

Otenemos el listado de productos de la página de ofertas del día de Amazon. De este listado, obtenemos cada url de los productos

        links_products = driver.find_elements(By.XPATH, '//div[contains(@class, "tallCellView")]//a[@class="a-link-normal"]')
        urls_list = []

        # Se obtienen las URLS
        for tag in links_products:
            urls_list.append(tag.get_attribute("href"))

Por cada producto, se extrae el nombre, su precio con oferta del día y el ahorro respecto a su precio original

        # Web scraping vertical
        for link in urls_list:

            try:
                driver.get(link)

                # Extracción de la página
                nombre = driver.find_element_by_xpath('//h1/span').text
                precio_del_dia = driver.find_element_by_xpath('//span[@id="priceblock_dealprice"]').text
                ahorro = driver.find_element_by_xpath('//td[contains(@class, "priceBlockSavingsString")]').text

                print(f"Nomre: {nombre}")
                print(f"Precio: {precio_del_dia}")
                print(f"Ahorro: {ahorro}")
                print()

                driver.back()
            except Exception as e:
                driver.back()


## Nota importante
El trabajo que realizar _Seleium_ es más pesdo al realizar varias peticiones al servidor, por lo que la extracción de datos se puede volver muy lenta.

## Ejecutar el proyecto

Basta con invocar

        python amazon.py

en consola.

## Recursos necesarios

Instalar Selenium

        pip install selenium

Descargar el driver en la versión correspondiente al navegador y al sistema operativo. Se puede descargar [aquí](https://selenium-python.readthedocs.io/installation.html#drivers)