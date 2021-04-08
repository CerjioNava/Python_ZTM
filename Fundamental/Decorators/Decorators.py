#DECORATORS
#Se declaran con '@' y sobrecargan las funciones para darle funcionalidad extra.
#Son funciones que 'envuelven (wrap)' otra función y la mejora.

#EXTRA: Las funciones ocupan espacio en la memoria como las variables

def hello():
	print ('helloooo')

greet = hello 		#Podemos asignar una función a otra.
print(hello)		#Devuelve la ubicación en la memoria de la función.
print(greet) 		#Ambas tendrán la misma ubicación entonces.
greet()				#Tambien se puede llamar la 'misma' función.
del hello 			#Elimina la función, ya no puede llamarse hello()
print(greet())		#None, ya que greet aun llama la misma ubicación
					#Pero no encuentra la función
print()

def hello2(func):	#Las funciones pueden tener otras funciones como parámetros.
	func()

def greet():
	print("Still here!")

a = hello2(greet)	#Asigna la función, que a su vez se ejecutra
print(a)
print()

#----------------------------------------------------------------------------------------

#Higher Order Function (HOC)
#1- Puede ser una función que acepta otra función como parámetro.
#2- Puede ser una función que DEVUELVA otra función.

#Ejemplo 1:
def high_func(func):	#Ya se vio la funcionalidad en los ejemplos
	func()				#anteriores

#Ejemplo 2:
def high_func2():
	def func2():
		return 5
	return func2

funct = high_func2()	#Devuelve la función
print("Funct Ubicación: ", funct)			#Devuelve ubicación
print("Funct: ", funct())			#Devuelve 5
print()

#----------------------------------------------------------------------------------------

#DECORATORS (ahora si)

def base_decorator(func):		#ESTRUCTURA BASE DE UN DECORADOR!
	def wrap_function():		#Envuelve una función y la mejora
		func()
	return wrap_function

def my_decorator(func):			#Ejemplo de un decorador personal
	def wrap_function():		#Donde 'func()' será 'hello()' u otra
		print('********')		
		func()					#Queda en medio de la 'decoración'
		print('********')
	return wrap_function

@my_decorator
def hello():
	print('helloooo')

@my_decorator
def bye():
	print('bye')
	print('byeeeeee')

hello()
print()
bye()
print()

#IMPORTANTE!!!! Forma más visual de los decoradores:

def hello_again ():
	print('Mas visual!')

my_func = my_decorator(hello_again)			#Esto se resume con un @my_decorator 
my_func()									#sobre hello_again()

#Otra forma:
my_decorator(hello_again)()					#Básicamente, esto hace el '@'
print()

#Ahora, si queremos un decorador con funciones que tomen parámetros:

def my_decorator2(func):					#Ejemplo de un decorador personal
	def wrap_function(*args, **kwargs):		#Donde 'func()' será 'hello()' u otra
		print('********')		
		func(*args, **kwargs)				#Queda en medio de la 'decoración'
		print('********')
	return wrap_function

@my_decorator2
def new_hello(message, emoji = ':)'):
	print (message, emoji)

new_hello("Holaaa con argumentos", ':)')