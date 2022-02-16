
def sockMerchant(n, arr):
    arr.sort()
    numberOfPairs = 0
    i = 0
    while i < len(arr):
        sock = arr[i]
        if i < len(arr) - 1:
            if arr[i+1] == sock:
                numberOfPairs += 1
                i += 1

        i += 1
    
    return numberOfPairs

n = 7
arr = [1,2,1,2,1,3,2]
numberOfPairs = sockMerchant(n, arr)
print(numberOfPairs)