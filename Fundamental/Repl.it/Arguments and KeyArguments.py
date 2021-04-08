#Arguments and KeyWorkd Arguments (*args **kwargs)

#*args
def super_func(*args):
  print(*args)  # 1 2 ...
  print(args)   #(1, 2, ..)
  return sum(args)

print(super_func(1, 2, 3, 4))
print()

#*args permite que una función reciba cualquier numero de argumentos

#**kwargs
def super_func(**kwargs):
  print(*kwargs.items())   
  return sum(kwargs.values())

print(super_func(num1=5, num2=6))
print()

#kwargs permiten que una función reciba un diccionario de esa forma

#Finalmente:

def super_func(*args, **kwargs):
  print(args, "\t", kwargs)
  total = 0

  for i in kwargs.values():
    total += i

  #return sum(args) + sum(kwargs.values())
  return sum(args) + total

print(super_func(1, 2, 3, num1=2, num=4))
print()

#Rule: params, *args, default params, **kwargs

#EXERCISE Highest even (par mayor)
#ME QUEDO MEJOR MUAHAHA 

def highest_even(*lista):
  
  value = 0

  for i in lista:
    if i % 2 == 0 and value < i:  
      value = i
    
  return value

print("Highest value: " + str(highest_even(10, 2, 3, 8, 11)))



