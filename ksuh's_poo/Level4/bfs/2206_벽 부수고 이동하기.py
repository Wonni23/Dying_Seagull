import sys

si = sys.stdin.readline

N, M = map(int, si().split())
a = [list(map(int, list(si().strip()))) for _ in range(N)]
b = [a[i][:] for i in range(N)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
INF = sys.maxsize

v1 = [[INF] * M for _ in range(N)]
v2 = [[INF] * M for _ in range(N)]
v1[0][0] = 1
v2[-1][-1] = 0
q = [(0, 0)]
dist = 2
while q:
    nq = []
    for x, y in q:
        if a[x][y] == 1:
            continue
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and v1[nx][ny] > dist:
                v1[nx][ny] = dist
                nq.append((nx, ny))
    q = nq
    dist += 1
q = [(N - 1, M - 1)]
dist = 1
while q:
    nq = []
    for x, y in q:
        if b[x][y] == 1:
            continue
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and v2[nx][ny] > dist:
                v2[nx][ny] = dist
                nq.append((nx, ny))
    q = nq
    dist += 1
ans = v1[-1][-1]

for i in range(N):
    for j in range(M):
        if a[i][j] == 1 and v1[i][j] != INF and v2[i][j] != INF:
            ans = min(ans, v1[i][j] + v2[i][j])

if ans == INF:
    print(-1)
else:
    print(ans)

# TC

# 6 4
# 0100
# 1110
# 1000
# 0000
# 0111
# 0000
#
# 15
#
# 4 4
# 0111
# 1111
# 1111
# 1110
#
# -1