#Useful Modules

from collections import Counter, defaultdict, OrderedDict

#Counter:
li = [1, 2, 3, 4, 4, 5, 5, 2, 5]
print(Counter(li))								#Crea un diccionario que indica cuantas veces un item
print()											#se repite dentro de un objeto iterable.

sentence = 'Ejemplo de string para el counter'
print(Counter(sentence))

#defaultdict:
dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print(dictionary['a'])		#Todo normal
print(dictionary['b'])		#Todo normal
print(dictionary['c'])		#La llave 'c' no existe, pero imprimira el string dado y no un error!
print()

#OrderedDict:
#Retiene el orden insertado de un diccionario.

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 2
d2['b'] = 1

print(d)
print(d2)
print(d==d2)					#False, distintos valores de key:value
print()

#Datetime: ejemplo

import datetime						#MUY UTIL!

print(datetime.time(5, 45, 2))
print(datetime.date.today())
print()

#Arrays
#Los arrays consume menos memoria que una lista.

from array import array

arr = array('i', [1, 2, 3])
print(arr)
print(arr[0])


#Linting:
#Permite ver errores en el código mientras escribimos.

#'pdb' (Python Debugger) es un builtin module.
#Python Debugger for interactive interpreters.

import pdb					#Recordar usar ctrl+w

def add_2(num1, num2):
	pdb.set_trace()			#Recordar usar 'help' dentro de la consola para ver las acciones.
	return num1+num2

print('pdb: ', add_2(2, 3))
