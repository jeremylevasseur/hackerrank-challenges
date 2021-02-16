# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    firstNumberOfStudents = int(input())
    firstListOfStudentNumbers = input().split()
    
    secondNumberOfStudents = int(input())
    secondListOfStudentNumbers = input().split()
    
    firstSet = set(firstListOfStudentNumbers)
    secondSet = set(secondListOfStudentNumbers)
    
    print(len(firstSet.union(secondSet)))