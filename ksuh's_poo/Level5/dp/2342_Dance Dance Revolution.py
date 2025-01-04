arr = list(map(int, input().split()))
arr.pop()
L = len(arr)
dp = [2]
INF = 999999
k = [[2, 2, 2, 2, 2],
     [2, 1, 3, 4, 3],
     [2, 3, 1, 3, 4],
     [2, 4, 3, 1, 3],
     [2, 3, 4, 3, 1]]

for i in range(1, L):
    v = arr[i]
    d = [INF] * 5
    x = arr[i - 1]
    for y, V in enumerate(dp):
        if V == INF:
            continue
        if v != y:
            z = k[x][v]
            d[y] = min(d[y], V + z)
        if v != x:
            z = k[y][v]
            d[x] = min(d[x], V + z)
    dp = d
    print("dp: ", dp)

print(min(dp))

# TC
# 1 2 2 4 0
# 8