#Enumerate
#Devuelve un objeto enumerado, es decir, los index de todas las iteraciones del item

#Ejemplo con un string
for i, char in enumerate("holaaa"):
  print(i, char)

print()

#Ejemplo con una lista o tupla
for i, char in enumerate([1, 2, 3]):
  print(i, char)

print()

#Ejemplo con un diccionario
for i, char in enumerate({'a':1,'b':2}):
  print(i, char)

print()

#Ejemplo 
for i, char in enumerate(list(range(10))):
  if char == 5:
    print ("index: " + str(i))
    print (f'index: {i}')

print()

#WHILE LOOPS
print("WHILE LOOPS:\n")
count = 0

while count < 10:
  
  count+=1

  if count == 4:
    print("Continue")
    continue
    
  if count == 6:
    print("Pass")
    pass

  if count == 8:
    print("Breaking")
    #break   #Rompe en su totalidad

  print(count)
  #
else:   
  #Else solo correra si termina el while, si se hace break no sucedera
  print("While loop finished")




