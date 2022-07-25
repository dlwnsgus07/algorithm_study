# 06 정렬 03. 두 배열의 원소 교체

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

mina = min(a)
maxb = max(b)

for i in range(k):

    if mina < maxb :
        mina, maxb = maxb, mina

    else:
        break

print(sum(a))
