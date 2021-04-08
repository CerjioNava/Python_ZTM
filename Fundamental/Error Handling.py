#Error Handling
#Nos permitirá seguir ejecutando el código aún si sucede algún error en el programa
#TRY

#Try intenta el proceso que está en el. Si no funciona salta al "except" donde 
#realiza la acción si existe un error, si no hay error entonces salta a "else".
#Finally se ejecuta al final de la secuencia sin importar todo lo anterior.

#EJEMPLO:
#Entrada de un valor int, si no es int puede dar error:

print("Example 1:\n")

while True:
	try:
		num = int(input("Enter a number: "))								#NOTA: Recordar usasr ctrl+w para correr con REPL
		print(f"10/{num} = {10/num}")
	except ValueError as error:
		print(f"Please enter a number because:\t{error}")
	except ZeroDivisionError as error:
		print(f"Please do not enter 0 because:\t{error}")
	else:
		print("Thank you!")
		break
	finally:
		print("Finally done!")

#Para especificar un error específico, en 'except' se puede especificar el error, y pueden haber multiples Except.		

print("\nExample 2:\n")

#EJEMPLO:

def division(num1, num2):
	try:
		num1 / num2
	except (TypeError, ZeroDivisionError) as error_text:						#Puede aceptar varios errores para una misma respuesta
		print(f'Please enter a valid number because:\t{error_text}')			#Así puede imprimir la razón del error!
	else:
		print(f'{num1}/{num2} = {num1/num2}\tThanks!')
	finally:
		print("Finally done!")

print(division('1', 2))				#TypeError
print(division(5, 0))				#ZeroDivisionError
print(division(10, 5))

# Raise se utiliza para definir nuestros propios errores a mostrar



