# <Silver 4> 주몽

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

material = list(map(int,sys.stdin.readline().split()))

material = sorted(material, reverse=True)

start = 0
end = len(material)-1

#print(material)
count = 0
while(start<end):
#    print(material[start] + material[end],start,end)
    if(material[start] + material[end] == m):
        count = count+1
        start = start+1
        end = end-1
    elif(material[start] + material[end] < m):
        end=end-1
    else:
        start=start+1

print(count) 
