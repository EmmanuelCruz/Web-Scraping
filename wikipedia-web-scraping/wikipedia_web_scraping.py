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

print(ingles.text_content())