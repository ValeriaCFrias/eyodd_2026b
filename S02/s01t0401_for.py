"""
 Ecribir un programa que calcule 
 la suma de los "n" numeros naturales.
 Por ejemplo si n=100, el programa
 calcula la suma de 1 al 100
"""
# Importamos biblioteca time
import time

#creando una marca de tiempo
timestamp_01= time.time()

#Programa que calcula la suma
# de los "n" numeros naturales
n=100
sum=0

#Ciclo for
for number in range(1,n+1):
    print(str(number) +" ")
    