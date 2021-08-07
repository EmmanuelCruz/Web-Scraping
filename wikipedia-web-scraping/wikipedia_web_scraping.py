import requests
from lxml import html

"""
head = {
	
}
"""

url = "https://www.wikipedia.org/"

answer = requests.get(url)

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