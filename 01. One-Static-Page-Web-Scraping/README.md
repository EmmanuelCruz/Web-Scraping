# Static One Page Web Scraping
## Emmanuel Cruz Hernández

----

## Descripción

Ejemplos de aplicación de forma teórica y práctica de Web Scraping, aplicado en particular a páginas estáticas y a un única URL para la extracción de diferentes datos.

----

## Encabezados

Son los datos necesarios para hacer una petición como un usuario. En particular, un encabezado tiene un atributo llamado _user-agent_, que contiene información del navegador y el sistema operativo que se está utilizando para la extracción de datos.

Esta información pasa como parámetro a la función _get_ en los _headers_. En caso de no pasar este parámetro, el valor por default para _headers_ es _boot_ y es más sencillo detectar la aplicación de web scraping.

 Sistema                       | USER-AGENT
 ----------------------------- | -------------
 WINDOWS + GOOGLE CHROME       | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36
 WINDOWS + GOOGLE CHROME       | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36
 WINDOWS + GOOGLE CHROME       | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36
 WINDOWS + GOOGLE CHROME       | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36
 WINDOWS + GOOGLE CHROME       | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36
 MAC + SAFARI 11.1             | Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15
 WINDOWS + INTERNET EXPLORER   | Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
 LINUX + CHROME 44             | Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36
 ANDROID + CHROME 70           | Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36


----

## Prácticas

* wikipedia-web-scraping: implementación de web scraping, manejando la página principal de forma estática para el acceso a elementos particulares con ***Requests***, ***LXML*** y ***XPATH***.
* stackOverFlow-web-scraping: implementación de web scraping para obtener las preguntas más frecuentes, junto con su descripción. En esta primera versión, se utiliza ***BeautifulSoup*** y ***Requests***.
* stackOverFlow-scrapy-scraping: implementación de web scraping para obtener las preguntas más frecuentes de StackOverFlow utilizando únicamente ***Scrapy***.
* gaceta-unam-web-scraping: implementación de web scraping para obtener el título de las notas, y su descripción del apartado de _Comunidad_ en la Gaceta de la UNAM utilizando ***Scrapy*** y ***BeautifulSoup***.
