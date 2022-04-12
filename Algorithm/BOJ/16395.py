import sys

n, k = map(int, sys.stdin.readline().split())

pascal = [[1], 
        [1,1]]

for i in range(2, n):
    next_row = [1]
    for j in range(1, i):
        next_row.append(pascal[i-1][j-1]+pascal[i-1][j])
    next_row.append(1)
    pascal.append(next_row)

print(pascal[n-1][k-1])
