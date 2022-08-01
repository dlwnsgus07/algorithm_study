# 다이나믹 프로그래밍 실전02. 1로 만들기

x = int(input())

d = [0] * 30000
count = 0



while True:
    if x == 0:
        return False
    
    if x % 5 == 0:
        x = x/5
        count += 1
        continue
    elif x%3 == 0:
        x = x/3
        count += 1
        continue
    elif x%2 == 0:
        x = x/2
        count += 1
        continue
    else:
        x = x-1
        count += 1
        continue

    
    d[x] = count


print(d[x])
