#백준 2212 센서
import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
s = sorted(list(map(int, sys.stdin.readline().split())))

if k>=n:
    print(0)
else :
    di = []
    for i in range(n-1):
        di.append(s[i+1]-s[i])  

    di.sort(reverse=True)
    
    for i in range(k-1):
        di.pop(0)

    print(sum(di))


