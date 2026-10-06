"""
 Ecribir un programa que calcule 
 la suma de los "n" numeros naturales.
 Por ejemplo si n=100, el programa
 calcula la suma de 1 al 100
"""
# Importar la biblioteca de tiempo
import time


# Función para calcular la suma
def sum_of_n(n):

    the_sum = 0

    while n > 0:
        the_sum = the_sum + n
        n = n - 1

    return the_sum


# Crear dataset
dataset = []

# Inicializar repetition
repetition = 1


# Repetir 10 veces
while repetition <= 10:

    # Tomo el tiempo inicial
    timestamp_01 = time.time()

    # Calculo los "n" numeros
    n = repetition * 100

    # Guardo el resultado
    result = sum_of_n(n)

    # Tomo el tiempo final
    timestamp_02 = time.time()

    # Calculando el tiempo
    elapsed_time = round((timestamp_02 - timestamp_01) * 1e6, 2)

    # Agregar la tripleta al dataset
    dataset.append((n, elapsed_time, result))

    # Aumentar repetition
    repetition = repetition + 1


# Imprimir el dataset
i = 0

while i < len(dataset):

    n, tiempo, resultado = dataset[i]

    print( (n,tiempo,resultado) )

    i = i + 1