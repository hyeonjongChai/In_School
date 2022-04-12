'''input'''

import sys

from quicksort import quicksortH, quicksortL

A = []
T = int(input())

print(T)
for i in range(T):
    a = input().split()
    a = A[1:]
    A.append(a)

for i in range(T):   
    for j in range(len(A[i])):
        A[i][j] = int(A[i][j])
 
for i in range(T):
    tmp = A[i].copy()
    quicksortH(A[i], 0, len(A[i])-1)
    quicksortL(tmp, 0, len(tmp) - 1)
    
    print(f"{swapH} {swapL} {compareH} {compareL}")
    swapH, swapL, compareH, compareL = 0, 0, 0, 0

