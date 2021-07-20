# <GOLD 1> 멀티탭 스케줄링

import sys

n , k = map(int,sys.stdin.readline().split())

array = list(map(int,sys.stdin.readline().split()))

plug = []
count = -1

for i in array:
    if(len(plug)==n):
        break
    count = count+1
    if(i not in plug):
        plug.append(i)

count=count+1
cnt = 0

while(count<k):
    if(array[count] in plug):
        count=count+1
        continue
    
    remove_prioty_list = [0]*n
    for index,i in enumerate(plug):
        for jindex , j in enumerate(array[count:]):
            if(j==i):
                remove_prioty_list[index] = jindex
                break
    
#    print(remove_prioty_list)
    maxnum = 0
    max_index = 0
    for index,i in enumerate(remove_prioty_list):
        if(i==0):
            max_index = index
            break
        else:
            if(maxnum<i):
                maxnum=i
                max_index=index

    
    plug[max_index] = array[count]
    cnt=cnt+1


    count = count+1

print(cnt)
        