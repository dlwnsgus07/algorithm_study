from itertools import permutations

N = int(input())
num = list(map(int, input().split()))
op_num = list(map(int, input().split()))
op_list = ['+', '-', '*', '/']
op = []

for k in range(len(op_num)):
    for _ in range(op_num[k]):
        op.append(op_list[k])

maxValue = -1e9
minValue = 1e9

def perm():
    global maxValue, minValue

    for i in permutations(op, N - 1):
        total = num[0]
        for j in range(1, N):
            if i[j-1] == '+':
                total += num[j]
            elif i[j-1] == '-':
                total -= num[j]
            elif i[j-1] == '*':
                total *= num[j]
            elif i[j-1] == '/':
                total = int(total / num[j])

        if total > maxValue:
            maxValue = total
        if total < minValue:
            minValue = total

perm()
print(maxValue)
print(minValue)
