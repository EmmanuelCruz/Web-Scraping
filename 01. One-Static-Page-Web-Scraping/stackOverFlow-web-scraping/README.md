# Web Scraping estático de StackOverFlow Questions.
## Emmanuel Cruz Hernández

----

## Descripción

Aplicación de web scraping estático de una sola página hacia el sitio web de [StackOverFlow](https://es.stackoverflow.com/questions/). Este web scraping es básico del nivel uno.
En este, se utilizará _BeautifulSoup_ para resolver el problema junto con _requests_.

----

## Parse
El parse, está dado por la clase BautifulSoup. Se crea un objeto que recibe como parámetro el texto del archivo HTML, que anteriormente se obtuvo con un objeto de tipo _requests_ y la función _get_.

		soup = BeautifulSoup(answer.text)

Donde answer es el resultado de la función _get_.

## Extraer información
Para este ejemplo, nos gustaría extraer cada una de las preguntas que se encuentra en el listado de preguntas más frecuentes en StackOverFlow. La estrategia es ver la estructura del archivo HTML, buscar su padre, poner atención en las clases o id de las etiquetas y ver como están compuestos los hijos de los datos que deseamos extraer.

Para este ejemplo en particular, se puede notar que las preguntas están dentro de un _div_ que en particular cuenta con un id llamado ***questions***. A su vez, cada pregunta está en un div con una clase ***question-summary***. Cada una de las preguntas está en una etiqueta ***h3*** que es hija de un div con clase ***summary***. Con esta información, ya podemos hacer la extracción de cada una de las preguntas en la página.

Beautiful soup cuenta con una función llamada _find_ que recibe varios parámetros opcionales, relacionados a la búsqueda que se requiere hacer. En este caso, lo primero que debemos buscar es un div con id="questions".

		contenedor = preguntas = find(id = "questions")

**Importante**: esta función solo devuelve un elemento. Que sirve perfecto para el caso del contenedor, ya que estamos hablando de un id. Pero para cada uno de los hijos que contiene las preguntas, podemos usar la función **find_all**.

		preguntas = contenedor.find_all(class_="question-summary")

Y finalmente, para ver cada una de las preguntas, podemos iterar la lista y buscar todos los _h3_.

		for pregunta in preguntas:
			p = pregunta.find("h3")
			descripcion = pregunta.find(class_="excerpt")
			print("PREGUNTA: " + p.text)
			print("DESCRIPCION: " + descripcion.text.replace("\n", "").strip())

Una de las ventajas de _BeautifulSoup_ respecto a _LXML_, es que si no cuenta con algún mecanismo para encontrar alguna etiqueta por sus atributos, puede navegar con sus primos, sus hijos o su padre. Por ejemplo, si quisiera la siguiente etiqueta _div_ en los primos, lo podría hacer con

		for pregunta in preguntas:
			p = pregunta.find("h3")
			descripcion = pregunta.find_next_sibling("div").text
			print("PREGUNTA: " + p.text)
			print("DESCRIPCION: " + descripcion.text.replace("\n", "").strip())

Nótese que en el segundo ejemplo, para obtener la descripción, no se necesitó de un atributo de la etiqueta para ubicarlo, sino que se accede a este por la navegación entre los familiares de la etiqueta, en este caso, las etiquetas primas.

----


## Instalación de bibliotecas

Aquí se muestra un listado de los recursos utilizados para aplicar web scraping en este proyecto.

		pip install requests


		pip install beautifulsoup4
