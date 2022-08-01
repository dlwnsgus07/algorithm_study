# 다이나믹 프로그래밍 실전 02. 1로 만들기 - 정답 코드

x = int(input())

d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] +1 
    
    if i%2 == 0:
        d[i] = min(d[i], d[i//2]+1) # 이 부분 이해가 안됨,,

    if i%3 == 0:
        d[i] = min(d[i], d[i//3]+1) # 그리고 왜 if/elif안쓰고 셋다 if야?
        
    if i%5 == 0:
        d[i] = min(d[i], d[i//5]+1) 
        
print(d[x])
        
