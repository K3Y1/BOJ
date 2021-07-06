N = int(input())
array = []
num = []
for i in range(N):
    array.append(list(map(int, input())))
counter = 0
def dfs(x, y):
    global counter
    if x<=-1 or x>=N or y<=-1 or y>=N:
        return False
    if array[x][y] == 1:
        array[x][y] = 0
        #print(x, y,"=",array[x][y])
        counter += 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x+1, y)
        return True
    return False
result = 0
for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            result += 1
            num.append(counter)
            counter = 0
print(result)
#print(num)
num.sort()
for i in range(len(num)):
    print(num[i])
