#Image Processing

#Instalamos la librería básica Pillow para la manipulación de imagenes desde consola!
#Ya podemos utilizar la librería en nuestro proyecto.
#PIL: Python Imaging Library
#Instalamos 'pip3 install Pillow'

from PIL import Image

img = Image.open('./Pokedex/pikachu.jpg')
print(img)						#Se imprime la ubicación del objeto en la memoria y
								#sus especificaciones como un Image Object.
print(img.format)				#Imprime el formato (JPG en este caso)
print(img.size)					#Dimensiones de la imagen (640x640)
print(img.mode)					#Colores (RGB en este caso)

from PIL import ImageFilter		#Otro de los módulos, para filtros.	

#NOTA: Trabajar con exportación de PNG, ya que soporta las funciones de la librería.

#img.show()			#Este comando abre el archivo de la imagen.

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('./saved_images/blur_pikachu', 'png')			#OJO: Así se guardó un archivo codificado
filtered_img.save('./saved_images/blur_pikachu.png', 'png')		#y así la imagen. IMPORTANTE!

filtered_img2 = img.filter(ImageFilter.SHARPEN)					#Podemos revisar la librería y ver que
filtered_img2.save('./saved_images/sharpen_pikachu.png', 'png')	#tantas funciones y módulos existen.

filtered_img3 = img.convert('L')								#Devuelve una copia convertida según el 'modo'
filtered_img3.save('./saved_images/grey_pikachu.png', 'png')	#especificado. i.e:'L' es 'greyscale'.

filtered_img4 = img.convert('CMYK')	
filtered_img4.save('./saved_images/cmyk_pikachu.jpg')									

rot_image45 = filtered_img3.rotate(45)						#Podemos rotarla de esta forma cualquier grado
rot_image45.save('./saved_images/rot45_pikachu.jpg')

rot_image90 = filtered_img3.rotate(90)						#Otro ángulo, solo por ejemplo.
rot_image90.save('./saved_images/rot90_pikachu.jpg')

resize_image = filtered_img3.resize((200, 200))				#resize para redimensionar la imagen.
resize_image.save('./saved_images/resized_pikachu.jpg')		#Recibe las dimensiones en forma de tupla.
#Nota: puede redimensionarse (más grande o más pequeño, fuera de proporción, etc...)

#Otro ejemplito, si queremos recortar una parte de la imagen:

crop_box = (100, 100, 400, 400)								#Se define un area de recorte en tupla
crop_img = filtered_img3.crop(crop_box)						#Se aplica el recorte y se guarda
crop_img.save('./saved_images/crop_pikachu.png', 'png')

#Ejemplo con la imagen 'astro.jpg', es demasiado grande.

astro_img = Image.open('./astro.jpg')
print(astro_img)

#Haciendo esto se pierde el aspect ratio de la imagen, mejor utilizar un método thumbnail!
new_astro_img = astro_img.resize((400, 400))
new_astro_img.save('./saved_images/thumbnail_astro.png', 'png')

#Sin importar que las dimensiones especificadas sean fuera de proporción, el método mantendrá
#el aspect ratio de la imagen según el rango de la dimensión.
astro_img.thumbnail((400, 200))
astro_img.save('./saved_images/thumbnail_astro_real.png', 'png')
print(astro_img.size)




#IMPORTANTE: Pillow es una librería básica para estas cosas sencillas, sin embargo, para
#cosas mucho más complicadas debemos aprender como usar OpenCV.