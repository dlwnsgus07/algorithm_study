# 실전 문제 3 게임 개발
N, M = map(int, input().split())
A, B, d = map(int, input().split())

left = A
right = B

arr = [list(map(int, input().split())) for _ in range(M)]
count = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 처음에는 방향 설정을 왼쪽으로 돌아서 전진하는 걸로 dx, dy를 만들었는데 그렇게 하니까 네 방향이 다 막혀있어 뒤쪽으로 가는 걸 구현하려하니 해당 로직을 위해 또 방향 관련된 배열을 만들어야했음

tryCnt = 0

while True:
    if d == 0:
        d = 3
    else:
        d -= 1

    if arr[left+dx[d]][right+dy[d]] == 0 and left+dx[d] >=0 and left+dx[d] < N and right+dy[d] >=0 and right+dy[d] < M:
        tryCnt = 0
        count += 1
        arr[left][right] = 3
        left += dx[d]
        right += dy[d]
        continue
    else:
        tryCnt += 1

    if tryCnt >= 4:
        if arr[left-dx[d]][right-dy[d]] == 1 or left-dx[d] < 0 or right-dy[d] < 0 or left-dx[d] > N-1 or right-dy[d] > M-1:
            break
        else:
            arr[left][right] = 3
            left -= dx[d]
            right -= dy[d]
            tryCnt = 0

print(count)


# while True:
#     if d == 0:
#         if right - 1 < 0 or arr[left][right-1] == 0 or arr[left][right-1] == 3:
#             d += 1
#             tryCnt += 1
#         if arr[left][right - 1] == 1:
#             tryCnt = 0
#             count += 1
#             right -= 1
#             arr[left][right] = 3
#             continue
#     elif d == 1:
#         if left - 1 < 0 or arr[left-1][right] == 0 or arr[left-1][right] == 3:
#             d += 1
#             tryCnt += 1
#         if arr[left-1][right] == 1:
#             tryCnt = 0
#             count += 1
#             left -= 1
#             arr[left][right] = 3
#             continue
#     elif d == 2:
#         if right + 1 < 0 or arr[left][right+1] == 0 or arr[left][right+1] == 3:
#             d += 1
#             tryCnt += 1
#         if arr[left][right+1] == 1:
#             tryCnt = 0
#             count += 1
#             right += 1
#             arr[left][right]=3
#             continue
#
#     elif d == 3:
#         if left + 1 < 0 or arr[left+1][right] == 0 or arr[left+1][right] == 3:
#             d = 0
#             tryCnt += 1
#         if arr[left+1][right] == 1:
#             tryCnt = 0
#             count += 1
#             left += 1
#             arr[left][right]=3
#             continue
#
#     if tryCnt >= 4:
#         if d == 0:
#             if left-1<0 or arr[left-1][right] == 0:
#                 break
#             else:
#                 tryCnt = 0
#                 arr[left][right] = 3
#         elif d == 1:
#             if right+1 < 0 or arr[left][right+1] == 0:
#                 break
#             else:
#                 tryCnt = 0
#                 arr[left][right+1]=3
#         elif d == 2:
#             if left+1 < 0 or arr[left+1][right]==0:
#                 break
#             else:
#                 tryCnt = 0
#                 arr[left+1][right] = 3
#         elif d == 3:
#             if right-1 < 0 or arr[left][right-1]==0:
#                 break
#             else:
#                 tryCnt = 0
#                 arr[left][right-1]=3
#
#
#
# print(arr)
# print(count)

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1