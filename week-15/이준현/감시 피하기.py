import sys

flag = False


def bt(cnt):
    global flag

    if cnt == 3:
        if bfs():
            flag = True
            return
    else:
        for x in range(n):
            for y in range(n):
                if matrix[x][y] == "X":
                    matrix[x][y] = "O"
                    bt(cnt + 1)
                    matrix[x][y] = "X"


def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for t in teacher:
        for k in range(4):
            nx, ny = t
            while 0 <= nx < n and 0 <= ny < n:
                if matrix[nx][ny] == "O":
                    break
                if matrix[nx][ny] == "S":
                    return False

                nx += dx[k]
                ny += dy[k]
    return True


n = int(sys.stdin.readline())

matrix = []
teacher = []
for i in range(n):
    matrix.append(list(map(str, sys.stdin.readline().split())))
    for j in range(n):
        if matrix[i][j] == "T":
            teacher.append([i, j])
bt(0)
if flag:
    print("YES")
else:
    print("NO")
