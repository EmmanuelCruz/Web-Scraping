import requests
from bs4 import BeautifulSoup

url = "https://es.stackoverflow.com/questions/"

answer = requests.get(url)

soup = BeautifulSoup(answer.text)

contenedor = soup.find(id = "questions")
preguntas = contenedor.find_all(class_="question-summary")

for pregunta in preguntas:
	p = pregunta.find("h3")
	descripcion = pregunta.find(class_="excerpt")
	print("PREGUNTA: " + p.text)
	print("DESCRIPCION: " + descripcion.text.replace("\n", "").strip())