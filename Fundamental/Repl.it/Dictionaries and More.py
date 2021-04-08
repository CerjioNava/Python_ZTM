#Dictionaries

#A diferencia de las listas [], este se define con corchetes {}
dict1 = {
  'a': 1,
  'b': '2b',
  'c': [3, 4, 5],
  'd': True,
  5 : 'value'
}

#Pueden contener casi cualquier variable/llave

print (dict1)
print (dict1['a'])
print (dict1[5])

print()

#Puedo crear listas con diccionarios adentro

list1 = [
  dict1,
  {
    'a': 1,
    2 : '2b',
    'etc': True
  }, 
  [3, 'hola', True]
]

print (list1)
print()

#Accediendo a un valor/llave del diccionario dentro de la lista
print (list1[1]['a'])
print (list1[0][5])
print (list1[0]['c'][1])
print ()

dict2 = {
  'basket': [1, 2, 3],
  'greet': 'hello',
  'age': 20  
}
print(dict2)
print()

#Si no existe la llave, devuelve None de esta forma y no un error (GET)
print (dict2.get('color'))

#A la vez, devolver un valor específico SOLO SI no existe la llave 
print (dict2.get('color', 'blue'))

#Si existe, imprime la existente
print (dict2.get('age', 55))
print()

#Se puede crear un diccionario de la forma
new_dict = dict(name = 'Cerjio')
print(new_dict)
#NO ES COMUN

#Se puede verificar si algo existe en el diccionario
print ('age' in new_dict)
print ('name' in new_dict)

print ('name' in new_dict.keys())
print ('Cerjio' in new_dict.values())
print()

#####
print(dict2.keys())
print(dict2.values())

#Items
print(dict2.items())
print()

#Copy
copy_dict = dict2.copy()
print("COPY\n" + str(copy_dict))

#Pop para eliminar una pareja
print(dict2.pop('basket'))
print(dict2)

#PopItem al azar
print(dict2.popitem())
print(dict2)
print()

#Update
print(dict1.update({'b':23}))
print(dict1.update({'b1':23}))
print(dict1)
