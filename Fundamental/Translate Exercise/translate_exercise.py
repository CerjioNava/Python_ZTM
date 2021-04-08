#EXERCISE TRANSLATOR!

#import translate

try:
	with open('translation_exercise.txt', mode='r') as file:
		text = file.read()
		#translation = translator.translate(text)
		translation = 'Here must be a translation'
		print(text)
		with open('trans_jap.txt', mode='w') as file2:
			file2.write(translation)
except FileNotFoundError as err:
	print('File not found!')
