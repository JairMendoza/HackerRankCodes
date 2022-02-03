import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    #nuevaString = ''
    hora = int(s[0:2])
    print(hora)
    if s[len(s)-1] == 'p':
        hora += 12
        print(hora)
    return s 


s = input()

result = timeConversion(s)
print(result)

    #fptr.write(result + '\n')

    #fptr.close()
