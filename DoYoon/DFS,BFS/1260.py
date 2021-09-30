from collections import deque

v, e, start = map(int, input().split())
graph = [[] for _ in range(v+1)] #adjacency list
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False] * (v+1)

dfs(graph, start, visited)
print("")

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
visited = [False] * (v+1)

bfs(graph, start, visited)