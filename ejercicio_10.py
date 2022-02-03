
def agregarNumeros(lista):
    
    for w in range(0 , 10):
        lista.append(int(input("Inserte un numero: ")))
    print(lista)

def ordenarNumeros(lista,listaImpares,listaPares):
    for i in lista:
        if i % 2 == 0:
            listaPares.append(i)
        else:
            listaImpares.append(i)
lista = []
listaPares = []
listaImpares = []
agregarNumeros(lista)
ordenarNumeros(lista,listaImpares,listaPares)
print("Lista de numeros pares: {}\nLista de numeros impares: {}".format(listaPares,listaImpares))
