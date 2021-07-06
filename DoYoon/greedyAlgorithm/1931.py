X = []

from sys import stdin
N = int(stdin.readline())
i = 0
while i < N: #input N data
    x, y = list(map(int, stdin.readline().split()))
    X.append([x,y])
    #print(X)
    i += 1

def y(X) :
    return X[1]
X.sort(key=y)
#print(X)

temp = X[0][1]
i=0
count = 0
while X[i][0] == X[i][1]:
    count += 1
    if X[i][1] == X[i+1][1]:
        temp = X[i+1][0]
    i += 1

if X[0][0] != X[0][1]:
    count += 1

while i<N:
    if X[i][0] == X[i][1]:
        count += 1
    elif temp <= X[i][0]:
        count += 1
        temp = X[i][1]
    i += 1
    #print(i)
print(count)
