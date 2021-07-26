# # <GOLD 2> 공항

# import sys

# n = int(sys.stdin.readline().strip())
# m = int(sys.stdin.readline().strip())

# airplane_list = []
# for i in range(m):
#     airplane = int(sys.stdin.readline().strip())
#     airplane_list.append(airplane)

# count = 0

# Gate_list = [[0, 0] for _ in range(n+2)]
# # print(Gate_list)

# for i in airplane_list:
#     ap = int(i)

#     if(Gate_list[ap][0] == 1):
#         break
#     elif(Gate_list[ap][0] == 0):  # 현재 위치에 아무것도 없을경우
#         change = list([ap, ap])
#         Gate_list[ap] = change
#         # print("a case")
#     elif(Gate_list[ap][0] != 0):  # 현재 위치에 1이 아닌 숫자가 들어있을 경우
#         front = Gate_list[ap][0]-1
#         back = Gate_list[ap][1]
#         change = list([[front, back]])*(back-front+1)
#         Gate_list[front: back+1] = change
#         ap = front
#         # print("b case")

#     if(Gate_list[ap-1][0] != 0):
#         front = Gate_list[ap-1][0]
#         back = Gate_list[ap][1]
#         change = list([[front, back]])*(back-front+1)
#         Gate_list[front:back+1] = change

#     if(Gate_list[ap+1][1] != 0):
#         front = Gate_list[ap][0]
#         back = Gate_list[ap+1][1]
#         change = list([[front, back]])*(back-front+1)
#         Gate_list[front:back+1] = change

#     count = count+1
# #     print(Gate_list)

# # print(Gate_list)
# print(count)

# ---------------- 시간 초과로 Union Find 도입 결정 -----------------------

import sys
g = int(sys.stdin.readline())
p = int(sys.stdin.readline())
plane = []
for _ in range(p):
    plane.append(int(sys.stdin.readline()))


def parent_find(x):
    if x == parent[x]:
        return x
    p = parent_find(parent[x])
    parent[x] = p
    return parent[x]


def union(x, y):
    x = parent_find(x)
    y = parent_find(y)
    parent[x] = y


# parent[0] = 0 까지 만들어준다. parent[x] = 0까지 만들어지는 게 핵심
parent = {i: i for i in range(g+1)}
cnt = 0
for i in plane:
    x = parent_find(i)
    if x == 0:
        break
    union(x, x-1)
    cnt += 1
print(cnt)
