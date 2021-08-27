from os import path
import requests
from PIL import Image
import io

import random
from time import sleep
from selenium import webdriver
 
driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://www.olxautos.com.mx/autos_c84")

# Dar click 2 veces a la lista para cargar más elementos
boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')

for i in range(2):
    print(f"Primera parte de la página {i}")

    # Dar click y buscar puede lanzar algunas excepciones
    # - Cuando se da click al botón sin que exista
    # - Que haya un cuadro de publicidad sobre el botón
    try:

        # Da click al boton para cargar más elementos
        boton.click()

        # Dormir antes de mostrar los datos mientas se cargan y Randomizar el tiempo de espera entre acciones
        sleep(random.uniform(8.0, 10.0))

        # Redefinir el boton de carga de elementos
        boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
    except:
        break


# Realiza Scroll
driver.execute_script("window.scrollTo({top:0, behavior: 'smooth'});")
sleep(5)
driver.execute_script("window.scrollTo({top:20000, behavior: 'smooth'});")
sleep(5)

# Todos los coches de la lista
autos = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

# Número de imagen
img_num = 1

for auto in autos:
    precio = auto.find_element_by_xpath('.//div[@data-aut-id="itemPrice"]').text
    print(precio)
    descripcion = auto.find_element_by_xpath('.//div[@data-aut-id="itemTitle"]').text
    print(descripcion)

    # Extracción de imagen

    url_image = auto.find_element_by_xpath('.//img').get_attribute('src')
    image_content = requests.get(url_image).content

    image_file = io.BytesIO(image_content)
    imagen = Image.open(image_file).convert('RGB')

    path = './images/' + str(img_num) + ".jpg"

    with open(path, 'wb') as f:
        imagen.save(f, "JPEG", quality = 70)

    img_num += 1