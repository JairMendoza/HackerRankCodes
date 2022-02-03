import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    count = 0
    for i in set(arr):
        if count < arr.count(i):
            count = arr.count(i)
    return len(arr) - count

if __name__ == '__main__':
    

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)
    print(result)
