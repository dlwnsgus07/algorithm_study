def R(y, n):
    if y + 1 <= n:
        return y + 1
    else:
        return y


def L(y):
    if y - 1 >= 1:
        return y - 1
    else:
        return y


def U(x):
    if x - 1 >= 1:
        return x - 1
    else:
        return x


def D(x, n):
    if x + 1 <= n:
        return x + 1
    else:
        return x


n = int(input())
command = list(map(str, input().split()))
x = 1
y = 1

for i in command:
    if i == 'R':
        y = R(y, n)
    elif i == 'L':
        y = L(y)
    elif i == 'U':
        x = U(x)
    elif i == 'D':
        x = D(x, n)
print(x, y)
#문제 해설을 보니 훨씬 간단하고 로직적으로 안정정이게 풀 수 있다.
#나의 풀이는 command가 R, L, U, D 4개로 한정이 되어서 코드가 짧게 나왔지만 command가 훨씬 많아진다고 생각하면 상당히 좋지 않은 코드가 될 것 같다.