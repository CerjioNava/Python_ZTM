#SERVER

#Desde el quick start de flask:

from flask import Flask, render_template, url_for, request, redirect
import csv						#Para csv EXCEL.

app = Flask(__name__)			#Utilizamos la clase Flask para instanciar app, __name__ será __main__ .
	
#00- HOME
@app.route('/')					#Decorador. 
def my_home():
    return render_template('index.html')

#Generic web page function
@app.route('/<string:page_name>')		
def html_page(page_name=''):
    return render_template(page_name)	

#Función para escribir la información en un archivo de texto. Data es un diccionario.
def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\nEMAIL: {email}\nSUBJECT:{subject}\nMESSAGE: {message}\n')

#Función para escribir la información en un archivo de CSV.
def write_to_csv(data):
	with open('database.csv', mode='a', newline='') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter=';', quotechar='"', quoting = csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])

#SEND form
@app.route('/submit_form', methods=['POST', 'GET'])		#Get para enviar data añadiendo la info al url
def submit_form():										#Post para enviar data con un body text.
    if request.method == 'POST':
    	try:
    		data = request.form.to_dict()
    		write_to_csv(data)
    		return redirect('/thankyou.html')
    	except:
    		return 'Did not save to database'
    else:
    	return 'Something is wrong, try again.'


'''
PASOS PARA PYTHON ANYWHERE!!!

Para hacer que la url no sea la local utilizaremos la página web 'pythonanywhere' y
allí obtendremos un link. Para esto, usamos github y clonamos el proyecto. 

	git clone PAGINA_SSH_clone_de_git

En el proyecto clonado añadiremos los archivos que tentativamente cambiarán.

NOTA:
	PIP FREEZE captura el paquete instalado en el enviroment actual (venv). VENV fue 
	creado justamente para que podamos ejecutar nuestra app/server en diferentes 
	máquinas y environments.

'pip freeze > requirements.txt' en nuestra carpeta para añadir dicho archivo. Nos
muestra las apps instaladas en el proyecto para que funcione. ESTO ES IMPORTANTE!
De esta forma, pythonanywhere se encarga de instalar los paquetes necesarios.

Copiamos en el clonado: server.py, /templates, /static, database.csv, requirements.txt.

Nos dirigimos a nuestra carpeta clonada desde 'cmd' y hacemos:
	git add . 
	git commit -m"my portfolio website"
	git push origin master

De esta manera, subimos a git todo lo necesario. Ahora obtenemos la url clonada HTTPS.

En pythonanywhere, en el dashboard pulsamos en consola: BASH, abriendo así la consola
donde nuestra computadora es hosteada. escribimos

	git clone PAGINA_HTTPS_clone_de_git

Vamos al dashboard nuevamente, entramos a WEB APPS y escogemos framework (para esta caso
escogeremos manual configuration y escogemos nuestra versión de python).

Procedemos a configurar la web app. (Podemos ves los pasos de la página guardada :D)
	Source code: portfo

De la página de pasos, tomamos del setting up venv:
	mkvirtualenv --python=/usr/bin/python3.6 my-virtualenv
	pip install flask
Y esto lo ingresamos en la consola BASH de pythonanywhere nuevamente.

NOTA: también pudimos ingresar 'pip install -r requirements.txt' si eran muchas cosas.

Ahora volvemos a la WEB TAB e ingresamos en Virtual Env la ubicación de nuestra venv, 
en este caso: 'my_virtualenv'.

Ingresamos ahora al WSGI File, eliminamos todo lo no referente a flask y descomentamos
la parte del código de flask. Quedando allí:

	import sys
	path = 'home/Cerjio/portfo'
	if path not in sys.path:
		sys.path.append(path)

	from server import app as application		#server es nuestro server.py

Guardamos nuestro archivo WSGI.
Reload del website.
Entramos a la website.


'''
