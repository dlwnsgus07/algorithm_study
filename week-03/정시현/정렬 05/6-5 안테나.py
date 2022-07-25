# 06-5 안테나

#n = int(input())

#l = list(map(int, input().split()))

#a = []
#count = 0

#for x in range(n):
#    for i in range(n):
#        count += abs(l[x]-l[i])
#    a.append(x, count)
#    count = 0

#a.sort(key = a[1])

#print(a[0])

n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n-1)//2])
