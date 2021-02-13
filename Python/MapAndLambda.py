cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
        
    fibonacciNumbers = [0]
    
    while len(fibonacciNumbers) < n:
        if len(fibonacciNumbers) < 2:
            fibonacciNumbers.append(1)
        else:
            newFibonacciNumber = fibonacciNumbers[-1] + fibonacciNumbers[-2]
            fibonacciNumbers.append(newFibonacciNumber)
    
    print(fibonacciNumbers)
    return fibonacciNumbers

if __name__ == '__main__':
    n = 5
    print(list(map(cube, fibonacci(n))))