from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Propiedad(Item):
	informacion = Field()


# Crawler
class UrbaniaCrawler(CrawlSpider):
	name = 'Urbania'

	custom_settings = {
	  'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
	  'CLOSESPIDER_PAGECOUNT': 70 
	}

	allowed_domains = ['grupourbania.com.mx']

	start_urls = ['https://www.grupourbania.com.mx/resultados.php?estado=CDMX&delegacion=&colonia=&min_precio=1764560&max_precio=&min_tam=77&recamaras=',
				'https://www.grupourbania.com.mx/resultados.php?estado=Quer%C3%A9taro&delegacion=&colonia=&min_precio=955000&max_precio=3308216&min_tam=98&recamaras=']

	download_delay = 1

	rules = (
		# Horizontalidad por tipo de información (Noticias o videos)
		Rule(
			LinkExtractor(
				allow=r'/casas-y-departamentos/'
			),
			follow=True,
			callback='parse_propiedad'
		),
	)

	def limpia(self, text):
		return text.replace("\t","").replace("\r","").replace("\n","").strip()

	def parse_propiedad(self, response):
		item = ItemLoader(Propiedad(), response)

		item.add_xpath('informacion', '//div[@class="development-section__data-block"]/div/text()', MapCompose(self.limpia))

		yield item.load_item()