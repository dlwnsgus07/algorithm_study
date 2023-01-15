from collections import deque

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
# 상, 하, 좌, 우, 왼쪽 대각선 위, 오른쪽 대각선 위, 왼쪽 대각선 아래, 오른족 대각선 아래
dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [1, -1, 0, 0, 1, 1, -1, -1]

max_value = 0
q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))


def BFS():
    global max_value
    while q:
        x, y, = q.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if arr[nx][ny] == 0:  # 상어가 아닐떄
                q.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1
                max_value = max(max_value, arr[nx][ny])


BFS()
print(max_value - 1)
