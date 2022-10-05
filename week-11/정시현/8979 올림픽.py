#백준 8979 올림픽

n, k = map(int, input().split())
con = []

for i in range (n):
    con.append(list(map(int, input().split())))
    if(con[i][0] == k):
        kc = con[i]

count = 0
for i in range(n):
    if(con[i][1] > kc[1]):
        count +=1
    elif(con[i][1] == kc[1] and con[i][2] > kc[2]):
        count +=1
    elif(con[i][1] == kc[1] and con[i][2] == kc[2] and con[i][3] > kc[3]):
        count +=1

print(count+1)
