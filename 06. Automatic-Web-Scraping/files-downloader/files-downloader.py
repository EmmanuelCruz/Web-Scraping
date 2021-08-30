import requests
from bs4 import BeautifulSoup

# URL Semilla
url = 'https://file-examples.com/index.php/sample-documents-download/sample-doc-download/'

response = requests.get(url)
soup = BeautifulSoup(response.text, features="lxml")

urls = []

files = soup.find_all('a', class_="download-button")

# Obtener las url's de los archivos
for file in files:
    urls.append(file['href'])

# Hacer el requerimiento de descarga de los archivos
i = 0
for url in urls:
    response_file = requests.get(url, allow_redirects=True)

    file_name = f'./archivos/file{i}.doc'
    i+=1

    out = open(file_name, 'wb')
    out.write(response_file.content)
    out.close()

