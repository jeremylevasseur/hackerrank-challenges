#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    numberOfPositiveElements = 0
    numberOfNegativeElements = 0
    numberOfZeroElements = 0
    
    for element in arr:
        if element == 0:
            numberOfZeroElements += 1
        elif element > 0:
            numberOfPositiveElements += 1
        else:
            numberOfNegativeElements += 1
    
    print("%.6f" % float(numberOfPositiveElements / len(arr)))
    print("%.6f" % float((numberOfNegativeElements / len(arr))))
    print("%.6f" % float((numberOfZeroElements / len(arr))))
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
