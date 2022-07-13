N = int(input())
inputData = list(map(str, input().split()))

left = 1
right = 1

for i in inputData:
    if i == "L":
        if right != 1:
            right -= 1
    elif i == "R":
        if right != N-1:
            right += 1
    elif i == "U":
        if left != 1:
            left -= 1
    elif i == "D":
        if left != N-1:
            left += 1

print(left, right)

