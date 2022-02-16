from pprint import pprint

def minion_game(string):
    scoreKevin = 0
    scoreStuart = 0
    vowels = "AEIOU"
    for i in range(len(string)):
        if string[i] in vowels:
            scoreKevin += (len(s) - i)
        else:
            scoreStuart += (len(s) - i)

    if scoreKevin > scoreStuart:
        print("Kevin %d" % scoreKevin)
    elif scoreStuart > scoreKevin:
        print("Stuart %d" % scoreStuart)
    else:
        print("Draw")


if __name__ == '__main__':
    s = "BAANANAS"
    minion_game(s)

