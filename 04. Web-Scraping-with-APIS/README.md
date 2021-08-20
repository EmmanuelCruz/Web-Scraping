# Web Scraping con APIs
## Emmanuel Cruz Hernández.

----

## Descripción

En esta sección se realizan ejercicios de extracción de datos basados en APIs que son independientes de la estructura de la página Web. Esta extracción de datos depende de un mecanismo que está completamente relacionado al servidor o la página web, que ya provee parte de la información a extraer.

Este formato de extracción de datos se muestra en un JSON. La desventaja es que si no está documentado, se debe indagar en una investigación para conocer el funcionamiento.

Algunas API's públicas son las que provee _Facebook_ y _Twitter_.

## ¿Qué es un API?

Un API se encarga de establecer una vía de comunicación entre lo que quieres hacer el usuario (el requerimiento) y lo que debe ser ejecutado dentro de una plataforma, lo cual devuelve al usuario una respuesta. Se pueden ver como el túnel de información, recibiendo retroalimentación del procedimiento. Es en sí, una abstracción de funciones y procedimientos.

Un API puede retornar información en diversos formatos tales como XML o JSON. Además pueden ejecutar procesos de manera remota o realizar alguna acción dentro de una plataforma, tal como eliminar un registro de una base de datos o invocar otros procedimientos.

## ¿Qué es una RESTful API?

Actualmente **REST**(_Representation State Transfer_) es la lógica más utilizada para la construcción de APIs de aplicaciones de software interactivas que trabajan sobre un esquema cliente servidor. Como tal es una lógica de restricciones y recomendaciones bajo la cual se puede construir una API.

Finalmente, **RESTful API** es una API ya implementada que se contruye a aprtir de la lógica de REST. Estas trabajan bajo una arquitectura Cliente-Servidor utilizando HTTP como protocolo. Una petición REST a u servidor requiere de tres elementos importantes:

* Verbo HTTP: objetivos del requerimiento del cliente, entre los más usados son GET, POST, PUT, PATCH, DELETE.
* URI: 
* Datos necesarios del requerimiento (como parámetros)