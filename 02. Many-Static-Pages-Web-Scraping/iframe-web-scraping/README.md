# Extracción de datos con Web Scraping de una página padre y un iFrame
## Emmanuel Cruz Hernández

---- 

## Descripción

En este ejemplo se muestra la extracción de datos de una página que contiene un iFrame. 

Un iFrame es una estructura HTML que funciona como una página independiente contenida en una página web padre. Tal cuál como ejemplos de páginas web que se encuentran en la página de [w3schools](https://www.w3schools.com/html/html_iframe.asp) con sus ejemplos de iFrames.

----

## Extracción de datos

Los primeros pasos de la extracción es idéntica a la de los ejemplos anteriores. La diferencia viene en la carga de otra página que se encuentra dentro de una página padre. El acceso a esta página es un requerimiento a la otra página a través de un Request, que recibe la URL de la página hija y la información necesaria que se requiera de la página padre con el parámetro _meta_, que en este caso es un diccionario.

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

Por otro lado, se define otro parse que funcionará para la página hija. Este parse se comporta idéntico a los pasados con la diferencia que se utilizan los datos de la página padre con el parámetro _meta_.

        def parse_iframe(self, response):
            item = ItemLoader(Titles(), response)
            item.add_xpath('titulo_frame', '//div[@id="main"]//h1/span/text()')

            item.add_xpath('titulo', response.meta.get('titulo'))

            yield item.load_item()

----

## Importaciones requeridas

        from scrapy.item import Field
        from scrapy.item import Item
        from scrapy.spiders import Spider
        from scrapy.selector import Selector
        from scrapy.loader import ItemLoader
        from scrapy import Request