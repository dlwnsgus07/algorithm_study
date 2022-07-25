n, x = map(int, input().split())

array = list(map(int, input().split()))


def binary_search_first(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if (mid == 0 or array[mid - 1] != target) and array[mid] == target:
            return mid
        elif array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return None


def binary_search_last(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if (mid == n - 1 or array[mid + 1] != target) and array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


first, last = binary_search_first(array, x, 0, n - 1), binary_search_last(array, x, 0, n - 1)
if first is None:
    print(-1)
else:
    print(last - first + 1)
