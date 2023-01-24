import sys

k, n = map(int, input().split())
klen = [int(sys.stdin.readline())for i in range(k)]

start = 1
end = max(klen)
while(start <= end):  #왜 <로 하면 안되는지 모르겠음
    mid =(start+end)//2
    sum = 0
    for i in klen:
        sum += i//mid
    if(sum >= n):
        start = mid+1
    elif(sum < n):
        end = mid-1
print(end)