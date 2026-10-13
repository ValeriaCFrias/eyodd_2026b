#array
#form array import
import array as arr
#creacion de un arreglo
#i:entero con signo
#I:Entero sin signo
#f:Numero decimal
#d:numero decimal doble
#u:caracter unicode
my_array=arr.array('i',[10,22,300,6,200,9,30,31,28,18,7])

#interacción automatica
# for num in my_array:
    # print(num)

#acceso indivudua a los elementos
# print(my_array[0]) #primer elemento
# print(my_array[1]) #segundo elemento
# print(my_array[1]) #tercer elemento

#Tamaño de un arreglo
#Length
# print(len(my_array))

#Interacción por indices
# for i in range(len(my_array)):
#     # print(f"Elemento{i+1}:{my_array[i]}")
#     if my_array[i]%2==0:
#         print(f"Elemento Num{i+1}:{my_array[i]}")
#Busqueda de un elemento
num_to_search = 200 
#modificando un valor usando
#backet notation
my_array[4]=200

try:
 print(f"localizadon 200: {my_array.index(num_to_search)}")
except:
 print("Numero no encontrado ⚠️")
 
