#Web/Mobile Development
'''
Este es un curso de Python, por lo que no se verá a todo detalle el desarrollo web.

COMO FUNCIONAN LAS WEBSITE?

Un browser (cliente) al entrar a una página web hace un request al servidor, el cual
devuelve entonces una respuesta con la información necesaria (HTML, CSS, JS) para 
que el browser se capaz de interpretarla y mostrarla al usuario.

Se comunican a traves de los protocolos http/https.

El servidor posee 3 tipos de archivos (HTML, CSS y JS):

-HTML: Posee el contenido o texto de una página web.
-CSS: Posee la estilización de la página web (colores, imagenes, posicionamiento, etc).
-JS: Maneja y permite el comportamiento de la pagina web.

IMPORTANTE!
-Python puede ser utilizado para escribir la lógica, el comportamiento y las reglas sobre
las cuales un servidor debe actuar.
-Python posee librerías 'http' básicas para creación de servidores, y debido a que este
tema es muy común, existe una amplia variedad de librerías y FRAMEWORKS ya preparados.
Para este caso utilizaremos 'Flask', pero también existe 'Django' que es mucho más grande.

------------------------------------------------------------------------------------------

Flask es un "micro" framework con gran cantidad de herramientas, beneficios y seguridad ya
predeterminadas. Se utiliza sobretodo en backend.

Necesitamos crear un Virtual Environmet (venv) para manipular de una forma más limpia las
dependencias de nuestro proyecto. Esto se debe a que en algún momento pueden existir distintas
versiones de las librerías que utilicemos en el proyecto lo cual puede romper la compatibilidad
del proyecto mismo. 

Los VENV son independientes de cada proyecto, únicos por cada uno y por ende un proyecto no
alterará de manera negativa a otro.

------------------------------------------------------------------------------------------

Para crear el 'venv' basta con dirigirnos a la carpeta desde la consola y escribir:
'python -m venv venv'.

NOTA: el segundo argumento refiere a la ubicación. 
Usamos 'python -m venv Web_Server\' desde la carpeta superior.

Luego de crear el 'venv' se debe activar, mediante:
'venv\'Scripts\activate'

Para correr flask en 'server.py' mediante la consola, escribimos:

 	set FLASK_APP=server.py
	flask run

De esta manera se nos devuelve una dirección local:		
	http://127.0.0.1:5000/
Allí se imprime la función

Para activar 'debug mode' y hacer cambios a tiempo real:
	set FLASK_ENV=development

De esta manera, el servidor al detectar el cambio resetea automáticamente.

------------------------------------------------------------------------------------------

VER LOS HTML UTILIZADOS PARA COMPRENDER!

Templates: Es donde se almacenan los HTMLs. (Carpeta llamata 'templates')

Static Files: Son archivos que no cambiarán luego de ser enviados por el servidor (CSS o JS).
Para ello se crea una carpeta 'static' donde se encuentren estos archivos.

Favicon: Es el icono del website (para ventanas y marcadores). Se exige por la website de 
manera obligatoria. Googleamos y encontramos para añadir al html:

	<link rel="shortcut icon" href="{{ url_for('static', filename='cacoicon.ico') }}">

------------------------------------------------------------------------------------------

MIME TYPES: (Multipurpose Internet Mail Extensions)

Indica la naturaleza y formato de un documento, archivo, etc. Los browser lo utilizan para
determinar como procesar una URL, por ello los servidores deben enviar el correcto MIME en 
el response's Content-Type header. Sino, el browser malinterpreta el contenido y la página
no funcionara correctamente.

Para el web dev tenemos MIME Types como: 
-text/Plain, text/CSS, text/HTML, text/JS.
-Tambien image/, video/, audio/, etc.

------------------------------------------------------------------------------------------

IMPORTANTE: Para la creación del portafolio descargamos 'free templates'.

Los archivos '.gz' son versiones comprimidas de archivos como CSS y JS, de manera que la
información que se envíe al frontend (browser) desde el servidor sea más ligera.

Los archivos '.map' ayudan en el debugging.

------------------------------------------------------------------------------------------

CSV FILES: Comma Separated Values (EXCEL)


'''

