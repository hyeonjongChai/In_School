import sys
T = int(sys.stdin.readline()) # 지폐금액
K = int(sys.stdin.readline()) # 동전의 가지수
coin = []

for _ in range(K):
    coin.append(list(map(int, sys.stdin.readline().split())))

dp = [[0]*(T+1) for _ in range(K+1)]