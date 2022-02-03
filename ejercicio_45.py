#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    count = 0
    if len(t) < len(s):
        for i in range(len(s)):
            if t[i] != s[i] or i + 1 == len(t):
                count = len(s) - len(t)
                break
    else:
        for i in range(len(t)):
            if t[i] != s[i] or i + 1 == len(s):
                count = (len(s) - i) + (len(t) - i)
                break
    if count <= k:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    print(result)
