#Sending Emails with Python

from email.message import EmailMessage		#Modulo built-in que trae Python para emails.
import smtplib								#Permite crear un servidor SMTP (Simple Mail Transfer Protocol)
											#para la conexión entre el cliente y el servidor.

from string import Template					#REVISAR DOCUMENTACIÓN. Aquí tenemos funciones muy utiles.
from pathlib import Path					#Parecido a 'os.path', nos permitira acceder al archivo html.

#NOTA: Revisas la librería smtplib y email.

html = Template(Path('index.html').read_text())		#Se lee el texto html y se convierte en template, para
													#así modificar directamente el $name.

email = EmailMessage()						#Creamos una variable clase
email['from'] = 'Sergio Nava'				#Añadimos quien envía, a quien y el título
email['to'] = 'cerjionava@gmail.com'
email['subject'] = 'Wenaaaaaas'

#El contenido del email puede ser un texto normal, un archivo html traducido, etc...

#email.set_content('Aprendiendo a enviar emails desde Python! :D')			#Se añade el contenido del email
email.set_content(html.substitute(name = 'BRO! This was $name!'), 'html') 	# {name:'Hey!', ...}

#El contenido está en html, así que debe indicarse en el segundo parámentro.

#NOTA: Al utilizar set_content más de una vez, solo se almacena el contenido del
#ultimo llamado. Se sobreescribe el contenido.

print('Sending email...')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:	#Con smtp se define el host y el puerto (estandar)
	smtp.ehlo()												#Parte del protocolo, no es obligatorio saber.
	smtp.starttls()											#Mecanismo de encriptado
	smtp.login('cerjionava@gmail.com', 'Zerolegendario0')	#Log en el servidor
	smtp.send_message(email)								#Se envía el mensaje
	print('Message was send!')