# <SILVER 1> 토마토(2차원)

import sys
from collections import deque

toamto_queue = deque()


# 입력부 
n,m = map(int,sys.stdin.readline().split())

tomato_map = []

for i in range(m):
    tomato = list(map(int,sys.stdin.readline().split()))
    tomato_map.append(tomato)

for y in range(0,m):
    for x in range(0,n):
        if(tomato_map[y][x]==1):
            toamto_queue.append([y,x,0])


last_day = 0
while(toamto_queue):
    location = toamto_queue.popleft()
    y_location = location[0]
    x_location = location[1]

    last_day = location[2]

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for i in range(0,4):
        day = location[2]
        nx = x_location+dx[i]
        ny = y_location+dy[i]
        if(nx>=0 and ny>=0 and nx<n and ny<m):
            if(tomato_map[ny][nx]==0):
                toamto_queue.append([ny,nx,day+1])
                tomato_map[ny][nx]=1

for y in range(0,m):
    for x in range(0,n):
        if(tomato_map[y][x]==0):
            print(-1)
            sys.exit(0)

print(last_day)