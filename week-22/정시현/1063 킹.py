k, s, n = input().split()
k = list(k)
k[0] = ord(k[0])
k[1] = int(k[1])
s = list(s)
s[0] = ord(s[0])
s[1] = int(s[1])
n = int(n)
m = [input() for i in range(n)]
size = 8
move = {'R':[+1,0], 'L':[-1,0], 'B':[0,-1], 'T':[0,+1], 'RT':[+1,+1], 'LT':[-1,+1], 'RB':[+1,-1], 'LB':[-1,-1]}

for i in range(n):
    m[i] = move[m[i]]
    nk = [ki + mi for ki, mi in zip(k, m[i])]
    if(nk[1] >=1 and nk[1]<=8 and nk[0] >=65 and nk[0] <=72):
        if(nk == s):
            ns = [si + mi for si, mi in zip(s, m[i])]
            if(ns[1] >=1 and ns[1]<=8 and ns[0] >=65 and ns[0] <=72):
                s = ns
                k = nk
            else:
                continue
        else:
            k = nk
    else:
        continue

k[0] = chr(k[0])
k[1] = str(k[1])
s[0] = chr(s[0])
s[1] = str(s[1])
k = ''.join(k)
s = ''.join(s)
print(k)
print(s)



