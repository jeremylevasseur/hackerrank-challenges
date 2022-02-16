def swap_case(string):
    outputString = ""
    for stringChar in string:
        if stringChar.isupper():
            outputString += stringChar.lower()
        else:
            outputString += stringChar.upper()
            
    return outputString

if __name__ == '__main__':
    s = "HackerRank"
    result = swap_case(s)
    print(result)