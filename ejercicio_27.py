import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    candles.sort(reverse = True)
    cont = 0
    print(candles)
    for i in range(len(candles)):
        if candles[i] == candles[0]:
            cont += 1
    return cont 

if __name__ == '__main__':
   

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print(result)
