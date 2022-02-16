import math
import os
import random
import re
import sys

def solve(nameString):
    capitalizedString = list(nameString)

    if nameString[0] != " ":
        capitalizedString[0] = nameString[0].upper()

    regexPattern1 = r" ([a-zA-Z])"
    for match in re.finditer(regexPattern1, nameString):
        capitalizedString[match.span()[1] - 1] = nameString[match.span()[1] - 1].upper()

    return "".join(capitalizedString)

if __name__ == '__main__':

    inputStrings = [
        "jeremy     levasseur     loool   lol lol",
        # " jeremy",
        # "levasseur ",
        # "jeremy levasseur"
    ]

    for inputString in inputStrings:
        result = solve(inputString)
        print(result)

