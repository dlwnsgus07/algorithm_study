count = 0

def dfs(graph, v, visited):
    global count
    visited[v] = True
    count += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    return count


computer = int(input())
n = int(input())
graph = [[] for _ in range(computer + 1)]
for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (computer + 1)

count = dfs(graph, 1, visited)
print(count - 1)
