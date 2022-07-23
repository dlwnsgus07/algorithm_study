def binary_search(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
array = list(map(int, input().split()))

m = int(input())
find = list(map(int, input().split()))

for i in find:
    result = binary_search(array, 0, n-1, i)
    if result is None:
        print("no", end=' ')
    else:
        print("yes", end=' ')

