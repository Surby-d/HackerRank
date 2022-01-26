#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    for i in grades:
        x = i % 10
        if i>=38:
            if x in range(3, 6):
                print(i+(5-x))
            elif x in range(8,10):
                print(i+(10-x))
            else:
                print(i)

        else:
            print(i)




grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

gradingStudents(grades)






