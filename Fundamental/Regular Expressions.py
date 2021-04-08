#Regular Expressions

#Python tiene una librería de expresiones regulares (RegEx)
import re

#Nota: Un Match Object es un objeto que contiene información sobre la búsqueda y el resultado.

#Ejemplo: Véase que...
something = 'Esto es solo un texto más, es normal'
#print('es' in something)					#Esta es la forma normal.

#Ahora con Regular Expressions:
print("Funciones con search:")
print("Search:", re.search('es', something))	#Devuelve un Match Object! Pero solo del primer encuentro.
a = re.search('es', something)					#También puede asignarse a una variable.
print("Span:", a.span())						#Imprime una tupla con la ubicación de la busqueda en el texto.
print("Start:", a.start())						#Devuelve donde comienza el texto buscado.
print("End:", a.end())							#Devuelve donde termina el texto buscado.
print("Group:", a.group())						#Devuelve la cadena de texto donde se encuentra.
print("String:", a.string)						#Devuelve el String donde se buscó (something)
print()

#IMPORTANTE: Si no se encuentra el texto buscado, no devolverá un Match Object, solo None, por
#ende no se puede acceder a los métodos de la forma anterior 'a.metodo()' y arrojará error.
#Así que podemos crear un patrón para evitar esto.

pattern = re.compile('es')					#Se crea un patrón de cadena de texto.
print("Compile:", pattern)
b = pattern.search(something)						#Igual se puede asignar a una variable
print("Search:", b)									#Y se busca directamente en un String.
print("Find All:", pattern.findall(something))		#Devuelve cada texto encontrado.
print("Full Match:", pattern.fullmatch(something))	#Devuelve None si el patrón no coincide
													#POR COMPLETO con el texto de busqueda.

pattern_fullmatch = re.compile('Esto es solo un texto más, es normal')	
print("Full Match:", pattern_fullmatch.fullmatch(something))	#Ahora si coincide por completo!										

pattern_match = re.compile('Esto es solo')
print("Match:", pattern_match.match(something))		#Devuelve si coinciden la cadena de texto al inicio.
print()

#Recordar googlear las distintas funcionalidades y secuencias utilizadas de esta librería!
#Como por ejemplo: Para la validación de un Email:

email = 'cerjionava@gmail.com'
email_not = 'Esto no es un email'
email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

print('Ejemplo de Email Validation:')
print(email_pattern.search(email))			#Devolverá el Match Object.
print(email_pattern.search(email_not))		#Devolverá None.
print()

#EXERCISE! EMAIL VALIDATION
#Password must have:
#- At least 8 char long
#- May contain any sort of letters, numbers and symbols ($%#@)

email_pattern2 = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
password_pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}[0-9]$")		#Todo esto es notación RegEx (REVISAR)
	
password = 'contrasena$3'							#Recordar 'ñ' no es parte de a-z.
print(password_pattern.findall(password))

def check_email(email_check):
	if email_pattern2.search(email_check):			#Usando el email_pattern2 ya definido
		print('Valid Email')
	else:
		print('Invalid Email')

def check_password(password_check):
	if password_pattern.search(password_check):		#Usando el password_pattern ya definido
		print('Valid Password')
	else:
		print('Invalid Password')

check_email(email)
check_password(password)
check_email('NotAValidEmail.@com')
check_password('Invalid Password')

#También hubiera servido usar 'fullmatch', pero Search es suficiente.
