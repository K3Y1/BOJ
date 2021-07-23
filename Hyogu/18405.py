import sys
from collections import deque
read = sys.stdin.readline
graph = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(s,array,a,b):
    count = 0

    array = sorted(array,key = lambda x : x[2])
    array = deque(array)

    while array:
        x,y,z,count = array.popleft()
        if count == s:
            break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=nx<n and 0<=ny<n and graph[ny][nx] ==0:
                graph[ny][nx] = z
                array.append(( nx,ny,z,count+1))
    print(graph[a-1][b-1])


array= []
n,k = map(int,read().split())
graph = [list(map(int,read().split())) for _ in range(n)]
s, x, y = map(int, read().split())
for i in range(n):
    for j in range(n):
        if graph[j][i] > 0:
            array.append((i,j,graph[j][i],0))
bfs(s,array,x,y)
