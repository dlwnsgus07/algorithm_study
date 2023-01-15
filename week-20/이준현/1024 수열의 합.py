n, m = map(int, input().split())
ans_list = []
# n이 정확히 m개의 연속된 수열의 합으로 구할 수 있을 떄
# m개로 나눳을 떄 몫이 0이하이면 문제가 있는 거임
# 나머지가 0인것을 계속 찾아 올라가야한다.
for i in range(m, 101):
    n_temp = n
    temp = sum(range(i))
    n_temp -= temp
    if n_temp < 0:
        break
    if n_temp % i == 0:
        for j in range(i):
            ans_list.append((n_temp // i) + j)
        break
if len(ans_list) == 0:
    print(-1)
else:
    for i in ans_list:
        print(i, end=' ')