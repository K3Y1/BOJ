# <Silver 1> 단지번호 붙이기

import sys

count = 0

def DFS(start_x , start_y , building_map, n):

    global count 
    count = count +1
#    print(start_x,start_y,count)
    building_map[start_x][start_y] = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0 ,0]

    for i in range(4):
        nx = start_x+dx[i]
        ny = start_y+dy[i]
        if(nx>=0 and ny>= 0 and nx < n and ny< n):
            if(building_map[nx][ny]!=0):
                DFS(nx,ny,building_map,n)
        
    


n = int(sys.stdin.readline())

building_map = [[0]*n for _ in range(n)]

for i in range(n):
    line = sys.stdin.readline().strip()
    for index, j in enumerate(line):
        building_map[i][index] = int(j)

building_list = []

for i in range(n):
    for j in range(n):
        if(building_map[i][j]!=0):
            count = 0
            DFS(i,j,building_map,n)
            building_list.append(count)

building_list.sort()

print(len(building_list))
for i in building_list:
    print(i)