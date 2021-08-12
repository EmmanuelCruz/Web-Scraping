from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Medicamento(Item):
	nombre = Field()
	precio = Field()

# Crawler
class FarmaciaCrawler(CrawlSpider):
	name = 'farmacia'

	custom_settings = {
	  'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
	  'CLOSESPIDER_PAGECOUNT': 10 
	}

	allowed_domains = ['farmaciasanpablo.com.mx']

	start_urls = ['https://www.farmaciasanpablo.com.mx/medicamentos/c/06']

	download_delay = 1

	rules = (
		# Horizontalidad
		Rule(
			LinkExtractor(
				allow=r'&page='
			),
			follow=True,
			callback = 'parse_medicamento'
		),
	)

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
