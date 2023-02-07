from queue import PriorityQueue
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
INF = 1e9
dist = [INF] * 100001
q = PriorityQueue()
q.put((0, n))
dist[n] = 0
while q:
    time, x = q.get()
    if x == m:
        break

    for i in (x - 1, x + 1):
        if 0 <= i <= 100000:
            cost = time + 1
            if dist[i] >= cost:
                dist[i] = cost
                q.put((cost, i))
    if 0 < x * 2 <= 100000:
        dist[x * 2] = dist[x]
        q.put((dist[x], x * 2))

print(dist[m])
