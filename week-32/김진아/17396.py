# 17396 백도어

import heapq
import sys
input = sys.stdin.readline

INF = sys.maxsize
n, m = map(int, input().split())
arr = list(map(int, input().split()))
graph = [[] for _ in range(n)]
distance = [INF] * n

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def solution(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        
        for (v, w) in graph[now]:
            cost = dist + w
            if cost < distance[v]  and arr[now] == 0:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

solution(0)

if distance[n-1] == INF:
    print(-1)
else:
    print(distance[n - 1])