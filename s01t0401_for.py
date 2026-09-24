import time

# Lista con los valores de n solicitados
valores_n = [100, 500, 1000, 1500, 2000, 2500, 3000, 3500]

print("--- MEDICIÓN DE TIEMPOS DE EJECUCIÓN ---")

for n in valores_n:
    # 1. Tomando el tiempo exacto antes de iniciar el cálculo
    timestamp_01 = time.time()
    
    # 2. Ciclo para calcular la suma de los n números naturales
    total_sum = 0
    for number in range(1, n + 1):
        total_sum += number
        
    # 3. Tomando el tiempo exacto al finalizar el cálculo (antes del print lento)
    timestamp_02 = time.time()
    
    # 4. Cálculo del tiempo transcurrido en microsegundos
    tiempo_microsegundos = (timestamp_02 - timestamp_01) * 1e6
    
    # 5. Impresión de resultados formateados de forma limpia
    print(f"Para n = {n:<7} -> La suma es: {total_sum:<15} | Tiempo transcurrido: {tiempo_microsegundos:.2f} microsegundos")