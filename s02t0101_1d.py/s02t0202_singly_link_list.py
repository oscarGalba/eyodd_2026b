# Importando clase node 
from s02t0201_linked_list import Node

# Creando la clase de una lista enlazada
class SinglyLinkedList:
    # Constructor de la clase de una lista enlazada
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Metodo de insercion de Nodo al final de la lista
    def append(self, data):
        new_node = Node(data)
        self.size += 1

        # Si la lista esta vacia, head y tail apuntan al nuevo nodo
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        # Si ya hay elementos, conectamos el tail actual al nuevo nodo
        self.tail.next = new_node
        self.tail = new_node

    # Insertando en posicion intermedia (basado en indice 0)
    def append_at_location(self, data, index):
        # Validar que el indice este dentro del rango permitido
        if index < 1 or index > self.size:
            raise IndexError("Índice fuera de rango")

        new_nodo = Node(data)
        #insertar al inicio
        if index ==1:
            new_node.next = self.head
            self.head = 

        # Si se inserta al final, reutilizamos append
        if index == self.size:
            self.append(data)
            return

        new_node = Node(data)
        self.size += 1

        # Si se inserta al inicio (indice 0)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # Recorrer hasta el nodo anterior a la posicion deseada
        current_node = self.head
        for _ in range(index - 1):
            current_node = current_node.next

        # Enlazar el nuevo nodo en medio
        new_node.next = current_node.next
        current_node.next = new_node


# 1 Creo funcion principal 
def main():
    # Creando una instancia de una lista enlazada
    my_list = SinglyLinkedList()
    
    # Agregar elementos a la lista 
    my_list.append(30)
    my_list.append(59)
    my_list.append(80)
    my_list.append(100)

    # Ejemplo usando append_at_location (inserta el 70 en la posicion 2)
    my_list.append_at_location(70, 2)

    # Recorrer la lista (asegurate de que Node tenga definido iter())
    if my_list.head:
        for value in my_list.head.iter():
            print(f"{value}, ", end="")
        print()

# Ejecutar el programa
if __name__ == "__main__":
    main()
