from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

# Para agregar un encabezado
opts = Options()
opts.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
)

driver = webdriver.Chrome("chromedriver.exe", chrome_options=opts)

# Se obtiene la página de la URL semilla
driver.get('https://autos.mercadolibre.com.mx/refacciones-autos-camionetas/')

while(True):
    links_products = driver.find_elements(By.XPATH, '//a[@class="ui-search-link"]')
    url_list = []

    for tag_a in links_products:
        url_list.append(tag_a.get_attribute("href"))

    # Web Scraping vertical

    for link in url_list:
        try:
            driver.get(link)

            # Extracción de la página
            titulo = driver.find_element_by_xpath('//h1').text
            precio = driver.find_element_by_xpath('//span[@class="price-tag-fraction"]').text

            print(titulo)
            print(precio)

            driver.back()
        except Exception as e:
            driver.back()
            print(e)

    try:
        boton_next = driver.find_element(By.XPATH, '//span[text()="Siguiente"]')
        boton_next.click()
    except:
        print("Ya no hay más páginas por recorrer")
        break