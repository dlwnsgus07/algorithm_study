min_value = 1e9
n, m = map(int, input().split())

matrix = [[] for i in range(m)]

for i in range(n):
    matrix[i] = list(input())

for a in range(n - 7):
    for b in range(m - 7):
        black = 0
        white = 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        if matrix[i][j] != "W":
                            white += 1
                        if matrix[i][j] != "B":
                            black += 1
                    else:
                        if matrix[i][j] != "B":
                            white += 1
                        if matrix[i][j] != "W":
                            black += 1
                else:
                    if j % 2 == 0:
                        if matrix[i][j] != "B":
                            white += 1
                        if matrix[i][j] != "W":
                            black += 1
                    else:
                        if matrix[i][j] != "W":
                            white += 1
                        if matrix[i][j] != "B":
                            black += 1
        if min_value >= min(black, white):
            min_value = min(black, white)
print(min_value)
