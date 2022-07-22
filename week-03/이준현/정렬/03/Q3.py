n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(k):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]

print(sum(A))

#나는 그냥 sort해서 처음부터 끝까지 무조건 비교를 하도록 하였는데 생각해보니 이미 정렬된 상태에서 비교를 하는 것이기 때문에
#한번이라도 비교되는 순간이 사라지면 break해주는게 평균수행시간 측면에서 보았을때 훨씬 좋다는걸 보고 다시 반성함