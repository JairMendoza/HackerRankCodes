#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for gato in range(1 , n+1):
        fila = ''
        for i in range(n , 0 , -1):
            if i <= gato:
                fila += '#'
            else:
                fila += ' '
        print(fila)
  
            

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)