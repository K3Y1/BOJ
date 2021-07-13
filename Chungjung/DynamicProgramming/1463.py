# <Silver 3> 1로 만들기

import sys 

n = int(sys.stdin.readline().rstrip())

dt = [0]*1000001

dt[1] = 0

for i in range(2,n+1):
    dt[i] = dt[i-1] + 1

    if(i%3==0):
        dt[i] = min(dt[i],dt[i//3]+1)
    if(i%2==0):
        dt[i] = min(dt[i],dt[i//2]+1)
        
print(dt[n])