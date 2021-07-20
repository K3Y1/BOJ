#Kruskal Algorithm 관련 문제
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i
sumDist = 0
for _ in range(e):
    a, b, dist = map(int, input().split())
    sumDist += dist
    edges.append((dist, a, b))
trash1, trash2 = map(int, input().split())

edges.sort()

for edge in edges:
    dist, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += dist
print(sumDist - result)