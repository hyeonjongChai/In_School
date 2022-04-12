def minCut(N, cuts):
    cuts.sort()
    cuts = [0]+cuts+[N]
    m = len(cuts)
    dp = [[0 for _ in range(m)] for _ in range(m)]
    for d in range(1, m+1):
        for i in range(m-d+1):
            j = i + d -1
            if i + 1 >= j:
                dp[i][j] = 0
                continue
            res = float('inf')
            for k in range(i+1,j):
                res = min(dp[i][k] + dp[k][j] + cuts[j]-cuts[i], res)
            dp[i][j] = res
    return (print(dp[0][m-1]), print(dp)) 

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, X = map(int, sys.stdin.readline().split())
    cuts = list(map(int, sys.stdin.readline().split()))
    minCut(N, cuts)
    