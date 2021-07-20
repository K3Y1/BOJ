# <SILVER 2> 특정 거리의 도시 찾기

import sys
from collections import deque

n , m , k ,x = map(int,sys.stdin.readline().split())

street_list = [[0] for _ in range(n+1)] 

queue = deque()

for i in range(m):
    start , end = map(int,sys.stdin.readline().split())
    street_list[start][0] = street_list[start][0]+1
    street_list[start].append(end)

visit_city = []
queue.append(x)
visit_city.append(x)


k_th_city = []
for i in range(0,k):
    k_th_city = []
    while(queue):
        queue_city = queue.pop()
        k_th_city.append(queue_city)

    for j in k_th_city:
        for t in street_list[j][1:]:
            if(t not in visit_city):
                queue.append(t)
                visit_city.append(t)

answer = []
if not queue:
    print(-1)
else:
    while(queue):
        answer.append(queue.pop())
    answer = sorted(answer)
    for i in answer:
        print(i)