#PDF With Python

#El conocimiento aplicado a los PDF es similar a excel u otro tipo de archivo.

#Recordar buscar la librería adecuada para nuestros proyectos.
#Instalamos 'pip3 install PyPDF2'

#Recordar revisar la documentación de las librerías que implementamos
import PyPDF2

with open('./PDFs/dummy.pdf', 'rb') as dummy_file:		# Usamos 'rb' para Read Binary
	#print(dummy_file)
	reader = PyPDF2.PdfFileReader(dummy_file)			#Asigna la lectura del pdf a una variable
	print(reader.numPages)								#Número de páginas
	
	#Modificando un PDF, deberá guardarse al final
	page = reader.getPage(0)							#Se obtiene la página
	page.rotateClockwise(90)							#Se rota
	writer = PyPDF2.PdfFileWriter()						#Se crea un objeto writer del PyPDF2
	writer.addPage(page)								#Se añade la página volteada

	with open('./new_pdfs/new_dummy.pdf', 'wb') as dummy_new:	#Y se crea un nuevo pdf
		writer.write(dummy_new) 								#Se escribe sobre el pdf

#EXERCISE: PDF Merger (Combinar dos PDF's)

