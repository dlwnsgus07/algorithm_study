n, m = map(int, input().split())

array = list(map(int, input().split()))


def binary_search(array, length, start, end):
    min_result = 0
    while start <= end:
        length_sum = 0
        mid = (end + start) // 2
        for i in array:
            if i > mid:
                length_sum += i - mid
        if length_sum == length:
            min_result = mid
            return min_result
        if length_sum < length:
            end = mid - 1
        else:
            min_result = mid
            start = mid + 1
    return min_result


result = binary_search(array, m, 0, max(array))

if result is None:
    print("error")
else:
    print(result)
