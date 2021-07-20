# <GOLD 5> 연구소

import sys
from copy import deepcopy
from collections import deque
from itertools import combinations

n , m = map(int,sys.stdin.readline().split())

lab_map = []

for i in range(n):
    lab_map_line = list(map(int,sys.stdin.readline().split()))
    lab_map.append(lab_map_line)

minimum_safe_area = 0
lab_empty_area = []
virus_location = deque()

def BFS(i,j,k):
    lab_map_copy[i[0]][i[1]] = 1
    lab_map_copy[j[0]][j[1]] = 1
    lab_map_copy[k[0]][k[1]] = 1

    global minimum_safe_area

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while(virus_location_copy):
        location = virus_location_copy.pop()
        location_x = location[1]
        location_y = location[0]

        for i in range(4):
            nx = location_x + dx[i]
            ny = location_y + dy[i]
            if(nx>=0 and ny >=0 and nx<m and ny<n):
                if(lab_map_copy[ny][nx]==0):
                    lab_map_copy[ny][nx]=2
                    virus_location_copy.append([ny,nx])
    
    cnt = 0
    for y in range(n):
        for x in range(m):
            if(lab_map_copy[y][x]==0):
                cnt = cnt+1
    
    if(cnt>minimum_safe_area):
        minimum_safe_area = cnt




for y in range(n):
    for x in range(m):
        if(lab_map[y][x]==0):
            lab_empty_area.append([y,x])
        if(lab_map[y][x]==2):
            virus_location.append([y,x])

zero_combi = combinations(lab_empty_area,3)

for combi in zero_combi:
    lab_map_copy = deepcopy(lab_map)
    virus_location_copy = deepcopy(virus_location)
    BFS(combi[0],combi[1],combi[2])
    

print(minimum_safe_area)