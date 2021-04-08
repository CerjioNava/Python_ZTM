#Functions

#Se definen con "def"

def say_hello():
  print("helloooo")

say_hello()

#Para llamar una función, tiene que haber sido declarada antes de la llamada :(

#Así que debemos definir las funciones al inicio

#Parámetros: dentro de () como name o age en la definición de la función (creación)

#Argumentos: parámetros con que se llama la función después

def say_something(name, age):
  print(f"My name is {name} and I'm {age} old")

say_something("Sergio", 21)
say_something(21, "Sergio")

#Los parámetros y argumentos utilizados fueron POSICIONALES, son los más ideales

#Keyword arguments: se específica el argumento, pero no es recomendable
say_something(age=22, name="Maria")

#Default parameters: si no le llama con parámetros, la función corre con sus parámetros predeterminados
def say_other(name="Cerjio", age=21):
  print(f"Nombre: {name}   Edad: {age}")

say_other()
say_other("Cesar")
say_other("Cesar", 54)
print()

#Lo anterior fueron procesos, ahora funciones que devuelvan valores:

def sum(num1, num2):
  return num1 + num2

print(sum(2, 4))

x = sum(3, 5)
print(x)

print(sum(x, 3))

#Se puede definir una función dentro de otra
def sum2(n, m):

  def sum3(o, p):
    return o+p
  
  return sum3(n,m) + n

print(sum2(1,2))

#Return devuelve un valor de la función y sale automáticamente de la función

#Los Métodos se utilizan como ".nombre_metodo()" como list.append(). Los métodos los poseen las clases