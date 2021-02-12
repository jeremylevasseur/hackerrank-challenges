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
    print(arr)
    # Write your code here
    backslashDiagSum = 0  # The diagonal with this shape \
    slashDiagSum = 0  # The diagonal with this shape /

    backslashDiagIterator = 0
    slashDiagIterator = len(arr[0]) - 1
    
    for i in range(len(arr)):
        
        backslashDiagSum += int(arr[i][backslashDiagIterator])
        slashDiagSum += int(arr[i][slashDiagIterator])
        
        backslashDiagIterator += 1
        slashDiagIterator -= 1
    
    return abs(backslashDiagSum - slashDiagSum)
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
