# Web Scraping con más de 1 URL semilla en Urbania.
## Emmanuel Cruz Hernández

----

## Descripción

Aplicación de web scraping vertical parados páginas del sitio web de [Urbania CDMX](https://www.grupourbania.com.mx/resultados.php?estado=CDMX&delegacion=&colonia=&min_precio=1764560&max_precio=&min_tam=77&recamaras=) y [Urbania Queretaro](https://www.grupourbania.com.mx/resultados.php?estado=Quer%C3%A9taro&delegacion=&colonia=&min_precio=955000&max_precio=3308216&min_tam=98&recamaras=). Se extrae información de las propiedades de ambos url's.
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

A diferencia de los ejemplos anteriores, en este web scraping se utilizan dos url semilla. Uno para las propiedades en CDMX y otra url para las propiedades en Querétaro.

		start_urls = ['https://www.grupourbania.com.mx/resultados.php-estado=CDMX&delegacion=&colonia=&min_precio=1764560&max_precio=&min_tam=77&recamaras=',
			'https://www.grupourbania.com.mx/resultados.php?estado=Quer%C3%A9taro&delegacion=&colonia=&min_precio=955000&max_precio=3308216&min_tam=98&recamaras=']

Es importante recalcar que en este parámetro se puden ingresar tantas URL semilla como sea necesario. Para este ejemplo y solución del problema sólo se usan dos.

Tenemos en principio la clase propiedad para almacenar la información de las propiedades de ambos lugares

		class Propiedad(Item):
			informacion = Field()

En este caso se hará web scraping vertical sobre las url semilla. El parse asociado a la regla de verticalidad es _parse\_propiedad_.

		# Horizontalidad por tipo de información (Noticias o videos)
		Rule(
			LinkExtractor(
				allow=r'/casas-y-departamentos/'
			),
			follow=True,
			callback='parse_propiedad'
		),
		
		...

		def limpia(self, text):
			return text.replace("\t","").replace("\r","").replace("\n","").strip()

		def parse_propiedad(self, response):
			item = ItemLoader(Propiedad(), response)

			item.add_xpath('informacion', '//div[@class="development-section__data-block"]/div/text()', MapCompose(self.limpia))

			yield item.load_item()

Finalmente como los datos estaban sucios, se limpian con MapCompose.

----

## Invocar la extracción

A diferencia de los otros ejemplos, este no tiene una llamada de función que regrese algún resultado, sino que todos los valores de la información necesaria para hacer la extracción se realiza directamente desde la consola al correr el programa.

		scrapy runspider urbania_web_scraping.py -o result.csv -t csv

O si se requieren almacenar los datos en json

		scrapy runspider urbania_web_scraping.py -o result.json -t json

----


## Instalación de bibliotecas

Aquí se muestra un listado de los recursos utilizados para aplicar web scraping en este proyecto.

		pip install scrapy
		
