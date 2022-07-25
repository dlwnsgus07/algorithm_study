# 이진 탐색 07-04 고정점 찾기

n = int(input())

nl = list(map(int, input().split()))

def func(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) //2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return func(array, target, start, mid-1)
    else:
        return func(array, target, mid+1, end)

count = 0

for i in range(n):
    result = func(nl, i, 0, n-1)
    if result == None:
        break
    
    elif nl[i] == i:
        print(i)
        count += 1

    else:
        break

if count == 0:
    print(-1)
