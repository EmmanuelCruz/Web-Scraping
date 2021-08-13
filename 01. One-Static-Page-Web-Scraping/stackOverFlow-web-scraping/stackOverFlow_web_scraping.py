import requests
from bs4 import BeautifulSoup

head = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
    } 

url = "https://es.stackoverflow.com/questions/"

answer = requests.get(url, headers = head)

soup = BeautifulSoup(answer.text)

contenedor = soup.find(id = "questions")
preguntas = contenedor.find_all(class_="question-summary")

for pregunta in preguntas:
	p = pregunta.find("h3")
	descripcion = pregunta.find(class_="excerpt")
	print("PREGUNTA: " + p.text)
	print("DESCRIPCION: " + descripcion.text.replace("\n", "").strip())
