arr = [[] for i in range(13)]
candidate = []
candidate2 = []
answer = 0
for i in range(1, 13):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, 13):
    if len(arr[i]) == 3:
        candidate.append(i)

for i in candidate:
    for j in arr[i]:
        if len(arr[j]) == 1:
            candidate2.append(i)

for i in candidate2:
    for j in arr[i]:
        if len(arr[j]) == 2:
            answer = i
print(answer)
