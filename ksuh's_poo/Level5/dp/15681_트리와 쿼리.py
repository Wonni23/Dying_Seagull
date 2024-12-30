# import sys
# from collections import defaultdict
#
# sys.setrecursionlimit(10 ** 5)
#
# si = sys.stdin.readline
# N, R, Q = map(int, si().split())
# E = [[] for _ in range(N + 1)]
# for _ in range(N - 1):
#     U, V = map(int, si().split())
#     E[U].append(V)
#     E[V].append(U)
#
# q = [i for i in E[R]]
# visited = [0] * (N + 1)
# chs = defaultdict(list)
# chs[R] = q[:]
# visited[R] = 1
# for i in q:
#     visited[i] = 1
#
# while q:
#     nq = []
#     for parent in q:
#         for child in E[parent]:
#             if not visited[child]:
#                 visited[child] = 1
#                 chs[parent].append(child)
#                 nq.append(child)
#     q = nq
# dp = [0] * (N + 1)
#
#
# def dfs(node):
#     dp[node] += 1
#     for child in chs[node]:
#         dp[node] += dfs(child)
#     return dp[node]
#
#
# dfs(R)
# ans = []
#
# for _ in range(Q):
#     ans.append(dp[int(si())])
# print("\n".join(map(str, ans)))

import sys

si = sys.stdin.readline
N, R, Q = map(int, si().split())
E = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    U, V = map(int, si().split())
    E[U].append(V)
    E[V].append(U)

visited = [0] * (N + 1)
visited[R] = 1
q = [(R, 0)]
dp = [0] * (N + 1)

while q:
    node, v = q.pop()
    if v == len(E[node]):
        for child in E[node]:
            dp[node] += dp[child]
        dp[node] += 1
    else:
        q.append((node, len(E[node])))
        for child in E[node]:
            if not visited[child]:
                visited[child] = 1
                q.append((child, 0))

ans = []

for _ in range(Q):
    ans.append(dp[int(si())])
print("\n".join(map(str, ans)))

# TC
# 9 5 3
# 1 3
# 4 3
# 5 4
# 5 6
# 6 7
# 2 3
# 9 6
# 6 8
# 5
# 4
# 8
#
# 9
# 4
# 1