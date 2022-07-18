# 구현 05 럭키 스트레이트

score = list(map(int, input()))

lt = int(len(score) /2)

sc1 = score[0:lt]
sc2 = score[lt:]

sum1 = 0
sum2 = 0

for i in range(lt):
    sum1 += sc1[i]
    sum2 += sc2[i]

if sum1 == sum2:
    print("LUCKY")

else:
    print("READY")
