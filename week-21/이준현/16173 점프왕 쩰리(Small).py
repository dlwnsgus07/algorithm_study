from collections import deque

n = int(input())
arr = []
q = deque()
for _ in range(n):
    arr.append(list(map(int, input().split())))
q.append((0, 0))
flag = False


def BFS(x, y):
    global flag
    while q:
        a, b = q.popleft()
        if arr[a][b] == 0:
            continue
        dx = [arr[a][b], 0]
        dy = [0, arr[a][b]]
        for i in range(2):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if arr[nx][ny] == -1:
                flag = True
                break
            q.append((nx, ny))


BFS(0, 0)
if flag:
    print("HaruHaru")
else:
    print("Hing")
