if __name__ == '__main__':
    data = [
        ['Harsh', 20],
        ['Beria', 20],
        ['Varun', 19],
        ['Kakunami', 19],
        ['Vikas', 21]
    ]

    records = []
    lowestGrade = 100
    secondLowestGrade = 100
    for i in range(len(data)):
        name = data[i][0]
        score = data[i][1]
        records.append([name, score])
        
        if score < secondLowestGrade and score != lowestGrade:
            secondLowestGrade = score
        
        if score < lowestGrade:
            secondLowestGrade = lowestGrade
            lowestGrade = score

    secondLowestGrades = []
    for i in range(len(records)):
        if records[i][1] == secondLowestGrade:
            secondLowestGrades.append(records[i][0])
    
    secondLowestGrades.sort()
    
    for i in range(len(secondLowestGrades)):
        print(secondLowestGrades[i])
    
    