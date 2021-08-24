import requests
from lxml import html

head = {
    'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
}

login_form = 'https://github.com/login'

# Mantener la sesión abierta
session = requests.Session()

login_form_res = session.get(login_form, headers=head)

# Para obtener el authenticity token
parser = html.fromstring(login_form_res.text)

a_token = parser.xpath('//input[@name="authenticity_token"]/@value')

login_url = 'https://github.com/session'

login_data = {
    "login": "usuario@correo",
    "password": open('password.txt').readline().strip(),
    "commit": "Sign in",
    "authenticity_token": a_token
}

session.post(
    login_url,
    data=login_data,
    headers=head
)

data_url = 'https://github.com/Usuario?tab=repositories'

respuesta = session.get(data_url, headers=head)

parser = html.fromstring(respuesta.text)
repositorios = parser.xpath('//h3[@class="wb-break-all"]/a/text()')

for repo in repositorios:
    print(repo)