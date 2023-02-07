import sys

input = sys.stdin.readline
answer = 0

n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_cost = cost[0]
answer += min_cost * dist[0]

for i in range(1, n - 1):
    if min_cost > cost[i]:
        min_cost = cost[i]
    answer += min_cost * dist[i]
print(answer)
