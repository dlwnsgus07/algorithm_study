# 5972 택배 배송

import heapq
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    q = []
    
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        
        for v, w in graph[now]:
            cost = dist + w
            
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))
        
dijkstra(1)

print(distance[n])