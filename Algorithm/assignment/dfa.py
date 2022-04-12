def strToInt(txt):
    strToInt = []
    for i in range(len(txt)):
        if txt[i] == 'A': strToInt.append(0)
        elif txt[i] == 'B': strToInt.append(1)
        elif txt[i] == 'C': strToInt.append(2)
    return strToInt

def constructDFA(pattern):
    notZero = 0
    DFA =  [[0 for _ in range(patLength+1)] for __ in range(R)]
    DFA[pattern[0]][0] = 1 
    X = 0

    for j in range(1, patLength):
        for c in range(R):
            DFA[c][j] = DFA[c][X]

        if j < patLength:
            DFA[pattern[j]][j] = j+1
            X = DFA[pattern[j]][X]

    for i in range(0,R):
        for j in range(0, patLength+1):
            if DFA[i][j] != 0:
                notZero += 1   
    return DFA, notZero

def KMP(text):
    patCount = 0
    i = 0
    j = 0
    for i in range(txtLength+1):
        if j < patLength:
            j = DFA[text[i]][j]
        
        if j == len(pattern):
            patCount += 1
    
    return patCount

from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    pattern, text = stdin.readline().split()
    pattern = strToInt(pattern)
    text = strToInt(text)

    patLength = len(pattern)
    txtLength = len(text)
    R = 3
    
    DFA, notZero = constructDFA(pattern)
    print(notZero, KMP(text))