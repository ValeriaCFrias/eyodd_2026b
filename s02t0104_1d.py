from array import array as arr
#Importando una función de 
# #archivo
from S02T0102_1d import print_array

my_array=arr('i',[2,10,15,20,10])

print("---ANTES DE LA ELIMINACIÓN---")
print_array(my_array)
elementos_a_eliminar = [10]

# 2. Crea el bucle for para recorrer cada elemento
for elemento in elementos_a_eliminar:
    try:
        my_array.remove(elemento)
        print(f"Elemento {elemento} eliminado correctamente.")
    except:
        print(f"El elemento {elemento} no se encuentra en el arreglo.")

print("---DESPUÉS DE LA ELIMINACIÓN---")
print_array(my_array)

#Eliminación
# try:
#  my_array.remove(100)
# except:

#  print(f"no se encuentraen el arreglo")
# print("---DESPUÉS DE LA ELIMINACIÓN---")
# print_array(my_array)



    
    