# Extracción de datos de GitHub
## Emmanuel Cruz Hernández

----

## Descripción

Extracción de datos de [GitHub](https://github.com/). Se utiliza el mecanismo de autenticación para tener acceso a los repositorios propios. Se hace un listado de los repositorios tanto públicos como privados, ya que gracias a la autenticación, se tiene acceso a esa información que es de caracter personal a través de la autenticación con el llenado de login.

## Módulos necesarios

        import requests
        from lxml import html

## Extracción de datos

Primero se define el header necesario para emular de mejor forma el comportamiento automático como un comportamiento humano.

        head = {
            'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
        }

Definimos la URL semilla, que corresponde a la del login para ingresar a GitHub.

        login_form = 'https://github.com/login'

Sin embargo, se requiere que el inicio de sesión esté activo durante toda la ejecución del programa, para este comportamiento se utiliza un objeto especial que está definido en _requests_ llamado _Session_.

        session = requests.Session()

        login_form_res = session.get(login_form, headers=head)

En particular en GitHub el inicio de sesión depende de un _Token de autenticidad_, el cual se genera automáticamente en cada inicio de sesión (¡Vaya dado curioso!). 

        # Para obtener el authenticity token
        parser = html.fromstring(login_form_res.text)

        a_token = parser.xpath('//input[@name="authenticity_token"]/@value')

Una vez teniendo el token, procedemos a obtener el endpoint que se obtiene después del inicio de sesión. Este se puede consutar en el apartado _NetWork_.

        login_url = 'https://github.com/session'

Esta información es la necesaria involucrada en la petición. El resto es llenar con nuestra información para que se pueda realizar el inicio de sesión con un resumen de todos los datos necesarios.

        login_data = {
            "login": "usuario@correo",
            "password": open('password.txt').readline().strip(),
            "commit": "Sign in",
            "authenticity_token": a_token
        }

Finalmente se realiza la petición con POST

        session.post(
            login_url,
            data=login_data,
            headers=head
        )

Hasta este punto, ya se ha realizado el login a github. Basta con obtener la dirección del listado de respositorios y hacer una extracción de datos con parse y requests al nombre de cada uno de los repositorios.

        data_url = 'https://github.com/Usuario?tab=repositories'

        respuesta = session.get(data_url, headers=head)

        parser = html.fromstring(respuesta.text)
        repositorios = parser.xpath('//h3[@class="wb-break-all"]/a/text()')

        for repo in repositorios:
            print(repo)