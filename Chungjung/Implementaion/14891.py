# <GOLD 5> 톱니바퀴

import sys

Gear_list = []

for i in range(4):
    Gear = list(map(int,sys.stdin.readline().strip()))
    Gear_list.append(Gear)


n = int(sys.stdin.readline().strip())
rotate_list = []

for i in range(n):
    k , r = map(int,sys.stdin.readline().split())
    k=k-1
    rotate_list.append([k,r])


# print(Gear_list)


def can_rotate(n1,n2):  # n1이 왼쪽 n2가 오른쪽에 있는 경우
    g1 = Gear_list[n1][2]
    g2 = Gear_list[n2][6]

    if(g1 == g2):
        return False #같으면 안돌아도 됨
    else:
        return True

def rotate(gear_num,direction):
    if(direction == -1):
        Gear_list[gear_num].append(Gear_list[gear_num][0])
        del Gear_list[gear_num][0]
    if(direction == 1):
        Gear_list[gear_num].insert(0,Gear_list[gear_num][-1])
        del Gear_list[gear_num][-1]

def DFS(gear,rotate_direction):
    visit_gear.append(gear)
    dx = [-1,1]
    for i in range(2):
        next_gear = gear+dx[i]
        if(next_gear>=0 and next_gear<4):
            if(i == 0 and can_rotate(next_gear,gear) and next_gear not in visit_gear):
                DFS(next_gear,rotate_direction*(-1))
            if(i == 1 and can_rotate(gear,next_gear)and next_gear not in visit_gear):
                DFS(next_gear,rotate_direction*(-1))

    rotate(gear,rotate_direction)

for i in rotate_list:
    gear = i[0]
    rotate_direction = i[1]
    visit_gear = []
    DFS(gear,rotate_direction)
#    print(Gear_list)

sum_gear = 0
for index,i in enumerate(Gear_list):
    if(index == 0 and i[0]==1):
        sum_gear = sum_gear + 1
    if(index == 1 and i[0]==1):
        sum_gear = sum_gear + 2
    if(index == 2 and i[0]==1):
        sum_gear = sum_gear + 4
    if(index == 3 and i[0]==1):
        sum_gear = sum_gear + 8

print(sum_gear)