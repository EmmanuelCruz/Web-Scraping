from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Hotel(Item):
	nombre = Field()
	descripcion = Field()
	precio = Field()
	facilidades = Field()

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