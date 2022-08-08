from collections import deque


def dfs(graph1, v1, visited1):
    visited[v1] = True
    print(v1, end=' ')
    for i in graph1[v1]:
        if not visited1[i]:
            dfs(graph1, i, visited1)


def bfs(graph2, v2, visited2):
    queue = deque([v2])
    visited2[v2] = True
    while queue:
        v2 = queue.popleft()
        print(v2, end=' ')
        for i in graph2[v2]:
            if not visited2[i]:
                queue.append(i)
                visited2[i] = True


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

dfs(graph, v, visited)
visited = [False] * (n+1)
print()
bfs(graph, v, visited)