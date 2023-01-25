import sys

sys.setrecursionlimit(30000)
INF = 1e9
n = int(input())
arr = [[0, 0, 0] for i in range(n)]
for i in range(n):
    arr[i][0], arr[i][1], arr[i][2] = map(int, input().split())
min_list = []
dp = [[INF, INF, INF] for i in range(n)]

dp[n-1][0] = arr[n-1][0]
dp[n-1][1] = arr[n-1][1]
dp[n-1][2] = arr[n-1][2]

for j in range(n-2, -1, -1):
    for i in range(3):
        if i == 0:
            dp[j][i] = arr[j][i] + min(dp[j+1][1], dp[j+1][2])
        elif i == 1:
            dp[j][i] = arr[j][i] + min(dp[j+1][0], dp[j+1][2])
        elif i == 2:
            dp[j][i] = arr[j][i] + min(dp[j+1][0], dp[j+1][1])

print(min(dp[0]))

# def post_order(index, depth):
#     if depth == (n - 1):
#         return arr[depth][index]
#     if index == 0:
#         return arr[depth][index] + min(post_order(1, depth + 1), post_order(2, depth + 1))
#     if index == 1:
#         return arr[depth][index] + min(post_order(0, depth + 1), post_order(2, depth + 1))
#     if index == 2:
#         return arr[depth][index] + min(post_order(0, depth + 1), post_order(1, depth + 1))

