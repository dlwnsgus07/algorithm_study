# n = int(input())
# arr = list(map(int, input().split()))
#
# result = - (1000 * n)
#
# for i in range(n):
#     for j in range(i + 1, n + 1):
#         result = max(result, sum(arr[i:j]))
#
# print(result)

n = int(input())
arr = list(map(int, input().split()))
result = [arr[0]]

for i in range(n - 1):
    result.append(max(result[i] + arr[i + 1], arr[i + 1]))

print(max(result))