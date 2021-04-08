#For Loops e iterables

dict1 = {
  'name': 'Cerjio',
  'age' : 21,
  'tall': True
}

count = 0

#Esto es un tuple  unpacking (key, value)
for (key, value) in dict1.items():
  count+=1
  print (key, '\t' , value)

  if (value == 'Cerjio'):
    print ("Name checked")
  elif (value > 18):
    print ("Old enough")
  
  if count == len(dict1):
    print ("Loop Finished")
    count = 0

print() 

for item in dict1.values():
  print (item)

print()

for item in dict1.keys():
  print (item)

#iterable - list, dictionary, tuple, set, string...
#iterate - one by one check each item in the collection


#Exercise Tricky Counter
print("\nCOUNTER EXERCISE\n")

my_list = list(range(11))
print (my_list)

#dos formas,  mismo resultado
total1 = 0
total2 = 0

for i in my_list:
  total1 += my_list[i]
  total2 += i

print ("Suma total: ", total1, total2)

#otrooo
total3 = 0
for i in range(11):
  total3 += i

print (total3)
print()

#Range puede ir en decremento
for _ in range(0, 10, 2):
  print(_)

print()

#Range puede ir en decremento
for _ in range(10, 0, -2):
  print(_)