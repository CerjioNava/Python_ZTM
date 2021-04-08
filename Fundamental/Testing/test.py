#test.py

import unittest		#Importamos el Unittest
import Testing		#Importamos el __main__

#Se crea una clase que herede de...
class test_main(unittest.TestCase):
	
	#Función default de unittest (setUp)
	def setUp(self):
		print('About to test')		#Se ejecuta en cada método testeado.

	#Test para comprobar que la función devuelve un valor esperado
	def test_do_stuff(self):
		'''TEST COMMENT'''
		test_num = 10 
		result = Testing.do_stuff(test_num)
		self.assertEqual(result, 50)					#OK		

	#Test para comprobar que la función devuelve un error esperado.
	def test_do_stuff2(self):
		test_num = 'No admite string, solo int' 
		result = Testing.do_stuff(test_num)
		self.assertIsInstance(result, ValueError)		#OK

	#Test para comprobar que la función devuelve un error por Type
	def test_do_stuff3(self):
		test_num = None 
		result = Testing.do_stuff(test_num)
		self.assertIsInstance(result, TypeError)		#OK

	#Test para comprobar que la función devuelve 
	def test_do_stuff3(self):
		result = Testing.do_stuff()
		self.assertEqual(result, 5)		#OK

	#Función default de unittest (tearDown)
	def tearDown(self):
		print('Cleaning up')		#Se ejecuta al final de cada método testeado.


#IMPORTANTE: Solo queremos que este archivo se ejecute si es ESTE el archivo main 
#que vamos a ejecutar para el test. No queremos que ejecutando el resto del proyecto
#se ejecute el archivo de prueba tambie.

if __name__ == '__main__':
	print('TEST:')
	unittest.main()				#EJECUTA EL TEST (OK si todo esta bien, FAIL si no lo está)
								#Luego de el test, no corre más código.

#Los métodos assert sirven para reportar fallas.

#NOTA: En un test no es tan importante preocuparse por un código eficiente, interesa 
#mucho más la legibilidad del código. Recordar que el test no se exporta en el proyecto

#Para correr TODOS los test creados en nuestro proyecto desde la cónsola:
#	python3 -m unittest
#	python3 -m unittest -v 			(Esto si quiero mayor detalle del test)