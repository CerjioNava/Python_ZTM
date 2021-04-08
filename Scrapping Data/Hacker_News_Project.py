#Hacker News Project

#Primero, instalamos Beautiful Soup y Requests.
# 'pip3 install beautifulsoup4' y 'pip3 install requests'

import requests					#Importamos requests 
from bs4 import BeautifulSoup	#Importamos BS4
import pprint	 				#Para una impresión más ordenada

#Request nos permitira comunicarnos con la url y descargar el html.

#Beautiful Soup nos permite trabajar con html y extraer la información que
#necesitamos y utilizarla para los fines que queramos.

url = 'https://news.ycombinator.com/news'			#Url de Hacker News.
url2 = 'https://news.ycombinator.com/news?p=2'
res = requests.get(url)								#Obtiene la respuesta.
res2 = requests.get(url2)	
#print(res.text)									#Imprime el html del response en forma de string.

#Aquí es donde Beautiful Soup entra, para convertir el string del response obtenido, 
#en un objeto manipulable posible de modificar y utilizar. 'PARSE'

soup = BeautifulSoup(res.text, 'html.parser')		#Se indica el string y que parser se utilizará.
soup2 = BeautifulSoup(res2.text, 'html.parser')

#Beautiful Soup Basics:

#print(soup)					#Imprime toda la respuesta html, pero podemos buscar más específico.
#print(soup.body)				#Imprime solo el 'body'.
#print(soup.find_all('div'))	#Imprime solo los objetos 'div' del texto en forma de lista.
#print(soup.find_all('a'))		#Imprime solo los links del texto en forma de lista. 'a'
#print(soup.title)				#Imprime el título de la página.
#print(soup.find('a'))			#Encuentra el primer objeto que coincida, no todos.
								#Find también sirve para buscar cosas específicas, como un ID.
#Etc...

#(IMPORTANTE!)
#Beautiful Soup Select: Nos permite extraer una parte de la información del soup (CSS Selector)
#Podemos utilizarlo no solo para obtener valors (div, a, etc) como antes. Podemos seleccionar 
#directamente las clases por ejemplo.

#print(soup.select('.score'))				#Imprime todos los span text que poseen clase score.
#print(soup.select('#score_24702393'))		#Imprime el span que posea el id específico.
#print(soup.select('.storylink'))			#Imprime la lista de objetos con storylink

#Queremos obtener solo los objetos de aquellos con más de 100 views.
#Todos los títulos en hackernews (links) son clase 'storylink'

links = soup.select('.storylink')			#Lista con los objetos que poseen storylinks.
subtext = soup.select('.subtext')			#Lista con los objetos que pueden poseer score.
links2 = soup2.select('.storylink')			
subtext2 = soup2.select('.subtext')		

mega_links = links + links2
mega_subtext = subtext + subtext2	

#print(subtext)

#Función para ordenar la lista de diccionarios según los votos, mayor a menor.
def sort_stories_by_votes(hackerlist):
	return sorted(hackerlist, key = lambda k: k['votes'], reverse = True)

#Función que devuelve la lista personalizada de links y puntos mayores a 100
def create_custom_hn(links, subtext):
	hn = []											#Se crea una lista vacía que devolver
	for index, item in enumerate(links):			#Por cada link en la página
		
		title = links[index].getText()				#Se obtiene el título
		href = links[index].get('href', None)		#Se obtiene el link (si no existe, queda None)
		vote = subtext[index].select('.score')		#Se obtiene (si existe) el score del subtext

		#Si realmente existe el score. Sino, no existe puntaje.
		if len(vote):					
			#Se obtienen los puntos convertidos en 'int' sin ' points'
			points = int(vote[0].getText().replace(' points', ''))	
			#print(points)
			if points > 99:
				hn.append({'title': title, 'link': href, 'votes': points})		#Se añade a la lista 'hn'

	return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))
