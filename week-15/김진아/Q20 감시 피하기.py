N = int(input())
graph = []
teacher = 0

for _ in range(N):
    data = list(input().strip().split(' '))
    teacher += data.count('T')
    graph.append(data)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        while 0 <= nx < N and 0 <= ny < N and graph[nx][ny] != '0':
            if graph[nx][ny] == 'S':
                return True
            else:
                nx += dx[i]
                ny += dy[i]
        return False

def solution(count):
    global answer
    if count == 3:
        cnt = 0
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 'T':
                    if not check(i, j):
                        cnt += 1
        if cnt == teacher:
            answer = True
        return
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                count += 1
                solution(count)
                graph[i][j] = 'X'
                count -= 1

answer = False
solution(0)

if answer:
    print('YES')
else:
    print('NO')