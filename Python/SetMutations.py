# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    aNumberOfElements = int(input())
    setA = set(input().split())
    
    numberOfOtherSets = int(input())
    
    for _ in range(numberOfOtherSets):
        operation, *numberOfDigitsInSet = input().split()
        newSet = set(input().split())
        
        if operation == "update":
            setA.update(newSet)
        elif operation == "intersection_update":
            setA.intersection_update(newSet)
        elif operation == "difference_update":
            setA.difference_update(newSet)
        elif operation == "symmetric_difference_update":
            setA.symmetric_difference_update(newSet)
        
    sumOfA = 0
    for element in setA:
        sumOfA += int(element)
        
    print(sumOfA)