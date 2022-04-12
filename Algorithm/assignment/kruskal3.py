from sys import stdin
def union(a, b):
    a = find(a)
    b = find(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])  # 경로 압축
    return parent[a]

T = int(stdin.readline())

for _ in range(T):
    V = int(stdin.readline())
    parent = list(range(V+1))
    edges = []
    for i in range(1, V+1): # i 1~10
        temp = list(map(int, stdin.readline().split()))

        for j in range(2, 2*temp[1]+2, 2):
            a, b, cost = temp[0], temp[j], temp[j+1]
            edges.append((cost, a, b))

    edges.sort()
    sum = 0
    for w, s, e in edges:
        if find(s) != find(e):
            union(s, e)
            sum += w

    print(sum)



