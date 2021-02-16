#!/bin/python3

import math
import os
import random
import re
import sys

def sum(arr):
    sum = 0

    for i in arr:
        sum = sum + i
    
    return sum
# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    total_sum = sum(arr)
    min_sum = total_sum -(arr[0])
    max_sum = total_sum -(arr[0])
    for i in arr:
        s = total_sum - i
        if s > max_sum:
            max_sum = s
        elif s < min_sum:
            min_sum = s
    
    print(str(min_sum) +" "+ str(max_sum))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
