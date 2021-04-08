#Generators
#Permiten generar una secuencia de valores sobre tiempo.
#Permiten pausar y resumir una función.
#Son iterables.
#Se usa 'yield'

#Un ejemplo de un generador es la función 'range()', que devuelve una secuencia pero no inmediatamente.

#EJEMPLO: Vease la diferencia

#Sin generador
def make_list(num):
	result = []
	for i in range(num):
		result.append(i)
	return result

my_list = make_list(10)
print("Creando una lista normal: \n", my_list)

#Con generador
def generator_function(num):
	for i in range(num):
		yield i							# Yield pausa la función y continua cuando se le ordena (Next)
										# SUSPENSIÓN DE ESTADO

print("Devolviendo uno a uno los valores sin crear una lista:")
for item in generator_function(10):
	print(item, end=' ')

print()

gen = generator_function(4)
print('\n',gen)							#Ubicación en la memoria del generador
print(next(gen))				#0		#Cada Next continua el loop y vuelve a detenerse en Yield
print(next(gen), next(gen))		#1 y 2
print(next(gen))				#3
#print(next(gen))						#Arroja error porque se acaba la iteración, no existe más numeros fuera del rango 4!



#Los generadores son super eficientes cuando se trata de calculos de listas MUY GRANDES, por ejemplo:
#Del archivo 'Decorators TIME EXAMPLE'

from time import time 									#Se importa de la librería
def time_performance(func):								#Base del decorador
	def wrap_function(*args, **kwargs):
		time1 = time()									#Comienza a correr el tiempo en una primera variable
		func(*args, **kwargs)							#Se llama la función que tomará mucho tiempo en terminar.
		time2 = time()									#Comienza a correr el tiempo en una segunda variable
		print(f'Tardó {time2-time1} segundos')			#Se imprime la diferencia de tiempo (inicio/final)
	return wrap_function

@time_performance
def time_gen(num):
	print('Con generador:', end=' ')
	for i in range(num):					#Nótese aquí la diferencia (GENERADOR)
		i*5

@time_performance
def time_list(num):
	print('Sin generador:', end=' ')
	for i in list(range(num)):				#Nótese aquí la diferencia (LISTA)
		i*5

print('NÓTESE LA DIFERENCIA!')
time_gen (1000000)							#Para el mismo rango de numero, sin generador tarda más!
time_list(1000000)	

#						