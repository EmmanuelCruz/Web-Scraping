# Extracción de datos automatizado por tiempo
## Emmanuel Cruz Hernández

----

## Descripción

Extracción del clima de [AccuWather](https://www.accuweather.com/) de las ciudades de México, Monterrey y Guadalajara.
A veces el clima es un dato que se encuentra en constante cambio, incluso en cuestión de segundos, por lo que este programa registra el clima cada minuto para este ejemplo en particular, pero puede moficarse a que el tiempo este definido de otra forma.

## Módulos necesarios

        import schedule
        import time
        from selenium import webdriver

## Extracción de datos

Definimos las url semillas, que en este caso son 3, una correspondiente a la Ciudad de México, Guadalajara y Monterrey.

        start_urls = ['https://www.accuweather.com/es/mx/aguascalientes/241700/weather-forecast/241700',
                            'https://www.accuweather.com/es/mx/guadalajara/243735/weather-forecast/243735',
                            'https://www.accuweather.com/es/mx/monterrey/244681/weather-forecast/244681']

Una vez definidas las URL que nos van a servir, accedemos a cada una de ellas. Una por cada iteración. Dentro del for, esperamos unos segundos a que se carguen los datos de la página, para así acceder al nombre, al clima actual y el clima general a través de expresiones XPATH.

Cada uno de los datos extraídos son almacenados en un archivo llamado _datos-clima.csv_.

        def extraer_clima():

            driver = webdriver.Chrome('chromedriver.exe')

            for url in start_urls:
                driver.get(url)

                time.sleep(2)

                ciudad = driver.find_element_by_xpath('//h1').text
                current = driver.find_element_by_xpath('//a[contains(@class, "cur-con-weather-card")]//div[@class="temp"]').text
                real_feal = driver.find_element_by_xpath('//a[contains(@class, "cur-con-weather-card")]//div[@class="real-feel"]').text

                f = open("datos-clima.csv", "a")
                f.write(f"{ciudad},{current},{real_feal}\n")
                f.close()

                print(ciudad)
                print(current)
                print(real_feal)
                print("\n")

            driver.close()

Una vez definida la función que permite hacer la extracción, invocamos la función repetidas veces para que los datos se estén extrayendo automáticamente cada minuto (nuevamente, el tiempo se puede modificar). Este programa usa _schedule_ para ejecutar la función cada cierto tiempo específico.

        schedule.every(1).minute.do(extraer_clima)

        extraer_clima()

        while True:
            schedule.run_pending()
            time.sleep(1)

----

## Instalación

        pip install schedule
        pip install selenium