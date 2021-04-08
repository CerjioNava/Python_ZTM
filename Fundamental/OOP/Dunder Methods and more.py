#DUNDER METHODS
#Son los métodos especiales built-in python definidos con "__" al inicio y final del mismo, tal como '__init__'.
#De igual forma es una convención de Python. PROVIENEN DE LA CLASE OBJECT de la que todos heredan.

#INTROSPECTION
#Determinar el tipo de un objeto durante la ejecución del código. 
# dir() devuelve todas las funciones y métodos de un objeto según su clase, más que nada los DUNDER METHODS

#EJERCICIO:

#Se puede heredar de una clase de python directamente
class SuperList(list):
	def __len__(self):
		return 1000

super_list1 = SuperList()
print(len(super_list1))					#Devolvera 1000 ya que cambiamos su función

super_list1.append(5)					#Se puede ya que la clase hereda de "list"
print(super_list1[0])

print(issubclass(SuperList, list))		#issubclass devuelve si una clase es subclase de la otra
print(issubclass(list, object))
print(issubclass(list, SuperList))
print()


#MULTIPLE INHERITANCE			IMPORTANTE!

class User():
	def sign_in(self):
		print("logged in")

	@staticmethod
	def log_out():
		print("logged out")

class Stats():
	def new_stats(self, health, power):
		self.health = health
		self.power = power

#Clase Monster deriva de User y Stats, posee sus métodos
class Monster(User, Stats):
	
	def __init__(self, name):
		self.name = name
		super().new_stats(100, 50)
		super().sign_in()

	def scream(self):
		print("Monster is screaming loudly!")

	def death(self):
		User.log_out()							#Es un método estático

new_monster = Monster("Slime")
print(f'Monter name: {new_monster.name}')
new_monster.scream()
new_monster.log_out()
new_monster.death()

print()

#Mientras más clases se hereden más complicado se puede volver, así que hay que trabajar lo más ordenado posible, por ello:

#MRO - Method Resolution Order
#Es una regla que Python sigue para determinar el orden de una estructura/jerarquía de herencia multiple.

#Ejemplo:  A <--- (B, C) <--- D

print("MRO Example:")

class A():			
	num = 10

class B(A):
	num = 2	
	pass

class C(A):
	num = 1

class D(B, C):		#Orden de la herencia: B y luego C.
	pass

print(D.num)		#Se imprimira "2" de la clase B, ya que es el primer valor "num" en el orden de la herencia
print(D.mro())		#Con esta función se imprime el orden de herencia y se observa: D, B, C, A, object.



