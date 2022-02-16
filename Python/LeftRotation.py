#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#
def performRotLeft(a, numberOfRotations):
    _a = a.copy()
    for j in range(len(a)):
        _a[j-numberOfRotations] = a[j]
    return _a

def rotLeft(a, d):
    # Write your code here
    remainder = d % len(a)
    a = performRotLeft(a, remainder)
    return a
        
            
