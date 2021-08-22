from scrapy import item
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy import Request

# Almacenamiento base de la información
class Titles(Item):
    titulo = Field()
    titulo_frame = Field()

# Spider para la extracción
class W3SchoolCrawler(Spider):
    name = "ws3"

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'REDIRECT_ENABLED': True
    }

    allowed_domains = ['w3schools.com']
    start_urls = ['https://www.w3schools.com/html/html_iframe.asp']

    download_delay = 1

    def parse(self, response):
        sel = Selector(response)

        titulo = sel.xpath('//div[@id="main"]//h1/span/text()').get()

        print(titulo)

        previous_data = {
            'titulo': titulo
        }

        url_iframe = sel.xpath('//div[@id="main"]//iframe[@width="99%"]/@src').get()

        url_iframe = 'https://www.w3schools.com/html/' + url_iframe

        yield Request(url_iframe, callback=self.parse_iframe, meta=previous_data)
    
    def parse_iframe(self, response):
        item = ItemLoader(Titles(), response)
        item.add_xpath('titulo_frame', '//div[@id="main"]//h1/span/text()')

        item.add_xpath('titulo', response.meta.get('titulo'))

        yield item.load_item()
