# 다이나믹 프로그래밍 실전 03. 개미 전사 - 정답 코드

n = int(input())

array = list(map(int, input().split()))

d = [0] * 100

d[0] = array [0]
d[1] = max(array[0], array[1])

for i in range(2,n):
    d[i] = max(d[i-1], d[i-2]+ array[i])


print(d[n-1])
