#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    i=0
    total = []
    temp = sum(arr)
    while i<len(arr):
        total.append(temp-(arr[i]))
        i+=1

    print(min(total), max(total))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
