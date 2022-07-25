n = int(input())

array = list(map(int, input().split()))

def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return None

# for 문으로 index를 검색하는데, 이미 정렬되었기 때문에 해당 Index보다 수가 작으면 아예 고려할 필요가 없음, index와 일치하면 return, 일치하지 않으면
#그대

result = binary_search(array, 0, n - 1)
if result is None:
    print(-1)
else:
    print(result)