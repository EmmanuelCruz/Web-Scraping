# Web Scraping vertical y horizontal de Mercado Libre.
## Emmanuel Cruz Hernández

----

## Descripción

Aplicación de web scraping vertical y horizontal para varias páginas del sitio web de [MercadoLibre](https://listado.mercadolibre.com.mx/musica-peliculas-y-series/peliculas/) en la sección de películas y series. En este, se utilizará _Scrapy_ como objeto para hacer las peticiones y también para el parse del HTML.

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

Dentro de la clase que almacenará los datos, se definen todas las propiedades que se desean extraer de la página. Tal como se vio en el módulo uno de web scraping.

		class Articulo(Item):
		    titulo = Field()
		    precio = Field()
		    descripcion = Field()

Una vez hecho esto, se define una clase que extiende a la clase _CrawlSpider_, la cual, contendrá la función encargada de obetener los elementos con el _parse()_ y almacenarlos en una instancia de la clase que se creó anteriormente.

Para hacer web scraping vertical (extracción de datos a profundidad), se crea una nueva variable rules, que almacena un objeto de tipo _Rule_, el cuál recibe un _LinkExtractor_, un _follow_ y un _callback_. A continuación se explica su funcionalidad:

* LinkExtractor: es un objeto que en su parámetro _allow_ recibe una expresión regular que especifica el contenido de una cadena dentro de los link donde se hará la búsqueda a profundidad de la página. Se buscarán todos aquellos link que comiencen con la especificación del dominio, seguidos de la expresión regular definida en el parámetro.
* follow: especifica si se seguirán las reglas definidas.
* callback: la función con la cuál se van a extraer los datos de cada página por profundiad.

Después de esto, se define la función para realizar el parse. El nombre de esta debe corresponder al nombre definido en _calback_.

Como se puede notar, hay una segunda regla. La primera es para definir el web scraping vertical y la segunda para el web scaping vertical. En la primera regla se recibe un LinkExtractor con la expresión regular que contiene el patrón de cada una de las páginas en la navegación. En este caso, cada página de mercado libre para el despliegue de lso productos está dado por la expresión _r'\_Desde\_'_.

La segunda regla, corresponde al web scraping horizontal, donde se obtienen los detalles de cada uno de los artículos encontrados en cada paginación. Otro detalle que es importante destacar es que el _custom\_settings_ recibe un parámetro adicional llamado _CLOSESPIDE0R\_PAGECOUNT_, que identifica el máximo de páginas en las que se van a descargar los items.

		class MercadoLibreCrawler(CrawlSpider):
			name = 'mercadoLibre'

			custom_settings = {
				'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
				'CLOSESPIDER_PAGECOUNT': 20 # Numero maximo de paginas en las cuales voy a descargar items. Scrapy se cierra cuando alcanza este numero
			}
			
			allowed_domains = ['articulo.mercadolibre.com.mx', 'listado.mercadolibre.com.mx']
			
			start_urls = ['https://listado.mercadolibre.com.mx/musica-peliculas-y-series/peliculas/']
			
			download_delay = 1
			
			# Tupla de reglas
			rules = (
				Rule( # Regla para la paginación. Web Scraping horizontal.
					LinkExtractor(
						allow=r'/_Desde_\d+' # Patron en donde se utiliza "\d+", expresion que puede tomar el valor de cualquier combinacion de numeros
					),
					follow=True
				),
				Rule( # Regla para profundidad. Web Scraping vertical.
					LinkExtractor(
						allow=r'/MLM-' 
					),
					follow=True,
					callback='parse_items'
				),
			)
			
			def limpia(self, texto):
				nuevo = texto.replace('\r', ' ').replace('\t', ' ').replace('\n', ' ')
				return nuevo
			
			def parse_items(self, response):
				item = ItemLoader(Articulo(), response)
				
				item.add_xpath('titulo', '//h1/text()', MapCompose(self.limpia))
				item.add_xpath('descripcion', '//div[@class="ui-pdp-description"]/p/text()', MapCompose(self.limpia))
				item.add_xpath('precio', '//span[@class = "price-tag-fraction"]/text()')
				
				yield item.load_item()

Finalmente, para limpiar los datos se utiliza en este caso _MapCompose_, que recibe el nombre de una función, la cuál se encargará de dar el formado a los datos, en este caso, quitar toda clase de saltos de línea y tabuladores entre el texto.

----

## Invocar la extracción

A diferencia de los otros ejemplos, este no tiene una llamada de función que regrese algún resultado, sino que todos los valores de la información necesaria para hacer la extracción se realiza directamente desde la consola al correr el programa.

		scrapy runspider mercado-libre-web-scraping.py -o result.csv -t csv

O si se requieren almacenar los datos en json

		scrapy runspider mercado-libre-web-scraping.py -o result.json -t json

----


## Instalación de bibliotecas

Aquí se muestra un listado de los recursos utilizados para aplicar web scraping en este proyecto.

		pip install scrapy
		
