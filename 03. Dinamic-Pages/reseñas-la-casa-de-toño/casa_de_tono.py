import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
 
# Acción para realizar scroll con JavaScript
scrolling_script = """
    document.getElementsByClassName('section-layout section-scrollbox cYB2Ge-oHo7ed cYB2Ge-ti6hGc')[0].scroll(0, 100000)
"""

# Para agregar un encabezado
opts = Options()
opts.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
)

driver = webdriver.Chrome("chromedriver.exe", options=opts)

# Se obtiene la página de la URL semilla
driver.get('https://www.google.com.mx/maps/place/La+Casa+de+To%C3%B1o/@19.3460137,-99.2731642,12z/data=!4m11!1m2!2m1!1sla+casa+de+to%C3%B1o!3m7!1s0x0:0x3466b88c477ff25c!8m2!3d19.3643183!4d-99.2872466!9m1!1b1!15sChBsYSBjYXNhIGRlIHRvw7FvIgOIAQFaEiIQbGEgY2FzYSBkZSB0b8Oxb5IBEm1leGljYW5fcmVzdGF1cmFudA?hl=es')

sleep(random.uniform(4.0, 5.0))

# Se harán 3 scrillins para cargar las reseñas
SCROLLS = 0
while SCROLLS!=2:
    # Se realiza el scroll
    driver.execute_script(scrolling_script)

    # Esperar antes de realizar la acción
    sleep(random.uniform(7.0, 13.0))

    # Se aumenta la cantidad de scrolls actuales
    SCROLLS += 1

restaurant_review = driver.find_elements(By.XPATH, '//div[@jstcache="435"]')

print(f"Elementos encontrados: {len(restaurant_review)}")

for review in restaurant_review:

    client = review.find_element_by_xpath('.//span[@jstcache="408"]').text
    tiempo = review.find_element_by_xpath('.//span[@jstcache="242"]').text
    resena = review.find_element_by_xpath('.//span[@jstcache="246"]').text

    print(f"""
    Nombre: {client}
    Fecha: {tiempo}
    Reseña:
    {resena}
    """)
