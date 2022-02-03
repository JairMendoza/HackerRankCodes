import math
import os
import random
import re
import sys

def nonDivisibleSubset(k, s):
    # Write your code here
    notMultiple = []
    multiple = []
    for i in range(len(s)):
        for x in range(i + 1 , len(s)):
            if (s[i] + s[x]) % k != 0:
                #notMultiple.append(s[i])
                notMultiple.append(s[x])
            else:
                #multiple.append(s[i])
                multiple.append(s[x])
    notMultiple = list(set(notMultiple))
    multiple = list(set(multiple))
    for i in multiple:
        if i in notMultiple == False:
            multiple.remove(i)
    return len(multiple)

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    print(result)