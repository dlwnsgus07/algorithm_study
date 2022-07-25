# 정렬 04 국영수

n = int(input())

score = []
for i in range (n):
    data = input().split()
    score.append(data[0], int(data[1]), int(data[2]), int(data[3]))


score2 = sorted(score, key = lambda data : (-data[1], data[2], -data[3], data[0]))

# 내림차순 -

for i in range (n):
    print(score[i][0])

# 이렇게 했는데 <TypeError: append() takes exactly one argument (4 given)> 떴음, 왜지,,?
# 성적이 낮은 순서로 어쩌구에서는 이런식으로 풀었던거 같은데 답지.. 혼란 혼돈 
