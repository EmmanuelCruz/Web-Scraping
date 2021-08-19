from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Para agregar un encabezado
opts = Options()
opts.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
)

driver = webdriver.Chrome("../chromedriver.exe", options=opts)

# Se obtiene la página de la URL semilla
driver.get('https://twitter.com/login')

# Acceso a usuario y contraseña
usuario = 'emmanuel.cruzhe@gmail.com'
password = open('password.txt').readline().strip()

## Obtención de inputs para ingresar a Twwiter
input_user = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//main//input[@name="session[username_or_email]"]'))
)
input_pass = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//main//input[@name="session[password]"]'))
)

# Para llenar los inputs

input_user.send_keys(usuario)
input_pass.send_keys(password)

####### Apartir de aquí, el navegador llena los campos. #######

# Identificación del botón de inicio de sesión

boton_inicio = driver.find_element_by_xpath('//main//div[@data-testid="LoginForm_Login_Button"]//div[@dir="auto"]')

boton_inicio.click()


# Obteniendo todos los twetts
tweets = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//section//article//div[@dir="auto"]'))
)

for tweet in tweets:
    print(tweet.text)