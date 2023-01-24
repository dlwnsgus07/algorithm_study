# import sys
# sys.setrecursionlimit(300000)
#
# input = sys.stdin.readline
# n, m = map(int, input().split())
# INF = 1e9
# dp = [INF] * (m + 1)
# dp[n] = 1
#
# for i in range(n + 1, m + 1):
#     if i % 2 == 0:
#         dp[i] = dp[i // 2] + 1
#     if i % 10 == 1:
#         dp[i] = min(dp[i], dp[i // 10] + 1)
# if dp[m] == INF:
#     print(-1)
# else:
#     print(dp[m])

n, m = map(int, input().split())
flag = False
count = 1
while True:
    if m % 2 == 0:
        m /= 2
    elif m % 10 == 1:
        m = m // 10
    else:
        flag = True
        break
    count += 1
    if m == n:
        break
    if m < n:
        flag = True
        break
if flag:
    print(-1)
else:
    print(count)
