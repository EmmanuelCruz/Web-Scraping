# Web Scraping aplicado a Udemy, en la sección de búsqueda _Python_.
## Emmanuel Cruz Hernández

----

## Descripción

En este ejemplo se extraen datos de Python encontrados en la página de [Udemy](https://www.udemy.com/courses/search/?src=ukw&q=python). Para la extracción de datos de este ejemplo se utiliza una técnica basada en API's, ya que no se puede hacer extracción con ninguna de las formas vistas anteriormente, ya que Udemy, así como otras plataformas, trabajan con carga de datos que se van llenando en la estructura HTML después de que la página es cargada, por lo que en principio es un HTML _vacío_.

----

## Extracción de datos

A diferencia de los niveles anteriores de _Web Scraping_, el basarse en una API puede tener ciertos problemas con los permisos de la página con la extracción del API. Puede lanzar una reestricción sobre los permisos de la extracción de datos, lanzando una respuesta _403_. Para resolver esto, es necesario ver los encabezados y verificar cuál es encabezado necesario que se involucra en la petición y definirlo en el _headers_. En este caso, para Udemy es necesario tener el header _referer_.

        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
            "referer": "https://www.udemy.com/courses/search/?src=ukw&q=python"
        }

Para este ejemplo sí se realizar un proceso de almacenamiento de datos pero es completamente opcional, bien se puede imprimir únicamente la información.

        # Cursos totales
        total_cursos = []

La paginación se puede hacer con el análisis del archivo JSON que provee la API. Viendo el patrón de diseño, podemos obtener la información con las distintas URL's asociadas a cada página. En este caso obtenemos información de los cursos en _Python_ de la página 1 a 3.

Por cada iteración se realiza la petición al servidor, se obtienen el arreglo que contiene los cursos y de cada curso se extrae el nombre, la cantidad de reviews y el rating de cada curso.

        # Hacer paginación
        for i in range (1, 3):
            url_api = f'https://www.udemy.com/api-2.0/search-courses/?src=ukw&q=python&skip_price=true&p={i}'

            response = requests.get(url_api, headers=headers)

            data = response.json()

            cursos = data['courses']

            for curso in cursos:

                # Almacenando los datos
                total_cursos.append({
                    "curso": curso['title'],
                    "reviews": curso['num_reviews'],
                    "rating": curso['rating']
                })

El almacenamiento de datos es independiente de la extracción de datos, así que el siguiente paso es opcional. Primero se crea la tabla, mostramos los datos y almacenamos el resultado en una archivo con extensión _CSV_.

        # Creando la tabla
        df = pd.DataFrame(total_cursos)

        print(df)

        df.to_csv("cursos_python.csv")

----

## Módulos necesarios

Para este ejemplo se requiere requests.

        pip install requests

Opcionalmente, si se requiere de un almacenamiento de datos, se requiere del módulo _pandas_.

        pip install pandas