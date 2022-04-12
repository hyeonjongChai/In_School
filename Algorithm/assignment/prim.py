import math
import sys

inf  = math.inf
adj_mat = []

def get_min_node(node_num):
    for i in range(node_num):
        if not visited[i]:
            v = i
            break
    for i in range(node_num):
        if not visited[i] and distances[i] < distances[v]:
            v = i

    return v

def prim(start, node_num):
    # distances 배열과 visted 배열 초기화
    for i in range(node_num):
        visited[i] = False
        distances[i] = inf

    # 시작노드의 distance 값을 0으로 초기화
    distances[start] = 0
    for i in range(node_num):
        node = get_min_node(node_num)
        visited[node] = True    # node 를 방문했다 표시

        for j in range(node_num):
            if adj_mat[node][j] != inf:
                if not visited[j] and adj_mat[node][j] < distances[j]:
                    distances[j] = adj_mat[node][j]


T = int(sys.stdin.readline())

for _ in range(T):
    nn = int(sys.stdin.readline())
    adj_mat = []

    for i in range(nn):
        adj_mat.append([inf]*nn)
        temp = list(map(int, sys.stdin.readline().split()))
        for j in range(2, len(temp)-1, 2):
            adj_mat[temp[0]-1][temp[0]-1] = 0 
            adj_mat[temp[0]-1][temp[j]-1] = temp[j+1] 

    node_num = len(adj_mat)
    visited = [False] * node_num
    distances = [inf] * node_num 

    prim(0, node_num)
    print(sum(distances))