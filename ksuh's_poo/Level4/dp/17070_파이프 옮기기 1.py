N = int(input())
arr = [input().split() for _ in range(N)]
dp_row, dp_col, dp_diag = [[0] * N for _ in range(N)], [[0] * N for _ in range(N)], [[0] * N for _ in range(N)]

for _ in range(1, N):
    if arr[0][_] == '1':
        break
    dp_row[0][_] = 1

for i in range(1, N):
    for j in range(1, N):
        if arr[i][j] == '1':
            continue
        dp_row[i][j] = dp_row[i][j - 1] + dp_diag[i][j - 1]
        dp_col[i][j] = dp_col[i - 1][j] + dp_diag[i - 1][j]
        if arr[i][j - 1] == '0' and arr[i - 1][j] == '0':
            dp_diag[i][j] = dp_diag[i - 1][j - 1] + dp_row[i - 1][j - 1] + dp_col[i - 1][j - 1]

print(dp_row[N - 1][N - 1] + dp_col[N - 1][N - 1] + dp_diag[N - 1][N - 1])
# 3
# 0 0 0
# 0 0 0
# 0 0 0
#
# 1
#
# 4
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0
#
# 3
#
# 5
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
#
# 0
#
# 6
# 0 0 0 0 0 0
# 0 1 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
#
# 13