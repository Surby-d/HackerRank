#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    l=[]
    flip = []
    for i in range(0,n+1,2):
        l.append([i, i+1])

    flip.append(l.index([p, p+1]) if p%2==0 else l.index([p-1, p]))
    l.sort(reverse=True)
    flip.append(l.index([p, p + 1]) if p % 2 == 0 else l.index([p - 1, p]))
    return(min(flip))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
