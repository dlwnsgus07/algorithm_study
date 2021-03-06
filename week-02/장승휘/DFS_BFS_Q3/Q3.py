from collections import deque

n, m, k, x = map(int,input().split())
graph = [[] for _ in range(n + 1)] # 맨 앞 인덱스 0은 쓰이지 않기 때문에..

for i in range (m):
	a, b = map(int,input().split())
	graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

queue = deque([x])

while queue :
	now = queue.popleft()
	for next in graph[now]:
		if distance[next] == -1:
			distance[next] = distance[now] + 1
			queue.append(next)

check = False

for i in range(1, n + 1):
	if distance[i] == k:
		print(i)
		check = True
		
if check == False:
	print(-1)
