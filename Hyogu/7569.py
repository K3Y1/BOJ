import sys
from collections import deque

read = sys.stdin.readline
graph = []
n, m, l = map(int,read().split())
graph = [[list(map(int,read().split())) for _ in range(m)] for _ in range(l)]

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

queue = deque()
for i in range(l):
    for j in range(m):
        for k in range(n):
            if graph[i][j][k] == 1:
                queue.append((i,j,k))
def bfs():
    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<l and 0<=ny<m and 0<=nz<n and graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = graph[x][y][z] + 1
                queue.append((nx,ny,nz))

bfs()
no = False
final = 0
for i in range(l):
    for j in range(m):
        for k in range(n):
            if graph[i][j][k] == 0:
                no = True
            else:
                final = max(final, graph[i][j][k])

if no:
    print("-1")
else:
    print(final-1)


