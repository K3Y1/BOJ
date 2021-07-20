import heapq
import sys

INF = int(1e9)
read = sys.stdin.readline
n , m = map(int,read().split())
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, read().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1 , v2 = map(int,read().split())




# print(graph)
def dijstra(start):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance



st=dijstra(1)


vv1=dijstra(v1)


vv2=dijstra(v2)


overall = min(st[v1]+vv1[v2]+vv2[n],st[v2]+vv2[v1]+vv1[n])
if overall >= INF:
    print("-1")
else:
    print(overall)
