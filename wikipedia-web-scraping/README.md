# Web Scraping estático de Wikipedia
## Emmanuel Cruz Hernández

----

## Descripción

Aplicación de web scraping estático de una sola página hacia el sitio web de [Wikipedia](https://www.wikipedia.org/). Este web scraping es básico del nivel uno.
En este ejemplo, se hace la extracción de datos con _requests_ y _lxml_, para las expresiones XPATH.

----

## Encabezados

Son los datos necesarios para hacer una petición como un usuario. En particular, un encabezado tiene un atributo llamado _user-agent_, que contiene información del navegador y el sistema operativo que se está utilizando para la extracción de datos.

Esta información pasa como parámetro a la función _get_ en los _headers_. En caso de no pasar este parámetro, el valor por default para _headers_ es _boot_ y es más sencillo detectar la aplicación de web scraping.


## Parse

La función _get_ y sus recursos dan paso a obtener el archivo HTML de una página. Sin embargo, se necesita parsear para obtener la información necesaria, con ayuda de la herramienta _lxml_. en particular, tiene un atributo que permite parsear a texto o cadena un archivo html.

		from lxml import html

La línea que permite parsear esta información, se invoca de la siguiente forma

		html.fromstring(htmlForm)

Donde htmlForm corresponde al archivo html que se quiere parsear al objeto. Este resultado se puede almacenar en una variable y a partir de esta, acceder a los métodos que tiene implementados para la extracción de datos.

## Extraer información

Para la extracción de una información específica contenida del archivo html, es necesario inspeccionar la página sobre la que se está haciendo el requerimiento. Se puede obtener información de su etiqueta, clase, id, entre otros.

Para este ejemplo particular, se hace extracción sobre el _id_, que recordemos, es único dentro de un archivo xml. Esto con ayuda de una función definida en lxml, que se invoca de la siguiente forma.

		parser.get_element_by_id("nombreId")

Y finalmente para obtener a su contenido, este resultado puede invocar una función que extrae el texto de la etiqueta con el id _nombreId_

		text_content()

Otra forma de extraer información es con ayuda de una expresión XPATH, como las mencionadas anteriormente. Para hacer uso de esta forma, se necesita de una expresión XPATH con la función _xpath_, implementada en el parser que se hizo anteriormente.

		resultado = parser.xpath("ExpresionXPATH")
		
Por ejemplo, si quiero obtener el texto que dice _Inglés_ en la página de _Wikipedia_, podría analizar las características y obtener la información creando la expresión XPATH-

		ingles = parser.xpath("//a[@id='js-link-box-en']/strong/text()")

El resultado de la extracción es una lista, con cada uno de los elementos que cumplen la condición XPATH.

Otro ejemplo que podríamos poner, es obtener todos los idiomas de la página principal de _Wikipedia_.

		idiomas = parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()")
		
En particular, la etiqueta padre donde se encuentran todos estos elementos es un div, que tiene en particular la clase 'central-featured-lang'. De esta clase, buscamos todas las subetiquetas de tipo _strong_ y extraemos el contenido. Esto dará una lista con todos los idiomas de la página principal.

----


## Instalación de bibliotecas

Aquí se muestra un listado de los recursos utilizados para aplicar web scraping en este proyecto.

		pip install requests


		pip install lxml
