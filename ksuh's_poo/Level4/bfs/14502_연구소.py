import sys

si = sys.stdin.readline

N, M = map(int, si().split())
lab = [list(map(int, si().split())) for _ in range(N)]
p, v = [], []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            v.append((i, j))
        elif lab[i][j] == 0:
            p.append((i, j))

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = 0
L = len(p)
for i in range(L - 2):
    for j in range(i + 1, L - 1):
        for k in range(j + 1, L):
            c = [lab[i][:] for i in range(N)]
            c[p[i][0]][p[i][1]] = 2
            c[p[j][0]][p[j][1]] = 2
            c[p[k][0]][p[k][1]] = 2
            q = [i for i in v]
            while q:
                x, y = q.pop()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M and c[nx][ny] == 0:
                        c[nx][ny] = 2
                        q.append((nx, ny))
            cnt = 0
            for x in range(N):
                for y in range(M):
                    if c[x][y] == 0:
                        cnt += 1
            if cnt > ans:
                ans = cnt

print(ans)
# TC
# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0
#
# 27
#
# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2
#
# 9
#
# 8 8
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
#
# 3