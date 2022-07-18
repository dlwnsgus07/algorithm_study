a = input()
coordinate = list()
x_coordinate = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]
count = 0

for i in a:
    coordinate.append(i)
for i in range(len(x_coordinate)):
    if coordinate[0] == x_coordinate[i]:
        x = i + 1
y = int(coordinate[1])

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    count = count + 1

print(count)