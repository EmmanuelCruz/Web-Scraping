from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Para agregar un encabezado
opts = Options()
opts.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
)

driver = webdriver.Chrome("../chromedriver.exe", options=opts)

# Se obtiene la página de la URL semilla
driver.get('http://www.fciencias.unam.mx/docencia/horarios/indiceplan/20221/1556')

links_courses = driver.find_elements_by_xpath('//div[@id="info-contenido"]//a')
url_list = []

print(len(links_courses))

for tag_a in links_courses:
    url_list.append(tag_a.get_attribute("href"))

print(len(url_list))

# Web Scraping vertical
for link in url_list:
    try:
        driver.get(link)

        materia = driver.find_element_by_xpath('//div[@id="info-contenido"]//h2').text

        print(f"Materia {materia}".upper())

        # Extracción de la página
        cursos = driver.find_elements_by_xpath('//div[@id="info-contenido"]/table')
        
        for curso in cursos:
            profes = curso.find_elements_by_xpath('.//a')

            counter = 0

            for profe in profes:
                if counter == 0 and profe.text!="":
                    print(f"Profesor: {profe.text}")
                elif profe.text!="":
                    print(f"Ayudante: {profe.text}")
                counter += 1
            
            print("\n")
        
        print("\n")

        driver.back()
    except Exception as e:
        driver.back()
        print(e)
