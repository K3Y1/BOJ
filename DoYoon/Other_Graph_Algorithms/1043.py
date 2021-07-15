#서로소 집합 알고리즘 관련 문제
import sys
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

cnt_people, cnt_party = map(int, input().split())
parent = [0] * (cnt_people+1)

for i in range(1, cnt_people+1):
    parent[i] = i

mylist = list(map(int, input().split()))

for i in range(1, mylist[0]):
    union_parent(parent, mylist[i], mylist[i+1])
if mylist[0] != 0:
    name_cant = min(mylist[1:])

partylist = []
for i in range(cnt_party):
    partylist.append(list(map(int, input().split())))
    for j in range(1, partylist[i][0]):
        union_parent(parent, partylist[i][j], partylist[i][j+1])
if mylist[0] == 0:
    print(cnt_party)
    sys.exit()
name_cant = parent[name_cant]
count_tell = 0
for i in range(cnt_party):
    for j in range(1, partylist[i][0]+1):
        if parent[partylist[i][j]] == name_cant:
            count_tell -= 1
            break
    count_tell += 1
#print(name_cant)
print(count_tell)
