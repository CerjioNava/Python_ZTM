#EXERCISE: PDF Merger (Combinar dos PDF's)

import sys, PyPDF2

inputs = sys.argv[1:]

#Función para combinar y mantener limpio el código
def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()					#La librería trae un combinador.
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)							#Por cada PDF en la lista, se añaden uno tras otro.
	merger.write('./new_pdfs/mergePDF.pdf')			#Al final se crea el nuevo super pdf

pdf_combiner(inputs)								#Se llama la función
print('DONE!')

#NOTA: No se necesito hacer el...
#with open('./PDFs/dummy.pdf', 'rb') as dummy_file.....
#Siempre es necesario revisar la documentación de las librerías, pueden
#ahorrarnos tiempo y trabajo!


#EXERCISE: Añadir Watermark al pdf anterior y crear con el un nuevo pdf.

outputPDF = PyPDF2.PdfFileWriter()										#Creamos la variable donde saldra el pdf

superPDF = PyPDF2.PdfFileReader(open('./new_pdfs/mergePDF.pdf', 'rb'))	#Se lee el pdf por marcar
wtrPDF = PyPDF2.PdfFileReader(open('./PDFs/wtr.pdf', 'rb'))				#Se lee la watermark
watermark = wtrPDF.getPage(0)											#Se guarda la watermark

for i in range(superPDF.getNumPages()):				#Por cada página en el pdf...
	page = superPDF.getPage(i)						#Se obtiene la página actual
	page.mergePage(watermark)						#Se le sobrepone la marca de agua
	outputPDF.addPage(page)							#Y se añade la página al pdf de salida

with open('./new_pdfs/wtrPDF.pdf', 'wb') as output_file:	#Se abre un archivo como escritura
	outputPDF.write(output_file)							#Se escribe el nuevo pdf.

print('Watermark DONE!')
