from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

# Clase de opiniones
class Opinion(Item):
	titulo = Field()
	calificacion = Field()
	contenido = Field()
	autor = Field()

class TripAdvisorCrawler(CrawlSpider):
	name = "Comentarios"

	custom_settings = {
	  'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
	  'CLOSESPIDER_PAGECOUNT': 150
	}

	allowed_domains = ['tripadvisor.com.mx']

	start_urls = ['https://www.tripadvisor.com.mx/Hotels-g150771-La_Paz_Baja_California-Hotels.html']

	# Segundos de espera entre consulta de páginas. EVITA BANEOS
	download_delay = 1

	rules = {
		# Horizontalidad de hoteles
		Rule(
			LinkExtractor(
				allow = r'-oa\d+'
			),
			follow = True
		),
		# Detalles de hoteles
		Rule(
			LinkExtractor(
				allow = r'/Hotel_Review-',
				restrict_xpaths = ['//div[@id="taplc_hsx_hotel_list_lite_dusty_hotels_combined_sponsored_0"]//a[@data-clicksource="HotelName"]']
			),
			follow = True
		),
		# Paginacion de opiniones de un hotel. Horizontal
		Rule(
			LinkExtractor(
				allow = r'Reviews-or'
			),
			follow = True
		),
		# Detalle del perfil de un usuario
		Rule(
			LinkExtractor(
				allow = r'/Profile/',
				restrict_xpaths = ['//div[@data-test-target="reviews-tab"]']
			),
			follow = True,
			callback = 'parse_opinion'
		),
	}

	def obtener_calificacion(self, texto):
		calif = texto.split("_")
		return calif[-1]

	def parse_opinion(self, response):
		sel = Selector(response)
		opiniones = sel.xpath('//div[@id="content"]/div/div')

		autor = sel.xpath('//h1/span/text()').get()

		for opinion in opiniones:
			item = ItemLoader(Opinion(), opinion)

			item.add_xpath('titulo', './/div[contains(@class, "_3IEJ3tAK")]/text()')
			item.add_xpath('calificacion', './/div[contains(@class, "_1VhUEi8g")]/span/@class', MapCompose(self.obtener_calificacion))
			item.add_xpath('contenido', './/q/text()')
			item.add_value('autor', autor)

			yield item.load_item()