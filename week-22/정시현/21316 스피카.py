star = {}
for _ in range(12):
    x, y = map(int, input().split())
    if x in star:
        star[x].append(y)
    else:
        star[x] = [y]
    if y in star:
        star[y].append(x)
    else:
        star[y] = [x]
s1 = []
s2 = []
s3 = []
for s in star:
    if len(star[s]) == 3:
        s3.append(s)
    elif len(star[s]) == 1:
        s1.append(s)
    elif len(star[s]) == 2:
        s2.append(s)

for s in s3:
    count = 0
    for i in star[s]:
        if i in s1:
            count += 1
        elif i in s2:
            count += 2
    if count == 3:
        print(s)
