#그리디 Q05 볼링공 고르기

n, m = map(int, input().split())
k = list(map(int,input().split()))

count = 0

for i in range(n):
    for j in range(n):
        if j>i:
            if k[i] != k[j]:
                count+= 1

           
print(count)
