import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []

for i in range(m):
    arr.append(list(map(int, input().split())))

q = deque()

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            q.append((j, i))


def BFS():
    #상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[ny][nx] != 0 or arr[ny][nx] == -1:
                continue
            arr[ny][nx] = arr[y][x] + 1
            q.append((nx, ny))
    for a in range(m):
        for b in range(n):
            if arr[a][b] == 0:
                print(-1)
                return
    print(max(map(max, arr)) - 1)


BFS()
