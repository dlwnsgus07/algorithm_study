import sys
import copy
from collections import deque

input = sys.stdin.readline

n, m, time = map(int, input().split())
arr = []
arr2 = []
visited = [[False] * m for i in range(n)]
visited2 = copy.deepcopy(visited)
for _ in range(n):
    matrix = list(map(int, input().split()))
    arr.append(matrix)
arr2 = copy.deepcopy(arr)


def BFS(x, y):
    q = deque()
    q.append((x, y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        px, py = q.popleft()
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if arr[nx][ny] == 0:
                if not visited[nx][ny]:
                    arr[nx][ny] = arr[px][py] + 1
                    visited[nx][ny] = True
                    q.append((nx, ny))


def MAGIC(x, y):
    q = deque()
    q.append((x, y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    m_dx, m_dy = 0, 0
    dist = 0
    flag = False
    while q:
        px, py = q.popleft()
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if arr2[nx][ny] == 2 and not visited2[nx][ny]:
                m_dx = nx
                m_dy = ny
                flag = True
                arr2[m_dx][m_dy] = arr2[px][py] + 1
                q.clear()
                break
            if arr2[nx][ny] != 1:
                if not visited2[nx][ny]:
                    q.append((nx, ny))
                    arr2[nx][ny] = arr2[px][py] + 1
                    visited2[nx][ny] = True
    if flag:
        short = arr2[m_dx][m_dy] + (n - 1) - m_dy + (m - 1) - m_dx
        return short
    return 0


BFS(0, 0)
magic_distance = MAGIC(0, 0)

basic_distance = arr[n - 1][m - 1]
answer = -1

if magic_distance == 0 and basic_distance != 0:
    answer = basic_distance
elif magic_distance != 0 and basic_distance == 0:
    answer = magic_distance
elif magic_distance != 0 and basic_distance != 0:
    answer = min(basic_distance, magic_distance)
else:
    answer = -1

if answer > time or answer == -1:
    print("Fail")
else:
    print(answer)
