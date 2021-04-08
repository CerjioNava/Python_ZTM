#Tuplas y Set

#TUPLAS
print("TUPLES\n")

#Son listas inmutables, básicamente

tuple1 = (1, 2, 3, 4)
tuple2 = tuple(range(5, 9))

print(tuple1)
print(tuple2)

#Dentro de un diccionario las tuplas si pueden ser utilizadas como llaves 

dict1 = {
  (1, 2): 'tupleKey',
  ('a', True) : 5
}

print(dict1[(1,2)])

#Puedo copiar una nueva tupla 
new_tuple = tuple1[1:3]
print (new_tuple)

#Para asignar valores de otra forma
a, b, *other = tuple1
print (a, b, other)
print()

#Metodos Count e Index
print(tuple1.index(4))
print(tuple1.count(3))
print()


#SET
print("SET\n")

#Colección sin orden de objetos únicos

set1 = {1, 2, 3, 4, 4}
print(set1)

#El "4" no se repetira en la impresión, será un objeto único, no se añadiran objetos repetidos al set

#Si añado valores nuevos o repetidos
set1.add(10)
set1.add(2)   #No se añadira
print(set1)

#Para convertir una lista con valores repetidos a un SET 
lista = [6, 7, 8, 4, 4, 10, 10]
set2 = set(lista)
print(set2)
#ELIMINA LOS REPETIDOS
#Es la misma logica para convertir de lista a set

#SET NO TIENEN INDEX, no pueden obtenerse los valores con index


#METODOS SET

#1- Difference, diferencia entre el primer set con el segundo

print("\nDifference entre set1 y set2")
print(set1.difference(set2))
 
#2- discard, elimina el valor de un set si existe
print("\nDiscard en set2")
set2.discard(10) #elimina 
print(set2)
set2.discard(5) #no elimina
print(set2)

#3- difference_update, 
print("\ndifference_update en set1 vs set2")
print(set1)
set1.difference_update(set2)    #elimina el 4 de set 1
print(set1)
print(set2)

#4- intersection, devuelve los valores compartidos entre 2 sets
print("\nintersection en set1 con set3")
set3 = [2, 3, 4]
print (set1.intersection(set3))
#Tambien con & funciona (AND) (set1 & set3)

#5- isdisjoint, devuelve true o false si los sets no comparten valores, respectivamente
print("\nisdisjoint entre set1 y set2, set1 y set3")
print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))

#6- union, une un set con otro y elimina repetidos
print("\nunion entre set1 y set2")
print(set1.union(set2))
#Tambien con | funciona (OR) (set1 | set2)

#issubset y issuperset. issubset define si un set se encuentra en otro (1, 2) en (1, 2, 3, ...) por ejemplo. issuperset define si un set posee lo mismo que el otro al menos")



