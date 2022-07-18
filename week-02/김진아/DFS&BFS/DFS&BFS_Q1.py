# 실전 문제 3 음료수 얼려 먹기
N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]


# x, y로 잡고 했더니 좌표 x, y와 반대로 돌아가다보니 헷갈려서 애먹음;;

def dfs(x, y):
    # 인덱스 확인
    if x < 0 or x > N - 1 or y < 0 or y > M - 1:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True

    return False

result = 0

for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)
