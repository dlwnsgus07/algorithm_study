#백준 1205 등수 구하기

import sys

n, k, p = map(int, sys.stdin.readline().split())
if(n > 0):
    l = list(map(int, sys.stdin.readline().split()))

    count = 0
    for i in range(n):
        if(l[i] > k):
            count +=1

    if(l[n-1] == k):
        count +=1 
    if(count+1 > n):
        print(-1)
    else:
        print(count+1)

else :
    print(1)
