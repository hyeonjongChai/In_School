def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    patCount = 0 
    lps = [0]*M

    computeLPS(pat, lps) # getFail

    i = 0 
    j = 0  
    while i < N:
        
        if pat[j] == txt[i]:
            
            i += 1
            j += 1
        elif pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

        if j == M:
            j = lps[j-1]
            patCount += 1
    return lps, patCount

def computeLPS(pat, lps):
    leng = 0 
    i = 1
    while i < len(pat):
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng-1]
            else:
                lps[i] = 0
                i += 1
    return lps


from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    pat, txt = stdin.readline().split()
    
    lps, patCount = KMPSearch(pat, txt)
    for i in lps:
        print(i, end = ' ')
    print(f"\n{patCount}")