import sys
input = sys.stdin.readline

n, m = map(int, input().split())
t = [int(input()) for _ in range(n)]

mini = min(t)
maxi = max(t) * m
result = maxi

while mini <= maxi:
    total = 0
    mid = (mini + maxi) // 2

    for i in range(n):
        total += mid // t[i]

    if total >= m:
        maxi = mid -1
        result = min(mid, result)

    else:
        mini = mid + 1

print(result)