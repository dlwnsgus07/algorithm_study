#백준 1541 잃어버린 괄호

func = list(input().split('-'))
print(func)

for i in range(len(func)):
    temp = 0
    tm = []
    if(func[i].isdigit()==False):
        tm = map(int,func[i].split('+'))
        temp = sum(tm)
        func[i] = temp

print(func)

        
func2 = list(map(int, func))

for i in range(len(func2)):
    if(i>=1):
        func2[0] -= func2[i]


print(func2[0])



