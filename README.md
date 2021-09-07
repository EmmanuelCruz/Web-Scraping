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
6. [Automatic-Web-Scraping](https://github.com/EmmanuelCruz/Web-Scraping/tree/master/06.%20Automatic-Web-Scraping)

----

## ¿Qué es el _Web Scraping_?

Es una técnica que permite datos de la web de una manera automática utilizando Software para programar el comportamiento. 
Existen mecanismos formales para descargar datos, como Twitter o Google, que se conocen como APIS. El _Web Scraping_ entra en juego cuando una página Web no cuenta con una API para la descarga y el análisis de datos, ya que permite descargar la información cual como se ve en los navegadores.
La principal desventaja del _Web Scraping_ es la dependencia visual de una página Web para automatizar el procedimiento de extracción.

----

## Tipos de _Web Scraping_

### _Web Scraping_ estático de una sola página

Es cuando la información se encuentra en una sola página Web y no carga información dinámicamente. Para este tipo de Web Scraping se va a utilizar:
* Request: para realizar los requerimientos.
* LXML y BeautifulSopu: para parsear los requerimientos y sus respuestas para extraer la información.
* Scrapy: para hacer requerimientos y parsear las respuestas para extraer la información

Para este módulo, se va a extraer información de Wikipedia, StackOverFlow y Diario e Universo.

### _Web Scraping_ estático de varias páginas de un mismo dominio.

Este tipo de Web Scraping también es conocido como _Scrolling horizontal y vertical_. Esta técnica permite extraer información por cada una de las páginas, esto es scrolling horizontal; también permite indagar en el contenido de las opciones de navegación de la página, esto es scrolling vertical.
También se utilizará Scrapy, extrayendo datos de Airbnb, Mercado Libre, TripAdvisor.

### _Web Scraping_ dinámico

Consiste en automatizar las acciones de un navegador. Controlar el navegador como si fuera un humano para cargar la información a forma de carga dinámica y extraer la información cuando se tenga todo elc ontenido.
Para este módulo se utiliza _Selenium Python_ y para los ejemplos se usa OLX, Mercado Libre, Google Places, Twitter.

### _Web Scraping_ de APIS

Es una combinación de los tres tipos de Web Scraping anteriores.

## Autenticación, capchas y iFrames.
Iniciar sesión, llenar formularios, autenticarnos para la extracción de datos de páginas web que lo requieran.

----

## Cheatsheet de XPATH

Es un documento en donde se puede visualizar de manera resumida, todas las acciones más importantes que se pueden hacer con una herramienta. En pocas palabras, es una técnica que sirve para extraer información de un archivo HTML, basado en las etiquetas, clases y atributos que estén contenidos. 

Existen varios comandos que permiten hacer esta extracción, incluso en tiempo real desde la consola del navegador. Algunos de ellos son:
* **//h1**: Para acceder a todas las etiquetas h1.
* **//div//p**: Para acceder a todos los párrafos que se encuentren dentro de todos los div.
* **//ul/li**: Para acceder a los li que son hijos directos de todos los ul.
* **/body**: Para acceder al body.
* **//button[text()="Submit"]**: Para acceder a todos los botones, cuyo texto sea _Submit_.
* **//a[@name or @href]**: Para acceder a todos las las referencias que tengan un atributo _name_ o un atributo _ref_.

Algunos otros se pueden contular [aquí](https://devhints.io/xpath#axes).

----

## Instalación

Se muestra una lista de los módulos necesarios que se usan en los proyectos para hacer web scraping.

Instalar _requests_

        pip install requests

Instalar _lxml_

        pip install lxml

Instalar _beautiful soup_

        pip install beautifulsoup4

Instalar _selenium_

        pip install selenium

Instalar _pillow_

        pip install pillow

Instalar _scrapy_

        pip install scrapy

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

