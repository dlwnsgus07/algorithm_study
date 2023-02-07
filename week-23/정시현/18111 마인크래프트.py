import sys
input = sys.stdin.readline
N,M,B = map(int,input().split())
li=[]
solve=[]
for i in range(N):
    li+=(map(int,input().split()))
for i in range(min(li),max(li)+1):
    bag=B
    sec=0
    for ground in li:
        if (ground-i)>0: 
            bag+=(ground-i)
            sec+=2*(ground-i)
        elif (ground-i)<0:
            bag+=(ground-i)
            sec+=1*(ground-i)*-1 
    if bag>=0:
        solve.append([sec,i])
solve.sort(key=lambda x:(x[0],-x[1])) 
print(solve[0][0],solve[0][1])