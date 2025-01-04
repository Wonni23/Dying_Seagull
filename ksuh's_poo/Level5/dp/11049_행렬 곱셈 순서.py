import sys
si = sys.stdin.readline

N = int(si())
arr = [list(map(int, input().split())) for _ in range(N)]
INF = sys.maxsize
dp = [[INF] * N for _ in range(N - 1)]

if N == 1:
    print(1)
    exit(0)

for _ in range(N - 1):
    dp[0][_] = arr[_][0] * arr[_][1] * arr[_ + 1][1]
for i in range(1, N - 1):
    for j in range(N - i - 1):
        x = arr[j][0] * arr[j + i + 1][1]
        dp[i][j] = min(dp[i - 1][j] + x * arr[j + i + 1][0],
                       dp[i - 1][j + 1] + x * arr[j][1])
        for k in range(2, i + 1):
            print(k - 2, i - k + 2)
            dp[i][j] = min(dp[i][j], dp[k - 2][j] + dp[i - k][j + k] + x * arr[j + k][0])
print(dp)
print(dp[-1][0])


# TC
#
# 3
# 5 3
# 3 2
# 2 6
#
# 90