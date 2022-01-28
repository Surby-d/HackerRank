#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import heapify, heappush, heappop
#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, arr):
    # Write your code here
    count = 0
    heapify(arr)
    while arr[0]<k:
        if len(arr)<2:
            return -1
        p, q = heappop(arr), heappop(arr)
        heappush(arr, p+2*q)
        count+=1
        
    else:
        return count   
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
