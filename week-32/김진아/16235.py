# 16235 나무 재테크

from collections import deque

def SS():
    for i in range(n):
        for j in range(n):
            for k in range(len(tree[i][j])):
                
                if food[i][j] >= tree[i][j][k]:
                    food[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    for _ in range(k, len(tree[i][j])):
                        food[i][j] += tree[i][j].pop() // 2
                    break
    return

def FW():
    for i in range(n):
        for j in range(n):
            for k in range(len(tree[i][j])):
                if tree[i][j][k] % 5 == 0:
                    for k in range(8):
                        nx, ny = i + dx[k], j + dy[k]
                        if 0 <= nx < n and 0 <= ny < n:
                            tree[nx][ny].appendleft(1)
            food[i][j] += a[i][j]
    return

n, m, k = map(int, input().split())
# 로봇
a = [list(map(int, input().split())) for _ in range(n)]
tree = [[deque() for _ in range(n)] for _ in range(n)]
food = [[5] * n for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)

for _ in range(k):
    SS()
    FW()

answer = 0

for i in range(n):
    answer += sum(map(len, tree[i]))

print(answer)

# from collections import deque
# from queue import PriorityQueue
# import heapq

# n, m, k = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(n)]
# tree = []

# dx = [-1, -1, -1, 0, 0, 1, 1, 1]
# dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# for i in range(m):
#     x, y, z = map(int, input().split())
#     tree.append((x - 1, y - 1, z))

# # 양분
# food = [[5 for _ in range(n)] for _ in range(n)]

# def seasons():
#     # 봄
#     global tree, food
#     tree.sort()
#     deadTrees = []
    
#     for i in range(len(tree)):
#         if i >= len(tree):
#             break
#         (x, y, z) = tree[i]

        
#         if z <= food[x][y]:
#             food[x][y] -= z
#             tree[i] = (x, y, z + 1)
#         else:
#             temp = tree.pop(i)
#             deadTrees.append(temp)
    
#     # 여름
#     for (x, y, z) in deadTrees:
#         food[x][y] += z // 2
    
#     # 가을
#     for (x, y, z) in tree:
#         if z % 5 != 0:
#             continue
        
#         for i in range(8):
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n:
#                 tree.append((nx, ny, 1))
    
#     # 겨울
#     for i in range(n):
#         for j in range(n):
#             food[i][j] += a[i][j]

# for i in range(k):
#     seasons()

# print(len(tree))