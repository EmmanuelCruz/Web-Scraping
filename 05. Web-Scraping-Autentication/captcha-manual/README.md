# Web Scraping con autenticación con Captchas
## Emmanuel Cruz Hernández

----

## Descripción

Llenado de formularios con Captchas integrados. El sistema se basa en el llenado automático de datos necesarios hasta llenar al sistema de Captchas. Este se resuelve manualmente, ya que el llenado de captchas automático depende de otros recursos.

## Módulos necesarios

        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options

## Extracción de datos

En realidad no es necesario definir los argumentos porque un sistema con captchas integrado puede detectar cuando se está haciendo un llenado automático, pero no está de más definirlo

        opts = Options()
        opts.add_argument(
            "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
        )

Definimos el driver, obtenemos la URL semilla e ingresamos a la página web con el driver.

        driver = webdriver.Chrome('chromedriver.exe', options=opts)

        url = 'https://www.google.com/recaptcha/api2/demo'
        driver.get(url)

En este caso, el captcha se encuentra dentro de un elemento _iFrame_, por lo que se trata como una página web individual, a la cuál se accede con la función _switch\_to.frame_. 

**NOTA**: en la documentación se menciona que se puede usar _switch\_to\_frame_, pero ya es obsoleto (deprecated) :(

        driver.switch_to.frame(driver.find_element_by_xpath('//iframe'))
        captcha = driver.find_element_by_xpath('//div[@class="recaptcha-checkbox-border"]')
        print(captcha)
        captcha.click()

La magía de una combinación de manejo de un sistema mitad automatizado, mitad manual se da por la función _input_, la cual deja detenido al sistema automático hasta dar click en consola

        input()


Finalmente, después de resolverse el captcha manual, se regresa a la página padre, es decir, salir del _iFrame_ y dar click al botón de inicio.

        driver.switch_to.default_content()

        submit = driver.find_element_by_xpath('//input[@id="recaptcha-demo-submit"]')
        submit.click()

Después de esta línea, ya se estaría dentro del sistema, el cual, ya es accesible a la extracción de datos con web scraping.

        contenido = driver.find_element_by_xpath('//div[@class="recaptcha-success"]')
        print(contenido.text)

