import sys

si = sys.stdin.readline
N, M = map(int, si().split())
p = [list(map(int, si().split())) for _ in range(N)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = [[0] * M for _ in range(N)]
q = [(0, _) for _ in range(M)] + [(N - 1, _) for _ in range(M)] + [(_, 0) for _ in range(1, N - 1)] + [(_, M - 1) for _ in range(1, N - 1)]
while q:
    nq = []
    for x, y in q:
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 1 <= nx < N - 1 and 1 <= ny < M - 1 and p[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                nq.append((nx, ny))
    q = nq
cheese = []
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if p[i][j] == 1:
            cheese.append((i, j))
        elif visited[i][j] == 0:
            p[i][j] = 2

time = 0
while cheese:
    nc = []
    candidates = []
    for x, y in cheese:
        air = 0
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if p[nx][ny] == 0:
                air += 1
        if air >= 2:
            candidates.append((x, y))
        else:
            nc.append((x, y))
    for x, y in candidates:
        p[x][y] = 0
    while candidates:
        ncd = []
        for x, y in candidates:
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if p[nx][ny] == 2:
                    p[nx][ny] = 0
                    ncd.append((nx, ny))
        candidates = ncd
    time += 1
    cheese = nc

print(time)


# TC
#
# 8 9
# 0 0 0 0 0 0 0 0 0
# 0 0 0 1 1 0 0 0 0
# 0 0 0 1 1 0 1 1 0
# 0 0 1 1 1 1 1 1 0
# 0 0 1 1 1 1 1 0 0
# 0 0 1 1 0 1 1 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
#
# 4
