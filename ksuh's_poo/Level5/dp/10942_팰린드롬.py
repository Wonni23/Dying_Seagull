import sys

si = sys.stdin.readline
N = int(si())
arr = [0] + list(map(int, si().split()))
dp = [0] * (N + 1)
dp1 = [0] * (N + 1)

for i in range(1, N + 1):
    m = min(i - 1, N - i)
    x = 0
    for j in range(1, m + 1):
        if arr[i - j] != arr[i + j]:
            break
        x = j
    dp[i] = x
for i in range(1, N):
    m = min(i, N - i)
    x = -1
    for j in range(m):
        if arr[i - j] != arr[i + 1 + j]:
            break
        x = j
    dp1[i] = x

M = int(si())
res = [0] * M

for _ in range(M):
    S, E = map(int, si().split())
    if (S + E) % 2:
        m = (S + E) // 2
        x = dp1[m]
        if m + x + 1 >= E:
            res[_] = 1
    else:
        m = (S + E) // 2
        x = dp[m]
        if m + x >= E:
            res[_] = 1
print("\n".join(map(str, res)))

x = 0
for x in range(4):
    if x == 2:
        x -= 1
        break
    print(x)
print("x: ", x)

# TC
# 7
# 1 2 1 3 1 2 1
# 4
# 1 3
# 2 5
# 3 3
# 5 7
#
# 1
# 0
# 1
# 1