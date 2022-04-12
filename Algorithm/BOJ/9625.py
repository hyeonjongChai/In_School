K = int(input())
A = [1, 0]
B = [0, 1]

for i in range(2, K+1):
    new_A = A[i-2] + A[i-1]
    new_B = B[i-2] + B[i-1]
    A.append(new_A)
    B.append(new_B)

print(A[-1], B[-1])
# 0   [1, 0]
# 1   [0, 1]
# 2   [1, 1]
# 3   [1, 2]
# 4   [2, 3]
