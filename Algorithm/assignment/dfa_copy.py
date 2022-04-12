import sys 

R = 3

# strToInt

def refine(abclist):
    refinelist = []
    for i in abclist:
        if i == 'A':
            refinelist.append(0)
        elif i == 'B':
            refinelist.append(1)
        else:
            refinelist.append(2)
    return refinelist

def construct_dfa(pattern):
    not_0_edge = 0
    patLength = len(pattern)
    DFA = []
    for i in range(0,R):
        DFA.append([])
        for j in range(0,patLength+1):
            DFA[i].append(0)
    DFA[pattern[0]][0] = 1
    X = 0
    
    for j in range(1, patLength+1):
        for c in range(0,R):
            DFA[c][j] = DFA[c][X]
        if j < patLength:
            DFA[pattern[j]][j] = j+1
            X = DFA[pattern[j]][X]
    for i in range(0,R):
        for j in range(0, patLength+1):
            if DFA[i][j] != 0:
                not_0_edge += 1   
    return DFA, not_0_edge

def find_pattern(DFA,pattern,text):
    pat_count = 0
    i = 0
    state = 0
    while(i < len(text)):
        state = DFA[text[i]][state]
        if state == len(pattern):
            pat_count += 1
        i += 1
    return pat_count

#입력
# 테스트 케이스 입력
test_case = int(str(sys.stdin.readline().rstrip()))

# 각 케이스 순서대로 입력, 답 저장
sol = []
for i in range(test_case):
    pattern, text = map(list,sys.stdin.readline().split())
    pattern = refine(pattern)
    text = refine(text)
    DFA, not_0_edge = construct_dfa(pattern)
    sol.append((not_0_edge, find_pattern(DFA,pattern,text)))

#출력
# 각 케이스들의 답을 순서대로 출력
for i in range(test_case):
    print(sol[i][0], end=' ')
    print(sol[i][1])