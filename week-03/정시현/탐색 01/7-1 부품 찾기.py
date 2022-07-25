# 이진 탐색 07-01 부품 찾기

n = int(input())
nl = list(map(int, input().split()))
# nl.sort() 안했는데 답은 똑같이 나왔음. 왜지/

m = int(input())
ml = list(map(int, input().split()))

def bsearch(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2

    if array[mid] == target:
        return mid
    elif array[mid] <target:
        return bsearch(array, target, mid+1, end)
    else:
        return bsearch(array, target, start, mid-1)
        

for i in range(m):
    result = bsearch(nl, ml[i], 0, n-1)
    if result == None:
        print('no', end = ' ')
    else:
        print('yes', end = ' ')
        
