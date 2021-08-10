from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

# Clase de noticias
class Noticia(Item):
	nombre = Field()
	contenido = Field()

# Clase de videos
class Video(Item):
	titulo = Field()
	fecha = Field()

# Crawler
class IGNCrawler(CrawlSpider):
	name = 'IGN-Xbox'

	custom_settings = {
	  'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
	  'CLOSESPIDER_PAGECOUNT': 70 
	}

	allowed_domains = ['latam.ign.com']

	start_urls = ['https://latam.ign.com/se/?model=article&q=xbox&order_by=-date']

	download_delay = 1

	rules = (
		# Horizontalidad por tipo de información (Noticias o videos)
		Rule(
			LinkExtractor(
				allow=r'type='
			),
			follow=True
		),
		# Horizontalidad por paginación
		Rule(
			LinkExtractor(
				allow=r'&page=\d+' 
			),
			follow=True
		),
		# Regla para detalles de Noticias
		Rule(
			LinkExtractor(
				allow = r'/news/'
			),
			follow = True,
			callback = 'parse_new'
		),
		# Regla para detalles de videos
		Rule(
			LinkExtractor(
				allow = r'/video/'
			),
			follow = True,
			callback = 'parse_video'
		),
	)

	def parse_new(self, response):
		item = ItemLoader(Noticia(), response)

		# Extracción de items de noticia
		item.add_xpath('nombre', '//h1[@id="id_title"]/text()')
		item.add_xpath('contenido', '//div[@id="id_text"]//*/text()')

		yield item.load_item()

	def parse_video(self, response):
		item = ItemLoader(Video(), response)

		# Extracción de items de video
		item.add_xpath('titulo', '//h1[@id="id_title"]/text()')
		item.add_xpath('fecha', '//span[@class="publish-date"]/text()')

		yield item.load_item()