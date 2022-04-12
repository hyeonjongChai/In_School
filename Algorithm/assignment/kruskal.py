import sys
# import math
# inf = math.inf

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    edges = []
    for i in range(1, n+1): # i 1~10
        temp = list(map(int, sys.stdin.readline().split()))
        v, e = n, temp[1]
        parent = [0] * (v+1)
        
        result = 0

        for k in range(1, v+1):
            parent[k] = k

        for j in range(2, 2*temp[1]+2, 2):
            a, b, cost = temp[0], temp[j], temp[j+1]
            edges.append((cost, a, b))
        
        edges.sort()
        # print(edges)
        for edge in edges:
            cost, a, b = edge
            if find_parent(parent,a) != find_parent(parent, b):
                union_parent(parent, a, b)
                result += cost
        
    print(result)