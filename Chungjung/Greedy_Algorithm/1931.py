# <Silver 2> 회의실 배정 

import sys 

n = int(sys.stdin.readline())


meeting = []
for i in range(n):
    s,e = map(int,sys.stdin.readline().split())
    meeting.append([s,e])

meeting = sorted(meeting, key = lambda x : (x[1] , x[0]))

finish_time = 0

cnt = 0
for i in meeting:
    if(i[0]>finish_time):
        cnt=cnt+1
        finish_time = i[1]

print(cnt)