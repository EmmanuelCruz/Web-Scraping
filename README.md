# Web Scraping
## Emmanuel Cruz Hernández

----

## Descripción

Repositorio con prácticas de _Web Scraping_ a distintas páginas como Twitter, Mercado Libre, Gaceta UNAM, página de horarios de la Facultad de Ciencias, OLX, entre otras, con distintas técnicas de web scraping, tales como se muestran a continuación:

* web scraping estático
* web scraping vertical
* web scraping horizontal
* web scraping dinámico
* web scraping con llenado de formularios
* web scraping con captchas
* web scraping con imágenes

La organización de este repositorio se divide en 6 apartado distintos

1. [One-Static-Page-Web-Scraping](https://github.com/EmmanuelCruz/Web-Scraping/tree/master/01.%20One-Static-Page-Web-Scraping)
2. [Many-Static-Pages-Web-Scraping](https://github.com/EmmanuelCruz/Web-Scraping/tree/master/02.%20Many-Static-Pages-Web-Scraping)
3. [Dinamic-Pages](https://github.com/EmmanuelCruz/Web-Scraping/tree/master/03.%20Dinamic-Pages)
4. [Web-Scraping-with-APIS](https://github.com/EmmanuelCruz/Web-Scraping/tree/master/04.%20Web-Scraping-with-APIS)
5. [Web-Scraping-Autentication](https://github.com/EmmanuelCruz/Web-Scraping/tree/master/05.%20Web-Scraping-Autentication)
6. Automatic-Web-Scraping

----

## Ética del uso del Web Scraping

Cada vez que se hace la extracción a una página web, se hace un requerimiento al servidor para obtener los datos. Si se envían requerimientos de manera desmesurada se puede colapsar un servidor con requerimientos de web scraping. A este problema se le conoce como _DoS_ (Denial of service).

Siempre es importante definir un buen timeout para que este problema no suceda. Otra forma de evitarlo es hacer una extracción de datos segmentada.

Otra cuestión importante es tener la segurida de los datos que se extraen, es decir, dar créditos y asegurar que la extracción de datos de una página específica es legal. Es importante hacer **web scraping responsable**.

### Mecanismos de banneo

Muchos servidores web, tienen un sistema implementado contra _DoS_, de tal forma que si se sobrepasa la cantidad de requerimientos por segundo, el servidor devolverá una respuesta 403, la cuál se refiere a una negación de una acción solicitada para un requerimiento que se detecta a partir de nuestra IP. Lo que se puede hacer para poder evitar un _DoS_ es considerar los siguientes puntos:

* Definir un tiempo de espera entre cada requerimiento al servidor
* Limitar la cantidad de datos descargados
* Tratar de humanizar el comportamiento del web scraping con el servidor
* Tratar de no hacer web scraping desde nuestra computadora local, una opción es usar una máquina virtual para hacer web scraping.
* Hacer uso de user-agents, que sirve como una cadena de información sobre el sistema operativo y el navegador utilizado. Si no se redefinen, el user agent por defecto será _robot_. Un módulo de apoyo es

        pip install Scrapy-UserAgents

Que permite randomizar cada user agent cada ciertos requerimientos. Los cambios se realizan en los _custom\_settings_ de la siguiente forma

        "DOWNLOADER_MIDDLEWARES": { # pip install Scrapy-UserAgents
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 500,
        }

* Uso de VPN's.

**Importante: Siempre hay que tener ética profesional para hacer buen uso de web scraping para hacer la extracción de datos**

Algunos puntos extra se pueden consultar [aquí](https://www.scrapehero.com/how-to-prevent-getting-blacklisted-while-scraping/).

