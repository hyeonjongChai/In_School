import sys
from itertools import permutations;

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

cards = [str(sys.stdin.readline().rstrip()) for i in range(n)]
nums = set()

for i in permutations(cards, k):
    nums.add(''.join(i))

print(len(nums))