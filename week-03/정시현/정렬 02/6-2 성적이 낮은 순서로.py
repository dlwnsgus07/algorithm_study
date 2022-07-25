# 06 정렬 02. 성적이 낮은 순서로 학생 출력하기

n = int(input())

score = []

#for i in range (n):
 #   for j in range(2):
  #      score.append(input().split())

#print(score)

#위에 주석처리한 부분은 왜 아래쪽거처럼 작동하지 않는지?
  # 문자열 / 숫자형으로 따로 형태 정해주지 않아서 그런가?

for i in range(n):
    input_data = input().split()
    score.append((input_data[0], int(input_data[1])))
    
def setting(data):
    return data[1]

result = sorted(score, key = setting)

for i in range (n):
    print(result[i][0], end = ' ')
