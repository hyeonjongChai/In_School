N = int(input())

tile = [4,6]

for i in range(2, N):
    new_t = tile[i-2] + tile[i-1]
    tile.append(new_t)

print(tile[N-1])