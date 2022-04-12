def hanoi_tower(n, a, b, c):
    # n: number of disks, a: source peg, c: target peg, b: intermediate peg
    global count
    if n > 0:
        hanoi_tower(n-1, a,c,b)
        count += 1
        print(f"{count}번째 이동// {a} ---> {c}")
        if (count == l):
            return print(a, c)
        hanoi_tower(n-1,b,a,c)

def solve_hanoi_tower(n):
    hanoi_tower(n, 1, 2, 3)

T = int(input())

for i in range(T):
    n, l = map(int, input().split())
    count = 0
    solve_hanoi_tower(n)


    