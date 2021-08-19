# Web Scraping en Twitter con web scraping dinámico
## Emmanuel Cruz Hernández

----

## Descripción

En este ejemplo se extrae información de tweets en [Twitter](https://twitter.com/login) realizando un proceso automático de ingreso de un usuario a una plataforma con formularios. Para esta extracción se usa _Selenium_.

## Importar

Para esta extracción de datos se importan los módulos siguientes:

                from selenium import webdriver
                from selenium.webdriver.common.by import By
                from selenium.webdriver.chrome.options import Options
                from selenium.webdriver.support.ui import WebDriverWait
                from selenium.webdriver.support import expected_conditions as EC

## Extracción de datos

Para extraer estos datos, es necesario tener descargado el driver del navegador. En este caso, el driver es _chromedriver.exe_. La ruta de su ubicación pasa como parámetro a la creacción del manejo de la página y para obtener una respuesta del servidor nuevamente se utiliza la función _get_. Nótese que con el parámetro _options_, se puede agregar un encabezado a la extracción de datos.

                opts = Options()
                opts.add_argument(
                        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
                )

                driver = webdriver.Chrome("../chromedriver.exe", options=opts)

La extracción de datos de Twitter comienza a partir del llenado del formulario de inicio de sesión. Este llenado de formularios está programado automáticamente desde el código con _Selenium_. Para tener mayor seguridad, la contraseña se puede pasar desde un archivo de texto para mayor seguridad y no poner información directamente en código. El archivo asociado a la contraseña es _password.txt_.

                # Acceso a usuario y contraseña
                usuario = 'correo@correo.com'
                password = open('password.txt').readline().strip()

                ## Obtención de inputs para ingresar a Twwiter
                input_user = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//main//input[@name="session[username_or_email]"]'))
                )
                input_pass = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//main//input[@name="session[password]"]'))
                )

Una vez que se obtiene la información del usuario y los datos que se deben llenar, se pocede a ingresar los datos en el input correspondiente y dar click al botón de inicio de sesión de forma automatizada.

                # Para llenar los inputs
                input_user.send_keys(usuario)
                input_pass.send_keys(password)

                # Identificación del botón de inicio de sesión
                boton_inicio = driver.find_element_by_xpath('//main//div[@data-testid="LoginForm_Login_Button"]//div[@dir="auto"]')

                boton_inicio.click()

Una vez inciada la sesión, se muestran los Tweets en la página principal, en donde ya se puede hacer una extracción de datos. En este caso, se imrpimen las primeras apariciones de los Tweets.


                # Obteniendo todos los twetts
                tweets = WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located((By.XPATH, '//section//article//div[@dir="auto"]'))
                )

                for tweet in tweets:
                        print(tweet.text)

## Ejecutar el proyecto

Basta con invocar

        python twitter.py

en consola.

## Recursos necesarios

Instalar Selenium

        pip install selenium

Descargar el driver en la versión correspondiente al navegador y al sistema operativo. Se puede descargar [aquí](https://selenium-python.readthedocs.io/installation.html#drivers)