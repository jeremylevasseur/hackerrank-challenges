#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def alternatingCharacters(s):
    # Write your code here
    deletionCounter = 0
    listOfAs = re.split("[B]+", s)
    listOfBs = re.split("[A]+", s)
    for aSubString in listOfAs:
        if len(aSubString) > 1:
            deletionCounter += len(aSubString) - 1

    for bSubString in listOfBs:
        if len(bSubString) > 1:
            deletionCounter += len(bSubString) - 1

    return deletionCounter


inputs = ["AAAA", "BBBBB", "ABABABAB", "BABABA", "AAABBB"]

for inputString in inputs:
    deletionCounter = alternatingCharacters(inputString)
    print(deletionCounter)
