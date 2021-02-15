
def runnerUp(n, arr):

    tempArr = list(arr)
    tempArr.sort(reverse=True)
    
    highestNum = min(tempArr)
    secondHighestNum = min(tempArr)
    
    for element in tempArr:
        if element >= highestNum:
            highestNum = element
        
        if element >= secondHighestNum and element != highestNum:
            secondHighestNum = element
    
    print(secondHighestNum)
    return secondHighestNum

n = 3
arr = [-10, 0, 10]
runnerUp(n, arr)