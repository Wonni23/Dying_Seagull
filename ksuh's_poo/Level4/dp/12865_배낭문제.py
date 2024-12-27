import sys

si = sys.stdin.readline
# 1<=N<=100, 1<=K<=100000
# 1<=W<=100000, 0<=V<=1000

N, K = map(int, si().split())
dp = [0] * (K + 1)
arr = [list(map(int, si().split())) for _ in range(N)]
arr.sort(key=lambda x: x[0])

for W, V in arr:
    for i in range(K, W - 1, -1):
        dp[i] = max(dp[i], dp[i - W] + V)
print(dp[K])

# TC
# 4 7
# 6 13
# 4 8
# 3 6
# 5 12
#
# 14