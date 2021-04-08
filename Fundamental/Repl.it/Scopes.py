#SCOPE
#-A que variables tengo acceso?

#Rules:
#1- Start with Local
#2- Parent Local
#3- Global
#4- Built in python functions

#Resumen: de adentro para afuera

#Global Keyword para acceder a variables globales:

total = 0

def count():
  global total
  total += 1
  return total

count()
count()
print(count())

total = 0
#SIGUE SIN SER EFICIENTE, entonces
def count():
  global total 
  total += 1
 
print(total) #0
count()
print(total) #1

#Nonlocal Keyword para utilizar variables que no son globales pero que se encuentran fuera del rango de la función en que se llama. Parent?

def outer():
  x = "local"   #llama a esta

  def inner():
    nonlocal x    #desde aqui
    x = "nonlocal"
    print("inner: ", x)
  
  inner()
  print("outer: ", x)

#Sin el nonlocal, las salidas serian local y nonlocal, y no nonlocal dos veces

outer()

z = '  Hello  '
z.upper()
print(z.upper())
