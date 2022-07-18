def rotation(direction):
    return (3 + direction) % 4


n, m = map(int, input().split())
count = 0
flag = True
rotation_count = 0
# 0 : 북쪽, 1 : 동쪽, 2: 남쪽, 3: 서쪽
x, y, direction = map(int, input().split())
matrix = list()
# 0 : 육지, 1: 바다
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
while flag:
    direction = rotation(direction)
    nx = x + dx[direction]
    ny = x + dy[direction]
    if rotation_count == 4:
        # 뒤로 한칸 가는거 + 범위 조정까지
        flag = False
    elif nx >= n or nx < 0 or ny >= m or ny < 0:
        rotation_count = rotation_count + 1
        continue
    else:
        if matrix[nx][ny] == 0:
            matrix[nx][ny] = 1
            count = count + 1
            x = nx
            y = ny
        else:
            rotation_count = rotation_count + 1
print(count)