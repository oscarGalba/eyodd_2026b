"""
Generators
Los generadores son funciones que pueden
pausar su ejecución.

Cuando se invoca una funcion generadora
devuelva un objeto generador (aka Iterador)

El codigo dentro de la funcion no se ejecuta
de inmediato, solo se compila


La funcion  se ejecuta unicamente cuando
iteras sobre el generador

"""

def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4


my_iterator = my_generator()


#print(next(my_iterator))
#print(next(my_iterator))
#print(next(my_iterator))
#print(next(my_iterator))

for value in my_iterator:
    print(value, end = "->")