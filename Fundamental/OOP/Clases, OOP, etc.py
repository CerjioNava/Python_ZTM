#OOP, Clases, etc.

class PlayerCharacter:

	#Class Objects Attributes								#Para cosas que no deberán cambiarse en las instancias
	membership = True										#Es "estático", no dinámico

	#Constructor de la clase
	def __init__(self, name, age):							#Self se refiere a la instancia (objeto) de esta clase.
		
		if self.membership:									#PlayerCharacter.membership
			self.name = name								#Atributos "dinámicos" específicos para cada instancia
			self.age = age

	#Funcion a la que podemos acceder desde afuera
	def run(self):
		print('run')
		print(f'My name is {self.name}')					#Sin el self no se accede al name, ya que name no es un atributo
		return 'done'										#de la clase sino que es definida en el constructor

	def run2(self, message):
		print(message)

	#PARA CREAR METODOS QUE PUEDAN SER UTILIZADOS SIN INSTANCIAR UN OBJETO
	#podemos utilizar @classmethod y @staticmethod

	#Utilizamos decorativos para definir metodos de clase y staticos
	@classmethod
	def class_method1(cls, num1, num2):						#cls es para referirse a la clase 
		return num1 + num2

	#Se puede usar "cls" para instanciar un objeto en la clase (llamando al constructor)
	@classmethod
	def class_method2(cls, num1, num2):						#cls es para referirse a la clase en general
		return cls('Teddy', num1 + num2)					#como si llamara el __init__

	#Los métodos estáticos funcionan igual que los classmethod a diferencia de que static no permite usar "cls"
	@staticmethod
	def static_method1(n1, n2):
		return n1 + n2

	#LOS CLASSMETHOD se utilizan más para cuando se quiera acceder a los Class Objecs Attributes
	#LOS STATICMETHOD se utilizan más cuando no sea necesario lo anterior, y se trabaje independiente a ellos



print(PlayerCharacter.class_method1(1, 2))

player3 = PlayerCharacter.class_method2(1, 3)	#Usa un class method para instanciar
print(f"Class Method 2: {player3.age} \n")


#Instanciando players
player1 = PlayerCharacter("Cerjio", 21)
player2 = PlayerCharacter("Sergio", 19)

#Se le puede añadir un atributo desde fuera de la clase
player2.attack = 50

#Se imprime a los atributos de las clases
print(player1.age)
print(player2.name)
player1.run()						
print(player2.run()	)				#También hay acceso a Run
player2.run2("Imprime esto")		


#EJERCICIO!

#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

cat1 = Cat("Miau1", 1)
cat2 = Cat("Miau2", 2)
cat3 = Cat("Miau3", 3)

# 2 Create a function that finds the oldest cat

def oldest_cat(*cats):
	return max(cats)
	
	'''
	old_cat = None
	
	for i in cats:
		if old_cat == None or old_cat.age < i.age:
			old_cat = i

	return old_cat
	'''

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f"The oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old")