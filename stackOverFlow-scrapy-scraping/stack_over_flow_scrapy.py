from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

# Clase para la pregunta
class Pregunta(Item):
	pregunta = Field()
	descripcion = Field()

# Spider para el parse
class StackOverFlowSpider(Spider):
	name = "My Spider"

	custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
    } 

	start_urls = ['https://stackoverflow.com/questions']

	# Parser
	def parse(self, response):
		sel = Selector(response)
		preguntas = sel.xpath('//div[@id="questions"]//div[@class="question-summary"]')

		for pregunta in preguntas:
			item = ItemLoader(Pregunta(), pregunta)
			item.add_xpath('pregunta', './/h3/a/text()')
			item.add_xpath('descripcion', './/div[@class="excerpt"]/text()')

			yield item.load_item()