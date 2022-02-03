import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def migratoryBirds(arr):
    # Write your code here
    cont = 0
    arrBirds = []
    conj = set(arr)
    newList = list(conj)
    for i in range(len(newList)):
        cont = 0
        for o in range(len(arr)):
            if newList[i] == arr[o]:
                cont += 1
        arrBirds.append([cont, newList[i]])
    arrBirds.sort(reverse=True)
    print(arrBirds)
    maxind = 0
    for i in range(len(arrBirds)-1):
        if i == 0:
            maxind = arrBirds[0][1]
        if arrBirds[i][0] == arrBirds[i+1][0]:
            maxind = arrBirds[i+1][1]
        else:
            break

    return maxind


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)
