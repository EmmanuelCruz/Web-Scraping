import requests
from lxml import html

head = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
    } 

url = "https://www.wikipedia.org/"

answer = requests.get(url, headers = head)

parser = html.fromstring(answer.text)

ingles = parser.get_element_by_id("js-link-box-en")

# Imprimir el contenido del elemento con id 'js-link-box-en'
print(ingles.text_content())

ingles2 = parser.xpath("//a[@id='js-link-box-en']/strong/text()")

print(ingles2)

# Se obtienen todos los idiomas.

idiomas = parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()")

for idioma in idiomas:
	print(idioma)
