#Functional Programming
#Al igual que OOP, separa los problemas en multiples cosas para mantener un mejor orden.

#Divide y vencerás.

##Separa Data y Functions! A diferencia de los 4 pilares de OOP, aquí todo se resume a 
#Pure Functions, separando la data y el comportamiento de un programa.

#Al final, la idea es hacer el código más limpio, legible, facil de hacerlo crecer y mantener, eficiente y DRY.

#Utilizaremos OOP y Functional Programming a la vez.

'''
PURE FUNCTIONS
En vez de tener un "encapsulamiento" de información como en el OOP (i.e. clases), aquí tendremos nuevas reglas:
-Para la misma entrada siempre tenga la misma salida. 
-No debe tener "efectos colaterales" que afecten fuera de dicha función (i.e. print desde la función o modificar
 variables ajenas a la función).
'''

#Ejemplo de una función pura:

def multiply_by2(li):					# No se altera ninguna variable externa ni imprime.
	new_list = []
	for item in li:
		new_list.append(item*2)
	return new_list

print("Función Pura:", multiply_by2([1, 2, 3]))


#Ejemplo de una función NO pura:

new_list2 = []							# La función está ALTERANDO una variable externa "new_list2"
def multiply_by2NO(li):
	for item in li:
		new_list2.append(item*2)
	return print("Función NO Pura:", new_list2)				# Está imprimiendo desde la función 

multiply_by2NO([1, 2, 3])	
print()

#Nótese que ambas funciones otorgan la misma salida, pero si por ejemplo 'new_list2' es alterada antes de
#llamar a la función (i.e. se sobreescriba como un string), la función dará un error y es problemático.
#Mientras más funciones puras existan, menos bugs podrán existir. Sin embargo, no siempre serán todas puras.

#-------------------------------------------------------------------------------------------------------------

#MAP, FILTER, ZIP, REDUCE.		Funciones importantes!

#MAP: 
#Tiene multiples funcionalidades, vease...

def multiply_by2MAP(item):										#Se observa la diferencia de cantidad de código a
	return item*2												#comparación de las funciones anteriores, sin crear
																#new_list para luego devolverla, map simplifica todo.	
print("MAP: " , list(map(multiply_by2MAP, [1, 2, 3])))
print(map(multiply_by2MAP, [1, 2, 3]))							#En si, Map recibe el nombre del método y los argumentos
																#iterables. El resto lo hace solo. Devuelve el objeto creado
																#en la ubicación específica de la memoria.
list1 = [1, 2, 3, 4]
print("list1*2 MAP: " , list(map(multiply_by2MAP, list1)))
print("list1: ", list1, "\t\tLa función no afecta el original")
print()

#FILTER:
#Filtra resultados, vease...

def only_par(item):								#AHHHHHHHHHHHHHHHHHHHH
												#if item % 2 == 0:		
												#	return item 				
	return item % 2 == 0						#El filtro al determinar si es true o false, devuelve item o no, respectivamente.

print("FILTER par: ", list(filter(only_par, list1)))

def only_a_init(item):					#Para practicar... una función que devuelve solo los string con inicial 'A'
	return item[0] == 'A'

print("FILTER A: ", list(filter(only_a_init, ['Alvaro', 'Sergio', 'Lili', 'Amer'])))
print()

#ZIP:
#Toma como argumentos a objetos iterables y los agrupa juntos en una nueva lista de tuplas.

#list1 = [1, 2, 3, 4]
list2 = [10, 20, 30]
tuple1 = ("Nombre 1", "Nombre2")
print("ZIP: ", list(zip(list1, list2, tuple1)))
print()

#REDUCE:
#Aplica una función de dos argumentos acumulativos a los items de la secuencia (izq a der), reduciendo
#la secuencia a un valor único. Básicamente suma todos los valores de una secuencia.

def accumulator(acc, item):
	print("Acumulado: ", acc, "Item: ", item)
	return acc + item

from functools import reduce 							#Tema avanzado :(
print("REDUCE: ", reduce(accumulator, list1, 2))		#La secuencia es list1 y el valor inicial del acumulador (2 i.e.).

