import time

n = 100
the_sum = 0

# Tomando el tiempo inicial
timestamp_01 = time.time()

while(n > 0):
    the_sum = the_sum + n
    n = n - 1

# Tomando el tiempo final
timestamp_02 = time.time()

print("La suma es:", the_sum)
print("Tiempo:", timestamp_02 - timestamp_01)