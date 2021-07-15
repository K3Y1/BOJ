import sys
from collections import deque
from array import *

read = sys.stdin.readline
table ={}
n = int(read())
m = int(read())
for i in range(n):
    table[i+1] = set()
for i in range(m):
    a, b = list(map(int, read().split()))
    table[a].add(b)
    table[b].add(a)
check = [False for _ in range(n)]


def bfs(num):
    queue = deque()
    count = 0
    queue.append(num)
    check[num-1] = True
    while queue:
        x = queue.popleft()
        for i in table[x]:
            if check[i-1] == False:
                count+=1
                check[i-1] = True
                queue.append(i)
    return count

print(bfs(1))