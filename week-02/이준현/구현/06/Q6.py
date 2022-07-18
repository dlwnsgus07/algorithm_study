str_input = input()
al = list()
sum_value = 0
for i in str_input:
    if i.isalpha():
        al.append(i)
    else:
        sum_value += int(i)

al.sort()
s = ''.join(al)
s = s+str(sum_value)
print(s)
