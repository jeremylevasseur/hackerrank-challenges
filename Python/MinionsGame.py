from pprint import pprint

from itertools import combinations


def is_vowel(character):
    if character.lower() in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False


def minion_game2(string):
    gameScore = {
        'Stuart': {
            'score': 0,
            'substrings': []
        },
        'Kevin': {
            'score': 0,
            'substrings': []
        }
    }

    stringList = list(string)
    allPossibleSubstrings = []

    i = 0
    while i < len(string):
        subSection = stringList[i:]
        j = 1
        while j < len(subSection) + 1:
            substring = stringList[i:i+j]
            joinedSubstring = "".join(substring)
            if not (joinedSubstring in allPossibleSubstrings):
                # Valid substring
                allPossibleSubstrings.append(joinedSubstring)
                numberOfPoints = 0
                for k in range(len(string)):
                    if k + len(joinedSubstring) > len(string):
                        break
                    else:
                        if string[k:k+len(joinedSubstring)] == joinedSubstring:
                            numberOfPoints += 1
                
                if is_vowel(substring[0]):
                    # Kevin's point
                    gameScore['Kevin']['score'] += numberOfPoints
                    gameScore['Kevin']['substrings'].append(substring)
                    print(substring, "==>", numberOfPoints, " Points to Kevin")
                else:
                    # Stuart's point
                    gameScore['Stuart']['score'] += numberOfPoints
                    gameScore['Stuart']['substrings'].append(substring)
                    print(substring, "==>", numberOfPoints, " Points to Stuart")

            j += 1

        i += 1

    # Game is now complete, will declare results
    if gameScore['Stuart']['score'] > gameScore['Kevin']['score']:
        # Stuart wins
        print("Stuart %d" % (gameScore['Stuart']['score']))
    elif gameScore['Stuart']['score'] < gameScore['Kevin']['score']:
        # Kevin wins
        print("Kevin %d" % (gameScore['Kevin']['score']))
    else:
        # Draw
        print("Draw")

def get_all_possible_substrings(string):
    
    stringList = list(string)
    allPossibleSubstrings = []

    i = 0
    while i < len(string):
        subSection = stringList[i:]
        j = 1
        while j < len(subSection) + 1:
            substring = stringList[i:i+j]
            joinedSubstring = "".join(substring)
            if not (joinedSubstring in allPossibleSubstrings):
                allPossibleSubstrings.append(joinedSubstring)
            j += 1

        i += 1
    
    return allPossibleSubstrings

def get_number_of_points(string, substring):
    numberOfPoints = 0
    for i in range(len(string)):
        if i + len(substring) > len(string):
            break
        else:
            if string[i:i+len(substring)] == substring:
                numberOfPoints += 1
    
    return numberOfPoints


def minion_game(string):
    gameScore = {
        'Stuart': {
            'score': 0,
            'substrings': []
        },
        'Kevin': {
            'score': 0,
            'substrings': []
        }
    }
    
    allPossibleSubstrings = get_all_possible_substrings(string)
    
    for substring in allPossibleSubstrings:
        numberOfPoints = get_number_of_points(string, substring)
        if is_vowel(substring[0]):
            # Kevin's point
            gameScore['Kevin']['score'] += numberOfPoints
            gameScore['Kevin']['substrings'].append(substring)
            # print(substring, "==>", numberOfPoints, " Points to Kevin")
        else:
            # Stuart's point
            gameScore['Stuart']['score'] += numberOfPoints
            gameScore['Stuart']['substrings'].append(substring)
            # print(substring, "==>", numberOfPoints, " Points to Stuart")

    # Game is now complete, will declare results
    if gameScore['Stuart']['score'] > gameScore['Kevin']['score']:
        # Stuart wins
        print("Stuart %d" % (gameScore['Stuart']['score']))
    elif gameScore['Stuart']['score'] < gameScore['Kevin']['score']:
        # Kevin wins
        print("Kevin %d" % (gameScore['Kevin']['score']))
    else:
        # Draw
        print("Draw")

if __name__ == '__main__':
    s = "BAANANAS"
    minion_game2(s)

