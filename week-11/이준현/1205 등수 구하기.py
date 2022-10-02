n, my_score, rank = map(int, input().split())
score = []
count = n+1
if n > 0:
    score = list(map(int, input().split()))
    score.sort(key=lambda x: -x)
    if n == rank and my_score <= score[-1]:
        print(-1)
    else:
        for i in range(n):
            if score[i] <= my_score:
                count = i + 1
                break
        print(count)
else:
    if rank >= 1:
        print(1)
    else:
        print(-1)





