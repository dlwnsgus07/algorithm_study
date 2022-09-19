# 백준 11047 동전0

n, k = map(int, input().split())

mon = []
for i in range(n):
    mon.append(int(input()))

count = 0

while(k>0):
    for i in range(n):
        count+= k//mon[n-1-i]
        k %= mon[n-1-i]

print(count)

