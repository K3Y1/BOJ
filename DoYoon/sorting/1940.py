N = int(input())
M = int(input())
mylist = []
mylist=list(map(int,input().split()))
count = 0
mylist.sort()
#print(mylist)
i = 0
j = N-1

while j-i >= 1:
    if mylist[i]+mylist[j] == M:
        count += 1
        i += 1
        j -= 1
    elif mylist[i]+mylist[j]>M:
        j -= 1
    elif mylist[i]+mylist[j]<M:
        i += 1
    #print(i, j)

print(count)
