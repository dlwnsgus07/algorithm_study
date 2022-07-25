# 06 정렬 01. 위에서 아래로

n = int(input())

num = []
for i in range (n):
    num.append(int(input()))


num.sort(reverse = True)


num = ' '.join(map(str,num))

print(num)
