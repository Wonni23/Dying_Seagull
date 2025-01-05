import sys

si = sys.stdin.readline
N, M, K = map(int, si().split())
c = [0] + list(map(int, si().split()))
p = [i for i in range(N + 1)]
cnt = [1] * (N + 1)


def find_parent(x):
    if p[x] != x:
        p[x] = find_parent(p[x])
    return p[x]


def unify(a, b):
    x, y = find_parent(a), find_parent(b)
    if x == y:
        return
    if x > y:
        x, y = y, x
    c[x] += c[y]
    cnt[x] += cnt[y]
    p[y] = x


for _ in range(M):
    a, b = map(int, si().split())
    unify(a, b)

candidates = [(cnt[i], c[i]) for i in range(1, N + 1) if p[i] == i]
candidates.sort()
dp = [0] * K

for cnt, cost in candidates:
    for i in range(K - 1, cnt - 1, -1):
        dp[i] = max(dp[i], dp[i - cnt] + cost)
print(dp[-1])

# TC

# 10 6 6
# 9 15 4 4 1 5 19 14 20 5
# 1 3
# 2 5
# 4 9
# 6 2
# 7 8
# 6 10
#
# 57
#
# 5 4 4
# 9 9 9 9 9
# 1 2
# 2 3
# 3 4
# 4 5
#
# 0