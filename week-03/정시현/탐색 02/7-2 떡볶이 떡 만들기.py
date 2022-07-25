# 이진 탐색 07-02 떡볶이 떡 만들기

n, m = map(int, input().split())

tl = list(map(int, input().split()))


#count = 0

#for i in range(n):
#    if tl[i] >= h:
#        break

#    else:
#        count += (h - tl[i])

start = 0
end = max(tl)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2

    for x in tl:
        if x>mid:
            total += x-mid

    if total < m:
        end = mid-1

    else:
        result = mid
        start = mid+1

print(result)
