# Web Scraping horizontal de Farmacia San Pablo.
## Emmanuel Cruz Hernández

----

## Descripción

Aplicación de web scraping horizontal para varias páginas del sitio web de [Farmacia San Pablo](https://www.farmaciasanpablo.com.mx/medicamentos/c/06). Se extrae información de más de un listado de medicamentos en varias paginas con una única URL semilla.
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

Para este ejemplo que fue más ue nada por diversión, se extrae información de los medicamentos, tales como su nombre y su precio. La extracción se lleva a lo más en 10 niveles de horizontalidad de 10 pasos de navegación, sin verticalidad.

		class Medicamento(Item):
			nombre = Field()
			precio = Field()

Sólo se define una regla, aquella que dará paso a la verticalidad. A partir de cada página, se obtuvo en el parse asociado a la regla una lista de _div_ que contiene cada producto. Para después extraer la información solicitada recorriendo cada div de interes y extrayendo la información con un _ItemLoader_.

		Rule(
			LinkExtractor(
				allow=r'&page='
			),
			follow=True,
			callback = 'parse_medicamento'
		),
		
		...
		
		def limpia(self, text):
			return text.replace("\t", "").replace("\r", "").replace("\n", "").strip()

		def parse_medicamento(self, response):
			sel = Selector(response)

			medicamentos = sel.xpath('//div[contains(@class, "product-list") and contains(@class, "product-listing")]/div')

			for medicamento in medicamentos:
				item = ItemLoader(Medicamento(), medicamento)

				item.add_xpath('nombre', './/p[@class="item-title"]/text()', MapCompose(self.limpia))
				item.add_xpath('precio', './/p[@class="item-prize"]/text()', MapCompose(self.limpia))

				yield item.load_item()

Y como los datos estában muy sucios, se aplica un MapCompose con la limpieza de los datos. Básicamente eliminar espacios al principio y al final, así como algunos saltos que afectan al texto.

----

## Invocar la extracción

A diferencia de los otros ejemplos, este no tiene una llamada de función que regrese algún resultado, sino que todos los valores de la información necesaria para hacer la extracción se realiza directamente desde la consola al correr el programa.

		scrapy runspider farmacia_san_pablo.py -o result.csv -t csv

O si se requieren almacenar los datos en json

		scrapy runspider farmacia_san_pablo.py -o result.json -t json

----


## Instalación de bibliotecas

Aquí se muestra un listado de los recursos utilizados para aplicar web scraping en este proyecto.

		pip install scrapy
		
