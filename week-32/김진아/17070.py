# # 17070 파이프 옮기기 1

from collections import deque
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

q = deque([(0, 1, 0)]) # 0 가로 1 세로 2 대각선

result = 0

# 끝에 거만 계산하면 되네;;;
def solution(x, y, d):
    global result
    if x == n - 1 and y == n - 1:
        result += 1
        return
    
    if d == 0:
        if 0 <= x < n and 0 <= y + 1 < n and arr[x][y + 1] == 0:
            solution(x, y + 1, 0)
        if 0 <= x + 1 < n and 0 <= y + 1 < n and arr[x + 1][y + 1] == 0 and arr[x][y + 1] == 0 and arr[x + 1][y] == 0:
            solution(x + 1, y + 1, 2)
    elif d == 1:
        if 0 <= x + 1 < n and 0 <= y < n and arr[x + 1][y] == 0:
            solution(x + 1, y, 1)
        if 0 <= x + 1 < n and 0 <= y + 1 < n and arr[x + 1][y + 1] == 0 and arr[x][y + 1] == 0 and arr[x + 1][y] == 0:            
            solution(x + 1, y + 1, 2)
    else:
        if 0 <= x < n and 0 <= y + 1 < n and arr[x][y + 1] == 0:
            solution(x, y + 1, 0)
        if 0 <= x + 1 < n and 0 <= y < n and arr[x + 1][y] == 0:
            solution(x + 1, y, 1)
        if 0 <= x + 1 < n and 0 <= y + 1 < n and arr[x + 1][y + 1] == 0 and arr[x][y + 1] == 0 and arr[x + 1][y] == 0:   
            solution(x + 1, y + 1, 2)

solution(0, 1, 0)
print(result)


# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]

# result = 0

# def solution(x1, y1, x2, y2):
#     global result
#     if x2 == n - 1 and y2 == n - 1:
#         result += 1
#         return
#     # 가로
#     if x1 == x2:
#         for (dx1, dy1, dx2, dy2) in [(0, 1, 0, 1), (0, 1, 1, 1)]:
#             nx1, ny1 = x1 + dx1, y1 + dy1
#             nx2, ny2 = x2 + dx2, y2 + dy2
            
#             if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n:
#                 if arr[nx1][ny1] == 1 or arr[nx2][ny2] == 1:
#                     continue
                
#                 if nx1 != nx2 and ny1 != ny2:
#                     if arr[nx2 - 1][ny2] == 1 or arr[nx2][ny2 - 1] == 1:
#                         continue
                        
#                 solution(nx1, ny1, nx2, ny2)
#     # 세로
#     elif y1 == y2:
#         for (dx1, dy1, dx2, dy2) in [(1, 0, 1, 0), (1, 0, 1, 1)]:
#             nx1, ny1 = x1 + dx1, y1 + dy1
#             nx2, ny2 = x2 + dx2, y2 + dy2
            
#             if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n:
#                 solution(nx1, ny1, nx2, ny2)
        
#     # 대각선
#     else:
#         for (dx1, dy1, dx2, dy2) in [(1, 1, 0, 1), (1, 1, 1, 0), (1, 1, 1, 1)]:
#             nx1, ny1 = x1 + dx1, y1 + dy1
#             nx2, ny2 = x2 + dx2, y2 + dy2
            
#             if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n:
#                 solution(nx1, ny1, nx2, ny2)
        
# solution(0, 0, 0, 1)

# print(result)