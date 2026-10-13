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
# for i in range(len(my_array)):
    # if my_array[i]
    # print(f"Elemento {i+1}: {my_array[i]}")
num_to_search = 200
#modificando un valor
#backet notation
my_array[7]= 200
try:
    print(f"Localizando  {num_to_search}: {my_array.index(num_to_search)}")
except:
    print("☢️ Numero no encontrado!!!")
#Busqueda por indice