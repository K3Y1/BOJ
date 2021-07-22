# <GOLD 5> 평범한 베낭 

import sys 

number , beg_maximum_weight = map(int,sys.stdin.readline().split())

weight =[0]
value = [0]

for i in range(number):
    w , v = map(int,sys.stdin.readline().split())
    weight.append(w)
    value.append(v)

DT = [[0]*(beg_maximum_weight+1) for _ in range(number+1)]

for i in range(1,number+1):
    for j in range(1,beg_maximum_weight+1):
        if(j<weight[i]):
            DT[i][j] = DT[i-1][j]
        else:
            DT[i][j] = max(DT[i-1][j-weight[i]]+value[i] , DT[i-1][j])



print(DT[number][beg_maximum_weight])