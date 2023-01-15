n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

arr.sort()
first = arr[0] - 0.5 + m
ans += 1

for i in arr:
    if first < i + 0.5:
        ans += 1
        first = i - 0.5 + m

print(ans)