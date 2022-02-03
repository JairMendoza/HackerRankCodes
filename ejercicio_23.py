import itertools, sys


if __name__ == '__main__':
    N, M = list(map(int, sys.stdin.readline().split()))
    x = [0] * N

    for _ in range(M):
        a, b, k = list(map(int, sys.stdin.readline().split()))

        x[a - 1] += k
        if b < N:
            x[b] -= k

    print(max(itertools.accumulate(x)))
# La version de arriba la copie de internet 
# la de abajo fue un intento fallido que despues volvi a intentar en el archivo arrayManipulation.py
# con exito en los primeros casos 
# pero con exedencia de tiempo en algunos casos.
'''
#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

from heapq import heappop
def arrayManipulation(n, queries):
    lista = []
    for i in queries:
        lista.append([i[0] , i[2] ])
        lista.append([i[1] + 1 , -1 * i[2] ])  

    contadorActual = 0
    alto = 0
    aux = []
    for c in range(len(lista)):
        aux = lista[c]
        contadorActual += aux[1]
        if contadorActual > alto:
            alto = contadorActual

    return alto

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(str(result) + '\n')'''
