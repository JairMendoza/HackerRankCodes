#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sumaMax = 0
    sumaMin = 0
    arr.sort()
    for i in range(0 , len(arr)-1):
        sumaMax += arr[i]
    for c in range(len(arr)-1 , 0 , -1):
        sumaMin += arr[c]
    print("{} {}".format(sumaMax , sumaMin))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
