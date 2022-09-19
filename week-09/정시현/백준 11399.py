# 백준 11399 ATM

n = int(input())

p = list(map(int, input().split()))
p.sort()

time = 0

sum = 0

for i in range (n):
    sum += p[i]
    time += sum

print(time)
