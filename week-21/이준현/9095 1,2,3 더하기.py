import sys

input = sys.stdin.readline
n = int(input())
arr = []
dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(n):
    arr.append(int(input()))

for i in range(4, max(arr) + 1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in arr:
    print(dp[i])
# 1= 1 = 1
# 2 = 2, 1,1 = 2
# 3 = 1 1 1, 2 1 , 1 2, 3 = 3
# 4 = 1 1 1 1,  1 1 2,   1 2 1,   2 1 1,   2 2,   1 3,  3 1 = 7
