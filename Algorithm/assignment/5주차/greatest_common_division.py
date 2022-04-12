def gcb(a, b=0):
    big = 0
    small = 0
    
    if a==0 :
        return print(b)

    elif b==0:
        return print(a)
    
    elif a >= b:
        big = a
        small = b
    
    elif a < b:
        small = a
        big = b
        
        
    if (big % small) == 0:
        return print(small)
    
    else:
        gcb(small, big%small)

import sys

T = int(input())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    gcb(a,b)