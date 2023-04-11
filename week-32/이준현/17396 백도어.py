import sys
import heapq

input = sys.stdin.readline
INF = int(1e10)
n, m = map(int, input().split())
visited = [True] * n
arr = list(map(int, input().split()))
dist = [INF] * n
graph = [[] for _ in range(n)]
for i in range(n - 1):
    if arr[i] == 1:
        visited[i] = False

for i in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))
q = []
if visited[0]:
    heapq.heappush(q, (0, 0))
    dist[0] = 0
while q:
    v, d = heapq.heappop(q)
    if dist[v] < d:
        continue
    for i, j in graph[v]:
        cost = d + j
        if cost < dist[i] and visited[i]:
            dist[i] = cost
            heapq.heappush(q, (i, cost))

if dist[-1] == INF:
    print(-1)
else:
    print(dist[-1])
