import sys
from collections import deque

input = sys.stdin.readline
INF = 1e9

n, m = map(int, input().split())
distance = [INF] * (n + 1)
graph = [[] for i in range(n + 1)]
for i in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

q = deque()
q.reverse();
q.append((1, 0))
q.ap
distance[1] = 0
while q:
    v, dist = q.popleft()
    if distance[v] < dist:
        continue
    for i in graph[v]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            q.append((i[0], cost))

print(distance[n])
