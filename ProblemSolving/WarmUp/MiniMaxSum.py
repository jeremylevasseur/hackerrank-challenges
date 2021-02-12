#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minimumSum = 0
    maximumSum = 0
    
    # Finding the minimum sum
    arr.sort()  # Array is now sorted from low to high
    for i in range(4):
        minimumSum += arr[i]
    
    arr.sort(reverse=True)
    for i in range(4):
        maximumSum += arr[i]
    
    print(str(minimumSum) + " " + str(maximumSum))
    
    # Finding the maximum sum

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
