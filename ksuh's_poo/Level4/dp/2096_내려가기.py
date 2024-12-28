import sys

si = sys.stdin.readline
N = int(si())
dp_m, dp_M = [0] * 3, [0] * 3

for _ in range(N):
    a, b, c = map(int, si().split())
    x, y = [0] * 3, [0] * 3
    x[0] = min(dp_m[0], dp_m[1]) + a
    x[1] = min(dp_m) + b
    x[2] = min(dp_m[1], dp_m[2]) + c
    y[0] = max(dp_M[0], dp_M[1]) + a
    y[1] = max(dp_M) + b
    y[2] = max(dp_M[1], dp_M[2]) + c
    dp_m = x
    dp_M = y

print(max(dp_M), min(dp_m))

# TC

# 3
# 1 2 3
# 4 5 6
# 4 9 0
#
# 18 6
#
# 3
# 0 0 0
# 0 0 0
# 0 0 0
#
# 0 0