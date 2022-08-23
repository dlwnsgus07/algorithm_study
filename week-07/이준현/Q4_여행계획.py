def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n + 1)
graph = [] * n

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

for i in range(1, n + 1):
    parent[i] = i

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union_parent(parent, i + 1, j + 1)

city = list(map(int, input().split()))

basic_parent = find_parent(parent, city[0])
can_trip = True
for i in city:
    j = find_parent(parent, i)
    if j != basic_parent:
        can_trip = False

if can_trip:
    print("YES")
else:
    print("NO")