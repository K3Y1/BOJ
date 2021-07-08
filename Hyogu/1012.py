import sys
from collections import deque
from sys import flags, stdin

Input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] ==1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
    return True




ite = int(Input())
for i in range(ite):
    count = 0
    m,n,k = map(int, input().split())
    #m은 가로, n은 세로이다
    graph=[]
    graph = [[0]*m for _ in range(n)]
    #가로 m 세로 n인 list를 초기화 한다.
    for j in range(k):
        a,b =map(int, input().split())
        graph[b][a] = 1
        #왜 b,a인가? ->
    for j in range(n):
        for jj in range(m):
            if(graph[j][jj] == 1):
                bfs(j,jj)
                graph[j][jj] = 0
                count += 1
    print(count)



