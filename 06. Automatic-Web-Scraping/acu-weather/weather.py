from twisted.internet import reactor
from twisted.internet import task
from twisted.internet.task import LoopingCall
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.spiders import Spider

class WeatherExtractor(Spider):
    name = "Wheater"
    
    custom_settings = {
	  'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
	}
    
    start_urls = ['https://www.accuweather.com/es/mx/mexico-city/242560/weather-forecast/242560',
                    'https://www.accuweather.com/es/mx/guadalajara/243735/weather-forecast/243735',
                    'https://www.accuweather.com/es/mx/monterrey/244681/weather-forecast/244681']
    
    download_delay = 1

    def parse(self, response):

        ciudad = response.xpath('//h1/text()').get()
        current = response.xpath('//a[contains(@class, "cur-con-weather-card")]//div[@class="temp"]/text()').get()
        real_feel = response.xpath('//a[contains(@class, "cur-con-weather-card")]//div[@class="real-feel"]/text()').get()

        # Limpiando
        real_feel = real_feel.replace('RealFeel®', '').replace('°','').replace('\n','').replace('\t','').replace('\r','').strip()
        current = current.replace('°','').replace('\n','').replace('\t','').replace('\r','').strip()

        print(ciudad)
        print(current)
        print(real_feel)

        f = open("datos-clima.csv", "a")
        f.write(f"{ciudad},{current},{real_feel}\n")
        f.close()

runner = CrawlerRunner()
task = LoopingCall(lambda: runner.crawl(WeatherExtractor))
task.start(20)

reactor.run()