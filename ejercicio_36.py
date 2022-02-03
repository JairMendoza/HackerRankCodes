#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    # la mejor forma****************
    '''size  =  [int ( i )  for  i  in  input () . split ()] 
    word  =  [ size [ ord ( c ) - ord ( 'a' )]  for  c  in  input ()] 
    print ( max ( word ) * len ( word ))'''
    #mi forma************************
    maxindex = 0
    index = 0
    for i in word:
        index = ord(i) - ord('a') 
        if h[index] > maxindex:
            maxindex = h[index]
    
    return (maxindex * len(word))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()