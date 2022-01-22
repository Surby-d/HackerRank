#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, m, queries):
    # Write your code here
    z=0
    maximum = 0
    array = [0 for _ in range(n+1)]
    for i in range(m):
        a, b, k = queries[i][0], queries[i][1], queries[i][2]
        array[a]+=k
        if(b+1)<=n:
            array[b+1]-=k
            
    for j in range(1, n+1):
        z+=array[j]
        if maximum<z: maximum=z
            
    return maximum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, m, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
