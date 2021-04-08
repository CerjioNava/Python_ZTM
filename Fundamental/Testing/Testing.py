#TESTING
#Es un método en software development donde se prueban partes de 
#código para comprobar que trabajan apropiadamente.

#Se crea un archivo test.py para cada módulo de prueba.

#Se crea con el fin de probar cosas del código y no pertenecerá 
#a la exportación final del proyecto.

#pylint, pyflakes, PEP-8...

#Unittest (PYTHON BUILT-IN MODULE)

def do_stuff(num = 1):
	try:
		print('Argumento:', num)
		return int(num)*5
	except (ValueError, TypeError) as err:
		return err




