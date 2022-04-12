import sys

N = int(input())
A = []

for i in range(N): A.append(int(sys.stdin.readline()))

# '''bubble sort'''
# for i in range(N):
#     for j in range(N-i-1):
#         if A[j] > A[j+1]: A[j], A[j+1] = A[j+1], A[j]

# for i in A: print(i)

'''insert sort'''
for i in range(1, N):
    key = A[i]
    j = i-1
    while (j >= 0 & key < A[i]):
        A[i+1] = A[i]
        j -= 1
    A[i+1] = key

print(A)
