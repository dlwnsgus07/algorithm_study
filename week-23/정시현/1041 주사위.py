import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

'''
테두리 애들 / 꼭지점 애들 / 나머지
나머지 : 한면만 보임 : min(num): (n-2)*(n-2)개 (한 면)
테두리 : 인접한 두 면 : (n-2) * 8 개 (두 면)
- 맨 밑면 테두리 : 한면만 보임 : (n-2) *4 개 (한 면)
꼭지점 : 한꼭지점 기준으로 세면 : 4 개 (3면)
- 맨 밑면 꼭지점 : 두면만 보임 : 4 개 (2면)

3면의 합, 2두면의 합 각각 최소 구해서 개수만큼 더하기
'''
num2 = []
num3 = []

for i in range(6):
    for j in range(i+1,6):
        if(i+j==5):
            continue
        num2.append(num[i]+num[j])        
num3.extend([num[0]+num[1]+num[2], num[0]+num[1]+num[3], num[0]+num[2]+num[4], num[0]+num[3]+num[4], num[1]+num[2]+num[5], num[1]+num[3]+num[5], num[2]+num[4]+num[5], num[3]+num[4]+num[5]])
n1 = min(num)
n2 = min(num2)
n3 = min(num3)

sum = (n-2)*(n-2)*n1 + (n-2)*8*n2 + (n-2)*4*n1 + 4*n3 + 4*n2
print(sum)