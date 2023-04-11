# 파이프 치우기
import sys
# from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dx = [0, 1, 1]
dy = [1, 0, 1]


def check_diagonal(x, y):
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or ny >= n or graph[nx][ny] == 1:
            return False
    return True


def DFS(x, y, direction):
    global ans
    if x == y == n - 1:
        ans += 1
        return
    if direction != 3:
        nx = x + dx[0]
        ny = y + dy[0]
        if not (nx >= n or ny >= n or graph[nx][ny] == 1):
            DFS(nx, ny, 2)
    if direction != 2:
        nx = x + dx[1]
        ny = y + dy[1]
        if not (nx >= n or ny >= n or graph[nx][ny] == 1):
            DFS(nx, ny, 3)
    if check_diagonal(x, y):
        nx = x + dx[2]
        ny = y + dy[2]
        DFS(nx, ny, 4)


# def BFS():
#     global ans
#     q = deque()
#     q.append((0, 1, 2))
#     # 2= 가로, 3 = 세로, 4 = 대각선
#     while q:
#         x, y, direction = q.popleft()
#         if x == y == n - 1:
#             ans += 1
#             continue
#         # 세로가 아니라면 (가로거나 대각선일떄)
#         if direction != 3:
#             nx = x + dx[0]
#             ny = y + dy[0]
#             if not (nx >= n or ny >= n or graph[nx][ny] == 1):
#                 q.append((nx, ny, 2))
#         # 가로가 아니라면(세로거나 대각선일때)
#         if direction != 2:
#             nx = x + dx[1]
#             ny = y + dy[1]
#             if not (nx >= n or ny >= n or graph[nx][ny] == 1):
#                 q.append((nx, ny, 3))
#
#         if check_diagonal(x, y):
#             nx = x + dx[2]
#             ny = y + dy[2]
#             q.append((nx, ny, 4))
#
#
# BFS()
if graph[n-1][n-1] == 1:
    print(0)
else:
    DFS(0, 1, 2)
    print(ans)
