test = int(input())
for _ in range(test):
    ans = 1
    volunteer = int(input())
    score = []
    index = 0
    for i in range(volunteer):
        a, b = map(int, input().split())
        score.append((a, b))
    score.sort()
    for i in range(volunteer):
        if score[i][1] < score[index][1]:
            ans += 1
            index = i
    print(ans)
    # 원래 이놈으로 했는데 계속 타임리밋떠서 다른거 봄...
    # interview = []
    # document = []
    # people = set()
    # for i in range(volunteer):
    #     a, b = map(int, input().split())
    #     interview.append((a, b))
    #     document.append((b, i))
    #
    # interview.sort()
    # document.sort()
    # for x, y in interview:
    #     for i, j in document:
    #         if j == y:
    #             break
    #         if j in people:
    #             ans += 1
    #             break
    #     people.add(y)