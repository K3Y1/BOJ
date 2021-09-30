from collections import deque

def bfs(graph, start, visited):
    count = 0
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        v = queue.popleft()
        count +=1
        #print(v, end=" ")
        for i in graph[v]:
            if visited[i]==False:
                queue.append(i)
                visited[i]=True
    return count-1

num_comptr = int(input())
num_conn = int(input())
graph = [[] for _ in range(num_comptr+1)]
for i in range(num_conn):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()
visited =[False]*(num_comptr+1)
print(bfs(graph, 1, visited))