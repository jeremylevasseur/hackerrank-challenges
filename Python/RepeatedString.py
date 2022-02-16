import math
import re

def repeatedString(s, n):
    # Write your code here
    lengthOfSubstring = len(s)
    cleanDivisions = int(math.floor(n/lengthOfSubstring))
    remainder = n % lengthOfSubstring
    substring = ""
    for i in range(cleanDivisions):
        substring += s
        
    substring += s[:remainder]
    r = re.findall('a', substring)
    return len(r)


repeatedString("aba", 10)