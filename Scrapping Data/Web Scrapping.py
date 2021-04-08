#Web Scrapping

#Se trata de, por medio de la programación, obtener data (información) de un website, limpiarla 
#de manera que sea util para nosotros el manejo de esa información.

#IMPORTANTE!
#HTML: Posee el contenido de una página web.
#CSS: Para la estilización de la página web.
#JS: Maneja el comportamiento de la información.

#IMPORTANTE!
#Cada website tiene información extraible y no extraible. Podemos saber esto entrando al
#robots.txt del website, añadiendo '/robots.txt' al final del url.

#Dentro del robots.txt se pueden observar listas extensas sobre permisos (allow y disallow)
#del tipo de información que el User-Agent puede extraer. Todo lo que no esté 'disallowed' 
#en la lista puede ser utilizado, y lo que esté 'allowed' serán rutas específicas (hijas) de
#alguna ruta padre que se encuentra 'disallowed'.
#Ejemplo: 'Disallow: /accounts' y 'Allow: /accounts/usernames'

#No debe utilizarse la información obtenida para métodos comerciales.

#Google Bot: Es el User-Agent que Google utiliza para indexar websites. Ya que Google es un motor
#de busqueda que indexa todas las páginas web de la red en una base de datos. 
#Este es quien realiza el web scrapping para definir de que trata la página web.
#Más o menos de esto se trata el SEO (Search Engine Optimization).

#Utilizaremos la librería 'Beautiful Soup' para web scrapping. Es muy famosa.

