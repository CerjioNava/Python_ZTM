#Password Checker

#Legítimamente la mejor manera de verificar si una clave como la tuya fue hackeada alguna vez.
#Y así decidir si tu clave es buena para ser usada o no.

import requests				#Nos permite hacer requests			(REVISAR DOCUMENTACIÓN)
import hashlib				#Para interpretar el código hash 	(REVISAR DOCUMENTACIÓN)
import sys

#Usaremos una API (Application Programming Interface) para comunicar entre dos aplicaciones.
'''
url = 'https://api.pwnedpasswords.com/range/' + 'password123'		#API de pwnedpasswords
response = requests.get(url)										#Obtenemos la respuesta con el url
print(response)														#Imprimimos la respuesta
'''
#NOTA: Importante saber que respuesta representa el código, i.e. [400] no es bueno. [200] si es bueno.

#NOTA: así como utilizamos el api es incorrecto, necesitamos usar 'hash' para almacenar y utilizar 
#información de manera segura. Utilizaremos por ahora un hash generator de SHA1.

#Una función HASH genera un patrón a partir de un valor asignado, por seguridad y mayor eficiencia
#durante el acceso de la información.

#No utilizaremos el código Hash completo: CBFDAC6008F9CAB4083784CBD1874F76618D2A97	(password123)
#Solo se otorga los primeros 5 valores: CBFDA
#Hecho esto, si se obtiene una respuesta [200]

#--------------------------------------------------------------------------------------------------

#Request the api data.		RECIBE LOS 5 CHAR Y DEVUELVE LA RESPUESTA DEL API
def request_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char	#CBFDA para password123
	response = requests.get(url)								#Obtenemos la respuesta con el url

	#Si la respuesta no es adecuada.
	if response.status_code != 200:	
		raise RuntimeError(f'Error Fetching: {response.status_code}, check the API and try again.')
	else:
		print(response, 'Good Response!')						#Imprimimos la respuesta

	return response												#Devolvemos la respuesta

#Get password leaks. 		COMPARA LA CLAVE CON LA RESPUESTA DEL API Y DEVUELVE EL CONTEO
def get_password_leaks_count(hash_response, hash_to_check):					
	#print(hash_response.text)												#Podemos imprimir la lista hash de primeros 5 char.
	hashes = (line.split(':') for line in hash_response.text.splitlines())  #split() divide el string en items de una lista según el parámetro de separación.
																			#splitlines() divide el string donde cada linea es un item de la lista.
	for h, count in hashes:
		if h == hash_to_check:
			return count
	return 0

#Check password if it exist in API response.	CONVIERTE LA CLAVE EN HASH, LLAMA EL REQUEST/CONTEO Y DEVUELVE	
def pwned_api_check(password):								
															#Para password = '123'
	#password.encode('utf-8')								#Imprime: b'123'
	#hashlib.sha1(password.encode('utf-8'))					#Imprime un objeto sha1 HASH y su ubicación
	#hashlib.sha1(password.encode('utf-8')).hexdigest() 	#Devuelve una cadena de texto hexadecimal del valor	

	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()	#Transforma a sha1
	first5_char, tail = sha1password[:5], sha1password[5:]						#Se divide
	response = request_api_data(first5_char)									#Se llama la 1ra función
	
	print('PASSWORD:', password)
	print('PASSWORD IN HASH:', first5_char, tail)
	return get_password_leaks_count(response, tail)			#Pudimos dejar esa función como parte de esta.

#Función principal que recorre todas las demás.		RECIBE LAS CLAVES Y DEVUELVE LOS RESULTADOS
def main(args):								#*args si es desde aqui, args si es por consola
	for password in args:
		count = pwned_api_check(password)
		if count:
			print(f'{password} was found {count} times... you should change your password', '\n')
		else:
			print(f'{password} was not found, carry on!', '\n')
	return 'Done!'


if __name__ == '__main__':
	print('\nSearching...\n')
	sys.exit(main(sys.argv[1:]))		#Para salir del proceso (imprimirá 'done!' del main())
	#main('password123')

