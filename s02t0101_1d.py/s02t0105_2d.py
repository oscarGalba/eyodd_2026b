from array import array as arr

def print_table(input_table):
# Imprimiendo cada elemento
 for row in input_table:
    for column in row:
        print(column, end=",")
    print("\b ")

table = [
    arr('i',[1,2,3]),
    arr('i',[4,5,6]),
    arr('i',[7,8,9]),
]
print_table(table)

row = 1
column = 2
value = 99

table[row].insert(column, value)
print("--- Despues de la insercion ---")
print_table(table)

new_row = arr('i',[100,200,300])
pos = 1
table.insert(pos, new_row)
print("--- Despues de la insercion ---")
print_table(table)

del table[2]
print("--- Despues de la eliminacion de la fila 2 ---")
print_table(table)