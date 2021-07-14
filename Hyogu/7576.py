import sys
from collections import deque
#i와 j, m과 n, 가로와 세로에 주의하자
# read = sys.stdin.readline()
graph=[]
n,m = map(int, input().split())
for _ in range(m):
    graph.append(list(map(int,input().split())))
    # print(graph)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

queue_1 = deque()
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            queue_1.append((i,j))
            # print((i,j))

def bfs():
    while queue_1:
        y,x = queue_1.popleft()
        # print((x,y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue_1.append((ny,nx))

bfs()
no = False
maximum = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            no=True
            break
        else:
            maximum = max(graph[i][j],maximum)
    if no:
        break

if no:
    print(-1)
else:
    print(maximum-1)