import sys
sys.setrecursionlimit(300000)

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

ans = 0


def binary(start, end):
    global ans
    if start > end:
        return None
    mid = (start + end) // 2
    target = 0
    for i in arr:
        target += i // mid
    if target >= n:
        if ans < mid:
            ans = mid
        binary(mid + 1, end)
    else:
        binary(start, mid - 1)


binary(1, max(arr))
print(ans)
