#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    j = 1

    for i in range(n):
        print( (n-j)*' ' + j*'#')
        j +=1
           

if __name__ == '__main__':
    n = int(input())

    staircase(n)
