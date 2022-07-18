# PART 03 7번 럭키 스트레이트
N = input()

left = 0
right = 0

for i in range(len(N)):
    if i < len(N) / 2:
        left += int(N[i])
    else:
        right += int(N[i])

if left == right:
    print("LUCKY")
else:
    print("READY")