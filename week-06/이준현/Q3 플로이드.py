INF = int(1e9)

city = int(input())
bus = int(input())

graph = [[INF] * (city + 1) for _ in range(city + 1)]

for a in range(1, city + 1):
    for b in range(1, city + 1):
        if a == b:
            graph[a][b] = 0


for _ in range(bus):
    a, b, c = map(int, input().split())
    if graph[a][b] == INF:
        graph[a][b] = c
    else:
        if c < graph[a][b]:
            graph[a][b] = c


for k in range(1, city + 1):
    for a in range(1, city + 1):
        for b in range(1, city + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, city + 1):
    for b in range(1, city + 1):
        if graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
