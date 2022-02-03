#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    energy = 100
    '''for i in range(k, len(c), k):
        if c[i] == 1:
            energy -= 3
        else:
            energy -= 1
        if i + k == len(c) and c[0] == 0:    
            return energy - 1
        if i + k == len(c) and c[0] == 1:
            return energy - 3'''
    count = k
    if k == len(c):
        if c[0] == 1:
            energy -= 3
        else:
            energy -= 1
    else:
        while count != 0:
            if c[count] == 1:
                energy -= 3
            else:
                energy -= 1
            count += k
            if count >= len(c):
                count = count - (len(c))
                if count == 0 and c[0] == 1:
                    energy -= 3
                elif count == 0 and c[0] == 0:
                    energy -= 1

    return energy
        
        

        
        
        

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    print(result)