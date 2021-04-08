#EJERCICIO:

#Importamos el módulo random
from random import randint

# Generar un numero del 1 al 10
answer = randint(1, 10)

while True:
    try:
        guess = int(input('Guess a number between 1-10: '))     # Input del usuario
        if 0 < guess < 11:                                      # Verificar si el número está dentro del rango 1-10
            if guess == answer:                                 # Verificar si el número es el correcto.
                print('GENIOUS!')
                break
            print('Keep trying!')
        else:
            print('I said 1-10!')
    except ValueError:
        print('Enter a number')

#Podemos utilizar el 'import sys' y lo demás para correrlo por consola.



