#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    deletedCharactersCounter = 0
    aSet = set(list(a))
    aCharacterCounter = dict(Counter(a))
    bSet = set(list(b))
    bCharacterCounter = dict(Counter(b))
    intersection = aSet & bSet
    symmetricDifference = aSet ^ bSet
    
    for symmetricCharacter in symmetricDifference:
        if symmetricCharacter in aCharacterCounter:
            deletedCharactersCounter += aCharacterCounter[symmetricCharacter]

        if symmetricCharacter in bCharacterCounter:
            deletedCharactersCounter += bCharacterCounter[symmetricCharacter]

    for intersectionCharacter in intersection:
        deletedCharactersCounter += abs(
            aCharacterCounter[intersectionCharacter] - bCharacterCounter[intersectionCharacter]
        )
        
    return deletedCharactersCounter
    

if __name__ == '__main__':

    a = 'abc'

    b = 'ccbee'

    res = makeAnagram(a, b)
    print(res)
