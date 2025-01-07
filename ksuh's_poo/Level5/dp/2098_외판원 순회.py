from itertools import combinations

def set_to_int(l):
    res = 0
    for item in l:
        res = res | 1<<(item - 1)
    return res

N = int(input())
adj = [[0]*(N+1)]
for _ in range(N):
    adj.append([0]+list(map(int, input().split())))
memo = [[16777216] * N for _ in range(1<<(N-1))]

for i in range(1, N):
    if adj[N][i] :
        memo[1<<(i-1)][i] = adj[N][i]

for i in range(2, N):
    for combi in combinations(range(1, N), i):
        bitset = set_to_int(combi)
        for v in combi:
            min_dist = 16777216
            bitset = bitset ^ (1<<(v-1))
            for u in combi:
                tmp = memo[bitset][u] + adj[u][v]
                if adj[u][v] != 0 and min_dist > tmp :
                    min_dist = tmp
            bitset = bitset | (1<<(v-1))
            memo[bitset][v] = min_dist

bitset = set_to_int([i for i in range(1, N)])
for i in range(1, N):
    final_cost = 16777216 if adj[i][N] == 0 else memo[bitset][i] + adj[i][N]
    memo[bitset][i] = final_cost

print(min(memo[bitset]))

# N = int(input())
# s = [list(map(int, input().split())) for _ in range(N)]
# INF = 20000000
# b = [1 << i for i in range(N)]
# dp = [[INF] * (1 << N) for _ in range(N)]
#
# stack = []
# for i in range(N):
#     for j in range(N):
#         if s[i][j]:
#             stack.append((i, j, b[i] + b[j], s[i][j]))
#
# for i in range(N - 2):
#     n = []
#     while stack:
#         start, prev, ss, t = stack.pop()
#         for k in range(N):
#             if ss & b[k] or s[prev][k] == 0:
#                 continue
#             to = ss | b[k]
#             new = t + s[prev][k]
#             if dp[k][to] > new:
#                 dp[k][to] = new
#                 n.append((start, k, to, new))
#     stack = n
# ans = INF
# for start, prev, ss, t in stack:
#     if s[prev][start]:
#         ans = min(ans, t + s[prev][start])
# print(ans)

# TC

# 4
# 0 10 15 20
# 5 0 9 10
# 6 13 0 12
# 8 8 9 0
#
# 35