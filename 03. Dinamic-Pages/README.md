# Dynamic Pages Web Scraping
## Emmanuel Cruz Hernández

----

## Descripción

En este módulo se trabaja con Web Scraping de nivel 3, que sirve para hacer web scraping a página que tienen caracter dinámico. A diferencia del web scraping de nivel 1 y 2, este web scraping tomará el comportamiento de una persona al realizar la extracción de información, como si estuviera dando click a botones para indagar en más información de la página.


----

## Prácticas

* olx: Extracción de precios e información de coches de OLX México con carga de páginas dinámicas.
* mercado-libre-web-scraping: Extracción de precio y nombre de productos de mercado libre usando web scraping vertical y horizontal con carga dinámica.
* reseñas-la-casa-de-toño: extracción de información sobre reseñas de La Casa de Toño (sucursal Cuajimalpa), con web scraping dinámico, con manejo automatizado de scroll.
* twitter-web-scraping: llenado de formularios automático para ingresar a Twitter y extraer información de los tweets.
* horarios-facultad-ciencias-2022-1: aprovechando que estamos en tiempo de incripciones, es un ejemplo de extracción de datos de los cursos de Ciencias de la Computación de la Facultad de Ciencias (UNAM) que hay en el semestre 2022-1.

----

## ¿Cuando usar web scraping dinámico?

El web scraping dinámico es aplicable cuando la carga de información de una página depende del scrolling del sitio, así como la dar click a botones que cargan más información. El web scraping dinámico es independiente del web scraping horizontal y vertical, es decir, no es lo mismo y se pueden combinar dependiendo de los datos que se pueden extraer.

Otra forma de verificar si una página utiliza carga dinámica podemos ingresar a la pestaña de inspeccionar página y en redes o _Network_ y muestra los requerimientos desde el servidor. Si la respuesta no es igual a lo que se está viendo en el navegador o falta información, entonces la página trabaja con carga dinámica. El trabajo es revisar el hover de los requerimientos para comparar si las URL's de cada elemento de la página es igual al del listado de redes. También se puede visualizar e _Preview_ del renderizado del HTML.

Un ejemplo de página dinámica que requieren de requerimientos posteriores son [Udemy](https://www.udemy.com/) o [Footdistrict](https://footdistrict.com/) para la carga de tallas.

Para resolver ese tipo de problemas, se puede utilizar Selenium o herramientas que se ven en web Scraping de nivel 4.

## Instalación

Para este módulo de web scraping se utiliza _Selenium_.

		pip install selenium

También es muy necesario tener un driver para realizar el web scraping, que se puede descargar en el enlace siguiente, donde se debe corresponder al navegador y al sistema operativo. Se puede descargar [aquí](https://selenium-python.readthedocs.io/installation.html#drivers)