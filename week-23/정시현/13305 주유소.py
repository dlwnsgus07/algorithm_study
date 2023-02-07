n = int(input())
len = list(map(int,input().split()))
mon = list(map(int,input().split()))

min = len[0] * mon[0]
cheap = mon[0]

for i in range(1, n-1):
    if cheap > mon[i]: 
        cheap = mon[i] 

    min += cheap * len[i]

print(min)