mylist = []
for i in range(9):
    mylist.append(int(input()))
#print(mylist)
maximum = max(mylist)
print(maximum)
result = 0
for i in range(9):
    if mylist[i]==maximum:
        result = i+1
        break
print(result)