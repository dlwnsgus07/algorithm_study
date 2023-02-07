import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

'''
테두리 애들 / 꼭지점 애들 / 나머지
나머지 : 한면만 보임
테두리 : 인접한 두 면
- 맨 밑면 테두리 : 한면만 보임
꼭지점 : 한꼭지점 기준으로 세면
- 맨 밑면 꼭지점 : 두면만 보임

'''