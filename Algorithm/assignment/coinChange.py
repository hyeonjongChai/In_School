def coinChange(coins, amount: int) -> int:
    dp = [float('inf') for _ in range(amount+1)]
    dp[0] = 0

    for i in range(len(dp)):
        for c in coins:
            if (i-c) >= 0:
                dp[i] = min(dp[i], dp[i-c]+1)
    return print(dp[-1])
    # return -1 if dp[-1] == float('inf') else dp[-1]

import sys

T = int(sys.stdin.readline()) 

for _ in range(T):
    change = int(sys.stdin.readline())
    citer, *coins = map(int, sys.stdin.readline().split())
    coinChange(coins, change)
