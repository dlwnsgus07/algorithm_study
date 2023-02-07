import sys
input = sys.stdin.readline

n, m, block = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 1e9
stage = 0

for k in range(257):
    max_value = 0
    min_value = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= k:
                max_value += graph[i][j] - k
            else:
                min_value += k - graph[i][j]
    if max_value + block >= min_value:
        if (max_value * 2) + min_value <= ans:
            ans = (max_value * 2) + min_value
            stage = k
print(ans, stage)