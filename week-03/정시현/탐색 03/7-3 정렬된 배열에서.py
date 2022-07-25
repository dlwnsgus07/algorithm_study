# 이진 탐색 07-03 정렬된 배수에서 특정 수의 개수 구하기

N, x = map(int, input().split())

nl = list(map(int, input().split()))

count = 0
for i in range(len(nl)):
    if nl[i] == x:
        count+=1

print(count)
