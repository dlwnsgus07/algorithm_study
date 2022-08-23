from collections import deque

g = int(input())
p = int(input())

queue = deque(i for i in range(1, g + 1))

edges = []

for i in range(p):
    edges.append(int(input()))

edges.sort(reverse=True)
count = 0

flag = True
for i in edges:
    if not flag:
        break
    while queue and flag:
        k = queue.pop()
        if i == k:
            count += 1
            break
        elif k < i:
            flag = False
print(count)


