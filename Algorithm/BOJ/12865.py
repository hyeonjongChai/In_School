import sys

N, K = map(int, sys.stdin.readline().split())

print(N, K)
for i in range(N):
    items = {}
    W, V = map(int, sys.stdin.readline().split())
    items[W] = V
    print(items)


    