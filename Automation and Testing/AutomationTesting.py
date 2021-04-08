#Automation/Testing

#Selenium es una de las herramientas para browser automation. Nos permitirá tomar,
#modificar y testear elementos de la página, etc.
#Cada browser tiene un driver específico para selenium. Se instala desde la página.
#El driver debe estar en la misma carpeta que nuestro .py.

from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

#print(chrome_browser)				#Se obtiene una instancia del Chrome 2.
#chrome_browser.maximize_window()	#Se instancia con vista maximizada.

#Para la práctica de esta sección, utilizaremos 'https://www.seleniumeasy.com/test/'
#ya que tiene buen contenido de práctica.

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
#Esto nos abre una ventana Chrome con la página a testear.

#Del html de la página, como ejemplo podemos confirmar que el siguiente texto existe
#en el campo <title>.
#print('Selenium Easy Demo' in chrome_browser.title)

#Sin embargo, es más fácil utilizar 'assert':

assert 'Selenium Easy Demo' in chrome_browser.title

#Se pueden usar Selectores para tomar valores por Tag Name, Link Text, Css, Class name, etc.
#	'driver.find_element_by' y '_id()', '_tag_name()', '_class_name()', etc.

#Obtenemos el botón.
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
print(show_message_button.get_attribute('innerHTML'))	#Devuelve el atributo del elemento show_message_button.
#assert 'Show Message' in chrome_browser.page_source	#Se verifica si Show Message existe allí.

#Obtenemos la casila y escribimos en ella.
user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()								#Limpia la casilla del mensaje
user_message.send_keys('I AM EXTRA COOL')			#Imita que un user escribe allí.

#Clickeamos el boton para enviar el mensaje.
show_message_button.click()

#Obtenemos la salida del mensaje.
output_message = chrome_browser.find_element_by_id('display')
assert 'I AM EXTRA COOL' in output_message

#Otra forma de utilizar los selectores es:
#button2 = chrome_browser.find_element_by_css_selector('.btn')	#Se busca por la clase css del objeto.
#button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn') #Busca entre los get-input

chrome_browser.close()	#Cierra la ventana abierta	(a veces no funciona)
chrome_browser.quit()	#Cierra todas las ventanas

#IMPORTANTE: Cualquier página puede detectar que es un robot automatizado ya que nadie puede escribir
#o mandar decenes o miles de click tan rápido. Para ello se utiliza WAITS de Selenium.



