N = int(input())
A = list(map(int, input().split()))
# dp_up = [1] * N
# dp_down = [1] * N
#
# for i in range(N):
#     for j in range(i - 1, -1, -1):
#         if A[i] > A[j]:
#             dp_up[i] = max(dp_up[i], dp_up[j] + 1)
#         elif A[i] == A[j]:
#             dp_up[i] = max(dp_up[i], dp_up[j])
#
# for i in range(N - 1, -1, -1):
#     for j in range(i + 1, N):
#         if A[i] > A[j]:
#             dp_down[i] = max(dp_down[i], dp_down[j] + 1)
#         elif A[i] == A[j]:
#             dp_down[i] = max(dp_down[i], dp_down[j])
# dp = [dp_up[i] + dp_down[i] for i in range(N)]
# print(max(dp) - 1)

from bisect import bisect_left

l = [A[0]]
dp_up = [1] * N
for i in range(1, N):
    if A[i] > l[-1]:
        l.append(A[i])
        dp_up[i] = len(l)
    else:
        idx = bisect_left(l, A[i])
        dp_up[i] = idx + 1
        l[idx] = A[i]
d = [A[-1]]
for i in range(N - 2, -1, -1):
    if A[i] > d[-1]:
        d.append(A[i])
        dp_up[i] += len(d)
    else:
        idx = bisect_left(d, A[i])
        dp_up[i] += idx + 1
        d[idx] = A[i]
print(max(dp_up) - 1)


# TC
# 10
# 1 5 2 1 4 3 4 5 2 1

# 7