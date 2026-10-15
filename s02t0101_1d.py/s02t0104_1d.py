#Importando funcion Array
#del modulo
from array import array as arr
from s02t0102_1d import print_array

my_array = arr('i', [2, 10, 15, 20, 10])
print("--- ANTES DE LA ELIMINACION ---")
print_array(my_array)

#ELIMINACION
numero_a_borrar = 10

# Este ciclo elimina todas las repeticiones del 10
while numero_a_borrar in my_array:
    my_array.remove(numero_a_borrar)

print("--- DESPUES DE LA ELIMINACION ---")
print_array(my_array)
