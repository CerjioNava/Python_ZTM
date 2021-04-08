#JPG to PNG (EXERCISE)

import sys
import os
from PIL import Image

#Toma el primer y segundo argumento desde consola (sys).
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print()
print(image_folder, output_folder)

#Check si la nueva carpeta existe, si no es así, se crea.
if not os.path.exists(output_folder):
	os.makedirs(output_folder)
	print('New folder created!')	

#Loop en ./Pokedex, convertirlas en PNG, guardar en la nueva carpeta.
for filename in os.listdir(image_folder):						#Devuelve la lista de objetos en la carpeta
	img = Image.open(f'{image_folder}{filename}')				#Se abren las imagenes de la lista
	clean_name = os.path.splitext(filename)[0]					#Se separa el nombre de la imagen de su formato
	img.save(f'{output_folder}{clean_name}.png', 'png')			#Se guarda en su respectiva carpeta
	print(f'{filename} converted to {clean_name}.png ')

print('DONE!')

