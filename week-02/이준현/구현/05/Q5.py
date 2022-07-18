flag = False
pre = 0
suf = 0
strikes = input()
strike = list()

for i in strikes:
    strike.append(i)
prefix = strike[:int(len(strike) / 2)]
suffix = strike[int(len(strike) / 2):]

for i in prefix:
    pre += int(i)

for i in suffix:
    suf += int(i)

if pre == suf:
    flag = True
else:
    flag = False

if flag:
    print("LUCKY")
else:
    print("READY")