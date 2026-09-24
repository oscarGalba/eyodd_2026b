import time

print("--- MEDICIÓN DE TIEMPOS ---")

# Repetimos 11 veces (del 1 al 11)
for i in range(1, 12):
    n = i * 500
    
    # 1. Tiempo inicial
    timestamp_01 = time.time()
    
    # 2. Sumamos los números
    total_sum = 0
    for numero in range(1, n + 1):
        total_sum = total_sum + numero
        
    # 3. Tiempo final
    timestamp_02 = time.time()
    
    # 4. Calculamos y redondeamos a 2 decimales
    tiempo = round((timestamp_02 - timestamp_01) * 1e6, 2)
    
    # Mostramos el resultado
    print("n =", n, "| Suma =", total_sum, "| Tiempo =", tiempo, "us")