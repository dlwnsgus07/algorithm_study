import sys

# input = sys.stdin.readline
INF = 1e9

n = int(input())

graph = [[INF] * (n + 1) for i in range(n + 1)]
start, end = 0, 0
candidate = []
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
while start != -1:
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
min_value = 0
max_arr = []
for i in range(1, n + 1):
    max_arr.append(max(graph[i][1:n + 1]))

min_value = int(min(max_arr))

for i in range(1, n + 1):
    if max(graph[i][1:n + 1]) == min_value:
        candidate.append(i)

print(min_value, end=' ')
print(len(candidate))
for i in candidate:
    print(i, end=' ')
