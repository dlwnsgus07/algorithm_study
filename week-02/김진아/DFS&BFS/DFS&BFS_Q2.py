# 실전 문제 4 미로 탈출
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()


def road(x, y):
    q.append((x, y))

    while q:
        cur = q.popleft()

        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]

            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[cur[0]][cur[1]] + 1
                q.append((nx, ny))

    return graph[N - 1][M - 1]

    # # 인덱스 확인
    #
    # if x < 0 or x > N - 1 or y < 0 or y > M - 1:
    #     return False
    #
    # if graph[x][y] == 1:
    #     graph[x][y] = 3
    #
    #     ## 그래서...
    #
    #     return True
    #
    # return False


# 징챠 어렵다....


print(road(0, 0))
