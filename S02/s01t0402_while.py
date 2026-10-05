"""
 Ecribir un programa que calcule 
 la suma de los "n" numeros naturales.
 Por ejemplo si n=100, el programa
 calcula la suma de 1 al 100
"""
#Importar la biblioteca dde tiempo.
import time

#crear varibles para el problema.
n = 100
the_sum = 0
#tomando el t1
timestamp_01=time.time()

#Iniciando la suma
#100
while(n>0):
     the_sum = the_sum + n
     n=n-1
     timestamp_02= time.time()
    #Imprimimos la solucion.
print(f"la suma es {the_sum}")
#calculando el timepo
elapsed_time=round((timestamp_02-timestamp_01)*1e6,2)
print(f"Tiempo de ejecución:{elapsed_time}us")