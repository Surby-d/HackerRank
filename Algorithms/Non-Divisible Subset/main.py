#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    if k==0 or k==1:
        return 1
    counts = [0]*k
    arr = [i%k for i in s]
    for i in set(arr):
        counts[i] = arr.count(i)
      
    c = min(1, counts[0])
    for x in range(1, k//2 +1):
        if x!=(k-x):
            c += max(counts[x], counts[k-x])
        
    if k%2==0:
        c+=1
        
    return c
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
