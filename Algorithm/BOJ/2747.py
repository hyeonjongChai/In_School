def fib(n):
    fib_list = [0] * (n+1)
    fib_list[0] = 0
    if n > 0:
        fib_list[1] = 1
        for i in range(2,n+1):   
            fib_list[i] = fib_list[n-1] + fib_list[n-2]

    return fib_list[n]

n = in