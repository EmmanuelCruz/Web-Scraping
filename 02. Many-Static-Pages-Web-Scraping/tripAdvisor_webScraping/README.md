# Web Scraping estático de TripAdvisor.
## Emmanuel Cruz Hernández

----

## Descripción

Aplicación de web scraping vertical para varias páginas del sitio web de [TripAdvisor](https://www.tripadvisor.com.mx/Hotels-g150771-La_Paz_Baja_California-Hotels.html). Este web scraping es básico del nivel dos.
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
Para extraer la información, primero se definen los módulos de los objetos que se desean extraer. En este caso, queremos el nombre del hotel, la descripcion, el precio y las facilidades de los hoteles de Baja California encontrados en _TripAdvisor_.

Dentro de la clase que almacenará los datos, se definen todas las propiedades que se desean extraer de la página. Tal como se vio en el módulo uno de web scraping.

		class Hotel(Item):
			nombre = Field()
			descripcion = Field()
			precio = Field()
			facilidades = Field()

Una vez hecho esto, se define una clase que extiende a la clase _CrawlSpider_, la cual, contendrá la función encargada de obetener los elementos con el _parse()_ y almacenarlos en una instancia de la clase que se creó anteriormente.

Para hacer web scraping vertical (extracción de datos a profundidad), se crea una nueva variable rules, que almacena un objeto de tipo _Rule_, el cuál recibe un _LinkExtractor_, un _follow_ y un _callback_. A continuación se explica su funcionalidad:

* LinkExtractor: es un objeto que en su parámetro _allow_ recibe una expresión regular que especifica el contenido de una cadena dentro de los link donde se hará la búsqueda a profundidad de la página. Se buscarán todos aquellos link que comiencen con la especificación del dominio, seguidos de la expresión regular definida en el parámetro.
* follow: especifica si se seguirán las reglas definidas.
* callback: la función con la cuál se van a extraer los datos de cada página por profundiad.

Después de esto, se define la función para realizar el parse. El nombre de esta debe corresponder al nombre definido en _calback_. Esta función utiliza XPATH para realizar la extracción de datos tal cual como se hizo en la extracción de datos de una sóla página estática con _Scrapy_([aquí](https://github.com/EmmanuelCruz/Static-One-Page-Web-Scraping/tree/master/stackOverFlow-scrapy-scraping)).

		class TripAdvisor(CrawlSpider):
			name = "Hoteles"

			start_urls = ['https://www.tripadvisor.com.mx/Hotels-g150771-La_Paz_Baja_California-Hotels.html']

			# Segundos de espera entre consulta de páginas. EVITA BANEOS
			download_delay = 2

			rules = {
				Rule(
					LinkExtractor(
						allow = r'/Hotel_Review-'
					),
					follow = True,
					callback = 'parse_hotel'
				)
			}

			def parse_hotel(self, response):
				sel = Selector(response)
				item = ItemLoader(Hotel(), sel)

				item.add_xpath('nombre', '//h1[@id = "HEADING"]/text()')
				item.add_xpath('descripcion', '//div[contains(@class, "_2f_ruteS")]//p/text()')
				item.add_xpath('precio', '//div[@data-sizegroup="hr_chevron_prices"]/text()')
				item.add_xpath('facilidades', '//div[@data-test-target="amenity_text"]/text()')

				yield item.load_item()

----

## Invocar la extracción

A diferencia de los otros ejemplos, este no tiene una llamada de función que regrese algún resultado, sino que todos los valores de la información necesaria para hacer la extracción se realiza directamente desde la consola al correr el programa.

		scrapy runspider trip_advisor_web_scraping.py -o result.csv -t csv

O si se requieren almacenar los datos en json

		scrapy runspider trip_advisor_web_scraping.py -o result.json -t json

----


## Instalación de bibliotecas

Aquí se muestra un listado de los recursos utilizados para aplicar web scraping en este proyecto.

		pip install scrapy
		
