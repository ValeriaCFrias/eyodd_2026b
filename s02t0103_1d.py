


from array import array as arr
#Importando una función de 
# #archivo
from S02T0102_1d import print_array

my_array=arr('i',[2,10,15,20])

print("---ANTES DE LA INSERCIÓN")
print_array(my_array)

#Interción
my_array.insert(1,90)
print("--Después de la inserción--")
print_array(my_array)

print("---DESPUES DE UN APPEND---")
my_array.append(1000)
print_array(my_array)

print("---SIMULAR UN APPEND CON INSER---")
my_array.insert(len(my_array),90000)
print_array(my_array)