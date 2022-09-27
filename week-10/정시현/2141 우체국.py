#백준 2141 우체국


n = int(input())

X = []
num = 0
for i in range(n):
    vil, peo = map(int, input().split())
    X.append([vil,peo])
    num += peo

X.sort(key=lambda x:x[0])

num2 = 0

for i in range(n):
    
    num2 += X[i][1]
    if(num2 > (num//2)):
        print(X[i][0])
        break
    
    

