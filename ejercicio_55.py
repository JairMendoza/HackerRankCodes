
import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    indi = 0
    count = 0
    while indi != len(c)-1:
        if indi + 2 < len(c):
            if c[indi + 2] == 0:
                indi += 2
                count += 1
            else:
                indi += 1
                count +=1
        else:
            indi += 1
            count +=1
    return count
            
        

if __name__ == '__main__':


    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)
