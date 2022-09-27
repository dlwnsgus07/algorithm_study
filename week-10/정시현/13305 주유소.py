#백준 13305 주유소

n = int(input())

road = list(map(int, input().split()))

pr = list(map(int, input().split()))
s = sum(road)
total = 0

while(len(pr)>0):
    
    tmp = min(pr)
    mini = pr.index(tmp)

    t=0           
    for i in range(mini):
         t+= road[i]
        
    total += (s-t)*tmp
    s=t

    del pr[mini:len(pr)]

print(total)
