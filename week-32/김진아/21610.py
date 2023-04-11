
# 21610 마법사 상어와 비바라기

from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# 8방향
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 대각선 확인 방향
cx = [-1, -1, 1, 1]
cy = [-1, 1, -1, 1]

# 구름이 있는 좌표
cloud = deque([(n - 2, 0), (n - 2, 1), (n - 1, 0), (n - 1, 1)])

def magic(d, s):
    prevCloud = []
    for i in range(len(cloud)):
        (r, c) = cloud[i]
        r = ((r + dx[d - 1] * s) + n) % n
        c = ((c + dy[d - 1] * s) + n) % n
        cloud[i] = (r, c)
        prevCloud.append((r, c))
        
        # 구름이 있는 칸에 비 내림
        a[r][c] += 1
    
    
    while cloud:
        (r, c) = cloud.pop()
        
        for i in range(4):
            nx = r + cx[i]
            ny = c + cy[i]
            
            if 0 <= nx < n and 0 <= ny < n and a[nx][ny] > 0:
                a[r][c] += 1
    
    for i in range(n):
        for j in range(n):
            if a[i][j] >= 2 and (i, j) not in prevCloud:
                a[i][j] -= 2
                cloud.append((i, j))
    

for i in range(m):
    d, s = map(int, input().split())
    magic(d, s)

print(sum(map(sum, a)))
