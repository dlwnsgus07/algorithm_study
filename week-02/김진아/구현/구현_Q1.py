# 실전 문제 2 왕실의 나이트
inputData = list(input())
left, right = ord(inputData[0])-96, inputData[1]

# case 1 : 오른쪽으로 한 칸 위쪽으로 두 칸
# case 2 : 오른쪽으로 한 칸 아래쪽으로 두 칸
# case 3 : 오른쪽으로 두 칸 위쪽으로 한 칸
# case 4 : 오른쪽으로 두 칸 아래쪽으로 한 칸
# case 5 : 왼쪽으로 한 칸 위쪽으로 두 칸
# case 6 : 왼쪽으로 한 칸 아래쪽으로 두 칸
# case 7 : 왼쪽으로 두 칸 위쪽으로 한 칸
# case 8 : 왼쪽으로 두 칸 아래쪽으로 한 칸

tasks = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]
count = 0

for task in tasks:
    if task[0] + int(left) >= 1 and task[1] + int(right) >= 1:
        count += 1

print(count)