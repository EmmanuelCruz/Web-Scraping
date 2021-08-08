# Web Scraping estático de Gaceta UNAM (Comunidad).
## Emmanuel Cruz Hernández

----

## Descripción

Aplicación de web scraping estático de una sola página hacia el sitio web de [StackOverFlow](https://es.stackoverflow.com/questions/). Este web scraping es básico del nivel uno.
En este, se utilizará _Scrapy_ como objeto para hacer las peticiones y _BeautifulSoup_ para el parse del HTML.

----

## Módulos requeridos

Para este ejemplo, son requeridos los siguientes módulos:

		from scrapy.item import Field
		from scrapy.item import Item
		from scrapy.spiders import Spider
		from scrapy.selector import Selector
		from scrapy.loader import ItemLoader

----

## Extraer información
Para extraer la información, primero se definen los módulos de los objetos que se desean extraer. En este caso, queremos las preguntas y las descripciones de las preguntas más sobresalientes de la página de preguntas de StackOverFlow.

Para utilizar scrapy se crea la clase del Item que queremos obtener. Por ejemplo, si queremos obtener las preguntas, podemos crear una clase _Pregunta_ que extienda a la clase Item, que se ecuentra en las bibliotecas de _Scrapy_.

Dentro de la clase se definen todas las propiedades que se desean extraer de la página. En este caso, queremos las preguntas, juntos con su descripción. Estos camos, deben ser un objeto de tipo Field.

		class Pregunta(Item):
			pregunta = Field()
			descripcion = Field()

Una vez hecho esto, se define una clase que extiende a la clase _Spider_, la cual, contendrá la función encargada de obetener los elementos con el _parse()_ y almacenarlos en una instancia de la clase que se creó anteriormenete.

A diferencia del parser usando puramente scrapy, aquí se utilizan las funciones implementadas para BeautifulSoup. Las funciones importantes para este ejemplo son ***find_all*** que recibe como parámetro la etiqueta que requiere buscar, las clases por las que quiere buscar, id's, etc. Para obtener el texto se utiliza el atributo _text_ que tienen los objetos de BeautifulSoup y ***add_value***, que dan un nuevo valor al atributo de la clase que contiene la información necesaria para almacenar los datos.

		def parse(self, response):
			soup = BeautifulSoup(response.body, features="lxml")
			articulos = soup.find_all('article', class_ = "type-post")

			for articulo in articulos:
				item = ItemLoader(Articulo(), articulo)

				titulo = articulo.find('h2', class_ = 'title', recursive = True)
				if titulo != None:
					titulo = titulo.text
				else:
					titulo = "N/A"
				descripcion = articulo.find('div', class_ = 'post-summary', recursive = True)
				if descripcion != None:
					descripcion = descripcion.text
				else:
					descripcion = "N/A"

				item.add_value('titulo', titulo)
				item.add_value('descripcion', descripcion)

				yield item.load_item()


----

## Invocar la extracción

A diferencia de los otros ejemplos, este no tiene una llamada de función que regrese algún resultado, sino que todos los valores de la información necesaria para hacer la extracción se realiza directamente desde la consola al correr el programa.

		scrapy runspider gaceta_unam_web_scraping.py -o result.csv -t csv

O si se requieren almacenar los datos en json

		scrapy runspider gaceta_unam_web_scraping.py -o result.json -t json

----


## Instalación de bibliotecas

Aquí se muestra un listado de los recursos utilizados para aplicar web scraping en este proyecto.

		pip install scrapy
		
		pip install beautifulsoup4
