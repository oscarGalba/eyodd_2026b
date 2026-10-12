import array as arr
my_array = arr.array('i',[3,8,5,1,6,23,34,56,246,39])
#interaccion automatica
#for num in my_array:
 #   print(num)

    #acceso individual a los elementos
#print(my_array[0])
#print(my_array[1])
#print(my_array[1]) 

#tamaño de un arreglo
#print(len(my_array))

#interaccion por indices
for i in range(len(my_array)):
    print(f"Elemento {i+1}: {my_array[i]}")