# <SILVER 1> 경쟁적 전염 

import sys
import heapq
from copy import deepcopy

n , k = map(int,sys.stdin.readline().split())

vitro = []

for i in range(n):
    vitro_line = list(map(int,sys.stdin.readline().split()))
    vitro.append(vitro_line)

s, print_y, print_x = map(int,sys.stdin.readline().split())

print_y = print_y-1
print_x = print_x-1

virus_queue = []
for i in range(n):
    for j in range(n):
        if(vitro[i][j]!=0):
            heapq.heappush(virus_queue,[vitro[i][j],i,j])

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(s):
    
    virus_queue_copy = []
    while(virus_queue):
        virus_location = heapq.heappop(virus_queue)
        virus_queue_copy.append(virus_location)
    virus_queue = []
    # print("virus queue:" ,end=' ')
    # print(virus_queue_copy)

    for j in virus_queue_copy:
        y = j[1]
        x = j[2]
        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]

            if(nx >=0 and ny>=0 and nx<n and ny<n):
                if(vitro[ny][nx]==0):
                    vitro[ny][nx] = j[0]
                    heapq.heappush(virus_queue,[vitro[ny][nx],ny,nx])
    # for l in vitro:
    #     print(l)

print(vitro[print_y][print_x])   
