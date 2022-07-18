# 구현 06 문자열 재정렬

s = input()

num = list(filter(str.isdigit,s))
num.sort()
num = ''.join(num)
alpha = list(filter(str.isalpha, s))
alpha.sort()
alpha = ''.join(alpha)


print(alpha+num)

# '구분자'.join(리스트) : ['a', 'b', 'c'] > 'a구분자b구분자c'
