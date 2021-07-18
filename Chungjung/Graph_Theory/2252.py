#<GOLD 2> 줄 세우기 

# ---------------------------------------------------------------------------------------------------------------------- 
# pypy version

# import sys
# from collections import deque

# n , m = map(int, sys.stdin.readline().split())

# compare_student_list = []

# for i in range(m):
#     compare_student = list(map(int,sys.stdin.readline().split()))
#     compare_student_list.append(compare_student)

# topological_end = [[0] for _ in range(n+1)]
# topological_start = [[0] for _ in range(n+1)]

# for i in compare_student_list:
#     a = i[0]   #a가 b보다 앞에 와야함 즉 a->b
#     b = i[1]

#     topological_end[b][0] = topological_end[b][0]+1

#     topological_start[a][0] = topological_start[a][0]+1
#     topological_start[a].append(b)

# deq = deque()

# max_value = int(sys.maxsize)

# for i in range(1,n+1):
#     if(topological_end[i][0]==0):
#         deq.append(i)
#         topological_end[i][0] = max_value  #이미 연결을 해재한 수는 maxsize로 변경해 버린다.


# while(deq):
#     number = deq.popleft()
#     print(number, end=" ")

#     for index , j in enumerate(topological_start[number]):
#         if(index!=0):
#             topological_end[j][0] = topological_end[j][0]-1

#     for i in range(1,n+1):
#         if(topological_end[i][0]==0):
#             deq.append(i)
#             topological_end[i][0] = max_value
    


# ---------------------------------------------------------------------------------------------------------------------- 
# python 3 version

import sys
from collections import deque

n , m = map(int, sys.stdin.readline().split())

compare_student_list = []

for i in range(m):
    compare_student = list(map(int,sys.stdin.readline().split()))
    compare_student_list.append(compare_student)

topological_end = [0]*(n+1)
topological_start = [[0] for _ in range(n+1)]

for i in compare_student_list:
    a = i[0]   #a가 b보다 앞에 와야함 즉 a->b
    b = i[1]

    topological_end[b] = topological_end[b]+1

    topological_start[a][0] = topological_start[a][0]+1
    topological_start[a].append(b)

deq = deque()

max_value = int(sys.maxsize)



for i in range(1,n+1):
    if(topological_end[i]==0):
        deq.append(i)
        topological_end[i] = max_value  #이미 연결을 해재한 수는 maxsize로 변경해 버린다.


temp_list = []

while(deq):
    number = deq.popleft()
    print(number, end=" ")

    for index , j in enumerate(topological_start[number]):
        if(index!=0):
            topological_end[j] = topological_end[j]-1
            temp_list.append(j)

    for i in temp_list:
        if(topological_end[i]==0):
            deq.append(i)
            topological_end[i] = max_value
    
    temp_list= []