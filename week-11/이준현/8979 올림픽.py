country = []

n, m = map(int, input().split())
count = 1
temp = -1

for _ in range(n):
    country.append(list(map(int, input().split())))

country.sort(key=lambda x: (-x[1], -x[2], -x[3]))

gold = country[0][1]
silver = country[0][2]
dong = country[0][3]

for i in country:
    if gold != i[1] or silver != i[2] or dong != i[3]:
        gold = i[1]
        silver = i[2]
        dong = i[3]
        count = count + temp + 1
        temp = 0
    else:
        temp += 1
    if i[0] == m:
        break
print(count)