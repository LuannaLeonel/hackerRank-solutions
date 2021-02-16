#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    primary = 0
    secondary = 0
    # Write your code here
    for i in range(len(arr)):
        for j in range(len(arr)):
            
            if(j == i):
                primary += arr[i][j]
            
            if ((i + j) == (len(arr) - 1)): 
                secondary += arr[i][j]
    
    diff = abs(primary - secondary)
    
    return diff


if __name__ == '__main__':
   fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()