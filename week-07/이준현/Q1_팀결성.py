def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)
for i in range(1, n):
    parent[i] = i

for i in range(m):
    is_team, a, b = map(int, input().split())

    if is_team == 0:
        union_parent(parent, a, b)
    else:
        x = find_parent(parent, a)
        y = find_parent(parent, b)

        if x != y:
            print("NO")
        else:
            print("YES")


