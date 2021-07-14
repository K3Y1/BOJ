# <Siver 3> 나무 자르기

import sys

n,m = map(int,sys.stdin.readline().split())

wood_list = list(map(int,sys.stdin.readline().split()))

max_wood = max(wood_list)

start = 0
end = max_wood


while(start<=end):
    mid = (start+end)//2

    sum = 0
    for i in wood_list:
        if(i-mid>=0):
            sum = sum+(i-mid)

    if(sum >= m):
        start = mid+1
    else:
        end = mid-1


print(end)