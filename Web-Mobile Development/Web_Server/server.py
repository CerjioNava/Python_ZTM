#SERVER

#Desde el quick start de flask:

from flask import Flask, render_template, url_for

app = Flask(__name__)			#Utilizamos la clase Flask para instanciar app, __name__ será __main__ .
	
@app.route('/')					#Decorador. 
def hello_world():
    return render_template('index_home.html')

    #return 'Hello, CERJIOOOO!'	#Enviamos un string pero Flask lo envía de forma 'html', así el browser lo interpreta.
    							#Para enviar HTML directamente, usamos la librería render_template.

@app.route('/blog')		
def blog():
    return render_template('index_blog.html')		#Así enviamos el html directamente.

@app.route('/blog/2020/dogs')		
def dogs():
    return 'THIS IS A BLOG ABOUT DOGS'

#@app.route('/favicon.ico')		
#def favicon():
#    return 'THIS IS A BLOG ABOUT DOGS'

@app.route('/user/<username>')					#Para trabajar con variables
def user(username='Enter username'):
    return render_template('index_user.html', name = username)	#Le pasamos un parámetro al html

@app.route('/user/<username>/<int:post_id>')
def userID(username='Enter username', post_id=0):
    return render_template('index_userID.html', name = username, id = post_id)	


#Cuando se llama render_template, busca el archivo en una carpeta 'templates' por default.
#TODOS los htmls se encuentran en templates.

'''
Para correr flask mediante la consola, escribimos:

 	set FLASK_APP=server.py
 	flask run

De esta manera se nos devuelve una dirección local:		
	http://127.0.0.1:5000/
Allí se imprime la función

Para activar 'debug mode' y hacer cambios a tiempo real:
	set FLASK_ENV=development

De esta manera, el servidor al detectar el cambio resetea automáticamente.

------------------------------------------------------------------------

NOTA: No dejar espacio antes o despues del '='

NOTA: Pueden haber varias funciones para una misma ruta, pero solo se imprimirá
la primera que encuentre en el código. SIN EMBARGO, no pueden haber dos funciones
con el mismo nombre aún con distintas rutas.

'''