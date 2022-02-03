if __name__ == '__main__':
    lista = []
    aux = []
    names = []
    segunda = 0
    listaOrdenada = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        aux.append(score)
        lista.append([name , score]) 
    aux.sort()
    for c in range (0 , (len(aux)-1)):
        if aux[c + 1] != aux[c]:
            segunda = aux[c + 1]
            break
    for z in range(0 , len(lista)):
        if lista[z][1] == segunda:
            listaOrdenada.append(lista[z][0])
    listaOrdenada.sort()
    for q in range(0 , len(listaOrdenada)):
        print(listaOrdenada[q])