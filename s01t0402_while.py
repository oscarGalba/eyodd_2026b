"""
Escribir un programa que calcule 
la suma de los "n" numeros naturales.
Por ejemplo si n = 100, el programa 
calculará la suma del 1 al 100
usando un ciclo while
"""

# Importar la biblioteca de tiempo
import time

# Variable para guardar el data set
dataset = []  # [(n, time, sum), (n, time, sum)]

# Repetimos el calculo con valores de 500 en 500
for repetition in range(1, 11):

    # Crear las variables para el problema
    n = repetition * 500
    the_sum = 0

    # Tomando el t1
    timestamp_01 = time.time()

    # Iniciando la suma
    while(n > 0):
        the_sum = the_sum + n
        n = n - 1

    # Tomamos el t2
    timestamp_02 = time.time()

    # Calculando el tiempo
    elapsed_time = round((timestamp_02 - timestamp_01) * 1e6, 2)

    # Agregamos la tripleta de los datos al dataset
    dataset.append((repetition * 500, elapsed_time, the_sum))

# Imprimimos el dataset
for tup in dataset:
    print(tup)