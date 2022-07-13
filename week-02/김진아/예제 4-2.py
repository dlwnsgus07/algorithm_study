N = input()
count = 0

for hour in range(int(N) + 1):
    for minute in range(60):
        for second in range(60):
            t = str(hour) + str(minute) + str(second)
            if "3" in t:
                count += 1

print(count)