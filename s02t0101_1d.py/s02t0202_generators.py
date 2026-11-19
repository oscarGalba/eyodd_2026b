"""""
Los generadores son funciones quew pueden 
pausar su ejecucion.

Cuando se invoca una funcion generadora 
devuelve un objeto generador(aka Iterador)

El codigo dentro de la funcion no se ejecuta 
de inmediato, solo se copila.

La funcion se ejecuta unicamente cuando 
iteras sobre el generador.
"""
def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4 

    # Se invoca la funcion generadora 
my_iterador = my_generator()

#se itera manualmente sobre el generador 
# print(next(my_iterador))#imprime 1
# print(next(my_iterador))#imprime 2
# print(next(my_iterador))#imprime 3
# print(next(my_iterador))#imprime 4

#Los iteradores se puede iterar por un for 
for value in my_iterador:
    print(value)