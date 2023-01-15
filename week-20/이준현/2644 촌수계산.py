from collections import deque

n = int(input())
dp = [0] * 100
start, end = map(int, input().split())
m = int(input())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def BFS(start):
    q = deque()
    distance = 0
    q.append(start)
    dp[start] = distance
    visited[start] = True
    while q:
        vertex = q.popleft()
        distance += 1
        for i in graph[vertex]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                dp[i] = dp[vertex] + 1

BFS(start)
if dp[end] == 0:
    print(-1)
else:
    print(dp[end])
