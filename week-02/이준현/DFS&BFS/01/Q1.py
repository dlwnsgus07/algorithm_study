#이건 중간에 답지 참고
n, m = map(int, input().split())
count = 0

graph = list()
for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y, counts):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return counts
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y, counts)
        dfs(x + 1, y, counts)
        dfs(x, y - 1, counts)
        dfs(x, y + 1, counts)
        return counts + 1
    return counts


for i in range(n):
    for j in range(m):
        count = dfs(i, j, count)
print(count)