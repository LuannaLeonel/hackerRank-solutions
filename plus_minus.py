#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    n = len(arr)
    plus = 0
    minus = 0
    zero = 0

    for e in arr:
        if(e > 0):
            plus+=1
        elif e < 0:
            minus += 1
        else:
            zero += 1

    ratio1 = plus / n
    ratio2 = minus / n
    ratio3 = zero / n

    print('{0:.6f}'.format(ratio1)+'\n'
         '{0:.6f}'.format(ratio2)+'\n' 
         '{0:.6f}'.format(ratio3)+'\n')


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
