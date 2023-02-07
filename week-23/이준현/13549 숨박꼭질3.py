from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

MAX = 1e9
ans = 0
distance = [MAX] * 100001

q = deque()
q.append(n)
distance[n] = 0

while q:
    x = q.popleft()
    if x == m:
        break
    else:
        for i in (x - 1, x + 1, 2 * x):
            if 0 <= i < 100001 and distance[i] == MAX:
                if x != 0 and i != 0 and i / x == 2:
                    distance[i] = distance[x]
                    q.appendleft(i)
                else:
                    distance[i] = distance[x] + 1
                    q.append(i)
print(distance[m])

