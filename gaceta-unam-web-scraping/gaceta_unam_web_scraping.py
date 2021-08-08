from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

# Clase para el articulo
class Articulo(Item):
	titulo = Field()
	descripcion = Field()

# Spider para el parse
class GacetaUnamSpider(Spider):
	name = "My Second Spider"

	custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
    } 

	start_urls = ['https://www.gaceta.unam.mx/comunidad']

	def parse(self, response):
		## CODIGO CON SOLUCION SCRAPY ##
		"""
		sel = Selector(response)

		articulos = sel.xpath('//div[contains(@class, "listing") and contains(@class, "listing-grid")]//article')

		print(f"Articulos: {len(articulos)}")
		for articulo in articulos:
			item = ItemLoader(Articulo(), articulo)

			item.add_xpath('titulo', './/h2[class="title"]/text()')
			item.add_xpath('descripcion', './/div[@class="post-summary"]/text()')

			yield item.load_item()
		"""

		## CODIGO CON SOLUCION USANDO BEATUTIFUL
		soup = BeautifulSoup(response.body, features="lxml")
		articulos = soup.find_all('article', class_ = "type-post")

		for articulo in articulos:
			item = ItemLoader(Articulo(), articulo)

			titulo = articulo.find('h2', class_ = 'title', recursive = True)
			if titulo != None:
				titulo = titulo.text
			else:
				titulo = "N/A"
			descripcion = articulo.find('div', class_ = 'post-summary', recursive = True)
			if descripcion != None:
				descripcion = descripcion.text
			else:
				descripcion = "N/A"

			item.add_value('titulo', titulo)
			item.add_value('descripcion', descripcion)

			yield item.load_item()