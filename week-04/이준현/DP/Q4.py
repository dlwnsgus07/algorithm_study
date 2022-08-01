n, m = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))
d = [-1] * 10001
for k in money:
    d[k] = 1
for i in range(money[1], m):
    for j in money:
        if d[i] == -1:
            continue
        if d[i+j] == -1:
            d[i + j] = d[i] + 1
        else:
            d[i + j] = min(d[i + j], d[i] + 1)

print(d[m])