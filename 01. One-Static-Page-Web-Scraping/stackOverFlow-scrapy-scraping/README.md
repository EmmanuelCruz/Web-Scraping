# Web Scraping estático de StackOverFlow Questions con Scrapy.
## Emmanuel Cruz Hernández

----

## Descripción

Aplicación de web scraping estático de una sola página hacia el sitio web de [StackOverFlow](https://es.stackoverflow.com/questions/). Este web scraping es básico del nivel uno.
En este, se utilizará _Scrapy_ como objeto para hacer las peticiones y también para hacer el parser del HTML.

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

Para el caso de _Scrapy_, la o las URL's se ingresan en forma de lista. En este caso sólo se hará la extracción de una única URL, por lo que basta tener una lista con un solo elementos.

Lo siguiente es definir una función que haga el _parser_, la cuál recibe como parámetro el árbol del HTML al cuál se le hará el parse. Este se maneja desde el lenguaje XPATH con ayuda de un objeto de tipo _Selector_. Este tiene implementada una función llamada _xpath_ que recibe como parámetro la expresión en XPATH, de lo que se quiere extraer. 

Finalmente, con un objeto de tipo _ItemLoader_ se crea el objeto de la clase que recibe dos parámetros, el primero es el nombre de la clase y el segundo es el objeto de donde se extraerán los datos. Los valores que son almacenados en la clase se les asigna un valor con la función **add_path**. Finalmente, para guardar los cambios del objeto se utiliza la palabra _yield_, seguido de la función **load_item** implementada en un _ItemLoader_. El resultado final se verá similar al siguiente

		class StackOverFlowSpider(Spider):
			name = "My Spider"

			custom_settings = {
			'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
		    	} 

			start_urls = ['https://stackoverflow.com/questions']

			# Parser
			def parse(self, response):
				sel = Selector(response)
				preguntas = sel.xpath('//div[@id="questions"]//div[@class="question-summary"]')

				for pregunta in preguntas:
					item = ItemLoader(Pregunta(), pregunta)
					item.add_xpath('pregunta', './/h3/a/text()')
					item.add_xpath('descripcion', './/div[@class="excerpt"]/text()')

					yield item.load_item()


----

## Invocar la extracción

A diferencia de los otros ejemplos, este no tiene una llamada de función que regrese algún resultado, sino que todos los valores de la información necesaria para hacer la extracción se realiza directamente desde la consola al correr el programa.

		scrapy runspider stack_over_flow_scrapy.py -o result.csv -t csv

O si se requiere almacenar la información en JSON

		scrapy runspider stack_over_flow_scrapy.py -o result.json -t json

----

## IMPORTANTE
Aplicar Web Scraping con Scrapy no funciona para todas las páginas. Otra cosa que es importante destacar es que los datos no salen limpios, ya que contienen varios saltos de línea, tabuladores, entre otras cosas que posteriormente se van a arreglar.

----


## Instalación de bibliotecas

Aquí se muestra un listado de los recursos utilizados para aplicar web scraping en este proyecto.

		pip install scrapy
