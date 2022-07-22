import math

n = int(input())
house = list(map(int, input().split()))
house.sort()

if n % 2 == 0:
    result = house[int(n / 2) - 1]

else:
    result = house[math.floor(n / 2)]

print(result)

print(house[n - 1])

#print(house[n-1] // 2) 와 이렇게 짧게 표현할 수 있었네...