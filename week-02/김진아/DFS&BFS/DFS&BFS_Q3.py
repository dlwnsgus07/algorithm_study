# PART 03 15번 특정 거리의 도시 찾기
# n, m, k, x = map(int, input().split())
# graph = [[] * (m + 1) for _ in range(m + 1)]
#
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# print(graph)
#
# def visit(G):
#
#     result = 0
#     if result == k:
#         print('찾음!')
#
# visit(x)

from collections import deque

# PART 03 15번 특정 거리의 도시 찾기
n, m, k, x = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(m)]

graph = [[] * (m + 1) for _ in range(m + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])

while q:
    cur = q.popleft()

    for i in graph[cur]:
        if distance[i] == -1:
            distance[i] = distance[cur] + 1
            q.append(i)

check = False

for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)

