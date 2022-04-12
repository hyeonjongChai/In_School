def kmp(text, pattern):
    ans = []
    fail = getFail(pattern)
    n = len(text)
    m = len(pattern)
    
    j = 0
    for i in range(n):
        while(j > 0 and text[i] != pattern[j]):
            j = fail[j-1]
            # print(j)
        
        if text[i] == pattern[j]:
            if j == m-1:
                ans.append()
                j = fail[j]
            
            else:
                j += 1

    return ans

def getFail(pattern):
    m = len(pattern)
    j = 0
    fail = [0] * m

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = fail[j-1]
        if pattern[i] == pattern[j]:
            fail[i] = j+1

    print(fail)
    return fail

from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    pattern, text = stdin.readline().split()
    ans = kmp(text, pattern)
    print(ans)
