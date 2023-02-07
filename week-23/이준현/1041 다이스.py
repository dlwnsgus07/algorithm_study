import sys

input = sys.stdin.readline

n = int(input())
dice = list(map(int, input().split()))

one = 4 * (n - 1) * (n - 2) + (n - 2) ** 2
two = 4 * (n - 1) + 4 * (n - 2)
three = 4

min_one_value = sorted(dice)[0]
min_list = [min(dice[0], dice[5]), min(dice[1], dice[4]), min(dice[2], dice[3])]
min_list.sort()
min_two_value = min_list[0] + min_list[1]
min_three_value = min_list[0] + min_list[1] + min_list[2]

if n == 1:
    print(sum(dice) - sorted(dice)[5])
else:
    print(one * min_one_value + two * min_two_value + three * min_three_value)
