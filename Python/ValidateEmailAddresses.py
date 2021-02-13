import re

def fun(s):
    
    # return True if s is a valid email, else return False
    regexPattern = "^[A-Za-z0-9_-]+[@][A-Za-z0-9]+[.][A-Za-z]{1,3}$"

    if(re.search(regexPattern,s)):  
        return True
    else:  
        return False



print(fun('la.ra@hackerrankcom'))
print(fun('brian-23@hackerrank.com'))
print(fun('britts_54@hackerrank.com'))
