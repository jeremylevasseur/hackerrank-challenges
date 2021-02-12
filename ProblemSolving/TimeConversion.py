#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    # Getting AM or PM
    amOrPm = s[-2:]
    
    # Getting hour, minute, and second values
    splitArray = s[:-2].split(":")
    hour = int(splitArray[0])
    minute = splitArray[1]
    second = splitArray[2]
    
    if amOrPm == "AM":
        
        if hour == 12:
            hour = "00"
        else:
            hour = "{:02d}".format(hour)
            
    else:
        
        if hour < 12:
            hour = "{:02d}".format(hour + 12)
        else:
            hour = "{:02d}".format(hour)
    
    return hour + ":" + minute + ":" + second

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
