import sys
from collections import deque
from sys import flags, stdin

Input = sys.stdin.readline
graph=[]
n,m = map(int, input().split())
# print(n)
# print(m)
for _ in range(n):
    x = list(map(int,input()))
    graph.append(x)
#이동할 네 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

#BFS구현
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))
    #가장 오른쪽 아래까지 최단경로 반환
    return graph[n-1][m-1]

print(bfs(0,0))

