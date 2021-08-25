from typing import Container
import requests
import json

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
}

endpoint = "https://api.github.com/user/repos?page=1"

usuario = 'Aquí va usuario GitHub'
password = open('./password.txt').readline().strip()

response = requests.get(endpoint, headers=headers, auth=(usuario, password))

repositorios = response.json()

for repo in repositorios:
    print(repo['name'])
