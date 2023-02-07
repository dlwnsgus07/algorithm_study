import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
ans = 1e9
for _ in range(n):
    arr.append(int(input()))

arr.sort()


def binary(start, end):
    global ans
    total = 0
    if start > end:
        return None
    mid = (start + end) // 2
    for i in arr:
        total += mid // i
    if total >= m:
        ans = mid
        binary(start, mid - 1)
    else:
        binary(mid + 1, end)


binary(0, max(arr) * m)
print(ans)
