import sys
input = sys.stdin.readline()
n, m = map(int, input().split())
mon = [int(input()) for i in range(n)]

count = 0
k = max(mon)
r = 0
while(True):

    for i in range(n):
        if(i==1):
            count += 1
            r = k-mon[0]
        else:
            if(r>=mon[i]):
                r = r-mon[i]
            else:
                count += 1
                r = k-mon[i]
    if(count <= m):
        break
    else:
        k += 100
print(k)