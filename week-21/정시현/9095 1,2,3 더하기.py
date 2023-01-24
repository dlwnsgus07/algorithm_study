t = int(input())
n = [int(input()) for i in range(t)]

# n <= 10 이렇게 n이 작으면 걍 1부터 10까지 출력값을 정해주고 싶어져..^^

def func(num):
    if(num==1):
        return 1
    elif(num==2):
        return 2
    elif(num==3):
        return 4
    else:
        return func(num-1) + func(num-2) + func(num-3)

for i in range(t):
    print(func(n[i]))