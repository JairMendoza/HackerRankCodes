#nodo de cada lista
class Node:
    def __init__(self , value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)
#lista anidada con toda la info 
class LinkedList:
    def __init__(self):
        self.first = None
        self.size = 0
    # funcion agregar un nuevo nodo
    def Append(self,value):
        myNode = Node(value)
        #verificamos si la lista esta vacia.
        if self.size == 0:
            self.first = myNode
        # de lo contrario vamos a tener que recorrer la lista uno a uno
        else:
            #tomamos el primer nodo de la lista para ir recorriendo uno a uno
            current = self.first
            #se hace el recorrido de la lista hasta que llegue al final 
            while current.next != None:
                #se asigna el siguiente next para seguir la lista
                current = current.next
            #se agrega el siguiente nodo 
            current.next = myNode
        #se agrega el tamaño a la lista 
        self.size += 1
        return myNode
    #funcion para remover un nuevo nodo
    def Remove(self, value):
        #verificamos que la lista no este vacia
        if self.size == 0:
            return False
        else:
            #recorremos la lista desde el inicio en busca del valos a eliminar
            current = self.first
            try:
                #buscamos el valor a eliminar
                while current.next.value != value:
                    #guardamos el valor del siguiente nodo al que vamos a eliminar
                    current = current.next
                #guardamos el nodo a eliminar     
                deletedNode = current.next
                #Saltamos el nodo a eliminar
                current.next = deletedNode.next
    
            except AttributeError:
                return False
        #eliminamos uno del tamaño de la lista
        self.size -= 1
        return deletedNode
    # funcion para saber el tamaño de la lista 
    def __len__(self):
        return self.size
    # funcion para regresar el valor de la lista
    def __str__(self):
        string = "["
        current = self.first
        for i in range(len(self)):
            string += str(current)
            if i != len(self) - 1: 
                string += str(", ")
            current = current.next
        string += "]"
        return string

myList = LinkedList()
myList.Append(1)
myList.Append(2)
myList.Append(3)
myList.Append(2)
myList.Append(5)
myList.Append(6)
print(myList)
print(myList.size)
myList.Remove(2)
print(myList)
