#MODULES
#Representa la manera de trabajar en varios scripts por separados pero todos en un mismo proyecto.
#NOTA: Se crea una carpeta _pycache_ donde se almacena el cache de los módulos.

import utility		                    			    #Importamos el .py creado para el ejemplo

print("UBICACION:", utility)					        ##Se muestra la ubicación del módulo
print("Función:", utility.multiply(2, 3), '\n')		    #Se puede utilizar las funciones

#Los paquetes son carpetas que contienen módulos, de esta forma si quiero importar un paquete:

import shopping.shopping_cart
#from shopping import shopping_cart                     #Otra forma de escribirlo

print("UBICACIÓN 2:", shopping.shopping_cart)
print("Función:", shopping.shopping_cart.buy('apple'), '\n')

#NOTA: todo paquete debe tener un archivo .py de nombre __init__.py
#que representa que la carpeta ES UN PAQUETE. Puede quedar en blanco.
#Pycharm lo crea automáticamente como parte del paquete.

#Mientras más paquetes dentro de otros paquetes tengamos, más complicado
#será escribir una y otra vez lineas de código, de esta manera:

from shopping.shopping_cart import  buy                 #MUCHO MÁS CÓMODO
print(buy('other apple'))

from utility import multiply, divide                    #Se pueden importar varias funciones
print(multiply(2, 4))
print(divide(6, 2))

#Para importar todas las funciones de un módulo:
#   'from utility import *'

#NOTA: Cada vez que importamos un paquete, se ejecuta su código completo.

print(__name__)                 #__main__ será el nombre del archivo que se ejecuta como principal.
if __name__ == '__main__':      #Esta es una manera de verificar que estamos ejecutando el __main__.
    print('Please run this')

#Los Python Built-in methods son muchos, y poseen gran variedad de funcionalidad.
#No dudar en googlear algo específico.

#Puedes importar módulos con un nombre distinto, de la forma:
#   import utility as nombre_cualquiera
#Y así llamarlo por el nuevo nombre.
#Si es posible, solo importar los métodos que necesito. 

