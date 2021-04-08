#Dos ejemplos dados por Andrei UNDER THE HOOD OF GENERATORS.

#NO ES NECESARIO SABERLO PERO NO ESTÁ DE MÁS TAMPOCO!

#Ejemplo 1:

def special_for(iterable):
  iterator = iter(iterable)				#Objeto iterable
  while True:
    try:
      iterator*5
      next(iterator)
    except StopIteration:
      break


#Ejemplo 2: Creando un generador propio

class MyGen:
  current = 0

  def __init__(self, first, last):
    self.first = first
    self.last = last
    MyGen.current = self.first 			#this line allows us to use the current number as the starting point for the iteration

  def __iter__(self):					#Esto permite la iteración del generador
    return self						 	#Devuelve la clase misma

  def __next__(self):
    if MyGen.current < self.last:		
      num = MyGen.current
      MyGen.current += 1
      return num
    raise StopIteration					#Si se acaba el rango de iteración, se detiene la iteración.

gen = MyGen(1,10)
for i in gen:
	print(i, end=' ')
print()

#EJERCICIO: NÚMEROS DE FIBONACCI 
#Con generadores, crear uno que imprima numeros de fibonacci según el rango que le otorguemos.

print('EJERCICIO FIBONACCI:')

#MI SOLUCION :(
def fib(num):
	n_2 = 0
	n_1 = 1
	yield n_2
	yield n_1
	for x in range(2, num+1):
		n = n_1 + n_2
		yield n_1 + n_2
		n_2 = n_1
		n_1 = n

#Solución Andrei (Mejor)
def fib2(num):
	a = 0
	b = 1
	for x in range(num+1):
		yield a
		temp = a
		a = b
		b += temp

for item in fib2(20):
	print(item, end='  ')





