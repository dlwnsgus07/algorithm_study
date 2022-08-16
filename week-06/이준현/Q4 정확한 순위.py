n, m = map(int, input().split())

graph = [[False] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = True

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = graph[a][b] or (graph[a][k] and graph[k][b])

count = 0

for a in range(1, n + 1):
    check_flag = True
    for b in range(1, n + 1):
        if not graph[a][b] and not graph[b][a]:
            check_flag = False
    if check_flag:
        count += 1

print(count)

