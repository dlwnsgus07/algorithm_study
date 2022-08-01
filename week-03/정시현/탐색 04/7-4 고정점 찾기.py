# 이진 탐색 07-04 고정점 찾기

n = int(input())

nl = list(map(int, input().split()))

def func(array, start, end):
    if start > end:
        return None
    mid = (start + end) //2

    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return func(array, start, mid-1)
    else:
        return func(array, mid+1, end)



result = func(nl, 0, n-1)

if result == None:
    print(-1)
    
else:
    print(result)


