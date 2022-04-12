import sys, copy
sys.setrecursionlimit(10**6)

compareH, swapH , compareL , swapL = 0,0,0,0

'''Hoare's partition'''

def quicksortH(A, low, high):
    if low < high:
        p = partitionH(A, low, high)
        quicksortH(A, low, p)
        quicksortH(A, p + 1, high)

def partitionH(A, low, high):
    global compareH
    global swapH

    pivot = A[low]
    i = low - 1
    j = high + 1

    while(True):
        i += 1
        compareH += 1 #compare
        while(A[i] < pivot):
            compareH += 1 #compare
            i += 1  
        j -= 1
        compareH += 1 #compare 
        while(A[j] > pivot):
            compareH += 1 #compare
            j -= 1
            
        if (i < j): 
            A[i], A[j] = A[j], A[i]
            swapH += 1 #swap
        else:
            return j 

'''Lomuto's partition'''

def quicksortL(A,low,high):
    if(low < high):
        p = partitionL(A, low, high)

        quicksortL(A, low, p-1)
        quicksortL(A, p+1, high)

def partitionL(A,low,high):
    global swapL, compareL

    pivot = A[low]
    j = low

    for i in range(low+1, high+1):
        compareL += 1 #compare
        if(A[i] < pivot):
            j += 1
            A[i], A[j] = A[j], A[i]
            swapL += 1 #swap

    pivot_pos = j
    A[pivot_pos], A[low] = A[low], A[pivot_pos]
    swapL += 1 #swap
    return pivot_pos


T = input()
A = []
for i in range(int(T)):
    a = input().split()
    a = a[1:]
    A.append(a)
for i in range(int(T)):
    for j in range(len(A[i])):
        A[i][j] = int(A[i][j])

for i in range(int(T)):
    tmp = A[i].copy()
    quicksortH(A[i], 0, len(A[i])-1)
    quicksortL(tmp, 0, len(tmp)-1)
    print(swapH, swapL, compareH, compareL)
    compareH, swapH , compareL , swapL = 0,0,0,0
