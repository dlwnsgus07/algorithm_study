n, m, k = map(int, input().split())
team = 0

for i in range(k):
    if n/2 >= m:
        n -= 1
    else:
        m -= 1

if m>= n/2:
    team = n//2
else:
    team = m
    
print(team)
