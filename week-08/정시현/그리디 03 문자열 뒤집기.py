# 그리디 Q03 문자열 뒤집기


data = input()
cnt0 = 0
cnt1 = 0

if data[0] == '1':
    cnt1 += 1
elif data[0] == '0':
    cnt0 += 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            cnt1 += 1
        elif data[i+1] == '0':
            cnt0 += 1

print(min(cnt0, cnt1))

    
