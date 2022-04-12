def coinCase(coins, change) -> int:
    dp = [0 for _ in range(change+1)]
    dp[0] = 1
    
    for c in coins:
        for j in range(1, change+1):
            if (j-c) >= 0:
                dp[j] += dp[j-c]
    return print(dp[-1])

import sys

T = int(sys.stdin.readline()) 

for _ in range(T):
    change = int(sys.stdin.readline())
    citer, *coins = map(int, sys.stdin.readline().split())
    coinCase(coins, change)