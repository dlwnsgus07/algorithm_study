x = int(input())
INF = 1e9
d = [INF] * 5001
d[3] = d[5] = 1
for i in range(6, x + 1):
    if min(d[i - 3], d[i - 5]) != INF:
        d[i] = min(d[i - 3], d[i - 5]) + 1

if d[x] == INF:
    print("-1")
else:
    print(d[x])
