n = int(input())
qtt = [int(input()) for i in range(n)]

wine = []
wine.append(qtt[0]) 
wine.append(qtt[0]+qtt[1])
wine.append(max(qtt[2]+qtt[0], qtt[2]+qtt[1], wine[1]))

for i in range(3,n):
    wine.append(max(qtt[i]+wine[i-2], qtt[i]+qtt[i-1]+wine[i-3], wine[i-1]))
    
print(max(wine))