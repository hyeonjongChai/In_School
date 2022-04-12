N = int(input())
fib = [0, 1]

for i in range(2, N+1):
    n = fib[i-1]+ fib[i-2]
    fib.append(n)

print(fib[N])