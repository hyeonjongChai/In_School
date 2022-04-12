import sys

T = int(sys.stdin.readline())
for _ in range(T):
    A, B = sys.stdin.readline().split()
    result = 0
    DP = [[0]*(len(B)+1) for _ in range(len(A)+1)]
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                DP[i][j] = DP[i-1][j-1] + 1
                result = max(DP[i][j], result)
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])
                result = max(result, DP[i][j])
    
    # print(DP)
    print(result)
