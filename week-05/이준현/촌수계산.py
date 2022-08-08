from collections import deque
n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
count = 1
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)


def BFS(graph, v1, v2, visited):
    global count
    queue = deque([v1])
    visited[v1] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                if i == v2:
                    return count
                queue.append(i)
                visited[i] = True
        count += 1
    return -1

count = BFS(graph, p1, p2, visited)

print(count)
