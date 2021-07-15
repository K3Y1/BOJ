import sys

read = sys.stdin.readline
INF = int(1e9)
n, m = map(int,read().split())
edges = []
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int,read().split())
    edges.append((a,b,c))
def b_f():
    distance[1] = 0
    for i in range(n):
        for j in range(m):
            x = edges[j][0]
            y = edges[j][1]
            z = edges[j][2]
            if distance[x] != INF and distance[y] > distance[x]+z:
                # print(distance)
                # print(j)
                distance[y] = distance[x]+z
                if i == n - 1:
                    return True
    return False

result = b_f()
if result:
    print("-1")
else:
    for i in range(2,n+1):
        if distance[i] == INF:
            print("-1")
        else:
            print(distance[i])