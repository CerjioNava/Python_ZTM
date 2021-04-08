#Matrix

matrix = [
  [1, 'a', True],
  [2, 'b', False, "hey"],
  [3, 'c']
]

#Imprimo la matriz separada
print (str(matrix[0]) + "\n" + str(matrix [1]) + "\n")

#Imprimo solo un valor
print (matrix[0][1])
print()

#Longitud de la matriz (x)
print (len(matrix))
print()

#Añado una lista a la matriz
matrix.append([1, 2])
print (matrix[3])
print()

#Añado un valor a una lista
matrix[0].append("hey")
print (matrix[0])
print()

#Añado varios valores a una lista
matrix[2].extend(["Other", "another"])
print (matrix[2])
print()

#Inserto un valor en un lugar de la matriz
matrix[2].insert(2, "hello")
print (matrix[2])
print()

#Remuevo un valor de la matriz
matrix[2].remove('another')
print (matrix[2])
print()

#Vacío una lista completa pero sigue existiendo
matrix[3].clear()
print(matrix)
print()

#Elimino el ultimo valor de la matriz (una lista)
new_list = matrix.pop()
print(matrix)
print()

#Pop si devuelve valor
print ("New List: " + str(new_list))

#index
print (matrix[0].index('a'))

#Python keywords
print ('b' in matrix[1])
print ('hey' in 'oh hey eoh')

#Contador en listas
print (matrix[0].count('a'))

#sort
#matrix[0].sort()
#print(matrix[0])
#Recordar Sorted

#Reverse voltea la lista
matrix[0].reverse()
print (matrix[0])
print()

#Reverse list creando una nueva sin afectar la original
print (matrix[0][::-1])
print (matrix[0])
print()

#Puede crearse una lista predeterminada de la manera
print(list(range(2, 10)))
print(list(range(10)))

#.join es un metodo str
sentence = ' - '
new_sentence = sentence.join(['hi', 'all', 'good?'])
print (new_sentence)

#Tambien join asi
sentence2 = ' __ '.join(['yeah', 'all', 'good'])
print (sentence2)

#List Unpacking
a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)
print()

d, e, f, *other, g = [1, 2, 3, 4, 5, 6, 7, 8]
print(d)
print(e)
print(f)
print(other)
print(g)
print()

#None (es parecido al Null)
weapon = None
print(weapon)
