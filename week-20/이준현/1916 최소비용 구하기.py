import sys
import heapq

INF = 1e9

input = sys.stdin.readline

n = int(input())
m = int(input())

visited = [False] * 1001
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))

start, end = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, vertex = heapq.heappop(q)
        if distance[vertex] < dist:
            continue
        for i in graph[vertex]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)
print(distance[end])