import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 2)
arr = [0]
for _ in range(n):
    arr.append(int(input()))
arr.append(0)
dp[1] = arr[1]
dp[2] = dp[1] + arr[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i-3] + arr[i - 1] + arr[i], dp[i-2]+arr[i], dp[i-1])

print(dp[n])