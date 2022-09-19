#백준 1969 DNA  / 틀림

n, m = map(int, input().split())
dna = [[]]

for i in range(n):
    dna.append(list(input()))

    # dna의 한 문자씩 가져와서 배열을 만들고 싶은데 어떻게 해야할지 모르겠음
    #for j in range(m):
    #    dna2.append(dna[i][j])

dna2 = []
hd=0

for j in range (m):
    a, t, g, c = 0, 0, 0, 0
    for i in range (n):
        
        if dna[i+1][j] == 'A':
            a +=1
        elif dna[i+1][j] == 'T':
            t += 1
        elif dna[i+1][j] == 'G':
            g += 1
        elif dna[i+1][j] == 'C':
            c += 1
        
    if max(a,t,g,c) == a:
        dna2.append('A')
    elif max(a,t,g,c) == t:
        dna2.append('T')
    elif max(a,t,g,c) == g:
        dna2.append('G')
    elif max(a,t,g,c) == c:
        dna2.append('C')
  
str = ''.join(dna2)
print(str)

# 해당되는 DNA가 여러개일 때 정렬은 어떻게 ?

for i in range (m):
    for j in range (n):
        if dna[j+1][i] != dna2[i]:
            hd+=1

print(hd)   


