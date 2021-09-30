from collections import deque

def near(a, b):
    if a[0]==b[0] and a[1] - b[1] == 1:
        return True
    if a[0]==b[0] and a[1] - b[1] == -1:
        return True
    if a[1]==b[1] and a[0] - b[0] == 1:
        return True
    if a[1]==b[1] and a[0] - b[0] == -1:
        return True
    else:
        return False

def bfs(graph):
    count = 0
    queue = deque()
    while len(graph)>0:
        queue.append(graph[0])
        del graph[0]
        count += 1
        while queue:
            v = queue.popleft()
            #print("v",v)
            temp = graph[:]
            for i in temp:
                #print("temp", temp)
                if near(v, i)==True:
                    #print("i", i)
                    queue.append(i)
                    graph.remove(i)
    return count

num_t = int(input())
for i in range(num_t):
    m, n, k = map(int,input().split())
    graph = []
    for j in range(k):
        temp = list(map(int, input().split()))
        graph.append(temp)
    print(bfs(graph))