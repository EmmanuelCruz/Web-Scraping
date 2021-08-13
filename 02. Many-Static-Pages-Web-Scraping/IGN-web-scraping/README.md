# Web Scraping estático de IGN.
## Emmanuel Cruz Hernández

----

## Descripción

Aplicación de web scraping vertical y horizontal para varias páginas del sitio web de [IGN Latam](https://latam.ign.com/se/?model=article&q=xbox&order_by=-date). Este web scraping es intermedio del nivel 2. Se extrae información de más de un tipo de objeto, en este caso de noticas, videos y galerías de Xbox.
En este, se utilizará _Scrapy_ como objeto para hacer las peticiones y también para el parse del HTML.


----

## Módulos requeridos

Para este ejemplo, son requeridos los siguientes módulos:

		from scrapy.item import Field
		from scrapy.item import Item
		from scrapy.spiders import CrawlSpider, Rule
		from scrapy.selector import Selector
		from scrapy.loader.processors import MapCompose
		from scrapy.linkextractors import LinkExtractor
		from scrapy.loader import ItemLoader

----

## Extraer información

Para esta página se utiliza un nuevo mecanismo de extracción de información, ya que se requiere extraer información de Noticas y Videos de Xbox en IGN. Al tener dos tipos de objetos diferentes de los cuales extraer información, se tienen dos clases con su representación.

		# Clase de noticias
		class Noticia(Item):
			nombre = Field()
			contenido = Field()

		# Clase de videos
		class Video(Item):
			titulo = Field()
			fecha = Field()

Además se agrega otro nivel de dificultad. La extracción comienza dentro de la página principal, donde se encuentra una pestaña de Videos y otra de Noticias relacionadas a una búsqueda, en este caso Xbox.

La primera regla que se define es la horizontalidad por el tipo de información. Permite moverse entre las dos pestañas mencionadas anteriormente:

		Rule(
			LinkExtractor(
				allow=r'type='
			),
			follow=True
		),

La segunda regla es otra regla horizontal para navegar entre cada una de las secciones, ya sea para videos o noticias.

		Rule(
			LinkExtractor(
				allow=r'&page=\d+' 
			),
			follow=True
		),

La tercera regla es una regla vertical para ver los detalles de las noticias. Esta regla llama al callback _parse\_new_ para extraer la información.

		Rule(
			LinkExtractor(
				allow = r'/news/'
			),
			follow = True,
			callback = 'parse_new'
		),
		
		...
		
		def parse_new(self, response):
			item = ItemLoader(Noticia(), response)

			# Extracción de items de noticia
			item.add_xpath('nombre', '//h1[@id="id_title"]/text()')
			item.add_xpath('contenido', '//div[@id="id_text"]//*/text()')

Finalmente, la última regla corresponde a la regla vertical para extraer la información de los videos. Su parse asociado es _parse\_video_

		def parse_video(self, response):
			item = ItemLoader(Video(), response)

			# Extracción de items de video
			item.add_xpath('titulo', '//h1[@id="id_title"]/text()')
			item.add_xpath('fecha', '//span[@class="publish-date"]/text()')

			yield item.load_item()

----

## Invocar la extracción

A diferencia de los otros ejemplos, este no tiene una llamada de función que regrese algún resultado, sino que todos los valores de la información necesaria para hacer la extracción se realiza directamente desde la consola al correr el programa.

		scrapy runspider ign_web_scraping.py -o result.csv -t csv


O si se requieren almacenar los datos en json

		scrapy runspider ign_web_scraping.py -o result.json -t json

----


## Instalación de bibliotecas

Aquí se muestra un listado de los recursos utilizados para aplicar web scraping en este proyecto.

		pip install scrapy
		
