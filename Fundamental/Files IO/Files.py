#FILE I/O

my_file = open('file_example.txt')				#Si no específicamos el modo, por default: mode='r' (READ)

print(my_file)									#Indica el nombre del archivo, el modo de apertura, etc.
print("Primera Lectura:\n" + my_file.read())			#Lee el archivo (solo puede hacerse una vez)

#Si queremos devolver el cursor en el archivo al inicio para poder leer...
my_file.seek(0)
print("Segunda Lectura:\n" + my_file.readline(), end='')		#readline() lee linea a linea
stream_string = my_file.readline()								#Podemos asignar a un string
print(stream_string)										#Se observa el contenido del string
print(my_file.read())					#Ya aquí leera la tercera linea, donde quedó el cursor.

my_file.seek(0)
print(my_file.readlines())				#Devuelve una lista con el contenido del texto
print()

#IMPORTANTE: Es necesario cerrar el archivo luego de que ya no sea necesario.
my_file.close()

#Para evitar las complicaciones anteriores...
#Built in statements para File I/O

with open ('file_example.txt') as my_file:			
	print("Usando with open! Cerrará solo")
	print(my_file.readlines())

with open ('to_write.txt', mode='w') as my_file2:		#Para escribir usamos mode='w'	
	text = my_file2.write('Escribiendo...')				#Para escribir y leer usamos mode='r+'
	print(text)

'''
#NOTA:
 'r' es para leer nada más (es el default)
 'w' es para escribir, y sobreescribe sobre el archivo EN BLANCO. Puede crear uno nuevo si no existe.
 'r+' es para lectura y escritura, pero sobreescribe sobre el texto 'existente', no elimina el contenido.
 'a' es Append, añade lo que se quiera al final del archivo.
'''
#Si queremos escribir en un archivo no existente (NUEVO) usamos 'w'.

with open ('new_file.txt', mode='w') as my_file3:
	text = my_file3.write('NUEVO ARCHIVO!')
	print(text)

#Si el archivo no esta en la misma carpeta que este código '.py', hay que especificar mejor
#el file path. Por ejemplo 'otra_carpeta/archivo.txt' (relative path).

#En otro caso se puede usar un 'absolute path', que proviene desde C:/... pero no es común.

#Para acceder directamente a la carpeta (Files IO) de este archivo .py, se usa './' al inicio
#de la ruta. Por ejemplo: './archivo.txt' o './otra_carpeta/archivo.txt'

#Si se utiliza '../' se accede a la carpeta atras de esta, es decir, en este caso se accedería
#a la carpeta 'Curso Udemy'.

#NOTA: para windows, linux y mac, los files paths son distintos.
#Se puede utilizar el módulo 'pathlib' que permite que funcione en los tres sistemas.

#IMPORTANTE: Utilizar si es necesario TRY para evitar errores:

try:
	with open ('new_file.txt', mode='r') as my_file4:
		text = my_file4.read()
		print('LECTURA TRY:', text)
except FileNotFoundError as err:
	print('File not found!')
except IOError as err:
	raise err