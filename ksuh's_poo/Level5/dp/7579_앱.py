# import sys
#
# si = sys.stdin.readline
# N, M = map(int, si().split())
# m = list(map(int, si().split()))
# c = list(map(int, si().split()))
# dp = [0] * 10001
#
# for i in range(N):
#     cost = c[i]
#     for j in range(10000, cost - 1, -1):
#         if dp[j - cost]:
#             dp[j] = max(dp[j], dp[j - cost] + m[i])
#     dp[cost] = max(dp[cost], m[i])
#
# for i in range(10001):
#     if dp[i] >= M:
#         ans = i
#         break
# print(ans)

def solution():
    import sys
    input = sys.stdin.buffer.readline
    _, M = map(int, input().split())
    dp = {0: 0}
    for m, c in sorted(zip(map(int, input().split()), map(int, input().split())), reverse=True, key=lambda x: x[0]):
        dp.update({ccc: mmm for cc, mm in dp.items() if mm < M and dp.get((ccc := cc + c), 0) < (mmm := mm + m)})
    print(min((cc for cc, mm in dp.items() if mm >= M)))

solution()

# TC
# 5 60
# 30 10 20 35 40
# 3 0 3 5 4
#
# 6