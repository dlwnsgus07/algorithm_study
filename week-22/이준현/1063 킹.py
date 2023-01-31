import sys
from collections import deque

input = sys.stdin.readline

x, y, n = map(str, input().split())
arr = [[0] * 9 for i in range(9)]
location = {}
command_list = {'R': (0, 1), 'L': (0, -1), 'B': (1, 0), 'T': (-1, 0), 'RT': (-1, 1), 'LT': (-1, -1), 'RB': (1, 1),
                'LB': (1, -1)}
command = deque()
n = int(n)
for i in range(1, 9):
    location["ABCDEFGH"[i - 1]] = i
king_location = (9 - int(x[1]), location.get(x[0]))
stone_location = (9 - int(y[1]), location.get(y[0]))

for i in range(n):
    command.append(input().strip())

while command:
    cmd = command.popleft()
    dx, dy = command_list[cmd]
    k_nx = king_location[0] + dx
    k_ny = king_location[1] + dy
    s_nx = -1
    s_ny = -1
    if k_nx == stone_location[0] and k_ny == stone_location[1]:
        s_nx = stone_location[0] + dx
        s_ny = stone_location[1] + dy
    # 돌이 같이 움직일때
    if s_nx != -1 or s_ny != -1:
        if s_nx > 8 or s_ny > 8 or s_nx <= 0 or s_ny <= 0:
            continue
        else:
            king_location = (k_nx, k_ny)
            stone_location = (s_nx, s_ny)
    else:
        if k_nx > 8 or k_ny > 8 or k_nx <= 0 or k_ny <= 0:
            continue
        else:
            king_location = (k_nx, k_ny)
print("ABCDEFGH"[king_location[1] - 1] + str(9 - king_location[0]))
print("ABCDEFGH"[stone_location[1] - 1] + str(9 - stone_location[0]))
