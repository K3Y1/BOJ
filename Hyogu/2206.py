import sys
from collections import deque

Input = sys.stdin.readline
graph=[]
n,m = map(int, input().split())
for _ in range(n):
    x = list(map(int,input()))
    graph.append(x)

dx = [0,0,1,-1]
dy = [1,-1,0,0]
visit = [[[-1]*2 for _ in range(m)] for _ in range(n)]
visit[0][0][0] = 1

def bfs_1():
    visit[0][0][0] = 1
    queue = deque()
    queue.append((0,0,0))
    while queue:
        x,y,z = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visit[nx][ny][z] == -1:
                    visit[nx][ny][z] = visit[x][y][z] + 1
                    queue.append((nx, ny,z))
                if graph[nx][ny] == 1 and visit[nx][ny][1] == -1 and z ==0:
                    visit[nx][ny][1] = visit[x][y][z] + 1
                    queue.append((nx,ny,1))

bfs_1()
ans1 = visit[n-1][m-1][0]
ans2 = visit[n-1][m-1][1]
if ans1 == -1 and ans2 == -1:
    print(-1)
elif ans1 != -1 and ans2 == -1:
    print(ans1)
elif ans1 == -1 and ans2 != -1:
    print(ans2)
else:
    print(min(ans1,ans2))
