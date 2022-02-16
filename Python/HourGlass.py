
import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def calculateHourglassSum(arr, topLeftRowIndex, topLeftColumnIndex):
    try:
        values = [
            arr[topLeftRowIndex][topLeftColumnIndex],  # Top row, far left value
            arr[topLeftRowIndex][topLeftColumnIndex + 1],  # Top row, middle value
            arr[topLeftRowIndex][topLeftColumnIndex + 2],  # Top row, far right value
            arr[topLeftRowIndex + 1][topLeftColumnIndex + 1],  # Middle row value
            arr[topLeftRowIndex + 2][topLeftColumnIndex],  # Bottom row, far left value
            arr[topLeftRowIndex + 2][topLeftColumnIndex + 1],  # Bottom row, middle value
            arr[topLeftRowIndex + 2][topLeftColumnIndex + 2],  # Bottom row, far right value
        ]
        return sum(values)
    except:
        print("Invalid starting coordinates")
        return False

def hourglassSum(arr):
    # Write your code here
    hourglassHeight = 3
    hourglassWidth = 3
    sums = []
    rowCounter = 0
    while rowCounter < (len(arr) - hourglassHeight + 1):
        columnCounter = 0
        while columnCounter < (len(arr[rowCounter]) - hourglassWidth + 1):
            sums.append(calculateHourglassSum(arr.copy(), rowCounter, columnCounter))
            columnCounter += 1
        
        rowCounter += 1
        
    return max(sums)