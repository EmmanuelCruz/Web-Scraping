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


# Todos los coches de la lista
autos = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

for auto in autos:
    precio = auto.find_element_by_xpath('.//div[@data-aut-id="itemPrice"]').text
    print(precio)
    descripcion = auto.find_element_by_xpath('.//div[@data-aut-id="itemTitle"]').text
    print(descripcion)