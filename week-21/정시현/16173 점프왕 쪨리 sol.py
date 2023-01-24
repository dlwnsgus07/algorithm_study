import sys
input=sys.stdin.readline

def dfs(x,y) :
    #영역을 벗어났거나 이미 방문을 했다면 return
    if x<=-1 or x>=N or y<=-1 or y>=N or visit[x][y]==1:
        return
    
    #방문한 곳의 이동 칸 수가 -1이라면 방문처리를 해주고 return 한다. 
    if graph[x][y] == -1 :
        visit[x][y] = 1
        return

    #방문했다고 표시해준다.
    visit[x][y]=1

    #상,하,좌,우를 요소 수만큼 점프하여 방문한다.
    dfs(x+graph[x][y],y)
    dfs(x,y+graph[x][y])

#게임 구역의 크기 N을 입력받는다.
N=int(input())

#게임판의 구역을 입력받는다. 2차원 리스트
graph=[list(map(int,input().split())) for _ in range(N)]

#방문여부를 저장할 visit 2차원 리스트를 만든다.
visit=[[0]*N for _ in range(N)]

#출발은 0,0에서 하므로 dfs(0,0)을 호출한다.
dfs(0,0)

#결과 출력
if visit[-1][-1] == 1 :
    print('HaruHaru')
else :
    print('Hing')