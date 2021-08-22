import requests
import pandas as pd

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
    "referer": "https://www.udemy.com/courses/search/?src=ukw&q=python"
}

# Cursos totales
total_cursos = []

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


# Creando la tabla
df = pd.DataFrame(total_cursos)

print(df)

df.to_csv("cursos_python.csv")