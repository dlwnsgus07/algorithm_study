# sol 07-03

from bisect import bisect_left, bisect_right

def countb(array, l_v, r_v):
    r_i = bisect_right(array, r_v)
    l_i = bisect_left(array, l_v)
    return r_i - l_i

n,x = map(int, input().split())
array = list(map(int, input().split()))

count = countb(array, x, x)

if count == 0:
    print(-1)

else :
    print(count)

    
