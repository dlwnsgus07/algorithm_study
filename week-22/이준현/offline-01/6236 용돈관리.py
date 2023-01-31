import sys
sys.setrecursionlimit(30000)
n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))
ans = 0


def binary(start, end):
    global ans
    if start > end:
        return None
    mid = (start + end) // 2
    money = mid
    count = 1
    for i in arr:
        if money < i:
            count += 1
            money = mid
        money -= i
    if count > m or mid < max(arr):
        binary(mid + 1, end)
    else:
        ans = mid
        binary(start, mid - 1)


binary(min(arr), sum(arr))
print(ans)
