#4 PILARES DE LA PROGRAMACIÓN ORIENTADA A OBJETOS:

'''

1- Encapsulation: 	Se refiere a la unión de información y funciones que manipulan dicha información. 
					Todo esto se "encapsula" en un objeto grande donde cualquiera pueda interactuar con ella.
					Por ejemplo: En una clase se almacenan atributos y funcionalidades para todas las instancias.

2- Abstraction:		Solo se da acceso a lo que es necesario, puedes utilizar funciones o métodos sin necesidad de
					saber como funciona a todo detalle. Por ejemplo utilizar "len()" sin realmente saber como fue
					implementada la función, basta con saber que devolverá la longitud del objeto.
					Se "abstrae" del usuario lo que no es necesario. RECORDAR USAR CONVENCIONES DE PRIVATE Y PUBLIC

3- Inheritance: 	Permite a un objeto obtener las propiedades de otro objeto ya existente. IMPORTANTISIMO

4- Polymorphism:	Se refiere a como clases de objeto pueden compartir el mismo nombre para sus métodos pero con 
					funcionalidades distintas. Permite redefinir funciones para cada clase.

'''


#Un problema que puede existir con las clases es la sobreescritura de métodos o atributos por parte de un usuario
#externo, lo cual puede dañar nuestro código. Es decir:

class ExampleClass:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def speak(self):
		print(f'My name is {self.name} and I\'m {self.age} old')


player1 = ExampleClass("Sergio", 21)
player1.speak()

player1.speak = 'Esto sobreescribió mi función Speak()'
print(player1.speak, "\n")

#player1.speak()			Esta función ya no existe en player1, fue sobreescrita. ESTO ES UN PROBLEMA


#PRIVATE Y PUBLIC
#En python no existe la posibilidad del Private y Public como en otros lenguajes, básicamente todo es alterable (PUBLIC),
#sin embargo existe una convención donde las variables y funciones que deberían ser "privadas" se les añade al 
#inicio de su identificador un "_", tal que 'variable_privada' sea '_variable_privada'.

#DUNDER METHODS
#Son los métodos especiales built-in python definidos con "__" al inicio y final del mismo, tal como '__init__'.
#De igual forma es una convención de Python. PROVIENEN DE LA CLASE OBJECT de la que todos heredan.

#INHERITANCE:
#Para heredar de una clase a otra, basta con colocar en '()' la clase de la cual se va a heredar, así:

#PARENT CLASS
class User():
	def user_stats(self, name, health):
		self.name = name
		self.health = health

	def sign_in(self):
		print("logged in")

#CHILD CLASS
class Warrior(User):
	def __init__(self, strength):
		self.strength = strength
		super().sign_in()						#Super() se utiliza para referirse a la clase padre 

	def attack(self):
		print(f"{self.name} attack with {self.strength} of power!")

class Wizard(User):
	def attack(self):
		print("Esto es un ejemplo de polimorfismo, mismo nombre de funcion attack pero distintas clases")
	pass


warrior1 = Warrior(50)
warrior2 = Warrior(75)

warrior1.user_stats("Guerrero 1", 100)			#Me permite acceder al metodo de User
print("Player: ", warrior1.name)				#e imprimirlo, de igual forma se accede
												#al metodo sign_in

print(f"Fuerza: {warrior1.strength}")
warrior1.attack()

warrior2.user_stats("Guerrero 2", 150)
warrior2.attack()
print()

#ISINSTANCE: es una built-it function, que nos permite verificar si un objeto es instancia de una clase

print(isinstance(warrior1, Warrior))			#TRUE, warrior1 es clase Warrior	
print(isinstance(warrior1, User))				#TRUE, warrior1 es clase User porque HEREDA de ella
print(isinstance(warrior1, Wizard))				#FALSE, warrior1 NO es clase Wizard
print() 

#IMPORTANTE!!! 	TODOS los objetos en python HEREDAN de la clase OBJECT, tal que:

print(isinstance(warrior1, object))				#TRUE
print(isinstance(warrior1.name, object))		#TRUE
x = 10
print(isinstance(x, object))					#TRUE	
print()

wizard1 = Wizard()
wizard1.attack()
print()

#POLIMORFISMO EJEMPLOS:

#Función que llame attack
def player_attack(character):
	character.attack()

player_attack(warrior1)					#Se llama la misma función para ambos, sin necesidad de que la función
player_attack(wizard1)					#Sepa que tipo es el character

lista = [Warrior(100), Wizard()]
warrior3 = lista[0]





