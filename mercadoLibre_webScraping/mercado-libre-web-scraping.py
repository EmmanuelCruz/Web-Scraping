from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Articulo(Item):
    titulo = Field()
    precio = Field()
    descripcion = Field()

class MercadoLibreCrawler(CrawlSpider):
    name = 'mercadoLibre'

    custom_settings = {
      'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
      'CLOSESPIDER_PAGECOUNT': 20 # Numero maximo de paginas en las cuales voy a descargar items. Scrapy se cierra cuando alcanza este numero
    }

    # Utilizamos 2 dominios permitidos, ya que los articulos utilizan un dominio diferente
    allowed_domains = ['articulo.mercadolibre.com.mx', 'listado.mercadolibre.com.mx']

    start_urls = ['https://listado.mercadolibre.com.mx/musica-peliculas-y-series/peliculas/']

    download_delay = 1

    # Tupla de reglas
    rules = (
        Rule( # Regla para la paginación. Web Scraping horizontal.
            LinkExtractor(
                allow=r'/_Desde_\d+' # Patron en donde se utiliza "\d+", expresion que puede tomar el valor de cualquier combinacion de numeros
            ), follow=True),
        Rule( # Regla para profundidad. Web Scraping vertical.
            LinkExtractor(
                allow=r'/MLM-' 
            ), follow=True, callback='parse_items'),
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
