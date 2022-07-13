# PART 03 8번 문자열 재정렬
S = list(input())

S.sort()

num = 0
character = ""

for i in S:
    if i.isalpha():
        character += i
    else:
        num += int(i)

print(character+str(num))