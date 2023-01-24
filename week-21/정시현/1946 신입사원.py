#pypy3로 하면 되고 python3로 하면 시간초과
t = int(input())
r = []
for i in range(t):
    n = int(input())
    m = [list(map(int, input().split())) for i in range(n)]
    
    m.sort()
    result = 1
    top = m[0][1]
    for j in range(1, len(m)):
        if(m[j][1] < top):
            result += 1
            top = m[j][1]
    r.append(result)

for i in range(len(r)):
    print(r[i])