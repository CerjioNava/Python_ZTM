#EJEMPLO DECORATOR MUY IMPORTANTE!

#En este ejemplo, veremos un uso importante de los decoradores donde utilizando la librería TIME
#podemos definir el tiempo que tarda en llevarse a cabo una función extensa (loop grande).

from time import time 									#Se importa de la librería

def time_performance(func):								#Base del decorador
	def wrap_function(*args, **kwargs):
		time1 = time()									#Comienza a correr el tiempo en una primera variable
		func(*args, **kwargs)							#Se llama la función que tomará mucho tiempo en terminar.
		time2 = time()									#Comienza a correr el tiempo en una segunda variable
		print(f'It took {time2-time1} seconds')			#Se imprime la diferencia de tiempo (inicio/final)
		#return wrap_function							#Se devuelve la función como se espera
	return wrap_function

@time_performance
def long_time():
	for i in range(1000000):
		i*5

long_time()												#NOTA: El tiempo de ejecución nunca será el mismo.


#EJERCICIO DECORADORES:
# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True 		#changing this will either run or not run the message_friends function.
}

def authenticated(fn):
 	def wrapper(user):
 		if(user['valid']):
 			return fn(user)
 	return	wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)




