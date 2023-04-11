import sys
from  collections import deque
input = sys.stdin.readline
n, m, k = map(int, input().split())

nutrient = [[5] * n for i in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
A = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
ans = 0


def spring_and_summer(x, y):
    death_tree = 0
    for i in range(len(trees[x][y])):
        tree = trees[x][y].popleft()
        if tree > nutrient[x][y]:
            death_tree += tree
        else:
            nutrient[x][y] -= tree
            trees[x][y].append(tree + 1)
    nutrient[x][y] += death_tree // 2


def fall_and_winter(x, y):
    for i in trees[x][y]:
        if i % 5 == 0:
            for j in range(8):
                nx = x + dx[j]
                ny = y + dy[j]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                trees[nx][ny].appendleft(1)
    nutrient[x][y] += A[x][y]


for i in range(m):
    x, y, age = map(int, input().split())
    trees[x - 1][y - 1].append(age)

for i in range(k):
    for a in range(0, n):
        for b in range(0, n):
            spring_and_summer(a, b)
    for a in range(0, n):
        for b in range(0, n):
            fall_and_winter(a, b)

for a in range(0, n):
    for b in range(0, n):
        ans += len(trees[a][b])

print(ans)
