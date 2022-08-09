n, m = map(int, input().split())
count = 0
plus = m % 2
if m <= n:
    print(n - m)

else:
    while m >= n:
        m = m // 2
        plus += m % 2
        count += 1
    left = n - m
    right = (2*m) - n
    if left <= right:
        print(count + plus + left)
    else:
        print(count + plus + right - 1)
# 다른것보다 어떤 1599 2425 처럼 2426에서 1을 빼는 경우가 더 이득일떄가 있음 이부분을 잘 다루면 될꺼같은데...