n = int(input())
minsum = 0
while n > 0:
    if n % 5 == 0: 
        minsum += (n//5)
        break
    else:
        n -= 2
        minsum += 1
if n < 0:
    print(-1)
else: 
    print(minsum)
    