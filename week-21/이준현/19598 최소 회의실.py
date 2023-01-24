# 소팅을 회의 시작 시간 기준? or 회의의 시간
import heapq

n = int(input())
arr = []
end_arr = []
count = 0
for _ in range(n):
    start, end = map(int, input().split())
    heapq.heappush(arr, (start, end))
min_start, min_end = heapq.heappop(arr)
heapq.heappush(end_arr, min_end)
count += 1
while arr:
    start, end = heapq.heappop(arr)
    # 회의실이 하나 더 생겨야 할 때
    if start < end_arr[0]:
        count += 1
        heapq.heappush(end_arr, end)
    else:
        heapq.heappop(end_arr)
        heapq.heappush(end_arr, end)
print(count)
