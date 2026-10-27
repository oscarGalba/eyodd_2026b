from array import array as arr

# Parametros de mi programa
rows = 5  # Lo subí a 5 para que alcances a ver la forma del triángulo
columns = 2 * rows - 1

# funcion para imprimir matrix
def print_matrix(input_matrix):
    for row in input_matrix:
        print(list(row))

# Creando el grid 2D
matrix = []

# Construyendo el grid
for _ in range(rows):
    new_row = arr('i', [0] * columns)
    matrix.append(new_row)

# Validando la contruccion del grid
print(f"Cantidad de filas: {len(matrix)}") # Corregido para medir las filas totales
print(f"Cantidad de columnas: {len(matrix[0])}")

# calculando el centro de la primera fila
center = columns // 2

# estableciendo el centro en 1
matrix[0][center] = 1

print("\nMatriz Inicial:")
print_matrix(matrix)

# siguiendo con la construccion del triangulo de sierpinsky
for row in range(1, rows):
    for col in range(0, columns):
        left_upper_cell = 0
        right_upper_cell = 0

        # Si la columna es mayor a 0, miramos arriba a la izquierda
        if col > 0:
            left_upper_cell = matrix[row - 1][col - 1]

        # Si la columna está antes del final de la fila, miramos arriba a la derecha
        if col < columns - 1:
            right_upper_cell = matrix[row - 1][col + 1]
            
        # Lógica XOR para Sierpinski: Da 1 solo si las celdas de arriba son diferentes
        if left_upper_cell != right_upper_cell:
            matrix[row][col] = 1
        else:
            matrix[row][col] = 0

print("\nResultado Final:")
print_matrix(matrix)