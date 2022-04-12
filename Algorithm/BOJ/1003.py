count0 = [1, 0]
count1 = [0, 1]

def fibonacci(n):
    if n == 0: return print('1 0')
    
    elif n == 1: return print('0 1')
    
    else: 
        for i in range(2, n+1):
            count0.append(count0[i-1] + count0[i-2])
            count1.append(count1[i-1] + count1[i-2])

    print(count0[n], count1[n])

import sys    

T = int(sys.stdin.readline())

for i in range(T):
    N = int(input())
    fibonacci(N)
    count0 = [1, 0]
    count1 = [0, 1]
    
