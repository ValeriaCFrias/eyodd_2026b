#Importando el modulo array
#La biblioteca
from array import array as arr

def print_array(input):
    print("[",end=" ")
    for element in input:
        print(element,end=',')
    print("\b]")

my_array=arr('i',[2,10,15,20])
print_array(my_array)