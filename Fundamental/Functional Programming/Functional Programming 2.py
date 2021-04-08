#Functional Programming 2

#EJERCICIO! Map, Filter, Zip y Reduce.

from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def cap(item):
	return item.capitalize()

print("MAP: ",list(map(cap, my_pets)))



#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print("ZIP: ", list(zip(my_strings, sorted(my_numbers))))

#my_numbers.sort()
#print("ZIP: ", list(zip(my_strings, my_numbers)))			ASI LO HICE YO, NO RECORDABA EL SORTED :(



#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def over_50(item):
	return item > 50

print("FILTER: ", list(filter(over_50, scores)))

'''
Extra: si quisiera recibir dicha lista y ordenarla menor a mayor
new_list = list(filter(over_50, scores))
new_list.sort()
print(new_list)
'''



#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def accum(acc, item):
	return acc + item

print("REDUCE: ", reduce(accum, (my_numbers + scores)))						#(list1 + list2) concatena una lista con la otra
#print("REDUCE: ", reduce(accum, my_numbers, reduce(accum, scores, 0)))		#Recursividad?
print()

#------------------------------------------------------------------------------------------------------------------------

#LAMBDA EXPRESSIONS (FUNCTIONS)
#Son funciones hechas solo para ser utilizadas una sola vez y ya. No ocupan espacio en la memoria.

#Se describen de la forma:	'lamba parametro: accion(params)'

#EJEMPLO: Usando Map, Filter y Reduce.

list1 = [1, 2, 3, 4]															#parametro es 'item' y accion es 'item*2'
print("Lambda MAP: ", list(map(lambda item: item*2, list1)))					#Multiplicador por 2 ya hecho anteriormente
print("Lambda FILTER: ", list(filter(lambda item: item%2==0, list1)))			#Filtro de pares
print("Lambda REDUCE: ", reduce(lambda acc, item: acc + item, list1))			#Acumulador (NOTESE EL USO DE DOS PARAMETROS)

#EJERCICIO: Hacer una lambda expression en una linea que imprima la potencia de la lista:
to_pow_list = [5, 4, 3]
print("Lambda POW: ", list(map(lambda item: item**2, to_pow_list)))

#EJERCICIO: List Sorting, ordenar la lista de tuplas según el segundo valor de cada tupla, de manera ascendente.
sorting_list = [(0,2), (4, 3), (9, 9), (10, -1)]

sorting_list.sort(key = lambda x: x[1])			#En mi vida no iba a hacer esto yo x_x		IMPORTANTE
print("Lambda SORTING: ", sorting_list)			#'key' define un criterio para la ejecución del sort, de esta forma de define
												# que use [1] por cada una de las tuplas y así ordene la lista.
												#Así, 'key' será el valor devuelto por la expresión lambda.



