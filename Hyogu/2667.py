import sys
from sys import flags, stdin

Input = sys.stdin.readline
graph=[]
k=int(Input())
for _ in range(k):
    x = list(map(int,input()))
    graph.append(x)
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(a,b,graph):
    graph[a][b] = 0
    cnt = 1
    stack = [(a,b)]
    while stack:
        x, y =stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<k and 0<=ny<k and graph[nx][ny]:
                cnt += 1
                graph[nx][ny] = 0
                stack.append((nx,ny))
    return cnt

array =[]
for i in range(k):
    for j in range(k):
        if graph[i][j] == 1:
            array.append(dfs(i,j, graph))


print(len(array))
for i in sorted(array):
    print(i)