#Functional Programming 3

#List, Set and Dictionary Comprehension (Finishing Functional Programming)

#LISTA Y SET EJEMPLO: Manera tradicional y luego utilizando comprension

#TRADICIONAL
lista_tradicional = []
for char in "hello":
	lista_tradicional.append(char)
print("Tradicional: ", lista_tradicional)

#COMPREHENSION 	
lista_comprehension = [char for char in "hello"]		#Se usa [param_adicionar for parametro in iterable]
print("Comprensión: ", lista_comprehension)
print()

lista_comprehension2 = [num*2 for num in range(0, 10)]
print("Comprensión 2: ", lista_comprehension2)

lista_comprehension3 = [num**2 for num in range(0, 10) if num % 2 == 0]		#SE PUEDEN AÑADIR CON UN CONDICIONAL!!!!!!!!!!!
print("Comprensión 3 PARES: ", lista_comprehension3)

#Para los SET es la misma lógica, solo que usamos {} en vez de []. Además los valores no estarán realmente
#ordenados y ninguno será repetido.

#DICTIONARY EJEMPLO:

simple_dict = {'a':1, 'b':2, 'c':3, 'd':4}						

dict1 = {key:value**2 for key,value in simple_dict.items()}						#Crea un diccionario y cada valor **2
print("DICTIONARY: ", dict1)

dict2 = {key:value**2 for key,value in simple_dict.items() if value % 2 == 0}	#Crea diccionario según el condicional (pares)
print("DICTIONARY 2: ", dict2)

dict3 = {num:num*2 for num in [1, 2, 3]}				#Ambas key y value derivadas del mismo num
print("DICTIONARY 3: ", dict3)


#EJERCICIO DE COMPRENSIÓN
#Igual que ejercicio pasado. ENCONTRAR LOS DUPLICADOS, esta vez con Comprensión!

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

'''	Solución antigua
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
'''

#duplicates = [char for char in some_list if (some_list.count(char) > 1)]	#Pero imprime (b, b, n, n) Solo debe ser (b, n)
duplicates = list(set( [char for char in some_list if (some_list.count(char) > 1)] ))
print(duplicates)

#COMPRENSIÓN PUEDE LLEGAR A SER CONFUSO PARA OTROS PROGRAMADORES QUE NO HAYAN HECHO EL CÓDIGO, POR ESO EVITAR 
#COMPLICACIONES COMO EN ESTA OCASIÓN!
