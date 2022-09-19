# 백준 1459 걷기

x, y, w, s = map(int, input().split())

time = 0
mi = min(x,y)
mx = max(x,y)

if s<= 2*w:

    if s<=w:
        k = (x+y)%2
        time += ((mx-k)*s+k*w)

    else:
        time += mi*s
        time += (mx-mi)*w  
else:
    time += (x+y)*w


print(time)
    
