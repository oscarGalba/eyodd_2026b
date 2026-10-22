from array import array as arr

# Parametros de mi programa
rows = 8
columns = 2 * rows - 1

# Creando el grid 2D
matrix = []
# Construyendo el grid
for _ in range(rows):
    new_row = arr('i', [0] * columns)
    matrix.append(new_row)

# Validando la contruccion del grid
print(f"Cantidad de filas: {len(matrix[0])}")
print(f"Cantidad de columnas: {len(matrix[0])}")

for row in matrix:
    print(list(row))