n = int(input())
mon = 1000-n
count = 0

while(mon>=500):
    mon -= 500
    count += 1

while(mon>=100):
    mon -= 100
    count += 1
while(mon>=50):
    mon -= 50
    count += 1
while(mon>=10):
    mon -= 10
    count += 1
while(mon>=5):
    mon -= 5
    count += 1
while(mon>=1):
    mon -= 1
    count += 1

print(count)
