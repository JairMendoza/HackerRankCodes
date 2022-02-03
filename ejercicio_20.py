#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    bestScore = 0
    worstScore = 0
    control = 0
    control2 = 0
    respon = []
    for i in range(0 , len(scores)-1):
        if i + 1 < len(scores):    
            if scores[i + 1] > scores[control]:
                bestScore += 1
                control = i + 1
        if i + 1 < len(scores): 
            if scores[i + 1] < scores[control2]:
                worstScore += 1
                control2 = i + 1
    respon.append(bestScore)
    respon.append(worstScore)
    return respon

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
