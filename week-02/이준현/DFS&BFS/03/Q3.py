from collections import deque
city, route, distance, number = map(int, input().split())
graph = [[] for _ in range(city + 1)]
result = []

distances = [-1]*(city+1)
distances[number] = 0

for _ in range(route):
    p, q = map(int, input().split())
    graph[p].append(q)


q = deque([number])

while q:
    now = q.popleft()
    for next in graph[now]:
        if distances[next] == -1:
            distances[next] = distances[now] + 1
            q.append(next)

check = False
for i in range(1, city+1):
    if distances[i] == distance:
        print(i)
        check = True
if check == False:
    print(-1)