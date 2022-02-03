#!/bin/python3

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    dupli = [x for x, y in collections.Counter(a).items() if y > 1]
    mini = []
    for i in dupli:
        inde = a.index(i)
        inde2 = a.index(i , inde+1)
        mini.append(max(inde , inde2) - min(inde , inde2))
    if len(mini) == 0:
        return -1
    else:
     return min(mini)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
